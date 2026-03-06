"""
Credit card network enumeration.
"""

from enum import StrEnum, unique


@unique
class CreditCardBrand(StrEnum):
    """
    Supported credit card brands.
    """

    VISA = 'visa'
    MASTERCARD = 'mastercard'
    AMEX = 'amex'
    DISCOVER = 'discover'
