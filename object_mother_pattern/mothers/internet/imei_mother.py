"""
ImeiMother module.
"""

from sys import version_info

if version_info >= (3, 12):
    from typing import override  # pragma: no cover
else:
    from typing_extensions import override  # pragma: no cover


from object_mother_pattern.models import BaseMother
from object_mother_pattern.mothers.primitives.string_mother import StringMother


class ImeiMother(BaseMother[str]):
    """
    ImeiMother class is responsible for creating valid International Mobile Equipment Identity values.

    Example:
    ```python
    from object_mother_pattern.mothers.internet import ImeiMother

    imei = ImeiMother.create()
    print(imei)
    # >>> 490154203237518
    ```
    """

    @classmethod
    @override
    def create(cls, *, value: str | None = None) -> str:
        """
        Create a random valid International Mobile Equipment Identity.

        Args:
            value (str | None, optional): Specific IMEI value to return. Defaults to None.

        Raises:
            TypeError: If the provided `value` is not a string.

        Returns:
            str: A valid International Mobile Equipment Identity.

        Example:
        ```python
        from object_mother_pattern.mothers.internet import ImeiMother

        imei = ImeiMother.create()
        print(imei)
        # >>> 490154203237518
        ```
        """
        if value is not None:
            if type(value) is not str:
                raise TypeError('ImeiMother value must be a string.')

            return value

        body = StringMother.numeric(min_length=14, max_length=14)
        total = sum(
            (
                int(digit),
                sum(divmod(int(digit) * 2, 10)),
            )[index % 2]
            for index, digit in enumerate(body)
        )
        check_digit = (10 - total % 10) % 10

        return f'{body}{check_digit}'

    @classmethod
    def invalid_value(cls) -> str:
        """
        Create an invalid International Mobile Equipment Identity value.

        Returns:
            str: Invalid International Mobile Equipment Identity string.
        """
        return StringMother.invalid_value()
