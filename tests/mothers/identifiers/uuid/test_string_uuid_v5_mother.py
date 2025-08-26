"""
Test module for the StringUuidMother class.
"""

from random import choice
from uuid import NAMESPACE_DNS, NAMESPACE_OID, NAMESPACE_URL, NAMESPACE_X500, UUID

from pytest import mark, raises as assert_raises

from object_mother_pattern.mothers import StringMother
from object_mother_pattern.mothers.identifiers import StringUuidV5Mother, UuidV5Mother


@mark.unit_testing
def test_string_uuid5_mother_happy_path() -> None:
    """
    Test StringUuidMother happy path.
    """
    value = StringUuidV5Mother.create()

    assert type(value) is str
    assert UUID(value).version == 5


@mark.unit_testing
def test_string_uuid5_mother_value() -> None:
    """
    Test StringUuidMother create method with value.
    """
    value = StringUuidV5Mother.create()

    assert StringUuidV5Mother.create(value=value) == value


@mark.unit_testing
def test_string_uuid5_mother_invalid_type() -> None:
    """
    Test StringUuidMother create method with invalid type.
    """
    assert type(StringUuidV5Mother.invalid_type()) is not str


@mark.unit_testing
def test_string_uuid5_mother_invalid_value() -> None:
    """
    Test StringUuidMother invalid_value method.
    """
    value = StringUuidV5Mother.invalid_value()

    assert type(value) is str
    assert not value.isprintable()


@mark.unit_testing
def test_string_uuid5_mother_invalid_value_type() -> None:
    """
    Test StringUuidMother create method with invalid value type.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='StringUuidV5Mother value must be a string.',
    ):
        StringUuidV5Mother.create(value=StringUuidV5Mother.invalid_type())


@mark.unit_testing
def test_string_uuid5_mother_namespace() -> None:
    """
    Test StringUuidV5Mother create method with namespace parameter.
    """
    namespace = choice(seq=(NAMESPACE_DNS, NAMESPACE_OID, NAMESPACE_URL, NAMESPACE_X500))  # noqa: S311
    value = StringUuidV5Mother.create(namespace=namespace)

    assert type(value) is str
    assert UUID(value).version == 5


@mark.unit_testing
def test_string_uuid5_mother_name() -> None:
    """
    Test StringUuidV5Mother create method with name parameter.
    """
    name = StringMother.create()
    value = StringUuidV5Mother.create(name=name)

    assert type(value) is str
    assert UUID(value).version == 5


@mark.unit_testing
def test_string_uuid5_mother_namespace_and_name() -> None:
    """
    Test StringUuidV5Mother create method with namespace and name parameters.
    """
    namespace = choice(seq=(NAMESPACE_DNS, NAMESPACE_OID, NAMESPACE_URL, NAMESPACE_X500))  # noqa: S311
    name = StringMother.create()
    value = StringUuidV5Mother.create(namespace=namespace, name=name)

    assert type(value) is str
    assert UUID(value).version == 5


@mark.unit_testing
def test_string_uuid5_mother_invalid_namespace_type() -> None:
    """
    Test StringUuidV5Mother create method with invalid namespace type.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='UuidV5Mother namespace must be a UUID.',
    ):
        StringUuidV5Mother.create(namespace=UuidV5Mother.invalid_type())


@mark.unit_testing
def test_string_uuid5_mother_invalid_name_type() -> None:
    """
    Test StringUuidV5Mother create method with invalid name type.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='UuidV5Mother name must be a string.',
    ):
        StringUuidV5Mother.create(name=StringMother.invalid_type())
