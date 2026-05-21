# Usage Guide

Object Mother Pattern helps tests express data intent without repeating setup boilerplate. Mothers are regular Python
classes with class methods, so they work naturally in pytest fixtures, factories, parameterized tests, and object mother
helpers in downstream projects.

## Generate Valid Values

```python
from object_mother_pattern import IntegerMother, StringMother

identifier = IntegerMother.positive()
name = StringMother.titlecase(min_length=6, max_length=24)
```

Use generated values when the test only needs a value that satisfies a type or invariant.

## Validate Explicit Values

```python
from object_mother_pattern import StringMother

value = StringMother.create(value='known-value')

assert value == 'known-value'
```

This pattern is useful when you want exact test data while still exercising the mother validation rules.

## Generate Negative Cases

```python
from pytest import raises

from object_mother_pattern import IntegerMother

with raises(TypeError):
    IntegerMother.create(value=IntegerMother.invalid_type())
```

Use `invalid_type()` for type-validation branches. Use domain helpers such as `out_of_range()` for value-validation
branches.

## Compose Lists And Dictionaries

Collection mothers accept callables, so they can compose existing mothers:

```python
from object_mother_pattern import IntegerMother, StringMother
from object_mother_pattern.models import DictMother, ListMother

numbers = ListMother.of_length(length=3, item_mother=IntegerMother.positive)

payload = DictMother.of_length(
    length=2,
    key_mother=lambda: StringMother.lowercase(min_length=4, max_length=8),
    value_mother=IntegerMother.create,
)
```

Dictionary keys must be hashable and unique enough to satisfy the requested length.

## Work With Enums

Use `EnumerationMother` to create small enum mothers:

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

`create(value=...)` validates that the provided value belongs to the configured enum.

## Create A Custom Mother

New mothers should subclass `BaseMother[T]` and follow the local convention:

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

Custom mothers should validate explicit values the same way they validate generated values.

## Usage Checklist

- Prefer exact values for exact string, serialization, or snapshot assertions.
- Prefer generated values for invariant-based tests.
- Keep random data out of assertions unless the assertion checks the invariant, not the exact output.
- Use existing mothers before adding new helpers.
- Put new mothers in the closest existing category.

