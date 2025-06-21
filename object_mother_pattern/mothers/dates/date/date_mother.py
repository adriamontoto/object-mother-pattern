"""
DateMother module.
"""

from sys import version_info

if version_info >= (3, 12):
    from typing import override  # pragma: no cover
else:
    from typing_extensions import override  # pragma: no cover

from datetime import UTC, date, datetime
from random import choice

from dateutil.relativedelta import relativedelta

from object_mother_pattern.models import BaseMother


class DateMother(BaseMother[date]):
    """
    DateMother class is responsible for creating random date values.

    Example:
    ```python
    from object_mother_pattern import DateMother

    date = DateMother.create()
    print(date)
    # >>> 2015-09-15
    ```
    """

    @classmethod
    @override
    def create(
        cls,
        *,
        value: date | None = None,
        start_date: date | None = None,
        end_date: date | None = None,
    ) -> date:
        """
        Create a random date value within the provided range. If a specific date value is provided via `value`, it is
        returned after validation. Otherwise, the method generates a random date between `start_date` and `end_date`.
        By default, if not specified, `start_date` is set to 100 years before today and `end_date` is set to today
        (both inclusive).

        Args:
            value (date | None, optional): Specific value to return. Defaults to None.
            start_date (date | None, optional): The beginning of the date range. Defaults to None.
            end_date (date | None, optional): The end of the date range. Defaults to None.

        Raises:
            TypeError: If the provided `value` is not a date.
            TypeError: If the provided `start_date` is not a date.
            TypeError: If the provided `end_date` is not a date.
            ValueError: If `end_date` is older than `start_date`.

        Returns:
            date: A randomly date value within the provided range.

        Example:
        ```python
        from object_mother_pattern import DateMother

        date = DateMother.create()
        print(date)
        # >>> 2015-09-15
        ```
        """
        if value is not None:
            if type(value) is not date:
                raise TypeError('DateMother value must be a date.')

            return value

        today = datetime.now(tz=UTC).date()
        if start_date is None:
            start_date = today - relativedelta(years=100)

        if end_date is None:
            end_date = today

        if type(start_date) is not date:
            raise TypeError('DateMother start_date must be a date.')

        if type(end_date) is not date:
            raise TypeError('DateMother end_date must be a date.')

        if start_date > end_date:
            raise ValueError('DateMother end_date must be older than start_date.')

        return cls._random().date_between(start_date=start_date, end_date=end_date)

    @classmethod
    def out_of_range(
        cls,
        *,
        start_date: date | None = None,
        end_date: date | None = None,
        range: int = 100,
    ) -> date:
        """
        Create a random date value that is either before the `start_date` or after the `end_date` by a time offset
        specified by the `range` parameter. By default, if `start_date` and `end_date` are not provided, they default
        to 100 years ago and today, respectively.

        Args:
            start_date (date | None, optional): The beginning of the date range. Defaults to None.
            end_date (date | None, optional): The end of the date range. Defaults to None.
            range (int, optional): The range of the date. Must be >= 0. Defaults to 100.

        Raises:
            TypeError: If the provided `start_date` is not a date.
            TypeError: If the provided `end_date` is not a date.
            ValueError: If `end_date` is older than `start_date`.
            TypeError: If the provided `range` is not an integer.
            ValueError: If `range` is a negative integer.

        Returns:
            date: A randomly date value out of the provided range.

        Example:
        ```python
        from object_mother_pattern import DateMother

        date = DateMother.out_of_range()
        print(date)
        # >>> 1881-01-28
        ```
        """
        today = datetime.now(tz=UTC).date()
        if start_date is None:
            start_date = today - relativedelta(years=100)

        if end_date is None:
            end_date = today

        if type(start_date) is not date:
            raise TypeError('DateMother start_date must be a date.')

        if type(end_date) is not date:
            raise TypeError('DateMother end_date must be a date.')

        if start_date > end_date:
            raise ValueError('DateMother end_date must be older than start_date.')

        if type(range) is not int:
            raise TypeError('DateMother range must be an integer.')

        if range < 0:
            raise ValueError('DateMother range must be a positive integer.')

        epsilon = relativedelta(days=1)
        return choice(  # noqa: S311
            seq=[
                cls._random().date_between(
                    start_date=start_date - relativedelta(years=range),
                    end_date=start_date - epsilon,
                ),
                cls._random().date_between(
                    start_date=end_date + epsilon,
                    end_date=end_date + relativedelta(years=range),
                ),
            ]
        )
