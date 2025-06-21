"""
StringDateMother module.
"""

from sys import version_info

if version_info >= (3, 12):
    from typing import override  # pragma: no cover
else:
    from typing_extensions import override  # pragma: no cover

from datetime import date

from object_mother_pattern.models import BaseMother
from object_mother_pattern.mothers.primitives import StringMother

from .date_mother import DateMother


class StringDateMother(BaseMother[str]):
    """
    StringDateMother class is responsible for creating random string date values in ISO format.

     Formats:
        - ISO: `YYYY-MM-DD`

    Example:
    ```python
    from object_mother_pattern import StringDateMother

    date = StringDateMother.create()
    print(date)
    # >>> 2015-09-15
    ```
    """

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
        Create a random string date value in ISO format within the provided range. If a specific string date value is
        provided via `value`, it is returned after validation. Otherwise, the method generates a random string date
        between `start_date` and `end_date`. By default, if not specified, `start_date` is set to 100 years before today
        and `end_date` is set to today (both inclusive).

        Args:
            value (str | None, optional): Specific value to return. Defaults to None.
            start_date (date | None, optional): The beginning of the date range. Defaults to None.
            end_date (date | None, optional): The end of the date range. Defaults to None.

        Raises:
            TypeError: If the provided `value` is not a string.
            TypeError: If the provided `start_date` is not a date.
            TypeError: If the provided `end_date` is not a date.
            ValueError: If `end_date` is older than `start_date`.

        Returns:
            str: A randomly string date value in ISO format within the provided range.

        Example:
        ```python
        from object_mother_pattern import StringDateMother

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
        Create a random string date value in ISO format that is either before the `start_date` or after the `end_date`
        by a time offset specified by the `range` parameter. By default, if `start_date` and `end_date` are not
        provided, they default to 100 years ago and today, respectively.

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
            str: A randomly string date value in ISO format out of the provided range.

        Example:
        ```python
        from object_mother_pattern import StringDateMother

        date = StringDateMother.out_of_range()
        print(date)
        # >>> 1881-01-28
        ```
        """
        return DateMother.out_of_range(start_date=start_date, end_date=end_date, range=range).isoformat()

    @classmethod
    def invalid_value(cls) -> str:
        """
        Create an invalid string value.

        Returns:
            str: Invalid string.
        """
        return StringMother.invalid_value()
