"""
Test module for the StringUuidMother class.
"""

from uuid import UUID

from pytest import mark, raises as assert_raises

from object_mother_pattern.mothers import StringUuidMother


@mark.unit_testing
def test_string_uuid_mother_happy_path() -> None:
    """
    Test StringUuidMother happy path.
    """
    value = StringUuidMother.create()

    assert type(value) is str
    UUID(value)


@mark.unit_testing
def test_string_uuid_mother_value() -> None:
    """
    Test StringUuidMother create method with value.
    """
    value = StringUuidMother.create()

    assert StringUuidMother.create(value=value) == value


@mark.unit_testing
def test_string_uuid_mother_invalid_type() -> None:
    """
    Test StringUuidMother create method with invalid type.
    """
    assert type(StringUuidMother.invalid_type()) is not str


@mark.unit_testing
def test_string_uuid_mother_invalid_value() -> None:
    """
    Test StringUuidMother invalid_value method.
    """
    value = StringUuidMother.invalid_value()

    assert type(value) is str
    assert not value.isprintable()


@mark.unit_testing
def test_string_uuid_mother_invalid_value_type() -> None:
    """
    Test StringUuidMother create method with invalid value type.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='StringUuidMother value must be a string.',
    ):
        StringUuidMother.create(value=StringUuidMother.invalid_type())
