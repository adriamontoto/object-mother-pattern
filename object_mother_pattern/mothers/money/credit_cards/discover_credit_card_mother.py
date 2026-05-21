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
    DiscoverCreditCardMother generates Discover card numbers.
    """

    _PREFIXES: tuple[str, ...] = ('6011', '65', *(str(prefix) for prefix in range(644, 650)))
    _LENGTH: int = 16

    @classmethod
    @override
    def create(cls, *, value: str | None = None) -> str:
        """
        Create a random Discover card number or return the provided value.
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
        Create an invalid Discover card number.
        """
        return StringMother.invalid_value()
