"""
Test module for the UuidV4Mother class.
"""

from uuid import UUID

from pytest import mark, raises as assert_raises

from object_mother_pattern.mothers.identifiers import UuidMother, UuidV4Mother


@mark.unit_testing
def test_uuid4_mother_happy_path() -> None:
    """
    Test UuidV4Mother happy path.
    """
    value = UuidV4Mother.create()

    assert isinstance(value, UUID)
    assert value.version == 4


@mark.unit_testing
def test_uuid4_mother_value() -> None:
    """
    Test UuidV4Mother create method with value.
    """
    value = UuidV4Mother.create()

    assert UuidV4Mother.create(value=value) == value


@mark.unit_testing
def test_uuid4_mother_invalid_type() -> None:
    """
    Test UuidV4Mother create method with invalid type.
    """
    assert type(UuidV4Mother.invalid_type()) is not UUID


@mark.unit_testing
def test_uuid4_mother_invalid_value_type() -> None:
    """
    Test UuidV4Mother create method with invalid value type.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='UuidV4Mother value must be a UUID.',
    ):
        UuidV4Mother.create(value=UuidV4Mother.invalid_type())


@mark.unit_testing
def test_uuid4_mother_invalid_uuid_version() -> None:
    """
    Test UuidV4Mother create method with invalid UUID version.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='UuidV4Mother value must be a UUID4.',
    ):
        UuidV4Mother.create(value=UuidMother.create(exclude_versions={4}))
