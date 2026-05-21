"""
CreditCardMother module.
"""

from sys import version_info

if version_info >= (3, 12):
    from typing import override  # pragma: no cover
else:
    from typing_extensions import override  # pragma: no cover


from random import choice
from typing import Iterable

from object_mother_pattern.models import BaseMother
from object_mother_pattern.mothers.primitives.string_mother import StringMother

from .amex_credit_card_mother import AmexCreditCardMother
from .credit_card_brand import CreditCardBrand
from .discover_credit_card_mother import DiscoverCreditCardMother
from .mastercard_credit_card_mother import MastercardCreditCardMother
from .visa_credit_card_mother import VisaCreditCardMother


class CreditCardMother(BaseMother[str]):
    """
    CreditCardMother randomly generates a card number from the supported networks
    (Visa, Mastercard, American Express, Discover).
    """

    _NETWORK_MOTHERS = (
        VisaCreditCardMother,
        MastercardCreditCardMother,
        AmexCreditCardMother,
        DiscoverCreditCardMother,
    )

    @classmethod
    @override
    def create(
        cls,
        *,
        value: str | None = None,
        brand: CreditCardBrand | str | None = None,
        exclude: Iterable[CreditCardBrand | str] | None = None,
    ) -> str:
        """
        Create a random credit card number or return the provided value.

        Args:
            value: Optional concrete number to return.
            brand: Target network (enum or string); if omitted, a random brand is chosen.
            exclude: Brands to skip when picking randomly.
        """
        if value is not None:
            if type(value) is not str:
                raise TypeError('CreditCardMother value must be a string.')
            return value

        available = cls._filtered_brands(exclude)

        if brand is None:
            brand_to_use = choice(seq=available)  # noqa: S311
        else:
            brand_to_use = cls._coerce_brand(brand)
            if brand_to_use not in available:
                raise ValueError('CreditCardMother brand is excluded.')

        return cls._mother_for_brand(brand_to_use).create()

    @classmethod
    def invalid_value(cls) -> str:
        """
        Create an invalid credit card number.
        """
        return StringMother.invalid_value()

    @classmethod
    def _filtered_brands(cls, exclude: Iterable[CreditCardBrand | str] | None) -> tuple[CreditCardBrand, ...]:
        brands = tuple(CreditCardBrand)
        if exclude is None:
            return brands

        excluded: set[CreditCardBrand] = {cls._coerce_brand(item) for item in exclude}
        remaining = tuple(brand for brand in brands if brand not in excluded)
        if not remaining:
            raise ValueError('CreditCardMother cannot exclude all brands.')
        return remaining

    @staticmethod
    def _coerce_brand(value: CreditCardBrand | str) -> CreditCardBrand:
        if isinstance(value, CreditCardBrand):
            return value
        if type(value) is not str:
            raise TypeError('CreditCardMother brand must be a CreditCardBrand or string.')

        try:
            return CreditCardBrand(value.lower())
        except ValueError as exc:
            raise ValueError(f'CreditCardMother brand must be one of {[b.value for b in CreditCardBrand]}.') from exc

    @staticmethod
    def _mother_for_brand(brand: CreditCardBrand) -> type[BaseMother[str]]:
        match brand:
            case CreditCardBrand.VISA:
                return VisaCreditCardMother
            case CreditCardBrand.MASTERCARD:
                return MastercardCreditCardMother
            case CreditCardBrand.AMEX:
                return AmexCreditCardMother
            case CreditCardBrand.DISCOVER:
                return DiscoverCreditCardMother
        # pragma: no cover
