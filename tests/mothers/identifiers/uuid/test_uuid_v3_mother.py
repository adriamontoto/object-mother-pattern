"""
Test module for the UuidV3Mother class.
"""

from random import choice
from uuid import NAMESPACE_DNS, NAMESPACE_OID, NAMESPACE_URL, NAMESPACE_X500, UUID

from pytest import mark, raises as assert_raises

from object_mother_pattern.mothers import StringMother
from object_mother_pattern.mothers.identifiers import UuidV3Mother


@mark.unit_testing
def test_uuid3_mother_happy_path() -> None:
    """
    Test UuidV3Mother happy path.
    """
    value = UuidV3Mother.create()

    assert type(value) is UUID
    assert value.version == 3


@mark.unit_testing
def test_uuid3_mother_value() -> None:
    """
    Test UuidV3Mother create method with value.
    """
    value = UuidV3Mother.create()

    assert UuidV3Mother.create(value=value) == value


@mark.unit_testing
def test_uuid3_mother_invalid_type() -> None:
    """
    Test UuidV3Mother create method with invalid type.
    """
    assert type(UuidV3Mother.invalid_type()) is not UUID


@mark.unit_testing
def test_uuid3_mother_invalid_value_type() -> None:
    """
    Test UuidV3Mother create method with invalid value type.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='UuidV3Mother value must be a UUID.',
    ):
        UuidV3Mother.create(value=UuidV3Mother.invalid_type())


@mark.unit_testing
def test_uuid3_mother_namespace() -> None:
    """
    Test UuidV3Mother create method with namespace parameter.
    """
    namespace = choice(seq=(NAMESPACE_DNS, NAMESPACE_OID, NAMESPACE_URL, NAMESPACE_X500))  # noqa: S311
    value = UuidV3Mother.create(namespace=namespace)

    assert type(value) is UUID
    assert value.version == 3


@mark.unit_testing
def test_uuid3_mother_name() -> None:
    """
    Test UuidV3Mother create method with name parameter.
    """
    name = StringMother.create()
    value = UuidV3Mother.create(name=name)

    assert type(value) is UUID
    assert value.version == 3


@mark.unit_testing
def test_uuid3_mother_namespace_and_name() -> None:
    """
    Test UuidV3Mother create method with namespace and name parameters.
    """
    namespace = choice(seq=(NAMESPACE_DNS, NAMESPACE_OID, NAMESPACE_URL, NAMESPACE_X500))  # noqa: S311
    name = StringMother.create()
    value = UuidV3Mother.create(namespace=namespace, name=name)

    assert type(value) is UUID
    assert value.version == 3


@mark.unit_testing
def test_uuid3_mother_invalid_namespace_type() -> None:
    """
    Test UuidV3Mother create method with invalid namespace type.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='UuidV3Mother namespace must be a UUID.',
    ):
        UuidV3Mother.create(namespace=UuidV3Mother.invalid_type())


@mark.unit_testing
def test_uuid3_mother_invalid_name_type() -> None:
    """
    Test UuidV3Mother create method with invalid name type.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='UuidV3Mother name must be a string.',
    ):
        UuidV3Mother.create(name=StringMother.invalid_type())
