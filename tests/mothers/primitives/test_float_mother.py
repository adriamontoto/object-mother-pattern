"""
Test module for the FloatMother class.
"""

from pytest import mark, raises as assert_raises

from object_mother_pattern.mothers import FloatMother, IntegerMother


@mark.unit_testing
def test_float_mother_create_method_happy_path() -> None:
    """
    Check that FloatMother create method returns a random float between -1 and 1 with a random number of decimals
    between 0 and 10.
    """
    value = FloatMother.create()

    assert type(value) is float
    assert -1 <= value <= 1
    assert 0 <= len(str(value).split('.')[1]) <= 10


@mark.unit_testing
def test_float_mother_create_method_value() -> None:
    """
    Check that FloatMother create method returns the provided value.
    """
    value = FloatMother.create()

    assert FloatMother.create(value=value) == value


@mark.unit_testing
def test_float_mother_create_method_invalid_value_type() -> None:
    """
    Check that FloatMother create method raises a TypeError when the provided value is not an integer or a float.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='FloatMother value must be an integer or a float.',
    ):
        FloatMother.create(value=FloatMother.invalid_type())


@mark.unit_testing
def test_float_mother_create_method_same_min_max() -> None:
    """
    Check that FloatMother create method returns the provided value when min and max are the same.
    """
    decimal_number = IntegerMother.create(min=0, max=10)
    value = FloatMother.create(decimals=decimal_number)

    assert FloatMother.create(min=value, max=value, decimals=decimal_number) == value


@mark.unit_testing
def test_float_mother_create_method_invalid_min_type() -> None:
    """
    Check that FloatMother create method raises a TypeError when the provided min is not an integer or a float.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='FloatMother min value must be an integer or a float.',
    ):
        FloatMother.create(min=FloatMother.invalid_type())


@mark.unit_testing
def test_float_mother_create_method_invalid_max_type() -> None:
    """
    Check that FloatMother create method raises a TypeError when the provided max is not an integer or a float.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='FloatMother max value must be an integer or a float.',
    ):
        FloatMother.create(max=FloatMother.invalid_type())


@mark.unit_testing
def test_float_mother_create_method_invalid_decimals_type() -> None:
    """
    Check that FloatMother create method raises a TypeError when the provided decimals is not an integer.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='FloatMother decimals value must be an integer.',
    ):
        FloatMother.create(decimals=IntegerMother.invalid_type())


@mark.unit_testing
def test_float_mother_create_method_min_greater_than_max() -> None:
    """
    Check that FloatMother create method raises a ValueError when the provided min is greater than max.
    """
    min_value = IntegerMother.negative()
    max_value = IntegerMother.positive()

    with assert_raises(
        expected_exception=ValueError,
        match='FloatMother min value must be less than or equal to max value.',
    ):
        FloatMother.create(min=max_value, max=min_value)


@mark.unit_testing
def test_float_mother_create_method_min_decimals_value() -> None:
    """
    Check that FloatMother create method raises a ValueError when the provided decimals is minimum permitted value.
    """
    with assert_raises(
        expected_exception=ValueError,
        match='FloatMother decimals value must be greater than or equal to 0.',
    ):
        FloatMother.create(decimals=-1)


@mark.unit_testing
def test_float_mother_create_method_negative_decimals_random_value() -> None:
    """
    Check that FloatMother create method raises a ValueError when the provided decimals is less than zero.
    """
    with assert_raises(
        expected_exception=ValueError,
        match='FloatMother decimals value must be greater than or equal to 0.',
    ):
        FloatMother.create(decimals=IntegerMother.negative())


@mark.unit_testing
def test_float_mother_create_method_max_decimal_value() -> None:
    """
    Check that FloatMother create method raises a ValueError when the provided decimals is higher than maximum
    permitted value.
    """
    with assert_raises(
        expected_exception=ValueError,
        match='FloatMother decimals value must be less than or equal to 10.',
    ):
        FloatMother.create(decimals=11)


@mark.unit_testing
def test_float_mother_create_method_max_decimal_random_value() -> None:
    """
    Check that FloatMother create method raises a ValueError when the provided decimals is higher than maximum
    permitted value.
    """
    with assert_raises(
        expected_exception=ValueError,
        match='FloatMother decimals value must be less than or equal to 10.',
    ):
        FloatMother.create(decimals=IntegerMother.create(min=11))


@mark.unit_testing
def test_float_mother_create_method_invalid_type() -> None:
    """
    Check that FloatMother create method raises a TypeError when the provided value is not an integer or a float.
    """
    assert type(FloatMother.invalid_type()) is not float


@mark.unit_testing
def test_float_mother_positive_method_happy_path() -> None:
    """
    Check that FloatMother positive method returns a positive float.
    """
    value = FloatMother.positive()

    assert type(value) is float
    assert 0 < value <= 1


