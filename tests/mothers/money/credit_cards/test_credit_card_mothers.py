"""
Tests for credit card mothers.
"""

from pytest import mark, raises as assert_raises

from object_mother_pattern.mothers import (
    AmexCreditCardMother,
    CreditCardBrand,
    CreditCardMother,
    DiscoverCreditCardMother,
    MastercardCreditCardMother,
    VisaCreditCardMother,
)
from object_mother_pattern.mothers.primitives import IntegerMother


def _luhn_is_valid(number: str) -> bool:
    digits = [int(char) for char in number if char.isdigit()]
    checksum = 0
    parity = len(digits) % 2
    for idx, digit in enumerate(digits):
        if idx % 2 == parity:
            digit *= 2
            if digit > 9:
                digit -= 9
        checksum += digit
    return checksum % 10 == 0


@mark.unit_testing
def test_amex_credit_card_mother_create() -> None:
    value = AmexCreditCardMother.create()

    assert len(value) == 15
    assert value.startswith(('34', '37'))
    assert value.isdigit()
    assert _luhn_is_valid(value)


@mark.unit_testing
def test_discover_credit_card_mother_create() -> None:
    value = DiscoverCreditCardMother.create()

    assert len(value) == 16
    assert value.startswith(('6011', '65', '64'))
    assert value.isdigit()
    assert _luhn_is_valid(value)


@mark.unit_testing
def test_mastercard_credit_card_mother_create() -> None:
    value = MastercardCreditCardMother.create()

    assert len(value) == 16
    assert value[:2].isdigit()
    assert value.isdigit()
    assert _luhn_is_valid(value)


@mark.unit_testing
def test_visa_credit_card_mother_create() -> None:
    value = VisaCreditCardMother.create()

    assert len(value) in (13, 16)
    assert value.startswith('4')
    assert value.isdigit()
    assert _luhn_is_valid(value)


@mark.unit_testing
def test_credit_card_mother_random_network() -> None:
    for _ in range(5):
        value = CreditCardMother.create()
        assert len(value) in (13, 15, 16)
        assert value.isdigit()
        assert _luhn_is_valid(value)


@mark.unit_testing
def test_credit_card_mother_choose_brand() -> None:
    value = CreditCardMother.create(brand=CreditCardBrand.VISA)
    assert value.startswith('4')

    value2 = CreditCardMother.create(brand='amex')
    assert value2.startswith(('34', '37'))
    assert len(value2) == 15


@mark.unit_testing
def test_credit_card_mother_exclude_all_brands() -> None:
    with assert_raises(
        expected_exception=ValueError,
        match='cannot exclude all',
    ):
        CreditCardMother.create(exclude=tuple(CreditCardBrand))


@mark.unit_testing
def test_credit_card_mother_invalid_brand_type() -> None:
    with assert_raises(
        expected_exception=TypeError,
        match='CreditCardMother brand must be a CreditCardBrand or string.',
    ):
        CreditCardMother.create(brand=IntegerMother.invalid_type())


@mark.unit_testing
def test_credit_card_mother_with_value() -> None:
    raw = '4111111111111111'
    assert CreditCardMother.create(value=raw) == raw


@mark.unit_testing
def test_credit_card_mother_invalid_type() -> None:
    with assert_raises(
        expected_exception=TypeError,
        match='CreditCardMother value must be a string.',
    ):
        CreditCardMother.create(value=IntegerMother.invalid_type())


@mark.unit_testing
def test_credit_card_mother_invalid_value() -> None:
    invalid = CreditCardMother.invalid_value()
    assert type(invalid) is str
    if invalid.isdigit():
        assert not _luhn_is_valid(invalid)
