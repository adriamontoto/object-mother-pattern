"""
Test module for the ImeiMother class.
"""

from pytest import mark, raises as assert_raises
from value_object_pattern.usables.internet.mobile import ImeiValueObject

from object_mother_pattern.mothers.internet import ImeiMother


@mark.unit_testing
def test_imei_mother_create_method_happy_path() -> None:
    """
    Check that ImeiMother create method returns a valid International Mobile Equipment Identity.
    """
    value = ImeiMother.create()

    assert type(value) is str
    assert ImeiValueObject(value=value).value == value


@mark.unit_testing
def test_imei_mother_create_method_value() -> None:
    """
    Check that ImeiMother create method returns the provided value.
    """
    value = ImeiMother.create()

    assert ImeiMother.create(value=value) == value


@mark.unit_testing
def test_imei_mother_create_method_invalid_value_type() -> None:
    """
    Check that ImeiMother create method raises a TypeError when the provided value is not a string.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='ImeiMother value must be a string.',
    ):
        ImeiMother.create(value=ImeiMother.invalid_type())


@mark.unit_testing
def test_imei_mother_invalid_type_method() -> None:
    """
    Check that ImeiMother invalid_type method returns a non-string value.
    """
    assert type(ImeiMother.invalid_type()) is not str


@mark.unit_testing
def test_imei_mother_invalid_value_method() -> None:
    """
    Check that ImeiMother invalid_value method returns an invalid International Mobile Equipment Identity.
    """
    value = ImeiMother.invalid_value()

    assert type(value) is str
    assert not value.isprintable()
