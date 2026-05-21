# Date And Time Mothers

Date and time mothers generate `date`, `datetime`, timezone, and string date/time values for tests.

## Imports

```python
from object_mother_pattern import DateMother, DatetimeMother, StringDateMother, StringDatetimeMother
from object_mother_pattern.mothers.dates import StringTimezoneMother, TimezoneMother
```

## Catalog

| Mother | Typical Uses |
| --- | --- |
| `DateMother` | Valid dates, range-bound dates, and dates outside a range. |
| `DatetimeMother` | Valid datetimes, range-bound datetimes, and datetimes outside a range. |
| `StringDateMother` | Date strings for parser and API-boundary tests. |
| `StringDatetimeMother` | Datetime strings for parser and API-boundary tests. |
| `TimezoneMother` | Timezone objects. |
| `StringTimezoneMother` | Timezone names as strings. |

## Example

```python
from datetime import date

from object_mother_pattern import DateMother

value = DateMother.create(
    start_date=date(year=2026, month=1, day=1),
    end_date=date(year=2026, month=12, day=31),
)
outside = DateMother.out_of_range(
    start_date=date(year=2026, month=1, day=1),
    end_date=date(year=2026, month=12, day=31),
)
```

## Guidance

- Prefer explicit dates when behavior depends on today, age, ordering, or calendar boundaries.
- Use generated range values to exercise invariants.
- Use out-of-range helpers for negative-path validation tests.
- Keep timezone tests explicit when daylight saving or offset behavior matters.
