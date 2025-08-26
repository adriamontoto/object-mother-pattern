"""
Test module for the UuidV5Mother class.
"""

from random import choice
from uuid import NAMESPACE_DNS, NAMESPACE_OID, NAMESPACE_URL, NAMESPACE_X500, UUID

from pytest import mark, raises as assert_raises

from object_mother_pattern.mothers import StringMother
from object_mother_pattern.mothers.identifiers import UuidV5Mother


@mark.unit_testing
def test_uuid5_mother_happy_path() -> None:
    """
    Test UuidV5Mother happy path.
    """
    value = UuidV5Mother.create()

    assert type(value) is UUID
    assert value.version == 5


@mark.unit_testing
def test_uuid5_mother_value() -> None:
    """
    Test UuidV5Mother create method with value.
    """
    value = UuidV5Mother.create()

    assert UuidV5Mother.create(value=value) == value


@mark.unit_testing
def test_uuid5_mother_invalid_type() -> None:
    """
    Test UuidV5Mother create method with invalid type.
    """
    assert type(UuidV5Mother.invalid_type()) is not UUID


@mark.unit_testing
def test_uuid5_mother_invalid_value_type() -> None:
    """
    Test UuidV5Mother create method with invalid value type.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='UuidV5Mother value must be a UUID.',
    ):
        UuidV5Mother.create(value=UuidV5Mother.invalid_type())


@mark.unit_testing
def test_uuid5_mother_namespace() -> None:
    """
    Test UuidV5Mother create method with namespace parameter.
    """
    namespace = choice(seq=(NAMESPACE_DNS, NAMESPACE_OID, NAMESPACE_URL, NAMESPACE_X500))  # noqa: S311
    value = UuidV5Mother.create(namespace=namespace)

    assert type(value) is UUID
    assert value.version == 5


@mark.unit_testing
def test_uuid5_mother_name() -> None:
    """
    Test UuidV5Mother create method with name parameter.
    """
    name = StringMother.create()
    value = UuidV5Mother.create(name=name)

    assert type(value) is UUID
    assert value.version == 5


@mark.unit_testing
def test_uuid5_mother_namespace_and_name() -> None:
    """
    Test UuidV5Mother create method with namespace and name parameters.
    """
    namespace = choice(seq=(NAMESPACE_DNS, NAMESPACE_OID, NAMESPACE_URL, NAMESPACE_X500))  # noqa: S311
    name = StringMother.create()
    value = UuidV5Mother.create(namespace=namespace, name=name)

    assert type(value) is UUID
    assert value.version == 5


@mark.unit_testing
def test_uuid5_mother_invalid_namespace_type() -> None:
    """
    Test UuidV5Mother create method with invalid namespace type.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='UuidV5Mother namespace must be a UUID.',
    ):
        UuidV5Mother.create(namespace=UuidV5Mother.invalid_type())


@mark.unit_testing
def test_uuid5_mother_invalid_name_type() -> None:
    """
    Test UuidV5Mother create method with invalid name type.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='UuidV5Mother name must be a string.',
    ):
        UuidV5Mother.create(name=StringMother.invalid_type())
