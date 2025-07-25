"""
Test module for the EnumerationMother class.
"""

from enum import Enum, auto, unique
from re import escape

from pytest import mark, raises as assert_raises

from object_mother_pattern.models import EnumerationMother


@unique
class _TestEnum(Enum):
    """
    Test enumeration for testing EnumerationMother.
    """

    VALUE_1 = auto()
    VALUE_2 = auto()
    VALUE_3 = auto()


class TestEnumMother(EnumerationMother[_TestEnum]):
    """
    TestEnumMother class.
    """


@mark.unit_testing
def test_enumeration_mother_can_be_instantiated() -> None:
    """
    Test EnumerationMother can be instantiated.
    """
    EnumerationMother()


@mark.unit_testing
def test_enumeration_mother_init_with_invalid_type() -> None:
    """
    Test EnumerationMother initialization with invalid type.
    """
    value = EnumerationMother.invalid_type(remove_types=(list, set, tuple, dict))

    with assert_raises(
        expected_exception=TypeError,
        match=r'EnumerationMother\[.*\] <<<.*>>> must be an Enum subclass. Got <<<.*>>> type.',
    ):

        class BooleanMother(EnumerationMother[value]):  # type: ignore[valid-type]
            pass


@mark.unit_testing
def test_enumeration_mother_init_without_parameterization() -> None:
    """
    Test EnumerationMother initialization without parameterization.
    """
    with assert_raises(
        expected_exception=TypeError,
        match=escape(
            pattern='EnumerationMother must be parameterized, e.g. "class ColorMother(EnumerationMother[ColorEnumeration])".'  # noqa: E501
        ),
    ):

        class ColorMother(EnumerationMother):  # type: ignore[type-arg]
            pass


@mark.unit_testing
def test_enumeration_mother_happy_path() -> None:
    """
    Test EnumerationMother happy path.
    """
    assert TestEnumMother().create() in tuple(_TestEnum)


@mark.unit_testing
def test_enumeration_mother_create_with_value() -> None:
    """
    Test EnumerationMother create method with specific value.
    """
    expected_value = _TestEnum.VALUE_1

    result = TestEnumMother.create(value=expected_value)

    assert result == expected_value


@mark.unit_testing
def test_enumeration_mother_create_with_invalid_value_type() -> None:
    """
    Test EnumerationMother create method with invalid value type.
    """
    with assert_raises(
        expected_exception=TypeError,
        match=r'_TestEnumMother value must be an instance of <<<.*>>> type.',
    ):
        TestEnumMother.create(value=EnumerationMother.invalid_type())


@mark.unit_testing
def test_enumeration_mother_invalid_type() -> None:
    """
    Test EnumerationMother invalid_type method.
    """
    result = EnumerationMother.invalid_type()

    assert type(result) is not Enum
