"""
StringDateMother module.
"""

from datetime import date
from sys import version_info

if version_info >= (3, 12):
    from typing import override  # pragma: no cover
else:
    from typing_extensions import override  # pragma: no cover

from object_mother_pattern.mothers.base_mother import BaseMother

from .date_mother import DateMother


class StringDateMother(BaseMother[str]):
    """
    StringDateMother class.

    Example:
    ```python
    from object_mother_pattern.mothers import StringDateMother

    date = StringDateMother.create()
    print(date)
    # >>> 2015-09-15
    ```
    """

    _type: type = str

    @classmethod
    @override
    def create(
        cls,
        *,
        value: str | None = None,
        start_date: date | None = None,
        end_date: date | None = None,
    ) -> str:
        """
        Create a random date value as a string in ISO format within the provided range. If a value is provided, it will
        be returned. If start_date is not provided, it will be set to 100 years ago. If end_date is not provided, it
        will be set to today. Range is inclusive.

        Args:
            value (str | None, optional): Date value as string. Defaults to None.
            start_date (date | None, optional): Start date. Defaults to None.
            end_date (date | None, optional): End date. Defaults to None.

        Raises:
            TypeError: If value is not a string.
            TypeError: If start_date is not a date.
            TypeError: If end_date is not a date.
            ValueError: If end_date is older than start_date.

        Returns:
            str: Random date as a string in ISO format.

        Example:
        ```python
        from object_mother_pattern.mothers import StringDateMother

        date = StringDateMother.create()
        print(date)
        # >>> 2015-09-15
        ```
        """
        if value is not None:
            if type(value) is not str:
                raise TypeError('StringDateMother value must be a string.')

            return value

        return DateMother.create(start_date=start_date, end_date=end_date).isoformat()

    @classmethod
    def out_of_range(
        cls,
        *,
        start_date: date | None = None,
        end_date: date | None = None,
        range: int = 100,
    ) -> str:
        """
        Create a random date value as a string in ISO format out of the provided range. If start_date is not provided,
        it will be set to 100 years. If end_date is not provided, it will be set to today. Range is inclusive.

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
            str: Random date out of range as a string in ISO format.

        Example:
        ```python
        from object_mother_pattern.mothers import StringDateMother

        date = StringDateMother.out_of_range()
        print(date)
        # >>> 1881-01-28
        ```
        """
        return DateMother.out_of_range(start_date=start_date, end_date=end_date, range=range).isoformat()