@mark.unit_testing
def test_float_mother_positive_method_invalid_max_type() -> None:
    """
    Check that FloatMother positive method raises a TypeError when the provided max is not an integer or a float.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='FloatMother max value must be an integer or a float.',
    ):
        FloatMother.positive(max=FloatMother.invalid_type())


@mark.unit_testing
def test_float_mother_positive_method_invalid_decimals_type() -> None:
    """
    Check that FloatMother positive method raises a TypeError when decimals is not an integer.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='FloatMother decimals value must be an integer.',
    ):
        FloatMother.positive(decimals=FloatMother.invalid_type())


@mark.unit_testing
def test_float_mother_positive_method_negative_decimals_value() -> None:
    """
    Check that FloatMother positive method raises a ValueError when decimals is less than zero.
    """
    with assert_raises(
        expected_exception=ValueError,
        match='FloatMother decimals value must be greater than or equal to 0.',
    ):
        FloatMother.positive(decimals=-1)


@mark.unit_testing
def test_float_mother_positive_method_decimals_above_max() -> None:
    """
    Check that FloatMother positive method raises a ValueError when decimals is higher than maximum permitted value.
    """
    with assert_raises(
        expected_exception=ValueError,
        match='FloatMother decimals value must be less than or equal to 10.',
    ):
        FloatMother.positive(decimals=11)


@mark.unit_testing
def test_float_mother_positive_method_max_value() -> None:
    """
    Check that FloatMother positive method max parameter is the maximum permitted value.
    """
    FloatMother.positive(max=1)


@mark.unit_testing
def test_float_mother_positive_method_max_random_value() -> None:
    """
    Check that FloatMother positive method max parameter is a random positive float.
    """
    max_value = FloatMother.positive()

    FloatMother.positive(max=max_value)


@mark.unit_testing
def test_float_mother_positive_method_handles_tiny_max() -> None:
    """
    Ensure positive handles a max smaller than the minimum positive step for the given decimals by collapsing the range.
    """
    max_value = 0.0005  # smaller than 10**-3
    decimals = 3

    value = FloatMother.positive(max=max_value, decimals=decimals)

    assert value == round(max_value, decimals)
    assert value > 0


@mark.unit_testing
def test_float_mother_positive_or_zero_method_happy_path() -> None:
    """
    Check that FloatMother positive_or_zero method returns a random float between 0 and 1.
    """
    value = FloatMother.positive_or_zero()

    assert type(value) is float
    assert 0 <= value <= 1


@mark.unit_testing
def test_float_mother_positive_or_zero_method_invalid_max_type() -> None:
    """
    Check that FloatMother positive_or_zero method raises a TypeError when the provided max is not an integer or a
    float.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='FloatMother max value must be an integer or a float.',
    ):
        FloatMother.positive_or_zero(max=FloatMother.invalid_type())


@mark.unit_testing
def test_float_mother_negative_method_happy_path() -> None:
    """
    Test FloatMother negative method.
    """
    value = FloatMother.negative()

    assert type(value) is float
    assert -1 <= value < 0


@mark.unit_testing
def test_float_mother_negative_method_invalid_min_type() -> None:
    """
    Check that FloatMother negative method raises a TypeError when the provided min is not an integer or a float.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='FloatMother min value must be an integer or a float.',
    ):
        FloatMother.negative(min=FloatMother.invalid_type())


@mark.unit_testing
def test_float_mother_negative_method_invalid_decimals_type() -> None:
    """
    Check that FloatMother negative method raises a TypeError when decimals is not an integer.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='FloatMother decimals value must be an integer.',
    ):
        FloatMother.negative(decimals=FloatMother.invalid_type())


@mark.unit_testing
def test_float_mother_negative_method_negative_decimals_value() -> None:
    """
    Check that FloatMother negative method raises a ValueError when decimals is less than zero.
    """
    with assert_raises(
        expected_exception=ValueError,
        match='FloatMother decimals value must be greater than or equal to 0.',
    ):
        FloatMother.negative(decimals=-1)


@mark.unit_testing
def test_float_mother_negative_method_decimals_above_max() -> None:
    """
    Check that FloatMother negative method raises a ValueError when decimals is higher than maximum permitted value.
    """
    with assert_raises(
        expected_exception=ValueError,
        match='FloatMother decimals value must be less than or equal to 10.',
    ):
        FloatMother.negative(decimals=11)


@mark.unit_testing
def test_float_mother_negative_method_min_value() -> None:
    """
    Check that FloatMother negative method min parameter is the minimum permitted value.
    """
    FloatMother.negative(min=-1)


@mark.unit_testing
def test_float_mother_negative_method_min_random_value() -> None:
    """
    Check that FloatMother negative method min parameter is a random negative float.
    """
    min_value = FloatMother.negative()

    FloatMother.negative(min=min_value)


@mark.unit_testing
def test_float_mother_negative_method_handles_tiny_min() -> None:
    """
    Ensure negative handles a min greater than its default maximum negative step for the given decimals by collapsing
    the range.
    """
    min_value = -0.0005  # closer to zero than -(10**-3)
    decimals = 3

    value = FloatMother.negative(min=min_value, decimals=decimals)

    assert value == round(min_value, decimals)
    assert value < 0


@mark.unit_testing
def test_float_mother_negative_or_zero_method_happy_path() -> None:
    """
    Check that FloatMother negative_or_zero method returns a random float between -1 and 0.
    """
    value = FloatMother.negative_or_zero()

    assert type(value) is float
    assert -1 <= value <= 0


@mark.unit_testing
def test_float_mother_negative_or_zero_method_invalid_min_type() -> None:
    """
    Check that FloatMother negative_or_zero method raises a TypeError when the provided min is not an integer or a
    float.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='FloatMother min value must be an integer or a float.',
    ):
        FloatMother.negative_or_zero(min=FloatMother.invalid_type())


