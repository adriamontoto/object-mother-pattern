"""
Test module for the StringUuidMother class.
"""

from random import choices
from uuid import UUID

from pytest import mark, raises as assert_raises

from object_mother_pattern.mothers import IntegerMother
from object_mother_pattern.mothers.identifiers import StringUuidMother


@mark.unit_testing
def test_string_uuid_mother_happy_path() -> None:
    """
    Test StringUuidMother happy path.
    """
    value = StringUuidMother.create()

    assert type(value) is str
    assert UUID(value).version in {1, 3, 4, 5, 6, 7, 8}


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


@mark.unit_testing
def test_string_uuid_mother_exclude_versions() -> None:
    """
    Test StringUuidMother create method with exclude_versions parameter.
    """
    # TODO: do it randomly
    excluded_versions = {1, 3, 6, 7, 8}
    allowed_versions = {4, 5}
    value = StringUuidMother.create(exclude_versions=excluded_versions)

    assert type(value) is str
    assert UUID(value).version in allowed_versions
    assert UUID(value).version not in excluded_versions


@mark.unit_testing
def test_string_uuid_mother_invalid_exclude_versions_type() -> None:
    """
    Test StringUuidMother create method with invalid exclude_versions type.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='UuidMother exclude_versions must be a set.',
    ):
        StringUuidMother.create(exclude_versions=[1, 2, 3])  # type: ignore[arg-type]


@mark.unit_testing
def test_string_uuid_mother_invalid_exclude_versions_value() -> None:
    """
    Test StringUuidMother create method with invalid exclude_versions value.
    """
    versions = choices(population=(10, 14, 7653, 13456), k=IntegerMother.positive())  # noqa: S311

    with assert_raises(
        expected_exception=ValueError,
        match=r'UuidMother exclude_versions must be a subset of \{1, 3, 4, 5, 6, 7, 8\}.',
    ):
        StringUuidMother.create(exclude_versions=set(versions))
