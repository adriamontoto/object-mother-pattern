"""
DiscoverCreditCardMother module.
"""

from sys import version_info

if version_info >= (3, 12):
    from typing import override  # pragma: no cover
else:
    from typing_extensions import override  # pragma: no cover

from object_mother_pattern.models import BaseMother
from object_mother_pattern.mothers.primitives.string_mother import StringMother

from ._helpers import _generate_luhn_number, _pick_prefix


class DiscoverCreditCardMother(BaseMother[str]):
    """
    DiscoverCreditCardMother generates Discover card numbers.
    """

    _PREFIXES: tuple[str, ...] = ('6011', '65') + tuple(str(prefix) for prefix in range(644, 650))
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

        prefix = _pick_prefix(cls._PREFIXES)
        return _generate_luhn_number(prefix=prefix, length=cls._LENGTH)

    @classmethod
    def invalid_value(cls) -> str:
        """
        Create an invalid Discover card number.
        """
        return StringMother.invalid_value()
