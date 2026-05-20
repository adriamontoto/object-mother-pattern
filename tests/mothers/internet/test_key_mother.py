"""
Test module for the KeyMother class.
"""

from re import Pattern, compile as re_compile

from pytest import mark, raises as assert_raises

from object_mother_pattern.mothers import IntegerMother, StringMother
from object_mother_pattern.mothers.internet import KeyMother

_KEY_REGEX: Pattern[str] = re_compile(pattern=r'^[a-z0-9]+(?:[.-][a-z0-9]+)*$')


@mark.unit_testing
def test_key_mother_happy_path() -> None:
    """
    Test KeyMother happy path.
    """
    value = KeyMother.create()

    assert type(value) is str
    assert 3 <= len(value) <= 64
    assert _KEY_REGEX.match(string=value) is not None


@mark.unit_testing
def test_key_mother_value() -> None:
    """
    Test KeyMother create method with value.
    """
    value = KeyMother.create()

    assert KeyMother.create(value=value) == value


@mark.unit_testing
def test_key_mother_invalid_value_type() -> None:
    """
    Test KeyMother create method with invalid value type.
    """
    with assert_raises(TypeError, match='KeyMother value must be a string.'):
        KeyMother.create(value=KeyMother.invalid_type())


@mark.unit_testing
def test_key_mother_invalid_min_length_type() -> None:
    """
    Test KeyMother create method with invalid min_length type.
    """
    with assert_raises(TypeError, match='KeyMother min_length must be an integer.'):
        KeyMother.create(min_length=IntegerMother.invalid_type())


@mark.unit_testing
def test_key_mother_invalid_max_length_type() -> None:
    """
    Test KeyMother create method with invalid max_length type.
    """
    with assert_raises(TypeError, match='KeyMother max_length must be an integer.'):
        KeyMother.create(max_length=IntegerMother.invalid_type())


@mark.unit_testing
def test_key_mother_min_length_less_than_one() -> None:
    """
    Test KeyMother create method with min_length less than 1.
    """
    with assert_raises(ValueError, match='KeyMother min_length must be greater than or equal to 1.'):
        KeyMother.create(min_length=IntegerMother.negative())


@mark.unit_testing
def test_key_mother_max_length_less_than_one() -> None:
    """
    Test KeyMother create method with max_length less than 1.
    """
    with assert_raises(ValueError, match='KeyMother max_length must be greater than or equal to 1.'):
        KeyMother.create(max_length=IntegerMother.negative())


@mark.unit_testing
def test_key_mother_min_length_greater_than_max_length() -> None:
    """
    Test KeyMother create method with min_length greater than max_length.
    """
    min_value = IntegerMother.create(min=1, max=31)
    max_value = IntegerMother.create(min=32, max=64)

    with assert_raises(ValueError, match='KeyMother min_length must be less than or equal to max_length.'):
        KeyMother.create(min_length=max_value, max_length=min_value)


@mark.unit_testing
def test_key_mother_invalid_type() -> None:
    """
    Test KeyMother invalid_type method returns non-str.
    """
    assert type(KeyMother.invalid_type()) is not str


@mark.unit_testing
def test_key_mother_of_length_method() -> None:
    """
    Test KeyMother of_length method.
    """
    key_length = IntegerMother.create(min=1, max=64)
    value = KeyMother.of_length(length=key_length)

    assert type(value) is str
    assert len(value) == key_length
    assert _KEY_REGEX.match(string=value) is not None


@mark.unit_testing
def test_key_mother_of_length_method_with_single_character() -> None:
    """
    Test KeyMother of_length method with the minimum length.
    """
    value = KeyMother.of_length(length=1)

    assert len(value) == 1
    assert _KEY_REGEX.match(string=value) is not None


@mark.unit_testing
def test_key_mother_invalid_key_value() -> None:
    """
    Test KeyMother invalid_value method.
    """
    value = KeyMother.invalid_value()

    assert type(value) is str
    assert not value.isprintable()


@mark.unit_testing
def test_key_mother_invalid_min_length_type_for_of_length() -> None:
    """
    Test KeyMother of_length method with invalid length type.
    """
    with assert_raises(TypeError, match='KeyMother min_length must be an integer.'):
        KeyMother.of_length(length=StringMother.invalid_type(remove_types=(int,)))
