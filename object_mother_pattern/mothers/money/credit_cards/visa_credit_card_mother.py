"""
VisaCreditCardMother module.
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


class VisaCreditCardMother(BaseMother[str]):
    """
    Generate Visa-like card numbers for tests.

    Generated values use Visa prefixes and lengths, then compute a Luhn-valid number. Passing `value` returns the
    explicit value after type validation for deterministic tests.
    """

    _PREFIXES: tuple[str, ...] = ('4',)
    _LENGTHS: tuple[int, ...] = (16, 13)

    @classmethod
    @override
    def create(cls, *, value: str | None = None) -> str:
        """
        Create a random Visa card number or return the provided value.

        Args:
            value (str | None): Explicit card number to validate and return.

        Raises:
            TypeError: If `value` is not a string.

        Returns:
            str: Explicit or generated Visa-like card number.
        """
        if value is not None:
            if type(value) is not str:
                raise TypeError('VisaCreditCardMother value must be a string.')
            return value

        prefix = choice(seq=cls._PREFIXES)  # noqa: S311
        length = int(choice(seq=tuple(str(length) for length in cls._LENGTHS)))  # noqa: S311
        return generate_luhn_number(prefix=prefix, length=length)

    @classmethod
    def invalid_value(cls) -> str:
        """
        Create an invalid Visa card number for negative-path tests.

        Returns:
            str: Invalid card-number value.
        """
        return StringMother.invalid_value()
