"""
Test module for the SlugMother class.
"""

from re import Pattern, compile as re_compile

from pytest import mark, raises as assert_raises

from object_mother_pattern.mothers import IntegerMother, StringMother
from object_mother_pattern.mothers.internet import SlugMother

_SLUG_REGEX: Pattern[str] = re_compile(pattern=r'^[a-z0-9]+(?:-[a-z0-9]+)*$')


@mark.unit_testing
def test_slug_mother_happy_path() -> None:
    """
    Test SlugMother happy path.
    """
    value = SlugMother.create()

    assert type(value) is str
    assert 3 <= len(value) <= 64
    assert _SLUG_REGEX.match(string=value) is not None


@mark.unit_testing
def test_slug_mother_value() -> None:
    """
    Test SlugMother create method with value.
    """
    value = SlugMother.create()

    assert SlugMother.create(value=value) == value


@mark.unit_testing
def test_slug_mother_invalid_value_type() -> None:
    """
    Test SlugMother create method with invalid value type.
    """
    with assert_raises(TypeError, match='SlugMother value must be a string.'):
        SlugMother.create(value=SlugMother.invalid_type())


@mark.unit_testing
def test_slug_mother_invalid_min_length_type() -> None:
    """
    Test SlugMother create method with invalid min_length type.
    """
    with assert_raises(TypeError, match='SlugMother min_length must be an integer.'):
        SlugMother.create(min_length=IntegerMother.invalid_type())


@mark.unit_testing
def test_slug_mother_invalid_max_length_type() -> None:
    """
    Test SlugMother create method with invalid max_length type.
    """
    with assert_raises(TypeError, match='SlugMother max_length must be an integer.'):
        SlugMother.create(max_length=IntegerMother.invalid_type())


@mark.unit_testing
def test_slug_mother_min_length_less_than_one() -> None:
    """
    Test SlugMother create method with min_length less than 1.
    """
    with assert_raises(ValueError, match='SlugMother min_length must be greater than or equal to 1.'):
        SlugMother.create(min_length=IntegerMother.negative())


@mark.unit_testing
def test_slug_mother_max_length_less_than_one() -> None:
    """
    Test SlugMother create method with max_length less than 1.
    """
    with assert_raises(ValueError, match='SlugMother max_length must be greater than or equal to 1.'):
        SlugMother.create(max_length=IntegerMother.negative())


@mark.unit_testing
def test_slug_mother_min_length_greater_than_max_length() -> None:
    """
    Test SlugMother create method with min_length greater than max_length.
    """
    min_value = IntegerMother.create(min=1, max=31)
    max_value = IntegerMother.create(min=32, max=64)

    with assert_raises(ValueError, match='SlugMother min_length must be less than or equal to max_length.'):
        SlugMother.create(min_length=max_value, max_length=min_value)


@mark.unit_testing
def test_slug_mother_invalid_type() -> None:
    """
    Test SlugMother invalid_type method returns non-str.
    """
    assert type(SlugMother.invalid_type()) is not str


@mark.unit_testing
def test_slug_mother_of_length_method() -> None:
    """
    Test SlugMother of_length method.
    """
    slug_length = IntegerMother.create(min=1, max=64)
    value = SlugMother.of_length(length=slug_length)

    assert type(value) is str
    assert len(value) == slug_length
    assert _SLUG_REGEX.match(string=value) is not None


@mark.unit_testing
def test_slug_mother_invalid_slug_value() -> None:
    """
    Test SlugMother invalid_value method.
    """
    value = SlugMother.invalid_value()

    assert type(value) is str
    assert not value.isprintable()


@mark.unit_testing
def test_slug_mother_invalid_min_length_type_for_of_length() -> None:
    """
    Test SlugMother of_length method with invalid length type.
    """
    with assert_raises(TypeError, match='SlugMother min_length must be an integer.'):
        SlugMother.of_length(length=StringMother.invalid_type())
