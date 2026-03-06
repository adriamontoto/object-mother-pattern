"""
Tests for IbanMother.
"""

from pytest import mark, raises as assert_raises

from object_mother_pattern.mothers import IbanMother
from object_mother_pattern.mothers.primitives import IntegerMother


def _iban_is_valid(iban: str) -> bool:
    if len(iban) < 4:
        return False

    rearranged = f'{iban[4:]}{iban[:4]}'
    remainder = 0
    for char in rearranged:
        numeric = str(ord(char) - 55) if char.isalpha() else char
        for digit in numeric:
            remainder = (remainder * 10 + int(digit)) % 97

    return remainder == 1


@mark.unit_testing
def test_iban_mother_create_happy_path() -> None:
    value = IbanMother.create()

    assert type(value) is str
    assert value[:2].isalpha()
    assert value.isalnum()
    assert _iban_is_valid(value)


@mark.unit_testing
def test_iban_mother_with_country_code() -> None:
    value = IbanMother.create(country_code='DE')

    assert value.startswith('DE')
    assert len(value) == 22
    assert _iban_is_valid(value)


@mark.unit_testing
def test_iban_mother_invalid_country_code() -> None:
    with assert_raises(
        expected_exception=ValueError,
        match='IbanMother country_code must be one of',
    ):
        IbanMother.create(country_code='ZZ')


@mark.unit_testing
def test_iban_mother_invalid_type() -> None:
    with assert_raises(
        expected_exception=TypeError,
        match='IbanMother value must be a string.',
    ):
        IbanMother.create(value=IntegerMother.invalid_type())


@mark.unit_testing
def test_iban_mother_invalid_value() -> None:
    invalid = IbanMother.invalid_value()
    assert type(invalid) is str
    if len(invalid) >= 4 and invalid[:2].isalpha():
        assert not _iban_is_valid(invalid)
