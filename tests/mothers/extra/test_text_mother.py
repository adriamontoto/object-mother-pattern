"""
Test module for the TextMother class.
"""

from pytest import mark, raises as assert_raises

from object_mother_pattern.mothers import IntegerMother, StringCase, StringMother
from object_mother_pattern.mothers.extra import TextMother


@mark.unit_testing
def test_text_mother_create_method_happy_path() -> None:
    """
    Check that TextMother create method returns a string value with a length between 1 and 1024.
    """
    value = TextMother.create()

    assert type(value) is str
    assert 1 <= len(value) <= 1024


@mark.unit_testing
def test_text_mother_create_method_value() -> None:
    """
    Check that TextMother create method returns the provided value.
    """
    value = TextMother.create()

    assert TextMother.create(value=value) == value


@mark.unit_testing
def test_text_mother_create_method_invalid_value_type() -> None:
    """
    Check that TextMother create method raises a TypeError when the provided value is not a string.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='TextMother value must be a string.',
    ):
        TextMother.create(value=TextMother.invalid_type())


@mark.unit_testing
def test_text_mother_create_method_invalid_min_length_type() -> None:
    """
    Check that TextMother create method raises a TypeError when the provided min_length is not an integer.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='TextMother min_length must be an integer.',
    ):
        TextMother.create(min_length=IntegerMother.invalid_type())


@mark.unit_testing
def test_text_mother_create_method_invalid_max_length_type() -> None:
    """
    Check that TextMother create method raises a TypeError when the provided max_length is not an integer.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='TextMother max_length must be an integer.',
    ):
        TextMother.create(max_length=IntegerMother.invalid_type())


@mark.unit_testing
def test_text_mother_create_method_min_length_zero() -> None:
    """
    Check that TextMother create method raises a ValueError when the provided min_length is zeros.
    """
    with assert_raises(
        expected_exception=ValueError,
        match='TextMother min_length must be greater than or equal to 1.',
    ):
        TextMother.create(min_length=0)


@mark.unit_testing
def test_text_mother_create_method_min_length_random_negative_value() -> None:
    """
    Check that TextMother create method raises a ValueError when the provided min_length is negative.
    """
    with assert_raises(
        expected_exception=ValueError,
        match='TextMother min_length must be greater than or equal to 1.',
    ):
        TextMother.create(min_length=IntegerMother.negative())


@mark.unit_testing
def test_text_mother_create_method_max_length_zero() -> None:
    """
    Check that TextMother create method raises a ValueError when the provided max_length is zero.
    """
    with assert_raises(
        expected_exception=ValueError,
        match='TextMother max_length must be greater than or equal to 1.',
    ):
        TextMother.create(max_length=0)


@mark.unit_testing
def test_text_mother_create_method_max_length_random_negative_value() -> None:
    """
    Check that TextMother create method raises a ValueError when the provided max_length is negative.
    """
    with assert_raises(
        expected_exception=ValueError,
        match='TextMother max_length must be greater than or equal to 1.',
    ):
        TextMother.create(max_length=IntegerMother.negative())


@mark.unit_testing
def test_text_mother_create_method_min_length_greater_than_max_length() -> None:
    """
    Check that TextMother create method raises a ValueError when the provided min_length is greater than max_length.
    """
    min_value = IntegerMother.create(min=1, max=1024)
    max_value = IntegerMother.create(min=1025, max=2048)

    with assert_raises(
        expected_exception=ValueError,
        match='TextMother min_length must be less than or equal to max_length.',
    ):
        TextMother.create(min_length=max_value, max_length=min_value)


@mark.unit_testing
def test_text_mother_create_method_truncate_length() -> None:
    """
    Check that TextMother create method truncates the text to the specified length.
    """
    length = IntegerMother.positive()
    value = TextMother.create(min_length=length, max_length=length)

    assert type(value) is str
    assert len(value) == length


@mark.unit_testing
def test_text_mother_create_method_ends_with_period() -> None:
    """
    Check that TextMother create method returns a string value that ends with a period.
    """
    value = TextMother.create()

    assert type(value) is str
    assert value[-1] == '.'


@mark.unit_testing
def test_text_mother_of_length_method_happy_path() -> None:
    """
    Check that TextMother of_length method returns a string value with a length equal to the provided length.
    """
    length = IntegerMother.positive()
    value = TextMother.of_length(length=length)

    assert type(value) is str
    assert len(value) == length
    assert value[-1] == '.'


@mark.unit_testing
def test_text_mother_create_method_lowercase_case() -> None:
    """
    Test TextMother create method with lowercase case.
    """
    value = TextMother.create(string_case=StringCase.LOWERCASE)

    assert value.islower()


@mark.unit_testing
def test_text_mother_create_method_uppercase_case() -> None:
    """
    Test TextMother create method with uppercase case.
    """
    value = TextMother.create(string_case=StringCase.UPPERCASE)

    assert value.isupper()


@mark.unit_testing
def test_text_mother_create_method_mixed_case() -> None:
    """
    Test TextMother create method with mixed case.
    """
    value = TextMother.create(string_case=StringCase.MIXEDCASE)

    assert all(char.islower() or char.isupper() or char.isdigit() or char.isspace() or char == '.' for char in value)


@mark.unit_testing
def test_text_mother_create_method_invalid_case() -> None:
    """
    Test TextMother create method with invalid case.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='TextMother string_case must be a StringCase.',
    ):
        TextMother.create(string_case=StringMother.invalid_type())


