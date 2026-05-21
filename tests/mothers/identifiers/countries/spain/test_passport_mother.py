"""
Test module for the PassportMother class.
"""

from pytest import mark, raises as assert_raises
from value_object_pattern.usables.identifiers.world.europe.spain import PassportValueObject

from object_mother_pattern.mothers import StringCase, StringMother
from object_mother_pattern.mothers.identifiers.countries.spain import PassportMother


@mark.unit_testing
def test_passport_mother_create_method_happy_path() -> None:
    """
    Check that PassportMother create method returns a valid Spanish passport.
    """
    value = PassportMother.create()

    assert type(value) is str
    assert PassportValueObject(value=value).value


@mark.unit_testing
def test_passport_mother_create_method_value() -> None:
    """
    Check that PassportMother create method returns the provided value.
    """
    value = PassportMother.create()

    assert PassportMother.create(value=value) == value


@mark.unit_testing
def test_passport_mother_create_method_invalid_value_type() -> None:
    """
    Check that PassportMother create method raises a TypeError when the provided value is not a string.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='PassportMother value must be a string.',
    ):
        PassportMother.create(value=PassportMother.invalid_type())


@mark.unit_testing
def test_passport_mother_create_method_lowercase_case() -> None:
    """
    Check that PassportMother create method returns lowercase letters when lowercase case is requested.
    """
    value = PassportMother.create(string_case=StringCase.LOWERCASE)

    assert PassportValueObject(value=value).value
    assert value == value.lower()


@mark.unit_testing
def test_passport_mother_create_method_uppercase_case() -> None:
    """
    Check that PassportMother create method returns uppercase letters when uppercase case is requested.
    """
    value = PassportMother.create(string_case=StringCase.UPPERCASE)

    assert PassportValueObject(value=value).value
    assert value == value.upper()


@mark.unit_testing
def test_passport_mother_create_method_mixed_case() -> None:
    """
    Check that PassportMother create method returns a valid passport when mixed case is requested.
    """
    value = PassportMother.create(string_case=StringCase.MIXEDCASE)

    assert PassportValueObject(value=value).value
    assert value.isalnum()


@mark.unit_testing
def test_passport_mother_create_method_invalid_case() -> None:
    """
    Check that PassportMother create method raises a TypeError when string_case is not a StringCase.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='PassportMother string_case must be a StringCase.',
    ):
        PassportMother.create(string_case=StringMother.invalid_type())


@mark.unit_testing
def test_passport_mother_invalid_type_method() -> None:
    """
    Check that PassportMother invalid_type method returns a non-string value.
    """
    assert type(PassportMother.invalid_type()) is not str


@mark.unit_testing
def test_passport_mother_invalid_value_method() -> None:
    """
    Check that PassportMother invalid_value method returns an invalid Spanish passport.
    """
    value = PassportMother.invalid_value()

    assert type(value) is str
    assert not value.isprintable()
