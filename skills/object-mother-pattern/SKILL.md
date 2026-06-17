---
name: object-mother-pattern
description: Use this skill whenever a user is writing Python tests, pytest fixtures, validation tests, factories, or generated test data with the object-mother-pattern package. It teaches agents how to choose and call Object Mother classes, compose ListMother and DictMother, create custom BaseMother subclasses, update exports and docs, and avoid brittle random assertions. Trigger when prompts mention object mothers, object_mother_pattern, Object Mother Pattern, test data, invalid values, boundary values, UUIDs, dates, URLs, identifiers, credit cards, or package mother APIs.
compatibility: Python projects using object-mother-pattern. The package supports Python 3.11 and newer; this repository tests Python 3.11, 3.12, 3.13, and 3.14.
---

# Object Mother Pattern

Use this skill to work with the `object-mother-pattern` Python package in tests, fixtures, and downstream projects.
The package provides reusable typed mother classes that generate valid, invalid, boundary, and explicit test data.

## First Steps

1. Identify whether the user is consuming the package, changing the package itself, or creating downstream custom mothers.
2. Check the installed package version or local repository when exact API availability matters.
3. Choose the most specific mother that matches the test intent.
4. Use generated values only when assertions check invariants. Use explicit literals or `create(value=...)` when exact output matters.
5. For negative tests, prefer `invalid_type()`, `invalid_value()`, `out_of_range()`, or category-specific helpers over ad hoc invalid data.

## Load References

Read only the references needed for the task:

| Need                                         | Read                             |
| -------------------------------------------- | -------------------------------- |
| Full public API, imports, method signatures  | `references/api-catalog.md`      |
| How to choose mothers and compose fixtures   | `references/usage-patterns.md`   |
| Testing strategy and anti-flakiness guidance | `references/testing-patterns.md` |
| Creating or editing custom mothers           | `references/custom-mothers.md`   |

## Core Rules

- Prefer existing mothers before inventing new fixture helpers.
- Use generated values for type, shape, and invariant tests.
- Use fixed literals for snapshots, serialization, exact strings, SQL, JSON, URLs, and reproduced bugs.
- Use `create(value=...)` when a test needs a known value but should still exercise mother validation.
- Keep random values out of exact assertions. Assert properties such as type, length, range, prefix, suffix, UUID version, URL scheme, or parsed components.
- Compose `ListMother` and `DictMother` with callables such as `IntegerMother.positive`, `StringMother.create`, or lambdas.
- Treat generated financial, identifier, person, and network values as test fixtures only, not real credentials, identities, ownership proof, or production data.

## Common Imports

```python
from object_mother_pattern import DateMother, IntegerMother, StringMother
from object_mother_pattern.models import DictMother, ListMother
from object_mother_pattern.mothers.internet import EmailAddressMother, UrlMother
from object_mother_pattern.mothers.identifiers.uuid import UuidV4Mother
```

Use top-level imports for common primitives, dates, datetimes, and money mothers. Use category imports for specialized
internet, identifier, people, extra text, and country-specific mothers.

## Quick Examples

Generate valid values when the exact value does not matter:

```python
from object_mother_pattern import IntegerMother
from object_mother_pattern.mothers.internet import EmailAddressMother

email = EmailAddressMother.create()
quantity = IntegerMother.positive()

assert '@' in email
assert quantity > 0
```

Validate an explicit value when exact data matters:

```python
from object_mother_pattern import StringMother

assert StringMother.create(value='invoice-paid') == 'invoice-paid'
```

Build a composed payload:

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

Test validation failures:

```python
from pytest import raises

from object_mother_pattern import IntegerMother

with raises(TypeError):
    IntegerMother.create(value=IntegerMother.invalid_type())

too_low_or_too_high = IntegerMother.out_of_range(min=1, max=10)
assert too_low_or_too_high < 1 or too_low_or_too_high > 10
```