@mark.unit_testing
def test_text_mother_empty_method_happy_path() -> None:
    """
    Check that TextMother empty method returns an empty string.
    """
    value = TextMother.empty()

    assert type(value) is str
    assert value == ''


@mark.unit_testing
def test_text_mother_of_length_method_invalid_length_type() -> None:
    """
    Check that TextMother of_length method raises a TypeError when the provided length is not an integer.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='TextMother min_length must be an integer.',
    ):
        TextMother.of_length(length=IntegerMother.invalid_type())


@mark.unit_testing
def test_text_mother_of_length_method_minimum_length_value() -> None:
    """
    Check that TextMother of_length method length parameter is the minimum permitted value.
    """
    TextMother.of_length(length=1)


@mark.unit_testing
def test_text_mother_of_length_method_length_random_positive_value() -> None:
    """
    Check that TextMother of_length method length parameter is a random positive integer.
    """
    length = IntegerMother.positive()
    TextMother.of_length(length=length)


@mark.unit_testing
def test_text_mother_of_length_method_invalid_length_zero() -> None:
    """
    Check that TextMother of_length method raises a ValueError when the provided length is negative.
    """
    with assert_raises(
        expected_exception=ValueError,
        match='TextMother min_length must be greater than or equal to 1.',
    ):
        TextMother.of_length(length=0)


@mark.unit_testing
def test_text_mother_of_length_method_invalid_length_random_negative_value() -> None:
    """
    Check that TextMother of_length method raises a ValueError when the provided length is negative.
    """
    with assert_raises(
        expected_exception=ValueError,
        match='TextMother min_length must be greater than or equal to 1.',
    ):
        TextMother.of_length(length=IntegerMother.negative())


@mark.unit_testing
def test_text_mother_of_length_method_length_equal_to_one() -> None:
    """
    Check that TextMother of_length method length parameter is of length equal to 1.
    """
    value = TextMother.of_length(length=1)

    assert value == '.'


@mark.unit_testing
def test_text_mother_invalid_type_method_happy_path() -> None:
    """
    Check that TextMother invalid_type method returns a non-string value.
    """
    assert type(TextMother.invalid_type()) is not str


@mark.unit_testing
def test_text_mother_invalid_value_method_happy_path() -> None:
    """
    Check that TextMother invalid_value method returns a non-printable string value.
    """
    value = TextMother.invalid_value()

    assert type(value) is str
    assert not value.isprintable()
