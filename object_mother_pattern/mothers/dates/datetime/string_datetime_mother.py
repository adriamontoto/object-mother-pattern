"""
StringDatetimeMother module.
"""

from sys import version_info

if version_info >= (3, 12):
    from typing import override  # pragma: no cover
else:
    from typing_extensions import override  # pragma: no cover

from datetime import datetime

from object_mother_pattern.models import BaseMother
from object_mother_pattern.mothers.primitives.string_mother import StringMother

from .datetime_mother import DatetimeMother


class StringDatetimeMother(BaseMother[str]):
    """
    StringDatetimeMother class is responsible for creating random string datetime values in ISO 8601 format.

     Formats:
        - ISO 8601: `YYYY-MM-DDTHH:MM:SS.mmmmmm+HH:MM`

    Example:
    ```python
    from object_mother_pattern import StringDatetimeMother

    datetime = StringDatetimeMother.create()
    print(datetime)
    # >>> 2015-08-12 16:41:53.327767+00:00
    ```
    """

    @classmethod
    @override
    def create(
        cls,
        *,
        value: str | None = None,
        start_datetime: datetime | None = None,
        end_datetime: datetime | None = None,
    ) -> str:
        """
        Create a random string datetime value in ISO 8601 format within the provided range. If a specific datetime value
        is provided via `value`, it is returned after validation. Otherwise, the method generates a random datetime
        between `start_datetime` and `end_datetime`. By default, if not specified, `start_datetime` is set to 100 years
        before today and `end_datetime` is set to today (both inclusive).

        Args:
            value (str | None, optional): Specific value to return. Defaults to None.
            start_datetime (datetime | None, optional): The beginning of the datetime range. Defaults to None.
            end_datetime (datetime | None, optional): The end of the datetime range. Defaults to None.

        Raises:
            TypeError: If the provided `value` is not a string.
            TypeError: If the provided `start_datetime` is not a datetime.
            TypeError: If the provided `end_datetime` is not a datetime.
            ValueError: If `end_datetime` is older than `start_datetime`.

        Returns:
            str: A randomly string datetime value in ISO 8601 format within the provided range.

        Example:
        ```python
        from object_mother_pattern import StringDatetimeMother

        datetime = StringDatetimeMother.create()
        print(datetime)
        # >>> 2015-08-12 16:41:53.327767+00:00
        ```
        """
        if value is not None:
            if type(value) is not str:
                raise TypeError('StringDatetimeMother value must be a string.')

            return value

        return DatetimeMother.create(
            value=value,
            start_datetime=start_datetime,
            end_datetime=end_datetime,
        ).isoformat()

    @classmethod
    def out_of_range(
        cls,
        *,
        start_datetime: datetime | None = None,
        end_datetime: datetime | None = None,
        range: int = 100,
    ) -> str:
        """
        Create a random string datetime value in ISO 8601 format that is either before the `start_datetime` or after
        the `end_datetime` by a time offset specified by the `range` parameter. By default, if `start_datetime` and
        `end_datetime` are not provided, they default to 100 years ago and today, respectively.

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
            str: A randomly string datetime value in ISO 8601 format out of the provided range.

        Example:
        ```python
        from object_mother_pattern import StringDatetimeMother

        datetime = StringDatetimeMother.out_of_range()
        print(datetime)
        # >>> 2055-07-08 15:30:49.091827+00:00
        ```
        """
        return DatetimeMother.out_of_range(
            start_datetime=start_datetime,
            end_datetime=end_datetime,
            range=range,
        ).isoformat()

    @classmethod
    def invalid_value(cls) -> str:
        """
        Create an invalid string value.

        Returns:
            str: Invalid string.
        """
        return StringMother.invalid_value()
