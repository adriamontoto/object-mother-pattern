# Testing Guide

Object mothers are most useful when tests describe the kind of data they need. The goal is not to maximize randomness;
the goal is to make setup reusable and assertions clear.

## Valid-Value Tests

Use generated data when the assertion checks an invariant:

```python
from object_mother_pattern import IntegerMother

value = IntegerMother.positive()

assert value > 0
```

## Exact-Value Tests

Use explicit values when the assertion depends on exact output:

```python
from object_mother_pattern import StringMother

value = StringMother.create(value='invoice-paid')

assert value == 'invoice-paid'
```

This keeps randomized output from making exact assertions brittle.

## Invalid-Type Tests

Use `invalid_type()` when testing type validation:

```python
from pytest import raises

from object_mother_pattern import StringMother

with raises(TypeError):
    StringMother.create(value=StringMother.invalid_type())
```

Some mothers override `invalid_type()` to avoid related acceptable types. For example, float validation accepts both
`int` and `float`, so its invalid-type helper excludes both.

## Boundary Tests

Use dedicated helpers for boundary conditions:

```python
from object_mother_pattern import IntegerMother

too_low_or_too_high = IntegerMother.out_of_range(min=1, max=10)

assert too_low_or_too_high < 1 or too_low_or_too_high > 10
```

Dates and datetimes also provide out-of-range helpers for calendar validation tests.

## Collection Tests

Use `ListMother` and `DictMother` to build payloads:

```python
from object_mother_pattern import IntegerMother, StringMother
from object_mother_pattern.models import DictMother

payload = DictMother.of_length(
    length=3,
    key_mother=lambda: StringMother.lowercase(min_length=4, max_length=12),
    value_mother=IntegerMother.positive,
)

assert len(payload) == 3
assert all(value > 0 for value in payload.values())
```

Use exact keys if the assertion depends on field names.

## Determinism Guidance

Generated values are intentionally random. Tests should usually assert properties, not exact generated values:

```python
from object_mother_pattern import StringMother

value = StringMother.of_length(length=12)

assert isinstance(value, str)
assert len(value) == 12
```

When exact output matters, pass `value=...` or use fixed literals.

## Testing Checklist

- Assert invariants for generated values.
- Use fixed values for serialization, snapshots, URLs, SQL, JSON, or exact messages.
- Use `invalid_type()` for type errors.
- Use `out_of_range()` and domain-specific helpers for value errors.
- Keep tests resilient to random ordering and random selection.
- Do not use object mothers as substitutes for property-based testing when exhaustive edge-case exploration is required.

