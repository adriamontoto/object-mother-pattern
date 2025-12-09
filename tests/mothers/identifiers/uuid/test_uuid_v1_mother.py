"""
Test module for the UuidV1Mother class.
"""

from uuid import UUID

from pytest import mark, raises as assert_raises

from object_mother_pattern.mothers.identifiers import UuidMother, UuidV1Mother


@mark.unit_testing
def test_uuid1_mother_happy_path() -> None:
    """
    Test UuidV1Mother happy path.
    """
    value = UuidV1Mother.create()

    assert isinstance(value, UUID)
    assert value.version == 1


@mark.unit_testing
def test_uuid1_mother_value() -> None:
    """
    Test UuidV1Mother create method with value.
    """
    value = UuidV1Mother.create()

    assert UuidV1Mother.create(value=value) == value


@mark.unit_testing
def test_uuid1_mother_invalid_type() -> None:
    """
    Test UuidV1Mother create method with invalid type.
    """
    assert type(UuidV1Mother.invalid_type()) is not UUID


@mark.unit_testing
def test_uuid1_mother_invalid_value_type() -> None:
    """
    Test UuidV1Mother create method with invalid value type.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='UuidV1Mother value must be a UUID.',
    ):
        UuidV1Mother.create(value=UuidV1Mother.invalid_type())


@mark.unit_testing
def test_uuid1_mother_invalid_uuid_version() -> None:
    """
    Test UuidV1Mother create method with invalid UUID version.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='UuidV1Mother value must be a UUID1.',
    ):
        UuidV1Mother.create(value=UuidMother.create(exclude_versions={1}))
