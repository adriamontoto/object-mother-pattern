"""
Test module for the BoolMother class.
"""

from pytest import raises as assert_raises

from object_mother_pattern.mothers import BoolMother


def test_bool_mother_happy_path() -> None:
    """
    Test BoolMother happy path.
    """
    value = BoolMother.create()

    assert type(value) is bool


def test_bool_mother_value() -> None:
    """
    Test BoolMother create method with value.
    """
    value = BoolMother.create()

    assert BoolMother.create(value=value) == value


def test_bool_mother_invalid_type() -> None:
    """
    Test BoolMother create method with invalid type.
    """
    assert type(BoolMother.invalid_type()) is not bool


def test_bool_mother_invalid_value_type() -> None:
    """
    Test BoolMother create method with invalid value type.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='BoolMother value must be a boolean.',
    ):
        BoolMother.create(value=BoolMother.invalid_type())
