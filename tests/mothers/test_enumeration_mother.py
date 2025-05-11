"""
Test module for the EnumerationMother class.
"""

from enum import Enum, auto, unique

from pytest import mark, raises as assert_raises

from object_mother_pattern.mothers import EnumerationMother


@unique
class _TestEnum(Enum):
    """
    Test enumeration for testing EnumerationMother.
    """

    VALUE_1 = auto()
    VALUE_2 = auto()
    VALUE_3 = auto()


@mark.unit_testing
def test_enumeration_mother_happy_path() -> None:
    """
    Test EnumerationMother happy path.
    """
    mother = EnumerationMother(enumeration=_TestEnum)

    assert mother.create() in list(_TestEnum)


@mark.unit_testing
def test_enumeration_mother_init_invalid_enumeration_type() -> None:
    """
    Test EnumerationMother initialization with invalid enumeration type.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='EnumerationMother enumeration must be a subclass of Enum.',
    ):
        EnumerationMother(enumeration=EnumerationMother.invalid_type())


@mark.unit_testing
def test_enumeration_mother_create_with_value() -> None:
    """
    Test EnumerationMother create method with specific value.
    """
    mother = EnumerationMother(enumeration=_TestEnum)
    expected_value = _TestEnum.VALUE_1

    result = mother.create(value=expected_value)

    assert result == expected_value


@mark.unit_testing
def test_enumeration_mother_create_with_invalid_value_type() -> None:
    """
    Test EnumerationMother create method with invalid value type.
    """
    mother = EnumerationMother(enumeration=_TestEnum)

    with assert_raises(
        expected_exception=TypeError,
        match='_TestEnumMother value must be an instance of _TestEnum.',
    ):
        mother.create(value=EnumerationMother.invalid_type())


@mark.unit_testing
def test_enumeration_mother_invalid_type() -> None:
    """
    Test EnumerationMother invalid_type method.
    """
    result = EnumerationMother.invalid_type()

    assert type(result) is not Enum
