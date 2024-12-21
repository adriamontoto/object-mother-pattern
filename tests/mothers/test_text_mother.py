"""
Test module for the TextMother class.
"""

from pytest import raises as assert_raises

from object_mother_pattern.mothers import IntegerMother, TextMother


def test_text_mother_happy_path() -> None:
    """
    Test TextMother happy path.
    """
    value = TextMother.create()

    assert type(value) is str
    assert 1 <= len(value) <= 1024


def test_text_mother_value() -> None:
    """
    Test TextMother create method with value.
    """
    value = TextMother.create()

    assert TextMother.create(value=value) == value


def test_text_mother_length_equal_to_zero() -> None:
    """
    Test TextMother create method with length equal to 0.
    """
    value = TextMother.of_length(length=0)

    assert value == ''


def test_text_mother_length_equal_to_one() -> None:
    """
    Test TextMother create method with length equal to 1.
    """
    value = TextMother.of_length(length=1)

    assert value == '.'


def test_text_mother_of_length_method() -> None:
    """
    Test TextMother of_length method.
    """
    text_length = IntegerMother.create(min=2, max=1024)
    value = TextMother.of_length(length=text_length)

    assert type(value) is str
    assert len(value) == text_length
    assert value[-1] == '.'


def test_text_mother_invalid_type() -> None:
    """
    Test TextMother create method with invalid type.
    """
    assert type(TextMother.invalid_type()) is not str


def test_text_mother_invalid_value_type() -> None:
    """
    Test TextMother create method with invalid value type.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='TextMother value must be a string.',
    ):
        TextMother.create(value=TextMother.invalid_type())


def test_text_mother_invalid_min_length_type() -> None:
    """
    Test TextMother create method with invalid min length type.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='TextMother min_length must be an integer.',
    ):
        TextMother.create(min_length=IntegerMother.invalid_type())


def test_text_mother_invalid_max_length_type() -> None:
    """
    Test TextMother create method with invalid max length type.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='TextMother max_length must be an integer.',
    ):
        TextMother.create(max_length=IntegerMother.invalid_type())


def test_text_mother_min_length_less_than_zero() -> None:
    """
    Test TextMother create method with min greater than max.
    """
    with assert_raises(
        expected_exception=ValueError,
        match='TextMother min_length must be greater than or equal to 0.',
    ):
        TextMother.create(min_length=IntegerMother.negative())


def test_text_mother_max_length_less_than_zero() -> None:
    """
    Test TextMother create method with max less than 0.
    """
    with assert_raises(
        expected_exception=ValueError,
        match='TextMother max_length must be greater than or equal to 0.',
    ):
        TextMother.create(max_length=IntegerMother.negative())


def test_text_mother_min_length_greater_than_max_length() -> None:
    """
    Test TextMother create method with min greater than max.
    """
    min_value = IntegerMother.create(min=1, max=1024)
    max_value = IntegerMother.create(min=1025, max=2048)

    with assert_raises(
        expected_exception=ValueError,
        match='TextMother min_length must be less than or equal to max_length.',
    ):
        TextMother.create(min_length=max_value, max_length=min_value)
