"""
Test module for the UuidMother class.
"""

from random import choices
from uuid import UUID

from pytest import mark, raises as assert_raises

from object_mother_pattern.mothers import IntegerMother
from object_mother_pattern.mothers.identifiers import UuidMother


@mark.unit_testing
def test_uuid_mother_happy_path() -> None:
    """
    Test UuidMother happy path.
    """
    value = UuidMother.create()

    assert type(value) is UUID
    assert value.version in {1, 3, 4, 5}


@mark.unit_testing
def test_uuid_mother_value() -> None:
    """
    Test UuidMother create method with value.
    """
    value = UuidMother.create()

    assert UuidMother.create(value=value) == value


@mark.unit_testing
def test_uuid_mother_invalid_type() -> None:
    """
    Test UuidMother create method with invalid type.
    """
    assert type(UuidMother.invalid_type()) is not UUID


@mark.unit_testing
def test_uuid_mother_invalid_value_type() -> None:
    """
    Test UuidMother create method with invalid value type.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='UuidMother value must be a UUID.',
    ):
        UuidMother.create(value=UuidMother.invalid_type())


@mark.unit_testing
def test_uuid_mother_exclude_versions() -> None:
    """
    Test UuidMother create method with exclude_versions parameter.
    """
    excluded_versions = {1, 3}  # Exclude versions 1 and 3
    allowed_versions = {4, 5}  # So only versions 4 and 5 are allowed
    value = UuidMother.create(exclude_versions=excluded_versions)

    assert type(value) is UUID
    assert value.version in allowed_versions
    assert value.version not in excluded_versions


@mark.unit_testing
def test_uuid_mother_invalid_exclude_versions_type() -> None:
    """
    Test UuidMother create method with invalid exclude_versions type.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='UuidMother exclude_versions must be a set.',
    ):
        UuidMother.create(exclude_versions=[1, 2, 3])  # type: ignore[arg-type]


@mark.unit_testing
def test_uuid_mother_invalid_exclude_versions_value() -> None:
    """
    Test UuidMother create method with invalid exclude_versions value.
    """
    versions = choices(population=(10, 14, 7653, 13456), k=IntegerMother.positive())  # noqa: S311

    with assert_raises(
        expected_exception=ValueError,
        match=r'UuidMother exclude_versions must be a subset of \{1, 3, 4, 5\}.',
    ):
        UuidMother.create(exclude_versions=set(versions))
