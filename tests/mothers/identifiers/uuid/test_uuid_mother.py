"""
Test module for the UuidMother class.
"""

from random import choice, choices
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
def test_uuid_mother_allow_versions() -> None:
    """
    Test UuidMother create method with allow_versions parameter.
    """
    version = choice(seq=(1, 3, 4, 5))  # noqa: S311
    value = UuidMother.create(allow_versions={version})

    assert type(value) is UUID
    assert value.version == version


@mark.unit_testing
def test_uuid_mother_invalid_allow_versions_type() -> None:
    """
    Test UuidMother create method with invalid allow_versions type.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='UuidMother allow_versions must be a set',
    ):
        UuidMother.create(allow_versions=[1, 2, 3])  # type: ignore[arg-type]


@mark.unit_testing
def test_uuid_mother_invalid_allow_versions_value() -> None:
    """
    Test UuidMother create method with invalid allow_versions value.
    """
    versions = choices(population=(10, 14, 7653, 13456), k=IntegerMother.positive())  # noqa: S311

    with assert_raises(
        expected_exception=ValueError,
        match=r'UuidMother allow_versions must be a subset of \{1, 3, 4, 5\}',
    ):
        UuidMother.create(allow_versions=set(versions))
