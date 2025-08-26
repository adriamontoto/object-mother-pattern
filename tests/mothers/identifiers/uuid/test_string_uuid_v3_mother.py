"""
Test module for the StringUuidMother class.
"""

from random import choice
from uuid import NAMESPACE_DNS, NAMESPACE_OID, NAMESPACE_URL, NAMESPACE_X500, UUID

from pytest import mark, raises as assert_raises

from object_mother_pattern.mothers import StringMother
from object_mother_pattern.mothers.identifiers import StringUuidV3Mother


@mark.unit_testing
def test_string_uuid3_mother_happy_path() -> None:
    """
    Test StringUuidMother happy path.
    """
    value = StringUuidV3Mother.create()

    assert type(value) is str
    assert UUID(value).version == 3


@mark.unit_testing
def test_string_uuid3_mother_value() -> None:
    """
    Test StringUuidMother create method with value.
    """
    value = StringUuidV3Mother.create()

    assert StringUuidV3Mother.create(value=value) == value


@mark.unit_testing
def test_string_uuid3_mother_invalid_type() -> None:
    """
    Test StringUuidMother create method with invalid type.
    """
    assert type(StringUuidV3Mother.invalid_type()) is not str


@mark.unit_testing
def test_string_uuid3_mother_invalid_value() -> None:
    """
    Test StringUuidMother invalid_value method.
    """
    value = StringUuidV3Mother.invalid_value()

    assert type(value) is str
    assert not value.isprintable()


@mark.unit_testing
def test_string_uuid3_mother_invalid_value_type() -> None:
    """
    Test StringUuidMother create method with invalid value type.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='StringUuidV3Mother value must be a string.',
    ):
        StringUuidV3Mother.create(value=StringUuidV3Mother.invalid_type())


@mark.unit_testing
def test_string_uuid3_mother_namespace() -> None:
    """
    Test StringUuidV3Mother create method with namespace parameter.
    """
    namespace = choice(seq=(NAMESPACE_DNS, NAMESPACE_OID, NAMESPACE_URL, NAMESPACE_X500))  # noqa: S311
    value = StringUuidV3Mother.create(namespace=namespace)

    assert type(value) is str
    assert UUID(value).version == 3


@mark.unit_testing
def test_string_uuid3_mother_name() -> None:
    """
    Test StringUuidV3Mother create method with name parameter.
    """
    name = StringMother.create()
    value = StringUuidV3Mother.create(name=name)

    assert type(value) is str
    assert UUID(value).version == 3


@mark.unit_testing
def test_string_uuid3_mother_namespace_and_name() -> None:
    """
    Test StringUuidV3Mother create method with namespace and name parameters.
    """
    namespace = choice(seq=(NAMESPACE_DNS, NAMESPACE_OID, NAMESPACE_URL, NAMESPACE_X500))  # noqa: S311
    name = StringMother.create()
    value = StringUuidV3Mother.create(namespace=namespace, name=name)

    assert type(value) is str
    assert UUID(value).version == 3


@mark.unit_testing
def test_string_uuid3_mother_invalid_namespace_type() -> None:
    """
    Test StringUuidV3Mother create method with invalid namespace type.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='UuidV3Mother namespace must be a UUID.',
    ):
        StringUuidV3Mother.create(namespace=StringMother.invalid_type())


@mark.unit_testing
def test_string_uuid3_mother_invalid_name_type() -> None:
    """
    Test StringUuidV3Mother create method with invalid name type.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='UuidV3Mother name must be a string.',
    ):
        StringUuidV3Mother.create(name=StringMother.invalid_type())
