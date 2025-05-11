"""
Test module for the FullNameMother class.
"""

from pytest import mark, raises as assert_raises

from object_mother_pattern.mothers import IntegerMother, StringMother
from object_mother_pattern.mothers.people import FullNameMother
from object_mother_pattern.mothers.people.full_name_mother import FullNameCase


@mark.unit_testing
def test_full_name_mother_happy_path() -> None:
    """
    Test FullNameMother happy path.
    """
    value = FullNameMother.create()

    assert type(value) is str
    assert 3 <= len(value) <= 128


@mark.unit_testing
def test_full_name_mother_name_has_trailing_spaces() -> None:
    """
    Test FullNameMother create method with name has trailing spaces.
    """
    value = FullNameMother.create()

    assert value.strip() == value


@mark.unit_testing
def test_full_name_mother_value() -> None:
    """
    Test FullNameMother create method with value.
    """
    value = FullNameMother.create()

    assert FullNameMother.create(value=value) == value


@mark.unit_testing
def test_full_name_mother_invalid_value_type() -> None:
    """
    Test FullNameMother create method with invalid value type.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='FullNameMother value must be a string.',
    ):
        FullNameMother.create(value=FullNameMother.invalid_type())


@mark.unit_testing
def test_full_name_mother_invalid_min_length_type() -> None:
    """
    Test FullNameMother create method with invalid min length type.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='FullNameMother min_length must be an integer.',
    ):
        FullNameMother.create(min_length=IntegerMother.invalid_type())


@mark.unit_testing
def test_full_name_mother_invalid_max_length_type() -> None:
    """
    Test FullNameMother create method with invalid max length type.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='FullNameMother max_length must be an integer.',
    ):
        FullNameMother.create(max_length=IntegerMother.invalid_type())


@mark.unit_testing
def test_full_name_mother_min_length_less_than_one() -> None:
    """
    Test FullNameMother create method with min less than 1.
    """
    with assert_raises(
        expected_exception=ValueError,
        match='FullNameMother min_length must be greater than or equal to 1.',
    ):
        FullNameMother.create(min_length=IntegerMother.negative())


@mark.unit_testing
def test_full_name_mother_max_length_less_than_one() -> None:
    """
    Test FullNameMother create method with max less than 1.
    """
    with assert_raises(
        expected_exception=ValueError,
        match='FullNameMother max_length must be greater than or equal to 1.',
    ):
        FullNameMother.create(max_length=IntegerMother.negative())


@mark.unit_testing
def test_full_name_mother_min_length_greater_than_max_length() -> None:
    """
    Test FullNameMother create method with min greater than max.
    """
    min_value = IntegerMother.create(min=1, max=1024)
    max_value = IntegerMother.create(min=1025, max=2048)

    with assert_raises(
        expected_exception=ValueError,
        match='FullNameMother min_length must be less than or equal to max_length.',
    ):
        FullNameMother.create(min_length=max_value, max_length=min_value)


@mark.unit_testing
def test_full_name_mother_case_lowercase() -> None:
    """
    Test FullNameMother create method with lowercase case.
    """
    value = FullNameMother.create(full_name_case=FullNameCase.LOWERCASE)

    assert value.islower()


@mark.unit_testing
def test_full_name_mother_case_uppercase() -> None:
    """
    Test FullNameMother create method with uppercase case.
    """
    value = FullNameMother.create(full_name_case=FullNameCase.UPPERCASE)

    assert value.isupper()


@mark.unit_testing
def test_full_name_mother_case_titlecase() -> None:
    """
    Test FullNameMother create method with titlecase case.
    """
    value = FullNameMother.create(full_name_case=FullNameCase.TITLECASE)
    assert value.istitle()


@mark.unit_testing
def test_full_name_mother_case_mixed() -> None:
    """
    Test FullNameMother create method with mixed case.
    """
    value = FullNameMother.create(full_name_case=FullNameCase.MIXED)

    assert any(char.islower() or char.isupper() for char in value)


@mark.unit_testing
def test_full_name_mother_invalid_full_name_case_type() -> None:
    """
    Test FullNameMother create method with invalid full name case type.
    """
    with assert_raises(TypeError, match='FullNameMother full_name_case must be a FullNameCase.'):
        FullNameMother.create(full_name_case=StringMother.invalid_type())


@mark.unit_testing
def test_full_name_mother_of_length_method() -> None:
    """
    Test FullNameMother of_length method.
    """
    length = IntegerMother.create(min=1, max=128)
    value = FullNameMother.of_length(length=length)

    assert type(value) is str
    assert len(value) == length


@mark.unit_testing
def test_full_name_mother_invalid_type() -> None:
    """
    Test FullNameMother create method with invalid type.
    """
    assert type(FullNameMother.invalid_type()) is not str


@mark.unit_testing
def test_full_name_mother_invalid_full_name_value() -> None:
    """
    Test FullNameMother create method with invalid full name value.
    """
    value = FullNameMother.invalid_value()

    assert type(value) is str
    assert not value.isprintable()
