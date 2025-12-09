"""
Test module for the StringUuidMother class.
"""

from uuid import UUID

from pytest import mark, raises as assert_raises

from object_mother_pattern.mothers import StringMother
from object_mother_pattern.mothers.identifiers import StringUuidV7Mother, UuidMother


@mark.unit_testing
def test_string_uuid7_mother_happy_path() -> None:
    """
    Test StringUuidMother happy path.
    """
    value = StringUuidV7Mother.create()

    assert type(value) is str
    assert UUID(value).version == 7


@mark.unit_testing
def test_string_uuid7_mother_value() -> None:
    """
    Test StringUuidMother create method with value.
    """
    value = StringUuidV7Mother.create()

    assert StringUuidV7Mother.create(value=value) == value


@mark.unit_testing
def test_string_uuid7_mother_invalid_type() -> None:
    """
    Test StringUuidMother create method with invalid type.
    """
    assert type(StringUuidV7Mother.invalid_type()) is not str


@mark.unit_testing
def test_string_uuid7_mother_invalid_value() -> None:
    """
    Test StringUuidMother invalid_value method.
    """
    value = StringUuidV7Mother.invalid_value()

    assert type(value) is str
    assert not value.isprintable()


@mark.unit_testing
def test_string_uuid7_mother_invalid_value_type() -> None:
    """
    Test StringUuidMother create method with invalid value type.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='StringUuidV7Mother value must be a string.',
    ):
        StringUuidV7Mother.create(value=StringUuidV7Mother.invalid_type())


@mark.unit_testing
def test_string_uuid7_mother_not_uuid_value() -> None:
    """
    Test StringUuidV7Mother create method with invalid value type.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='StringUuidV7Mother value must be a UUID.',
    ):
        StringUuidV7Mother.create(value=StringMother.create())


@mark.unit_testing
def test_string_uuid7_mother_invalid_uuid_version() -> None:
    """
    Test UuidV7Mother create method with invalid UUID version.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='UuidV7Mother value must be a UUID7.',
    ):
        StringUuidV7Mother.create(value=str(UuidMother.create(exclude_versions={7})))