@mark.unit_testing
def test_float_mother_negative_or_zero_method_min_value() -> None:
    """
    Check that FloatMother negative_or_zero method min parameter is the minimum permitted value.
    """
    FloatMother.negative_or_zero(min=-1)


@mark.unit_testing
def test_float_mother_negative_or_zero_method_min_random_value() -> None:
    """
    Check that FloatMother negative_or_zero method min parameter is a random negative float.
    """
    min_value = FloatMother.negative_or_zero()

    FloatMother.negative_or_zero(min=min_value)


@mark.unit_testing
def test_float_mother_out_of_range_method_happy_path() -> None:
    """
    Check that FloatMother out_of_range method returns a random float value that is either less than min_value or
    greater than max_value.
    """
    min_value = FloatMother.negative()
    max_value = FloatMother.positive()

    value = FloatMother.out_of_range(min=min_value, max=max_value)

    assert type(value) is float
    assert value < min_value or value > max_value
    assert value != min_value and value != max_value


@mark.unit_testing
def test_float_mother_out_of_range_method_invalid_min_type() -> None:
    """
    Check that FloatMother out_of_range method raises a TypeError when the provided min is not an integer or a float.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='FloatMother min value must be an integer or a float.',
    ):
        FloatMother.out_of_range(min=FloatMother.invalid_type())


@mark.unit_testing
def test_float_mother_out_of_range_method_invalid_max_type() -> None:
    """
    Check that FloatMother out_of_range method raises a TypeError when the provided max is not an integer or a float.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='FloatMother max value must be an integer or a float.',
    ):
        FloatMother.out_of_range(max=FloatMother.invalid_type())


@mark.unit_testing
def test_float_mother_out_of_range_method_min_greater_than_max() -> None:
    """
    Check that FloatMother out_of_range method raises a ValueError when the provided min is greater than max.
    """
    min_value = FloatMother.positive()
    max_value = FloatMother.negative()

    with assert_raises(
        expected_exception=ValueError,
        match='FloatMother min value must be less than or equal to max value.',
    ):
        FloatMother.out_of_range(min=min_value, max=max_value)


@mark.unit_testing
def test_float_mother_out_of_range_method_invalid_range_type() -> None:
    """
    Check that FloatMother out_of_range method raises a TypeError when the provided range is not an integer or a float.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='FloatMother range must be an integer or a float.',
    ):
        FloatMother.out_of_range(range=FloatMother.invalid_type())


@mark.unit_testing
def test_float_mother_out_of_range_method_invalid_decimals_type() -> None:
    """
    Check that FloatMother out_of_range method raises a TypeError when decimals is not an integer.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='FloatMother decimals value must be an integer.',
    ):
        FloatMother.out_of_range(decimals=FloatMother.invalid_type())


@mark.unit_testing
def test_float_mother_out_of_range_method_negative_decimals_value() -> None:
    """
    Check that FloatMother out_of_range method raises a ValueError when decimals is less than zero.
    """
    with assert_raises(
        expected_exception=ValueError,
        match='FloatMother decimals value must be greater than or equal to 0.',
    ):
        FloatMother.out_of_range(decimals=-1)


@mark.unit_testing
def test_float_mother_out_of_range_method_decimals_above_max() -> None:
    """
    Check that FloatMother out_of_range method raises a ValueError when decimals is higher than maximum permitted value.
    """
    with assert_raises(
        expected_exception=ValueError,
        match='FloatMother decimals value must be less than or equal to 10.',
    ):
        FloatMother.out_of_range(decimals=11)


@mark.unit_testing
def test_float_mother_out_of_range_method_negative_range_value() -> None:
    """
    Check that FloatMother out_of_range method raises a ValueError when the provided range is the minimum permitted
    value.
    """
    with assert_raises(
        expected_exception=ValueError,
        match='FloatMother range must be greater than 0.',
    ):
        FloatMother.out_of_range(range=0)
