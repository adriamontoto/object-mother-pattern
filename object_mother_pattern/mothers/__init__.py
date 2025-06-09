from enum import StrEnum, unique

from .base_mother import BaseMother
from .dates import DateMother, DatetimeMother, StringDateMother, StringDatetimeMother
from .enumeration_mother import EnumerationMother
from .identifiers import StringUuidMother, UuidMother
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
    'BaseMother',
    'BooleanMother',
    'BytesMother',
    'DateMother',
    'DatetimeMother',
    'EnumerationMother',
    'FloatMother',
    'IntegerMother',
    'StringCase',
    'StringDateMother',
    'StringDatetimeMother',
    'StringMother',
    'StringUuidMother',
    'UuidMother',
)
