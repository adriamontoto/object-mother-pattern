"""
Test module for the StringUUIDMother class.
"""

from uuid import UUID

from pytest import raises as assert_raises

from object_mother_pattern.mothers import StringUUIDMother


def test_string_uuid_mother_happy_path() -> None:
    """
    Test StringUUIDMother happy path.
    """
    value = StringUUIDMother.create()

    assert type(value) is str
    UUID(value)


def test_string_uuid_mother_value() -> None:
    """
    Test StringUUIDMother create method with value.
    """
    value = StringUUIDMother.create()

    assert StringUUIDMother.create(value=value) == value


def test_string_uuid_mother_invalid_type() -> None:
    """
    Test StringUUIDMother create method with invalid type.
    """
    assert type(StringUUIDMother.invalid_type()) is not str


def test_string_uuid_mother_invalid_value() -> None:
    """
    Test StringUUIDMother invalid_value method.
    """
    value = StringUUIDMother.invalid_value()

    assert type(value) is str
    assert not value.isprintable()


def test_string_uuid_mother_invalid_value_type() -> None:
    """
    Test StringUUIDMother create method with invalid value type.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='StringUUIDMother value must be a string.',
    ):
        StringUUIDMother.create(value=StringUUIDMother.invalid_type())
