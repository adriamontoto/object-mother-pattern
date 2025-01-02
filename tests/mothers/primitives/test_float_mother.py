"""
Test module for the FloatMother class.
"""

from pytest import raises as assert_raises

from object_mother_pattern.mothers import FloatMother, IntegerMother


def test_float_mother_happy_path() -> None:
    """
    Test FloatMother happy path.
    """
    value = FloatMother.create()

    assert type(value) is float
    assert -1 <= value <= 1


def test_float_mother_value() -> None:
    """
    Test FloatMother create method with value.
    """
    value = FloatMother.create()

    assert FloatMother.create(value=value) == value


def test_float_mother_invalid_type() -> None:
    """
    Test FloatMother create method with invalid type.
    """
    assert type(FloatMother.invalid_type()) is not float


def test_float_mother_same_min_max() -> None:
    """
    Test FloatMother create method with same min and max.
    """
    value = FloatMother.create()

    assert FloatMother.create(min=value, max=value) == value


def test_float_mother_invalid_value_type() -> None:
    """
    Test FloatMother create method with invalid value type.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='FloatMother value must be an integer or a float.',
    ):
        FloatMother.create(value=FloatMother.invalid_type(remove_types=[int]))


def test_float_mother_invalid_min_type() -> None:
    """
    Test FloatMother create method with invalid min type.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='FloatMother min value must be an integer or a float.',
    ):
        FloatMother.create(min=FloatMother.invalid_type(remove_types=[int]))


def test_float_mother_invalid_max_type() -> None:
    """
    Test FloatMother create method with invalid max type.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='FloatMother max value must be an integer or a float.',
    ):
        FloatMother.create(max=FloatMother.invalid_type(remove_types=[int]))


def test_float_mother_invalid_decimals_type() -> None:
    """
    Test FloatMother create method with invalid decimals type.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='FloatMother decimals value must be an integer.',
    ):
        FloatMother.create(decimals=IntegerMother.invalid_type())


def test_float_mother_invalid_decimals_less_than_zero() -> None:
    """
    Test FloatMother create method with invalid decimals value less than zero.
    """
    with assert_raises(
        expected_exception=ValueError,
        match='FloatMother decimals value must be greater than or equal to 0.',
    ):
        FloatMother.create(decimals=IntegerMother.negative())


def test_float_mother_invalid_decimals_higher_than_ten() -> None:
    """
    Test FloatMother create method with invalid decimals value higher than ten.
    """
    with assert_raises(
        expected_exception=ValueError,
        match='FloatMother decimals value must be less than or equal to 10.',
    ):
        FloatMother.create(decimals=IntegerMother.create(min=11))


def test_float_mother_min_greater_than_max() -> None:
    """
    Test FloatMother create method with min greater than max.
    """
    min_value = FloatMother.negative()
    max_value = FloatMother.positive()

    with assert_raises(
        expected_exception=ValueError,
        match='FloatMother min value must be less than or equal to max value.',
    ):
        FloatMother.create(min=max_value, max=min_value)


def test_float_mother_positive() -> None:
    """
    Test FloatMother positive method.
    """
    value = FloatMother.positive()

    assert type(value) is float
    assert value > 0


def test_float_mother_positive_invalid_max_type() -> None:
    """
    Test FloatMother positive method with invalid max type.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='FloatMother max value must be an integer.',
    ):
        FloatMother.positive(max=FloatMother.invalid_type(remove_types=[int]))


def test_float_mother_positive_max_less_than_one() -> None:
    """
    Test FloatMother positive method with max less than 1.
    """
    max_value = FloatMother.create(max=0)

    with assert_raises(
        expected_exception=ValueError,
        match='FloatMother min value must be less than or equal to max value.',
    ):
        FloatMother.positive(max=max_value)


def test_float_mother_negative() -> None:
    """
    Test FloatMother negative method.
    """
    value = FloatMother.negative()

    assert type(value) is float
    assert value < 0


def test_float_mother_negative_invalid_min_type() -> None:
    """
    Test FloatMother negative method with invalid min type.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='FloatMother min value must be an integer.',
    ):
        FloatMother.negative(min=FloatMother.invalid_type(remove_types=[int]))


def test_float_mother_negative_min_greater_than_zero() -> None:
    """
    Test FloatMother negative method with min greater than 0.
    """
    min_value = FloatMother.create(min=1)

    with assert_raises(
        expected_exception=ValueError,
        match='FloatMother min value must be less than or equal to max value.',
    ):
        FloatMother.negative(min=min_value)
