"""
Test module for the UsernameMother class.
"""

from pytest import mark, raises as assert_raises

from object_mother_pattern.mothers import IntegerMother, StringMother
from object_mother_pattern.mothers.people import UsernameMother


@mark.unit_testing
def test_username_mother_happy_path() -> None:
    """
    Test UsernameMother happy path.
    """
    value = UsernameMother.create()

    assert type(value) is str
    assert 3 <= len(value) <= 32


@mark.unit_testing
def test_username_mother_name_has_trailing_spaces() -> None:
    """
    Test UsernameMother create method with name has trailing spaces.
    """
    value = UsernameMother.create()

    assert value.strip() == value


@mark.unit_testing
def test_username_mother_ends_with_alphabetic_or_numeric() -> None:
    """
    Test UsernameMother create method with ends with alphabetic or numeric.
    """
    value = UsernameMother.create()

    assert value[-1].isalnum()


@mark.unit_testing
def test_username_mother_value() -> None:
    """
    Test UsernameMother create method with value.
    """
    value = UsernameMother.create()

    assert UsernameMother.create(value=value) == value


@mark.unit_testing
def test_username_mother_invalid_value_type() -> None:
    """
    Test UsernameMother create method with invalid value type.
    """
    with assert_raises(TypeError, match='UsernameMother value must be a string.'):
        UsernameMother.create(value=UsernameMother.invalid_type())


@mark.unit_testing
def test_username_mother_invalid_min_length_type() -> None:
    """
    Test UsernameMother create method with invalid min_length type.
    """
    with assert_raises(TypeError, match='UsernameMother min_length must be an integer.'):
        UsernameMother.create(min_length=IntegerMother.invalid_type())


@mark.unit_testing
def test_username_mother_invalid_max_length_type() -> None:
    """
    Test UsernameMother create method with invalid max_length type.
    """
    with assert_raises(TypeError, match='UsernameMother max_length must be an integer.'):
        UsernameMother.create(max_length=IntegerMother.invalid_type())


@mark.unit_testing
def test_username_mother_invalid_separator_type() -> None:
    """
    Test UsernameMother create method with invalid separator type.
    """
    with assert_raises(TypeError, match='UsernameMother separator must be a string.'):
        UsernameMother.create(separators=StringMother.invalid_type())


@mark.unit_testing
def test_username_mother_min_length_less_than_one() -> None:
    """
    Test UsernameMother create method with min_length less than 1.
    """
    with assert_raises(ValueError, match='UsernameMother min_length must be greater than or equal to 1.'):
        UsernameMother.create(min_length=IntegerMother.negative())


@mark.unit_testing
def test_username_mother_max_length_less_than_one() -> None:
    """
    Test UsernameMother create method with max_length less than 1.
    """
    with assert_raises(ValueError, match='UsernameMother max_length must be greater than or equal to 1.'):
        UsernameMother.create(max_length=IntegerMother.negative())


@mark.unit_testing
def test_username_mother_min_length_greater_than_max_length() -> None:
    """
    Test UsernameMother create method with min_length greater than max_length.
    """
    min_value = IntegerMother.create(min=1, max=16)
    max_value = IntegerMother.create(min=17, max=32)

    with assert_raises(ValueError, match='UsernameMother min_length must be less than or equal to max_length.'):
        UsernameMother.create(min_length=max_value, max_length=min_value)


@mark.unit_testing
def test_username_mother_invalid_type() -> None:
    """
    Test UsernameMother invalid_type method returns non-str.
    """
    assert type(UsernameMother.invalid_type()) is not str


@mark.unit_testing
def test_username_mother_of_length_method() -> None:
    """
    Test UsernameMother of_length method.
    """
    text_length = IntegerMother.create(min=1, max=32)
    value = UsernameMother.of_length(length=text_length)

    assert type(value) is str
    assert len(value) == text_length


@mark.unit_testing
def test_username_mother_invalid_username_value() -> None:
    """
    Test UsernameMother invalid_value method.
    """
    value = UsernameMother.invalid_value()

    assert type(value) is str
    assert not value.isprintable()
