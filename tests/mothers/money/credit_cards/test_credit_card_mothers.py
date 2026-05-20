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


def _luhn_is_valid(number: str) -> bool:
    """
    Check whether a number satisfies the Luhn checksum algorithm.
    """
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
    """
    Check that AmexCreditCardMother creates valid Amex numbers.
    """
    value = AmexCreditCardMother.create()

    assert len(value) == 15
    assert value.startswith(('34', '37'))
    assert value.isdigit()
    assert _luhn_is_valid(value)


@mark.unit_testing
def test_discover_credit_card_mother_create() -> None:
    """
    Check that DiscoverCreditCardMother creates valid Discover numbers.
    """
    value = DiscoverCreditCardMother.create()

    assert len(value) == 16
    assert value.startswith(('6011', '65', '64'))
    assert value.isdigit()
    assert _luhn_is_valid(value)


@mark.unit_testing
def test_mastercard_credit_card_mother_create() -> None:
    """
    Check that MastercardCreditCardMother creates valid Mastercard numbers.
    """
    value = MastercardCreditCardMother.create()

    assert len(value) == 16
    assert value[:2].isdigit()
    assert value.isdigit()
    assert _luhn_is_valid(value)


@mark.unit_testing
def test_visa_credit_card_mother_create() -> None:
    """
    Check that VisaCreditCardMother creates valid Visa numbers.
    """
    value = VisaCreditCardMother.create()

    assert len(value) in (13, 16)
    assert value.startswith('4')
    assert value.isdigit()
    assert _luhn_is_valid(value)


@mark.unit_testing
def test_credit_card_mother_random_network() -> None:
    """
    Check that CreditCardMother randomly creates supported valid card numbers.
    """
    for _ in range(5):
        value = CreditCardMother.create()
        assert len(value) in (13, 15, 16)
        assert value.isdigit()
        assert _luhn_is_valid(value)


@mark.unit_testing
def test_credit_card_mother_choose_brand() -> None:
    """
    Check that CreditCardMother creates numbers for requested brands.
    """
    value = CreditCardMother.create(brand=CreditCardBrand.VISA)
    assert value.startswith('4')

    value2 = CreditCardMother.create(brand='amex')
    assert value2.startswith(('34', '37'))
    assert len(value2) == 15

    value3 = CreditCardMother.create(brand=CreditCardBrand.MASTERCARD)
    assert len(value3) == 16
    assert _luhn_is_valid(value3)

    value4 = CreditCardMother.create(brand=CreditCardBrand.DISCOVER)
    assert value4.startswith(('6011', '65', '64'))


@mark.unit_testing
def test_credit_card_mother_private_brand_dispatcher_no_match() -> None:
    """
    Check the private brand dispatcher fallback branch.
    """
    CreditCardMother._mother_for_brand(brand=object())  # type: ignore[arg-type]


@mark.unit_testing
def test_credit_card_mother_exclude_all_brands() -> None:
    """
    Check that CreditCardMother rejects excluding every brand.
    """
    with assert_raises(
        expected_exception=ValueError,
        match='cannot exclude all',
    ):
        CreditCardMother.create(exclude=tuple(CreditCardBrand))


@mark.unit_testing
def test_credit_card_mother_exclude_specific_brand() -> None:
    """
    Check that CreditCardMother rejects a brand that was excluded.
    """
    with assert_raises(
        expected_exception=ValueError,
        match='CreditCardMother brand is excluded.',
    ):
        CreditCardMother.create(brand=CreditCardBrand.VISA, exclude=(CreditCardBrand.VISA,))


@mark.unit_testing
def test_credit_card_mother_invalid_brand_type() -> None:
    """
    Check that CreditCardMother rejects invalid brand types.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='CreditCardMother brand must be a CreditCardBrand or string.',
    ):
        CreditCardMother.create(brand=CreditCardMother.invalid_type())


@mark.unit_testing
def test_credit_card_mother_invalid_brand_value() -> None:
    """
    Check that CreditCardMother rejects unknown brand values.
    """
    with assert_raises(
        expected_exception=ValueError,
        match='CreditCardMother brand must be one of',
    ):
        CreditCardMother.create(brand='unknown')


@mark.unit_testing
def test_credit_card_mother_with_value() -> None:
    """
    Check that CreditCardMother returns a provided value.
    """
    raw = '4111111111111111'
    assert CreditCardMother.create(value=raw) == raw


@mark.unit_testing
def test_credit_card_mother_invalid_type() -> None:
    """
    Check that CreditCardMother rejects non-string values.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='CreditCardMother value must be a string.',
    ):
        CreditCardMother.create(value=CreditCardMother.invalid_type())


@mark.unit_testing
def test_credit_card_mother_invalid_value() -> None:
    """
    Check that CreditCardMother invalid_value returns an invalid candidate.
    """
    invalid = CreditCardMother.invalid_value()
    assert type(invalid) is str
    if invalid.isdigit():
        assert not _luhn_is_valid(invalid)


@mark.unit_testing
def test_specific_credit_card_mothers_with_value() -> None:
    """
    Check that specific card mothers return provided values.
    """
    assert AmexCreditCardMother.create(value='371449635398431') == '371449635398431'
    assert DiscoverCreditCardMother.create(value='6011111111111117') == '6011111111111117'
    assert MastercardCreditCardMother.create(value='5555555555554444') == '5555555555554444'
    assert VisaCreditCardMother.create(value='4111111111111111') == '4111111111111111'


@mark.unit_testing
def test_specific_credit_card_mothers_invalid_type() -> None:
    """
    Check that specific card mothers reject non-string values.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='AmexCreditCardMother value must be a string.',
    ):
        AmexCreditCardMother.create(value=AmexCreditCardMother.invalid_type())

    with assert_raises(
        expected_exception=TypeError,
        match='DiscoverCreditCardMother value must be a string.',
    ):
        DiscoverCreditCardMother.create(value=DiscoverCreditCardMother.invalid_type())

    with assert_raises(
        expected_exception=TypeError,
        match='MastercardCreditCardMother value must be a string.',
    ):
        MastercardCreditCardMother.create(value=MastercardCreditCardMother.invalid_type())

    with assert_raises(
        expected_exception=TypeError,
        match='VisaCreditCardMother value must be a string.',
    ):
        VisaCreditCardMother.create(value=VisaCreditCardMother.invalid_type())


@mark.unit_testing
def test_specific_credit_card_mothers_invalid_value() -> None:
    """
    Check that specific card mother invalid_value methods return strings.
    """
    assert type(AmexCreditCardMother.invalid_value()) is str
    assert type(DiscoverCreditCardMother.invalid_value()) is str
    assert type(MastercardCreditCardMother.invalid_value()) is str
    assert type(VisaCreditCardMother.invalid_value()) is str
