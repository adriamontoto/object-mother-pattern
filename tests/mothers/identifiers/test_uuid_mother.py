"""
Test module for the UuidMother class.
"""

from uuid import UUID

from pytest import raises as assert_raises

from object_mother_pattern.mothers import UuidMother


def test_uuid_mother_happy_path() -> None:
    """
    Test UuidMother happy path.
    """
    value = UuidMother.create()

    assert type(value) is UUID


def test_uuid_mother_value() -> None:
    """
    Test UuidMother create method with value.
    """
    value = UuidMother.create()

    assert UuidMother.create(value=value) == value


def test_uuid_mother_invalid_type() -> None:
    """
    Test UuidMother create method with invalid type.
    """
    assert type(UuidMother.invalid_type()) is not UUID


def test_uuid_mother_invalid_value_type() -> None:
    """
    Test UuidMother create method with invalid value type.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='UuidMother value must be a UUID.',
    ):
        UuidMother.create(value=UuidMother.invalid_type())
