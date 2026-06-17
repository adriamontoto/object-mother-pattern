# Custom Mothers

Use this reference when creating or editing a mother in a downstream project or in this repository.

## Shape

Subclass `BaseMother[T]` and implement `create()` as a class method. The normal convention is:

- accept `value: T | None = None`
- if `value` is provided, validate it and return it unchanged
- if no value is provided, generate a valid random value
- raise `TypeError` for wrong Python types
- raise `ValueError` for values of the right type that violate domain rules

```python
from random import randint

from object_mother_pattern.models import BaseMother


class PositiveIntegerMother(BaseMother[int]):
    @classmethod
    def create(cls, *, value: int | None = None) -> int:
        if value is not None:
            if type(value) is not int:
                raise TypeError('PositiveIntegerMother value must be an integer.')

            if value <= 0:
                raise ValueError('PositiveIntegerMother value must be positive.')

            return value

        return randint(a=1, b=100)
```

## Helper Methods

Add helper methods only when they express recurring test intent. Good helpers describe the value shape:

- `empty()`
- `of_length(length=...)`
- `positive()`
- `out_of_range(...)`
- `invalid_value()`
- format-specific helpers such as `with_query()` or `mobile()`

Prefer a small expressive helper over repeated literals across tests.

## Invalid Helpers

`BaseMother.invalid_type()` is inherited by subclasses and returns a value that is not the target type. If a mother accepts
multiple related types, override it to exclude all accepted types.

Add `invalid_value()` when consumers often need a wrong value with the correct Python type.

## Validation

Use existing validators or local validation primitives when nearby code does so. In this repository, many domain mothers
delegate explicit values to `value_object_pattern` validators. Preserve local error-message style:

```python
raise TypeError('StringMother value must be a string.')
raise ValueError('StringMother min_length must be less than or equal to max_length.')
```

Do not silently coerce explicit values. If `create(value=...)` receives an invalid type or shape, raise an exception.

## Repository Integration

When adding a public mother to this package:

- place it in the closest category under `object_mother_pattern/mothers/`
- add or update tests under the matching `tests/mothers/` path
- update category `__init__.py` exports when intended for users
- update `object_mother_pattern/__init__.py` only for top-level public exports
- update docs/catalog content when user-facing behavior changes
- update `skills/object-mother-pattern/` when public API, method signatures, or testing guidance changes
- keep `object_mother_pattern/py.typed` present

## Python Version Pattern

When using `typing.override`, preserve the repository compatibility pattern:

```python
from sys import version_info

if version_info >= (3, 12):
    from typing import override  # pragma: no cover
else:
    from typing_extensions import override  # pragma: no cover
```

The package supports Python 3.11 and newer.
