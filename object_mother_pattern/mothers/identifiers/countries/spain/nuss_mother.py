"""
NussMother module for Spanish Social Security Number values.
"""

from sys import version_info

if version_info >= (3, 12):
    from typing import override  # pragma: no cover
else:
    from typing_extensions import override  # pragma: no cover


from random import choice
from typing import ClassVar

from object_mother_pattern.models import BaseMother
from object_mother_pattern.mothers.primitives.string_mother import StringMother


class NussMother(BaseMother[str]):
    """
    NussMother class is responsible for creating valid Spanish Social Security Number values.

    Example:
    ```python
    from object_mother_pattern.mothers.identifiers.countries.spain import NussMother

    nuss = NussMother.create()
    print(nuss)
    # >>> 281234567849
    ```
    """

    _PROVINCE_CODES: ClassVar[tuple[str, ...]] = tuple(f'{number:02d}' for number in range(1, 53))

    @classmethod
    @override
    def create(cls, *, value: str | None = None) -> str:
        """
        Create a random valid Spanish Social Security Number.

        Args:
            value (str | None, optional): Specific NUSS value to return. Defaults to None.

        Raises:
            TypeError: If the provided `value` is not a string.

        Returns:
            str: A valid Spanish Social Security Number.

        Example:
        ```python
        from object_mother_pattern.mothers.identifiers.countries.spain import NussMother

        nuss = NussMother.create()
        print(nuss)
        # >>> 281234567849
        ```
        """
        if value is not None:
            if type(value) is not str:
                raise TypeError('NussMother value must be a string.')

            return value

        province = choice(seq=cls._PROVINCE_CODES)  # noqa: S311
        sequential = StringMother.numeric(min_length=8, max_length=8)
        control = int(f'{province}{sequential}') % 97

        return f'{province}{sequential}{control:02d}'

    @classmethod
    def invalid_value(cls) -> str:
        """
        Create an invalid Spanish Social Security Number value.

        Returns:
            str: Invalid Spanish Social Security Number string.
        """
        return StringMother.invalid_value()
