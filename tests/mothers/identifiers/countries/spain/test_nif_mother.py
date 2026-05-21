"""
Test module for the NifMother class.
"""

from pytest import mark, raises as assert_raises
from value_object_pattern.usables.identifiers.world.europe.spain import NifValueObject

from object_mother_pattern.mothers import StringCase, StringMother
from object_mother_pattern.mothers.identifiers.countries.spain import NifMother


@mark.unit_testing
def test_nif_mother_create_method_happy_path() -> None:
    """
    Check that NifMother create method returns a valid Spanish company NIF.
    """
    value = NifMother.create()

    assert type(value) is str
    assert NifValueObject(value=value).value


@mark.unit_testing
def test_nif_mother_create_method_value() -> None:
    """
    Check that NifMother create method returns the provided value.
    """
    value = NifMother.create()

    assert NifMother.create(value=value) == value


@mark.unit_testing
def test_nif_mother_create_method_invalid_value_type() -> None:
    """
    Check that NifMother create method raises a TypeError when the provided value is not a string.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='NifMother value must be a string.',
    ):
        NifMother.create(value=NifMother.invalid_type())


@mark.unit_testing
def test_nif_mother_create_method_lowercase_case() -> None:
    """
    Check that NifMother create method returns lowercase letters when lowercase case is requested.
    """
    value = NifMother.create(string_case=StringCase.LOWERCASE)

    assert NifValueObject(value=value).value
    assert value == value.lower()


@mark.unit_testing
def test_nif_mother_create_method_uppercase_case() -> None:
    """
    Check that NifMother create method returns uppercase letters when uppercase case is requested.
    """
    value = NifMother.create(string_case=StringCase.UPPERCASE)

    assert NifValueObject(value=value).value
    assert value == value.upper()


@mark.unit_testing
def test_nif_mother_create_method_mixed_case() -> None:
    """
    Check that NifMother create method returns a valid NIF when mixed case is requested.
    """
    value = NifMother.create(string_case=StringCase.MIXEDCASE)

    assert NifValueObject(value=value).value
    assert value.isalnum()


@mark.unit_testing
def test_nif_mother_create_method_invalid_case() -> None:
    """
    Check that NifMother create method raises a TypeError when string_case is not a StringCase.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='NifMother string_case must be a StringCase.',
    ):
        NifMother.create(string_case=StringMother.invalid_type())


@mark.unit_testing
def test_nif_mother_create_method_digit_control_first_letter() -> None:
    """
    Check that NifMother create method returns a digit control character for digit-control entity letters.
    """
    value = NifMother.create(first_letter='A')

    assert NifValueObject(value=value).value
    assert value[-1].isdigit()


@mark.unit_testing
def test_nif_mother_create_method_letter_control_first_letter() -> None:
    """
    Check that NifMother create method returns a letter control character for letter-control entity letters.
    """
    value = NifMother.create(first_letter='P')

    assert NifValueObject(value=value).value
    assert value[-1].isalpha()


@mark.unit_testing
def test_nif_mother_create_method_digit_or_letter_control_first_letter() -> None:
    """
    Check that NifMother create method returns a valid control character for flexible entity letters.
    """
    value = NifMother.create(first_letter='C')

    assert NifValueObject(value=value).value
    assert value[-1].isalnum()


@mark.unit_testing
def test_nif_mother_create_method_invalid_first_letter_type() -> None:
    """
    Check that NifMother create method raises a TypeError when first_letter is not a string.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='NifMother first_letter must be a string.',
    ):
        NifMother.create(first_letter=NifMother.invalid_type())


@mark.unit_testing
def test_nif_mother_create_method_invalid_first_letter_value() -> None:
    """
    Check that NifMother create method raises a ValueError when first_letter is not a valid NIF first letter.
    """
    with assert_raises(
        expected_exception=ValueError,
        match='NifMother first_letter must be a valid Spanish company NIF first letter.',
    ):
        NifMother.create(first_letter='I')


@mark.unit_testing
def test_nif_mother_invalid_type_method() -> None:
    """
    Check that NifMother invalid_type method returns a non-string value.
    """
    assert type(NifMother.invalid_type()) is not str


@mark.unit_testing
def test_nif_mother_invalid_value_method() -> None:
    """
    Check that NifMother invalid_value method returns an invalid Spanish company NIF.
    """
    value = NifMother.invalid_value()

    assert type(value) is str
    assert not value.isprintable()
