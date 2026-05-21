# Object Mother Pattern Documentation

Object Mother Pattern provides reusable, typed generators for test data. The package is organized around small mother
classes that can either validate an explicit value or generate a value that satisfies a domain-specific shape.

Use this page as the documentation hub:

| Guide | Purpose |
| --- | --- |
| [Usage Guide](usage/README.md) | Imports, the `create(value=...)` convention, collection mothers, and custom mothers. |
| [Catalog](catalog/README.md) | Feature map by mother category. |
| [Primitive Catalog](catalog/primitives/README.md) | Scalar value generators and invalid primitive helpers. |
| [Date Catalog](catalog/dates/README.md) | Date, datetime, timezone, range, and out-of-range mothers. |
| [Identifier Catalog](catalog/identifiers/README.md) | UUID, world, Spanish, and vehicle-plate mothers. |
| [Internet Catalog](catalog/internet/README.md) | URL, host, address, key, slug, and network mothers. |
| [Money Catalog](catalog/money/README.md) | IBAN, credit-card, and cryptocurrency mothers. |
| [People And Text Catalog](catalog/people/README.md) | Names, usernames, passwords, and text snippets. |
| [Testing Guide](testing/README.md) | Patterns for valid values, invalid types, boundaries, and deterministic assertions. |
| [Data Safety](data-safety/README.md) | Security and correctness boundaries for generated test data. |

## Public Import Shapes

The most common mothers are available from the top-level package:

```python
from object_mother_pattern import DateMother, IntegerMother, StringMother
```

Specialized groups are available from their category packages:

```python
from object_mother_pattern.mothers.identifiers.uuid import UuidV4Mother
from object_mother_pattern.mothers.internet import DomainMother
from object_mother_pattern.models import DictMother, ListMother
```

## Core Contract

Most mothers follow this shape:

```python
value = SomeMother.create()
known_value = SomeMother.create(value=existing_value)
wrong_type = SomeMother.invalid_type()
```

`create(value=...)` validates and returns a provided value. Calling `create()` without `value` generates a random valid
value. `invalid_type()` is intended for negative-path tests.

## Recommended Use

1. Use generated values when the test only cares about invariants.
2. Use explicit values when an assertion depends on exact output.
3. Use range helpers such as `out_of_range()` for validation tests.
4. Use collection mothers to compose realistic payloads from smaller mothers.
5. Do not use generated data as production secrets or cryptographic material.
