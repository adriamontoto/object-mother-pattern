"""
VisaCreditCardMother module.
"""

from sys import version_info

if version_info >= (3, 12):
    from typing import override  # pragma: no cover
else:
    from typing_extensions import override  # pragma: no cover

from object_mother_pattern.models import BaseMother
from object_mother_pattern.mothers.primitives.string_mother import StringMother

from ._helpers import _generate_luhn_number, _pick_prefix


class VisaCreditCardMother(BaseMother[str]):
    """
    VisaCreditCardMother generates Visa card numbers.
    """

    _PREFIXES: tuple[str, ...] = ('4',)
    _LENGTHS: tuple[int, ...] = (16, 13)

    @classmethod
    @override
    def create(cls, *, value: str | None = None) -> str:
        """
        Create a random Visa card number or return the provided value.
        """
        if value is not None:
            if type(value) is not str:
                raise TypeError('VisaCreditCardMother value must be a string.')
            return value

        prefix = _pick_prefix(cls._PREFIXES)
        length = int(_pick_prefix(tuple(str(length) for length in cls._LENGTHS)))
        return _generate_luhn_number(prefix=prefix, length=length)

    @classmethod
    def invalid_value(cls) -> str:
        """
        Create an invalid Visa card number.
        """
        return StringMother.invalid_value()
