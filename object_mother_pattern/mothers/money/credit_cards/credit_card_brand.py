"""
Credit card network enumeration.
"""

from enum import StrEnum, unique


@unique
class CreditCardBrand(StrEnum):
    """
    Supported credit-card brands for generated card values.

    The enum is used by aggregate credit-card mothers to select or exclude a brand while keeping tests explicit about
    the payment network shape they need.
    """

    VISA = 'visa'
    MASTERCARD = 'mastercard'
    AMEX = 'amex'
    DISCOVER = 'discover'
