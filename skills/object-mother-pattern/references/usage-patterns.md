# Usage Patterns

This reference helps choose the right mother and write stable test setup.

## Choosing Generated Or Explicit Values

Use generated values when the test cares about a property:

```python
from object_mother_pattern import IntegerMother

value = IntegerMother.positive()

assert value > 0
```

Use explicit values when the value itself is the example:

```python
from object_mother_pattern import StringMother

value = StringMother.create(value='paid')

assert value == 'paid'
```

Prefer fixed literals for:

- snapshots and golden files
- exact serialization, JSON, SQL, and URL assertions
- error messages and UI copy
- bug reproduction
- deliberately chosen boundaries

Prefer generated values for:

- validation success paths where only the shape matters
- non-empty strings or text
- positive, negative, odd, even, or ranged numbers
- syntactically valid identifiers, URLs, email addresses, IP addresses, domains, and card-like values
- factory inputs where the tested behavior does not depend on exact data

## Common Import Paths

```python
from object_mother_pattern import (
    BooleanMother,
    BytesMother,
    CreditCardMother,
    DateMother,
    DatetimeMother,
    FloatMother,
    IbanMother,
    IntegerMother,
    StringDateMother,
    StringDatetimeMother,
    StringMother,
)
from object_mother_pattern.models import BaseMother, DictMother, EnumerationMother, ListMother
from object_mother_pattern.mothers.internet import EmailAddressMother, UrlMother
from object_mother_pattern.mothers.identifiers.uuid import UuidV4Mother
from object_mother_pattern.mothers.people import UsernameMother
```

Top-level imports cover the most common primitives, date/datetime values, and money values. Specialized categories live
under `object_mother_pattern.mothers.<category>`.

## Collections

`ListMother` and `DictMother` accept callables. Pass a class method directly when no extra arguments are needed, and use a
lambda when the nested mother needs parameters.

```python
from object_mother_pattern import IntegerMother, StringMother
from object_mother_pattern.models import DictMother, ListMother

ids = ListMother.of_length(length=3, item_mother=IntegerMother.positive)

payload = DictMother.of_length(
    length=2,
    key_mother=lambda: StringMother.lowercase(min_length=4, max_length=8),
    value_mother=IntegerMother.create,
)
```

Dictionary keys must be hashable and distinct enough to satisfy the requested length. Use exact keys when field names are
important to the assertion.

## Enums

Use `EnumerationMother` for small enum fixtures. Subclass it with the enum type and call `create()`.

```python
from enum import Enum, unique

from object_mother_pattern.models import EnumerationMother


@unique
class Status(Enum):
    DRAFT = 'draft'
    PUBLISHED = 'published'
    ARCHIVED = 'archived'


class StatusMother(EnumerationMother[Status]):
    pass


status = StatusMother.create(exclude={Status.ARCHIVED})
```

Use `create(value=...)` to validate that an explicit enum member belongs to the enum. Use `exclude=...` when the code path
must avoid one or more enum values.

## Domain Selection

- Use `StringMother` for generic string constraints.
- Use `UsernameMother`, `FullNameMother`, `PasswordMother`, or `TextMother` for human-readable fixture shapes.
- Use URL, host, domain, IP, network, port, key, slug, email, IMEI, AWS region, and user-agent mothers for internet-shaped data.
- Use UUID version-specific mothers when code branches on UUID version.
- Use Spanish/world identifier mothers only when that domain format is relevant.
- Use brand-specific credit-card mothers when the brand matters; use `CreditCardMother` when any supported brand is acceptable.

## Exactness And Randomness

Generated values are intentionally random. Do not assert the exact generated value unless the helper is deterministic by
definition, such as `BooleanMother.true()`, `StringMother.empty()`, or a known port helper such as `PortMother.https()`.
When randomness is involved, assert invariants:

```python
from object_mother_pattern import StringMother

value = StringMother.of_length(length=12)

assert isinstance(value, str)
assert len(value) == 12
```
