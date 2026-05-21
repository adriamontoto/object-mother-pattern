"""
DiscoverCreditCardMother module.
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


class DiscoverCreditCardMother(BaseMother[str]):
    """
    Generate Discover-like card numbers for tests.

    Generated values use Discover prefixes and lengths, then compute a Luhn-valid number. Passing `value` returns the
    explicit value after type validation for deterministic tests.
    """

    _PREFIXES: tuple[str, ...] = ('6011', '65', *(str(prefix) for prefix in range(644, 650)))
    _LENGTH: int = 16

    @classmethod
    @override
    def create(cls, *, value: str | None = None) -> str:
        """
        Create a random Discover card number or return the provided value.

        Args:
            value (str | None): Explicit card number to validate and return.

        Raises:
            TypeError: If `value` is not a string.

        Returns:
            str: Explicit or generated Discover-like card number.
        """
        if value is not None:
            if type(value) is not str:
                raise TypeError('DiscoverCreditCardMother value must be a string.')
            return value

        prefix = choice(seq=cls._PREFIXES)  # noqa: S311
        return generate_luhn_number(prefix=prefix, length=cls._LENGTH)

    @classmethod
    def invalid_value(cls) -> str:
        """
        Create an invalid Discover card number for negative-path tests.

        Returns:
            str: Invalid card-number value.
        """
        return StringMother.invalid_value()
