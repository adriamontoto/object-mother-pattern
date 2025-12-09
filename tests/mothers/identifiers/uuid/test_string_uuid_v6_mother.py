"""
Test module for the StringUuidMother class.
"""

from uuid import UUID

from pytest import mark, raises as assert_raises

from object_mother_pattern.mothers import StringMother
from object_mother_pattern.mothers.identifiers import StringUuidV6Mother, UuidMother


@mark.unit_testing
def test_string_uuid6_mother_happy_path() -> None:
    """
    Test StringUuidMother happy path.
    """
    value = StringUuidV6Mother.create()

    assert type(value) is str
    assert UUID(value).version == 6


@mark.unit_testing
def test_string_uuid6_mother_value() -> None:
    """
    Test StringUuidMother create method with value.
    """
    value = StringUuidV6Mother.create()

    assert StringUuidV6Mother.create(value=value) == value


@mark.unit_testing
def test_string_uuid6_mother_invalid_type() -> None:
    """
    Test StringUuidMother create method with invalid type.
    """
    assert type(StringUuidV6Mother.invalid_type()) is not str


@mark.unit_testing
def test_string_uuid6_mother_invalid_value() -> None:
    """
    Test StringUuidMother invalid_value method.
    """
    value = StringUuidV6Mother.invalid_value()

    assert type(value) is str
    assert not value.isprintable()


@mark.unit_testing
def test_string_uuid6_mother_invalid_value_type() -> None:
    """
    Test StringUuidMother create method with invalid value type.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='StringUuidV6Mother value must be a string.',
    ):
        StringUuidV6Mother.create(value=StringUuidV6Mother.invalid_type())


@mark.unit_testing
def test_string_uuid6_mother_not_uuid_value() -> None:
    """
    Test StringUuidV6Mother create method with invalid value type.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='StringUuidV6Mother value must be a UUID.',
    ):
        StringUuidV6Mother.create(value=StringMother.create())


@mark.unit_testing
def test_string_uuid6_mother_invalid_uuid_version() -> None:
    """
    Test UuidV6Mother create method with invalid UUID version.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='UuidV6Mother value must be a UUID6.',
    ):
        StringUuidV6Mother.create(value=str(UuidMother.create(exclude_versions={6})))
