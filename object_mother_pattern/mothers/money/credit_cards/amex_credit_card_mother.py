"""
AmexCreditCardMother module.
"""

from sys import version_info

if version_info >= (3, 12):
    from typing import override  # pragma: no cover
else:
    from typing_extensions import override  # pragma: no cover


from random import choice

from object_mother_pattern.models import BaseMother
from object_mother_pattern.mothers.primitives.string_mother import StringMother

from .utils import generate_luhn_number


class AmexCreditCardMother(BaseMother[str]):
    """
    Generate American Express-like card numbers for tests.

    Generated values use American Express prefixes and lengths, then compute a Luhn-valid number. Passing `value`
    returns the explicit value after type validation for deterministic tests.
    """

    _PREFIXES: tuple[str, ...] = ('34', '37')
    _LENGTH: int = 15

    @classmethod
    @override
    def create(cls, *, value: str | None = None) -> str:
        """
        Create a random American Express card number or return the provided value.

        Args:
            value (str | None): Explicit card number to validate and return.

        Raises:
            TypeError: If `value` is not a string.

        Returns:
            str: Explicit or generated American Express-like card number.
        """
        if value is not None:
            if type(value) is not str:
                raise TypeError('AmexCreditCardMother value must be a string.')
            return value

        prefix = choice(seq=cls._PREFIXES)  # noqa: S311
        return generate_luhn_number(prefix=prefix, length=cls._LENGTH)

    @classmethod
    def invalid_value(cls) -> str:
        """
        Create an invalid American Express card number for negative-path tests.

        Returns:
            str: Invalid card-number value.
        """
        return StringMother.invalid_value()
