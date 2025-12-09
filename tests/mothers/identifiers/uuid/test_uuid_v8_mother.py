"""
Test module for the UuidV8Mother class.
"""

from uuid import UUID

from pytest import mark, raises as assert_raises

from object_mother_pattern.mothers.identifiers import UuidMother, UuidV8Mother


@mark.unit_testing
def test_uuid8_mother_happy_path() -> None:
    """
    Test UuidV8Mother happy path.
    """
    value = UuidV8Mother.create()

    assert isinstance(value, UUID)
    assert value.version == 8


@mark.unit_testing
def test_uuid8_mother_value() -> None:
    """
    Test UuidV8Mother create method with value.
    """
    value = UuidV8Mother.create()

    assert UuidV8Mother.create(value=value) == value


@mark.unit_testing
def test_uuid8_mother_invalid_type() -> None:
    """
    Test UuidV8Mother create method with invalid type.
    """
    assert type(UuidV8Mother.invalid_type()) is not UUID


@mark.unit_testing
def test_uuid8_mother_invalid_value_type() -> None:
    """
    Test UuidV8Mother create method with invalid value type.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='UuidV8Mother value must be a UUID.',
    ):
        UuidV8Mother.create(value=UuidV8Mother.invalid_type())


@mark.unit_testing
def test_uuid8_mother_invalid_uuid_version() -> None:
    """
    Test UuidV8Mother create method with invalid UUID version.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='UuidV8Mother value must be a UUID8.',
    ):
        UuidV8Mother.create(value=UuidMother.create(exclude_versions={8}))
