"""
DatetimeMother module.
"""

from sys import version_info

if version_info >= (3, 12):
    from typing import override  # pragma: no cover
else:
    from typing_extensions import override  # pragma: no cover

from datetime import UTC, datetime
from random import choice

from dateutil.relativedelta import relativedelta

from object_mother_pattern.models import BaseMother


class DatetimeMother(BaseMother[datetime]):
    """
    DatetimeMother class is responsible for creating random datetime values.

    Example:
    ```python
    from object_mother_pattern import DatetimeMother

    datetime = DatetimeMother.create()
    print(datetime)
    # >>> 2015-08-12 16:41:53.327767+00:00
    ```
    """

    @classmethod
    @override
    def create(
        cls,
        *,
        value: datetime | None = None,
        start_datetime: datetime | None = None,
        end_datetime: datetime | None = None,
    ) -> datetime:
        """
        Create a random datetime value within the provided range. If a specific datetime value is provided via `value`,
        it is returned after validation. Otherwise, the method generates a random datetime between `start_datetime` and
        `end_datetime`. By default, if not specified, `start_datetime` is set to 100 years before today and
        `end_datetime` is set to today (both inclusive).

        Args:
            value (datetime | None, optional): Specific value to return. Defaults to None.
            start_datetime (datetime | None, optional): The beginning of the datetime range. Defaults to None.
            end_datetime (datetime | None, optional): The end of the datetime range. Defaults to None.

        Raises:
            TypeError: If the provided `value` is not a datetime.
            TypeError: If the provided `start_datetime` is not a datetime.
            TypeError: If the provided `end_datetime` is not a datetime.
            ValueError: If `end_datetime` is older than `start_datetime`.

        Returns:
            datetime: A randomly datetime value within the provided range.

        Example:
        ```python
        from object_mother_pattern import DatetimeMother

        datetime = DatetimeMother.create()
        print(datetime)
        # >>> 2015-08-12 16:41:53.327767+00:00
        ```
        """
        if value is not None:
            if type(value) is not datetime:
                raise TypeError('DatetimeMother value must be a datetime.')

            return value

        today = datetime.now(tz=UTC)
        if start_datetime is None:
            start_datetime = today - relativedelta(years=100)

        if end_datetime is None:
            end_datetime = today

        if type(start_datetime) is not datetime:
            raise TypeError('DatetimeMother start_datetime must be a datetime.')

        if type(end_datetime) is not datetime:
            raise TypeError('DatetimeMother end_datetime must be a datetime.')

        start_datetime = cls._force_utc(date=start_datetime)
        end_datetime = cls._force_utc(date=end_datetime)
        if start_datetime > end_datetime:
            raise ValueError('DatetimeMother end_datetime must be older than start_datetime.')

        return cls._random().date_time_between(start_date=start_datetime, end_date=end_datetime, tzinfo=UTC)

    @classmethod
    def out_of_range(
        cls,
        *,
        start_datetime: datetime | None = None,
        end_datetime: datetime | None = None,
        range: int = 100,
    ) -> datetime:
        """
        Create a random datetime value that is either before the `start_datetime` or after the `end_datetime` by a time
        offset specified by the `range` parameter. By default, if `start_datetime` and `end_datetime` are not provided,
        they default to 100 years ago and today, respectively.

        Args:
            start_datetime (datetime | None, optional): The beginning of the datetime range. Defaults to None.
            end_datetime (datetime | None, optional): The end of the datetime range. Defaults to None.
            range (int, optional): The range of the datetime. Must be >= 0. Defaults to 100.

        Raises:
            TypeError: If the provided `start_datetime` is not a datetime.
            TypeError: If the provided `end_datetime` is not a datetime.
            ValueError: If `end_datetime` is older than `start_datetime`.
            TypeError: If the provided `range` is not an integer.
            ValueError: If `range` is a negative integer.

        Returns:
            datetime: A randomly datetime value out of the provided range.

        Example:
        ```python
        from object_mother_pattern import DatetimeMother

        datetime = DatetimeMother.out_of_range()
        print(datetime)
        # >>> 2055-07-08 15:30:49.091827+00:00
        ```
        """
        today = datetime.now(tz=UTC)
        if start_datetime is None:
            start_datetime = today - relativedelta(years=100)

        if end_datetime is None:
            end_datetime = today

        if type(start_datetime) is not datetime:
            raise TypeError('DatetimeMother start_datetime must be a datetime.')

        if type(end_datetime) is not datetime:
            raise TypeError('DatetimeMother end_datetime must be a datetime.')

        start_datetime = cls._force_utc(date=start_datetime)
        end_datetime = cls._force_utc(date=end_datetime)
        if start_datetime > end_datetime:
            raise ValueError('DatetimeMother end_datetime must be older than start_datetime.')

        if type(range) is not int:
            raise TypeError('DatetimeMother range must be an integer.')

        if range < 0:
            raise ValueError('DatetimeMother range must be a positive integer.')

        epsilon = relativedelta(days=1)
        return choice(  # noqa: S311
            seq=[
                cls._random().date_time_between(
                    start_date=start_datetime - relativedelta(years=range),
                    end_date=start_datetime - epsilon,
                    tzinfo=UTC,
                ),
                cls._random().date_time_between(
                    start_date=end_datetime + epsilon,
                    end_date=end_datetime + relativedelta(years=range),
                    tzinfo=UTC,
                ),
            ]
        )

    @classmethod
    def _force_utc(cls, date: datetime) -> datetime:
        """
        Force a datetime to be timezone-aware.

        Args:
            date: The datetime to force to be timezone-aware.

        Returns:
            datetime: Timezone-aware datetime.
        """
        if date.tzinfo is None:
            date = date.replace(tzinfo=UTC)  # pragma: no cover

        return date
