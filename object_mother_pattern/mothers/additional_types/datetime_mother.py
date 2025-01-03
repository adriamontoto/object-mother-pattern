"""
DatetimeMother module.
"""

from datetime import UTC, datetime
from random import choice
from sys import version_info

from dateutil.relativedelta import relativedelta

if version_info >= (3, 12):
    from typing import override  # pragma: no cover
else:
    from typing_extensions import override  # pragma: no cover

from object_mother_pattern.mothers.base_mother import BaseMother


class DatetimeMother(BaseMother[datetime]):
    """
    DatetimeMother class.

    Example:
    ```python
    from object_mother_pattern.mothers import DatetimeMother

    datetime = DatetimeMother.create()
    print(datetime)
    # >>> 2015-08-12 16:41:53.327767+00:00
    ```
    """

    _type: type = datetime

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
        Create a random datetime value within the provided range. If a value is provided, it will be returned.
        If start_datetime is not provided, it will be set to 100 years ago. If end_datetime is not provided, it will be
        set to today. Range is inclusive.

        Args:
            value (datetime | None, optional): Datetime value. Defaults to None.
            start_datetime (datetime | None, optional): Start datetime. Defaults to None.
            end_datetime (datetime | None, optional): End datetime. Defaults to None.

        Raises:
            TypeError: If value is not a datetime.
            TypeError: If start_datetime is not a datetime.
            TypeError: If end_datetime is not a datetime.
            ValueError: If end_datetime is older than start_datetime.

        Returns:
            datetime: Random datetime.

        Example:
        ```python
        from object_mother_pattern.mothers import DatetimeMother

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

        start_datetime = cls.__force_utc(date=start_datetime)
        end_datetime = cls.__force_utc(date=end_datetime)
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
        Create a random datetime value out of the provided range. If start_datetime is not provided, it will be set to
        100 years. If end_datetime is not provided, it will be set to today. Range is inclusive.

        Args:
            start_datetime (datetime | None, optional): Out of range start datetime. Defaults to None.
            end_datetime (datetime | None, optional): Out of range end datetime. Defaults to None.
            range (int, optional): Out of range range. Defaults to 100.

        Raises:
            TypeError: If start_datetime is not a datetime.
            TypeError: If end_datetime is not a datetime.
            ValueError: If end_datetime is older than start_datetime.
            TypeError: If range is not an integer.
            ValueError: If range is a negative integer.

        Returns:
            datetime: Random datetime out of range.

        Example:
        ```python
        from object_mother_pattern.mothers import DatetimeMother

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

        start_datetime = cls.__force_utc(date=start_datetime)
        end_datetime = cls.__force_utc(date=end_datetime)
        if start_datetime > end_datetime:
            raise ValueError('DatetimeMother end_datetime must be older than start_datetime.')

        if type(range) is not int:
            raise TypeError('DatetimeMother range must be an integer.')

        if range < 0:
            raise ValueError('DatetimeMother range must be a positive integer.')

        return choice(
            seq=[
                cls._random().date_time_between(
                    start_date=start_datetime - relativedelta(years=range),
                    end_date=start_datetime,
                    tzinfo=UTC,
                ),
                cls._random().date_time_between(
                    start_date=end_datetime,
                    end_date=end_datetime + relativedelta(years=range),
                    tzinfo=UTC,
                ),
            ]
        )

    @classmethod
    def __force_utc(cls, date: datetime) -> datetime:
        """
        Force a datetime to be timezone-aware.

        Args:
            date: Datetime.

        Returns:
            datetime: Timezone-aware datetime.
        """
        if date.tzinfo is None:
            date = date.replace(tzinfo=UTC)  # pragma: no cover

        return date
