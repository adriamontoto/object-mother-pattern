"""
Test module for the StringMother class.
"""

from pytest import raises as assert_raises

from object_mother_pattern.mothers import IntegerMother, StringMother


def test_string_mother_happy_path() -> None:
    """
    Test StringMother happy path.
    """
    value = StringMother.create()

    assert type(value) is str


def test_string_mother_value() -> None:
    """
    Test StringMother create method with value.
    """
    value = StringMother.create()

    assert StringMother.create(value=value) == value


def test_string_mother_invalid_type() -> None:
    """
    Test StringMother create method with invalid type.
    """
    assert type(StringMother.invalid_type()) is not str


def test_string_mother_invalid_value() -> None:
    """
    Test StringMother invalid_value method.
    """
    value = StringMother.invalid_value()

    assert type(value) is str
    assert not value.isprintable()


def test_string_mother_invalid_value_type() -> None:
    """
    Test StringMother create method with invalid value type.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='StringMother value must be a string.',
    ):
        StringMother.create(value=StringMother.invalid_type())


def test_string_mother_invalid_min_length_type() -> None:
    """
    Test StringMother create method with invalid min_length type.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='StringMother min_length must be an integer.',
    ):
        StringMother.create(min_length=IntegerMother.invalid_type())


def test_string_mother_invalid_min_length_value() -> None:
    """
    Test StringMother create method with invalid min_length value.
    """
    with assert_raises(
        expected_exception=ValueError,
        match='StringMother min_length must be greater than 0.',
    ):
        StringMother.create(min_length=IntegerMother.negative())


def test_string_mother_invalid_max_length_type() -> None:
    """
    Test StringMother create method with invalid max_length type.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='StringMother max_length must be an integer.',
    ):
        StringMother.create(max_length=IntegerMother.invalid_type())


def test_string_mother_invalid_max_length_value() -> None:
    """
    Test StringMother create method with invalid max_length value.
    """
    with assert_raises(
        expected_exception=ValueError,
        match='StringMother max_length must be greater than 0.',
    ):
        StringMother.create(max_length=IntegerMother.negative())


def test_string_mother_min_length_greater_than_max_length() -> None:
    """
    Test StringMother create method with min_length greater than max_length.
    """
    min_value = IntegerMother.create(min=0)
    max_value = IntegerMother.create(min=1000, max=2000)

    with assert_raises(
        expected_exception=ValueError,
        match='StringMother min_length must be less than or equal to max_length.',
    ):
        StringMother.create(min_length=max_value, max_length=min_value)


def test_string_mother_of_length() -> None:
    """
    Test StringMother of_length method.
    """
    length = IntegerMother.create(min=0)
    value = StringMother.of_length(length=length)

    assert len(value) == length


def test_string_mother_of_length_invalid_length_type() -> None:
    """
    Test StringMother of_length method with invalid length type.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='StringMother min_length must be an integer.',
    ):
        StringMother.of_length(length=IntegerMother.invalid_type())


def test_string_mother_of_length_invalid_length_value() -> None:
    """
    Test StringMother of_length method with invalid length value.
    """
    with assert_raises(
        expected_exception=ValueError,
        match='StringMother min_length must be greater than 0.',
    ):
        StringMother.of_length(length=IntegerMother.negative())
