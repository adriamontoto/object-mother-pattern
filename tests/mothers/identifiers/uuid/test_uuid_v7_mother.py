"""
Test module for the UuidV7Mother class.
"""

from uuid import UUID

from pytest import mark, raises as assert_raises

from object_mother_pattern.mothers.identifiers import UuidMother, UuidV7Mother


@mark.unit_testing
def test_uuid7_mother_happy_path() -> None:
    """
    Test UuidV7Mother happy path.
    """
    value = UuidV7Mother.create()

    assert isinstance(value, UUID)
    assert value.version == 7


@mark.unit_testing
def test_uuid7_mother_value() -> None:
    """
    Test UuidV7Mother create method with value.
    """
    value = UuidV7Mother.create()

    assert UuidV7Mother.create(value=value) == value


@mark.unit_testing
def test_uuid7_mother_invalid_type() -> None:
    """
    Test UuidV7Mother create method with invalid type.
    """
    assert type(UuidV7Mother.invalid_type()) is not UUID


@mark.unit_testing
def test_uuid7_mother_invalid_value_type() -> None:
    """
    Test UuidV7Mother create method with invalid value type.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='UuidV7Mother value must be a UUID.',
    ):
        UuidV7Mother.create(value=UuidV7Mother.invalid_type())


@mark.unit_testing
def test_uuid7_mother_invalid_uuid_version() -> None:
    """
    Test UuidV7Mother create method with invalid UUID version.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='UuidV7Mother value must be a UUID7.',
    ):
        UuidV7Mother.create(value=UuidMother.create(exclude_versions={7}))
