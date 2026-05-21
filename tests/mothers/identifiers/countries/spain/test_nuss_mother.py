"""
Test module for the NussMother class.
"""

from pytest import mark, raises as assert_raises
from value_object_pattern.usables.identifiers.world.europe.spain import NussValueObject

from object_mother_pattern.mothers.identifiers.countries.spain import NussMother


@mark.unit_testing
def test_nuss_mother_create_method_happy_path() -> None:
    """
    Check that NussMother create method returns a valid Spanish Social Security Number.
    """
    value = NussMother.create()

    assert type(value) is str
    assert NussValueObject(value=value).value == value


@mark.unit_testing
def test_nuss_mother_create_method_value() -> None:
    """
    Check that NussMother create method returns the provided value.
    """
    value = NussMother.create()

    assert NussMother.create(value=value) == value


@mark.unit_testing
def test_nuss_mother_create_method_invalid_value_type() -> None:
    """
    Check that NussMother create method raises a TypeError when the provided value is not a string.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='NussMother value must be a string.',
    ):
        NussMother.create(value=NussMother.invalid_type())


@mark.unit_testing
def test_nuss_mother_invalid_type_method() -> None:
    """
    Check that NussMother invalid_type method returns a non-string value.
    """
    assert type(NussMother.invalid_type()) is not str


@mark.unit_testing
def test_nuss_mother_invalid_value_method() -> None:
    """
    Check that NussMother invalid_value method returns an invalid Spanish Social Security Number.
    """
    value = NussMother.invalid_value()

    assert type(value) is str
    assert not value.isprintable()
