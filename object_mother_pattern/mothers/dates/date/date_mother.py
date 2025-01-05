"""
DateMother module.
"""

from datetime import UTC, date, datetime
from random import choice
from sys import version_info

from dateutil.relativedelta import relativedelta

if version_info >= (3, 12):
    from typing import override  # pragma: no cover
else:
    from typing_extensions import override  # pragma: no cover

from object_mother_pattern.mothers.base_mother import BaseMother


class DateMother(BaseMother[date]):
    """
    DateMother class.

    Example:
    ```python
    from object_mother_pattern.mothers import DateMother

    date = DateMother.create()
    print(date)
    # >>> 2015-09-15
    ```
    """

    _type: type = date

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
        Create a random date value within the provided range. If a value is provided, it will be returned.
        If start_date is not provided, it will be set to 100 years ago. If end_date is not provided, it will be set to
        today. Range is inclusive.

        Args:
            value (date | None, optional): Date value. Defaults to None.
            start_date (date | None, optional): Start date. Defaults to None.
            end_date (date | None, optional): End date. Defaults to None.

        Raises:
            TypeError: If value is not a date.
            TypeError: If start_date is not a date.
            TypeError: If end_date is not a date.
            ValueError: If end_date is older than start_date.

        Returns:
            date: Random date.

        Example:
        ```python
        from object_mother_pattern.mothers import DateMother

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
        Create a random date value out of the provided range. If start_date is not provided, it will be set to 100
        years. If end_date is not provided, it will be set to today. Range is inclusive.

        Args:
            start_date (date | None, optional): Out of range start date. Defaults to None.
            end_date (date | None, optional): Out of range end date. Defaults to None.
            range (int, optional): Out of range range. Defaults to 100.

        Raises:
            TypeError: If start_date is not a date.
            TypeError: If end_date is not a date.
            ValueError: If end_date is older than start_date.
            TypeError: If range is not an integer.
            ValueError: If range is a negative integer.

        Returns:
            date: Random date out of range.

        Example:
        ```python
        from object_mother_pattern.mothers import DateMother

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

        return choice(
            seq=[
                cls._random().date_between(start_date=start_date - relativedelta(years=range), end_date=start_date),
                cls._random().date_between(start_date=end_date, end_date=end_date + relativedelta(years=range)),
            ]
        )
