"""
Test module for the IntegerMother class.
"""

from pytest import raises as assert_raises

from object_mother_pattern.mothers import IntegerMother


def test_integer_mother_happy_path() -> None:
    """
    Test IntegerMother happy path.
    """
    value = IntegerMother.create()

    assert type(value) is int
    assert -100 <= value <= 100


def test_integer_mother_value() -> None:
    """
    Test IntegerMother create method with value.
    """
    value = IntegerMother.create()

    assert IntegerMother.create(value=value) == value


def test_integer_mother_invalid_type() -> None:
    """
    Test IntegerMother create method with invalid type.
    """
    assert type(IntegerMother.invalid_type()) is not int


def test_integer_mother_same_min_max() -> None:
    """
    Test IntegerMother create method with same min and max.
    """
    value = IntegerMother.create()

    assert IntegerMother.create(min=value, max=value) == value


def test_integer_mother_invalid_value_type() -> None:
    """
    Test IntegerMother create method with invalid value type.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='IntegerMother value must be an integer.',
    ):
        IntegerMother.create(value=IntegerMother.invalid_type())


def test_integer_mother_invalid_min_type() -> None:
    """
    Test IntegerMother create method with invalid min type.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='IntegerMother min value must be an integer.',
    ):
        IntegerMother.create(min=IntegerMother.invalid_type())


def test_integer_mother_invalid_max_type() -> None:
    """
    Test IntegerMother create method with invalid max type.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='IntegerMother max value must be an integer.',
    ):
        IntegerMother.create(max=IntegerMother.invalid_type())


def test_integer_mother_min_greater_than_max() -> None:
    """
    Test IntegerMother create method with min greater than max.
    """
    min_value = IntegerMother.negative()
    max_value = IntegerMother.positive()

    with assert_raises(
        expected_exception=ValueError,
        match='IntegerMother min value must be less than or equal to max value.',
    ):
        IntegerMother.create(min=max_value, max=min_value)


def test_integer_mother_positive() -> None:
    """
    Test IntegerMother positive method.
    """
    value = IntegerMother.positive()

    assert type(value) is int
    assert value > 0


def test_integer_mother_positive_invalid_max_type() -> None:
    """
    Test IntegerMother positive method with invalid max type.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='IntegerMother max value must be an integer.',
    ):
        IntegerMother.positive(max=IntegerMother.invalid_type())


def test_integer_mother_positive_max_less_than_one() -> None:
    """
    Test IntegerMother positive method with max less than 1.
    """
    max_value = IntegerMother.create(max=0)

    with assert_raises(
        expected_exception=ValueError,
        match='IntegerMother min value must be less than or equal to max value.',
    ):
        IntegerMother.positive(max=max_value)


def test_integer_mother_negative() -> None:
    """
    Test IntegerMother negative method.
    """
    value = IntegerMother.negative()

    assert type(value) is int
    assert value < 0


def test_integer_mother_negative_invalid_min_type() -> None:
    """
    Test IntegerMother negative method with invalid min type.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='IntegerMother min value must be an integer.',
    ):
        IntegerMother.negative(min=IntegerMother.invalid_type())


def test_integer_mother_negative_min_greater_than_zero() -> None:
    """
    Test IntegerMother negative method with min greater than 0.
    """
    min_value = IntegerMother.create(min=1)

    with assert_raises(
        expected_exception=ValueError,
        match='IntegerMother min value must be less than or equal to max value.',
    ):
        IntegerMother.negative(min=min_value)
