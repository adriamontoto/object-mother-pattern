"""
Test module for the BooleanMother class.
"""

from pytest import mark, raises as assert_raises

from object_mother_pattern.mothers import BooleanMother


@mark.unit_testing
def test_bool_mother_happy_path() -> None:
    """
    Test BooleanMother happy path.
    """
    value = BooleanMother.create()

    assert type(value) is bool


@mark.unit_testing
def test_bool_mother_value() -> None:
    """
    Test BooleanMother create method with value.
    """
    value = BooleanMother.create()

    assert BooleanMother.create(value=value) == value


@mark.unit_testing
def test_bool_mother_true_method() -> None:
    """
    Test BooleanMother true method.
    """
    assert BooleanMother.true() is True


@mark.unit_testing
def test_bool_mother_false_method() -> None:
    """
    Test BooleanMother false method.
    """
    assert BooleanMother.false() is False


@mark.unit_testing
def test_bool_mother_invalid_type() -> None:
    """
    Test BooleanMother create method with invalid type.
    """
    assert type(BooleanMother.invalid_type()) is not bool


@mark.unit_testing
def test_bool_mother_invalid_value_type() -> None:
    """
    Test BooleanMother create method with invalid value type.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='BooleanMother value must be a boolean.',
    ):
        BooleanMother.create(value=BooleanMother.invalid_type())
