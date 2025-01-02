"""
Test module for the UUIDMother class.
"""

from uuid import UUID

from pytest import raises as assert_raises

from object_mother_pattern.mothers import UUIDMother


def test_uuid_mother_happy_path() -> None:
    """
    Test UUIDMother happy path.
    """
    value = UUIDMother.create()

    assert type(value) is UUID


def test_uuid_mother_value() -> None:
    """
    Test UUIDMother create method with value.
    """
    value = UUIDMother.create()

    assert UUIDMother.create(value=value) == value


def test_uuid_mother_invalid_type() -> None:
    """
    Test UUIDMother create method with invalid type.
    """
    assert type(UUIDMother.invalid_type()) is not UUID


def test_uuid_mother_invalid_value_type() -> None:
    """
    Test UUIDMother create method with invalid value type.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='UUIDMother value must be a UUID.',
    ):
        UUIDMother.create(value=UUIDMother.invalid_type())
