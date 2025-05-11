"""
Test module for the FloatMother class.
"""

from pytest import mark, raises as assert_raises

from object_mother_pattern.mothers import FloatMother, IntegerMother


@mark.unit_testing
def test_float_mother_happy_path() -> None:
    """
    Test FloatMother happy path.
    """
    value = FloatMother.create()

    assert type(value) is float
    assert -1 <= value <= 1


@mark.unit_testing
def test_float_mother_value() -> None:
    """
    Test FloatMother create method with value.
    """
    value = FloatMother.create()

    assert FloatMother.create(value=value) == value


@mark.unit_testing
def test_float_mother_invalid_type() -> None:
    """
    Test FloatMother create method with invalid type.
    """
    assert type(FloatMother.invalid_type()) is not float


@mark.unit_testing
def test_float_mother_same_min_max() -> None:
    """
    Test FloatMother create method with same min and max.
    """
    value = FloatMother.create()

    assert FloatMother.create(min=value, max=value, decimals=10) == value


@mark.unit_testing
def test_float_mother_invalid_value_type() -> None:
    """
    Test FloatMother create method with invalid value type.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='FloatMother value must be an integer or a float.',
    ):
        FloatMother.create(value=FloatMother.invalid_type(remove_types=(int,)))


@mark.unit_testing
def test_float_mother_invalid_min_type() -> None:
    """
    Test FloatMother create method with invalid min type.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='FloatMother min value must be an integer or a float.',
    ):
        FloatMother.create(min=FloatMother.invalid_type(remove_types=(int,)))


@mark.unit_testing
def test_float_mother_invalid_max_type() -> None:
    """
    Test FloatMother create method with invalid max type.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='FloatMother max value must be an integer or a float.',
    ):
        FloatMother.create(max=FloatMother.invalid_type(remove_types=(int,)))


@mark.unit_testing
def test_float_mother_invalid_decimals_type() -> None:
    """
    Test FloatMother create method with invalid decimals type.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='FloatMother decimals value must be an integer.',
    ):
        FloatMother.create(decimals=IntegerMother.invalid_type())


@mark.unit_testing
def test_float_mother_invalid_decimals_less_than_zero() -> None:
    """
    Test FloatMother create method with invalid decimals value less than zero.
    """
    with assert_raises(
        expected_exception=ValueError,
        match='FloatMother decimals value must be greater than or equal to 0.',
    ):
        FloatMother.create(decimals=IntegerMother.negative())


@mark.unit_testing
def test_float_mother_invalid_decimals_higher_than_ten() -> None:
    """
    Test FloatMother create method with invalid decimals value higher than ten.
    """
    with assert_raises(
        expected_exception=ValueError,
        match='FloatMother decimals value must be less than or equal to 10.',
    ):
        FloatMother.create(decimals=IntegerMother.create(min=11))


@mark.unit_testing
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


@mark.unit_testing
def test_float_mother_positive() -> None:
    """
    Test FloatMother positive method.
    """
    value = FloatMother.positive()

    assert type(value) is float
    assert value >= 0


@mark.unit_testing
def test_float_mother_positive_invalid_max_type() -> None:
    """
    Test FloatMother positive method with invalid max type.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='FloatMother max value must be an integer.',
    ):
        FloatMother.positive(max=FloatMother.invalid_type(remove_types=(int,)))


@mark.unit_testing
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


@mark.unit_testing
def test_float_mother_negative() -> None:
    """
    Test FloatMother negative method.
    """
    value = FloatMother.negative()

    assert type(value) is float
    assert value <= 0


@mark.unit_testing
def test_float_mother_negative_invalid_min_type() -> None:
    """
    Test FloatMother negative method with invalid min type.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='FloatMother min value must be an integer.',
    ):
        FloatMother.negative(min=FloatMother.invalid_type(remove_types=(int,)))


@mark.unit_testing
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


@mark.unit_testing
def test_float_mother_out_of_range() -> None:
    """
    Test FloatMother out_of_range method.
    """
    min_value = FloatMother.create(max=0)
    max_value = FloatMother.create(min=0)
    range_value = FloatMother.create(min=0)
    value = FloatMother.out_of_range(min=min_value, max=max_value, range=range_value)

    assert type(value) is float
    assert value < min_value or value > max_value
    assert (min_value - range_value <= value <= min_value) or (max_value <= value <= max_value + range_value)


@mark.unit_testing
def test_float_mother_out_of_range_invalid_min_type() -> None:
    """
    Test FloatMother out_of_range method with invalid min type.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='FloatMother min value must be an integer or a float.',
    ):
        FloatMother.out_of_range(min=FloatMother.invalid_type(remove_types=(int, float)))


@mark.unit_testing
def test_float_mother_out_of_range_invalid_max_type() -> None:
    """
    Test FloatMother out_of_range method with invalid max type.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='FloatMother max value must be an integer or a float.',
    ):
        FloatMother.out_of_range(max=FloatMother.invalid_type(remove_types=(int, float)))


@mark.unit_testing
def test_float_mother_out_of_range_min_greater_than_max() -> None:
    """
    Test FloatMother out_of_range method with min greater than max.
    """
    min_value = FloatMother.positive()
    max_value = FloatMother.negative()

    with assert_raises(
        expected_exception=ValueError,
        match='FloatMother min value must be less than or equal to max value.',
    ):
        FloatMother.out_of_range(min=min_value, max=max_value)


@mark.unit_testing
def test_float_mother_out_of_range_invalid_range_type() -> None:
    """
    Test FloatMother out_of_range method with invalid range type.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='FloatMother range must be an integer or a float.',
    ):
        FloatMother.out_of_range(range=FloatMother.invalid_type(remove_types=(int, float)))


@mark.unit_testing
def test_float_mother_out_of_range_negative_range() -> None:
    """
    Test FloatMother out_of_range method with negative range.
    """
    with assert_raises(
        expected_exception=ValueError,
        match='FloatMother range must be a positive value.',
    ):
        FloatMother.out_of_range(range=FloatMother.negative())
