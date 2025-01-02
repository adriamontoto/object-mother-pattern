"""
StringDatetimeMother module.
"""

from datetime import datetime
from sys import version_info

if version_info >= (3, 12):
    from typing import override  # pragma: no cover
else:
    from typing_extensions import override  # pragma: no cover

from object_mother_pattern.mothers.base_mother import BaseMother

from .datetime_mother import DatetimeMother


class StringDatetimeMother(BaseMother[str]):
    """
    StringDatetimeMother class.

    Example:
    ```python
    from object_mother_pattern.mothers import StringDatetimeMother

    datetime = StringDatetimeMother.create()
    print(datetime)
    # >>> 2015-08-12 16:41:53.327767+00:00
    ```
    """

    _type: type = str

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
        Create a random datetime as in ISO 8601 format value within the provided range. If a value is provided, it will
        be returned. If start_datetime is not provided, it will be set to 100 years ago. If end_datetime is not
        provided, it will be set to today. Range is inclusive.

        Args:
            value (str | None, optional): Datetime value as string. Defaults to None.
            start_datetime (datetime | None, optional): Start datetime. Defaults to None.
            end_datetime (datetime | None, optional): End datetime. Defaults to None.

        Raises:
            TypeError: If value is not a string.
            TypeError: If start_datetime is not a datetime.
            TypeError: If end_datetime is not a datetime.
            ValueError: If end_datetime is older than start_datetime.

        Returns:
            str: Random datetime as string in ISO 8601 format.

        Example:
        ```python
        from object_mother_pattern.mothers import StringDatetimeMother

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
        Create a random datetime value as string in ISO 8601 format out of the provided range. If start_datetime is not
        provided, it will be set to 100 years. If end_datetime is not provided, it will be set to today. Range is
        inclusive.

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
            str: Random datetime out of range as string in ISO 8601 format.

        Example:
        ```python
        from object_mother_pattern.mothers import StringDatetimeMother

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
