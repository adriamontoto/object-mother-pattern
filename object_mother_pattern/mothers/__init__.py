from enum import StrEnum, unique


@unique
class StringCase(StrEnum):
    """
    Type of string case.
    """

    LOWERCASE = 'lowercase'
    UPPERCASE = 'uppercase'
    MIXEDCASE = 'mixedcase'


from .dates import DateMother, DatetimeMother, StringDateMother, StringDatetimeMother  # noqa: E402
from .money import (  # noqa: E402
    AmexCreditCardMother,
    BtcWalletMother,
    CreditCardBrand,
    CreditCardMother,
    DiscoverCreditCardMother,
    IbanMother,
    MastercardCreditCardMother,
    VisaCreditCardMother,
)
from .primitives import BooleanMother, BytesMother, FloatMother, IntegerMother, StringMother  # noqa: E402

__all__ = (
    'AmexCreditCardMother',
    'BooleanMother',
    'BtcWalletMother',
    'BytesMother',
    'CreditCardBrand',
    'CreditCardMother',
    'DateMother',
    'DatetimeMother',
    'DiscoverCreditCardMother',
    'FloatMother',
    'IbanMother',
    'IntegerMother',
    'MastercardCreditCardMother',
    'StringCase',
    'StringDateMother',
    'StringDatetimeMother',
    'StringMother',
    'VisaCreditCardMother',
)
