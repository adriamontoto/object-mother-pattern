"""
Test module for the UuidV6Mother class.
"""

from uuid import UUID

from pytest import mark, raises as assert_raises

from object_mother_pattern.mothers.identifiers import UuidMother, UuidV6Mother


@mark.unit_testing
def test_uuid6_mother_happy_path() -> None:
    """
    Test UuidV6Mother happy path.
    """
    value = UuidV6Mother.create()

    assert isinstance(value, UUID)
    assert value.version == 6


@mark.unit_testing
def test_uuid6_mother_value() -> None:
    """
    Test UuidV6Mother create method with value.
    """
    value = UuidV6Mother.create()

    assert UuidV6Mother.create(value=value) == value


@mark.unit_testing
def test_uuid6_mother_invalid_type() -> None:
    """
    Test UuidV6Mother create method with invalid type.
    """
    assert type(UuidV6Mother.invalid_type()) is not UUID


@mark.unit_testing
def test_uuid6_mother_invalid_value_type() -> None:
    """
    Test UuidV6Mother create method with invalid value type.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='UuidV6Mother value must be a UUID.',
    ):
        UuidV6Mother.create(value=UuidV6Mother.invalid_type())


@mark.unit_testing
def test_uuid6_mother_invalid_uuid_version() -> None:
    """
    Test UuidV6Mother create method with invalid UUID version.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='UuidV6Mother value must be a UUID6.',
    ):
        UuidV6Mother.create(value=UuidMother.create(exclude_versions={6}))
