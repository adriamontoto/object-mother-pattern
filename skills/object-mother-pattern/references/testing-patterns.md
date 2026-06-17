# Testing Patterns

Object mothers should make test intent clearer. They are not a reason to make tests random for its own sake.

## Valid Values

Use generated values when the test checks that a valid value flows through code:

```python
from object_mother_pattern.mothers.internet import EmailAddressMother

email = EmailAddressMother.create()

assert '@' in email
```

For generated values, assert the invariant that matters:

- `type(value) is int`
- `1 <= value <= 10`
- `len(value) == 12`
- `uuid.version == 4`
- `parts.scheme == 'https'`
- `all(item > 0 for item in values)`

## Explicit Values

Use fixed literals when the exact example is part of the behavior:

```python
from object_mother_pattern import StringMother

value = StringMother.create(value='invoice-paid')

assert value == 'invoice-paid'
```

This pattern keeps validation centralized while preserving deterministic tests.

## Invalid Types

Use `invalid_type()` for type-validation branches:

```python
from pytest import raises

from object_mother_pattern import IntegerMother

with raises(TypeError):
    IntegerMother.create(value=IntegerMother.invalid_type())
```

Some mothers override `invalid_type()` to avoid related acceptable types. For example, `FloatMother` accepts `int` and
`float`, so its invalid-type helper excludes both.

## Invalid Values

Use `invalid_value()` for values with the correct Python type but invalid domain shape:

```python
from object_mother_pattern.mothers.internet import UrlMother

value = UrlMother.invalid_value()

assert type(value) is str
```

`invalid_value()` is common on domain mothers, string UUID mothers, internet mothers, identifier mothers, money mothers,
people mothers, and extra text mothers. Use the API catalog to confirm availability.

## Boundaries And Ranges

Use dedicated helpers for value boundaries:

```python
from object_mother_pattern import IntegerMother

value = IntegerMother.out_of_range(min=1, max=10)

assert value < 1 or value > 10
```

Useful boundary helpers include:

- `IntegerMother.positive()`, `positive_or_zero()`, `negative()`, `negative_or_zero()`, `even()`, `odd()`, `out_of_range()`
- `FloatMother.positive()`, `positive_or_zero()`, `negative()`, `negative_or_zero()`, `out_of_range()`
- `StringMother.empty()`, `of_length()`, casing helpers, `not_trimmed()`, `invalid_value()`
- `BytesMother.empty()`, `of_length()`
- `DateMother.out_of_range()` and `DatetimeMother.out_of_range()`
- `StringDateMother.invalid_value()` and `StringDatetimeMother.invalid_value()`

## Collections

Use collection mothers for payloads when shape matters more than exact field names:

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

Use exact dictionaries when the code under test branches on key names.

## Anti-Flakiness Checklist

- Do not use generated strings in snapshots.
- Do not compare two independently generated random values for equality.
- Do not assert random ordering unless ordering is the behavior under test.
- Do not use date/datetime generation for today-sensitive logic unless the allowed range is explicit.
- Do not use object mothers as a substitute for property-based testing when exhaustive exploration is required.
- Use explicit values for edge cases that must be reproducible.
