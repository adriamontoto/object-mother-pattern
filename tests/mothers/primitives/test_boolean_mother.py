"""
Test module for the BooleanMother class.
"""

from pytest import mark, raises as assert_raises

from object_mother_pattern.mothers import BooleanMother


@mark.unit_testing
def test_boolean_mother_create_method_happy_path() -> None:
    """
    Check that BooleanMother create method returns a boolean value.
    """
    value = BooleanMother.create()

    assert type(value) is bool


@mark.unit_testing
def test_boolean_mother_create_method_value() -> None:
    """
    Check that BooleanMother create method returns the provided value.
    """
    value = BooleanMother.create()

    assert BooleanMother.create(value=value) == value


@mark.unit_testing
def test_boolean_mother_create_method_invalid_value_type() -> None:
    """
    Check that BooleanMother create method raises a TypeError when the provided value is not a boolean.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='BooleanMother value must be a boolean.',
    ):
        BooleanMother.create(value=BooleanMother.invalid_type())


@mark.unit_testing
def test_boolean_mother_true_method_happy_path() -> None:
    """
    Check that BooleanMother true method returns True.
    """
    assert BooleanMother.true() is True


@mark.unit_testing
def test_boolean_mother_false_method_happy_path() -> None:
    """
    Check that BooleanMother false method returns False.
    """
    assert BooleanMother.false() is False


@mark.unit_testing
def test_boolean_mother_invalid_type_method() -> None:
    """
    Check that BooleanMother invalid_type method returns a value that is not a boolean.
    """
    assert type(BooleanMother.invalid_type()) is not bool
