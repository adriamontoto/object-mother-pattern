from enum import StrEnum, unique

from .dates import DateMother, DatetimeMother, StringDateMother, StringDatetimeMother
from .primitives import BooleanMother, BytesMother, FloatMother, IntegerMother, StringMother


@unique
class StringCase(StrEnum):
    """
    Type of string case.
    """

    LOWERCASE = 'lowercase'
    UPPERCASE = 'uppercase'
    MIXEDCASE = 'mixedcase'


__all__ = (
    'BooleanMother',
    'BytesMother',
    'DateMother',
    'DatetimeMother',
    'FloatMother',
    'IntegerMother',
    'StringCase',
    'StringDateMother',
    'StringDatetimeMother',
    'StringMother',
)
