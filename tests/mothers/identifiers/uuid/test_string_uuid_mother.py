"""
Test module for the StringUuidMother class.
"""

from random import choice, choices
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
    assert UUID(value).version in {1, 3, 4, 5}


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
        match=r'StringUuidMother value must be a string.',
    ):
        StringUuidMother.create(value=StringUuidMother.invalid_type())


@mark.unit_testing
def test_string_uuid_mother_allow_versions() -> None:
    """
    Test StringUuidMother create method with allow_versions parameter.
    """
    version = choice(seq=(1, 3, 4, 5))  # noqa: S311
    value = StringUuidMother.create(allow_versions={version})

    assert type(value) is str
    assert UUID(value).version == version


@mark.unit_testing
def test_string_uuid_mother_invalid_allow_versions_type() -> None:
    """
    Test StringUuidMother create method with invalid allow_versions type.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='UuidMother allow_versions must be a set',
    ):
        StringUuidMother.create(allow_versions=[1, 2, 3])  # type: ignore[arg-type]


@mark.unit_testing
def test_string_uuid_mother_invalid_allow_versions_value() -> None:
    """
    Test StringUuidMother create method with invalid allow_versions value.
    """
    versions = choices(population=(10, 14, 7653, 13456), k=IntegerMother.positive())  # noqa: S311

    with assert_raises(
        expected_exception=ValueError,
        match=r'UuidMother allow_versions must be a subset of \{1, 3, 4, 5\}',
    ):
        StringUuidMother.create(allow_versions=set(versions))
