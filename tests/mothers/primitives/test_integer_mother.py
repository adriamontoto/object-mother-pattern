"""
Test module for the IntegerMother class.
"""

from pytest import mark, raises as assert_raises

from object_mother_pattern.mothers import IntegerMother


@mark.unit_testing
def test_integer_mother_create_method_happy_path() -> None:
    """
    Check that IntegerMother create method returns a random integer between -100 and 100.
    """
    value = IntegerMother.create()

    assert type(value) is int
    assert -100 <= value <= 100


@mark.unit_testing
def test_integer_mother_create_method_value() -> None:
    """
    Check that IntegerMother create method returns the provided value.
    """
    value = IntegerMother.create()

    assert IntegerMother.create(value=value) == value


@mark.unit_testing
def test_integer_mother_create_method_invalid_value_type() -> None:
    """
    Check that IntegerMother create method raises a TypeError when the provided value is not an integer.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='IntegerMother value must be an integer.',
    ):
        IntegerMother.create(value=IntegerMother.invalid_type())


@mark.unit_testing
def test_integer_mother_create_method_same_min_max() -> None:
    """
    Check that IntegerMother create method returns the provided value when min and max are the same.
    """
    value = IntegerMother.create()

    assert IntegerMother.create(min=value, max=value) == value


@mark.unit_testing
def test_integer_mother_create_method_invalid_max_type() -> None:
    """
    Check that IntegerMother create method raises a TypeError when the provided max is not an integer.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='IntegerMother max value must be an integer.',
    ):
        IntegerMother.create(max=IntegerMother.invalid_type())


@mark.unit_testing
def test_integer_mother_create_method_invalid_min_type() -> None:
    """
    Check that IntegerMother create method raises a TypeError when the provided min is not an integer.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='IntegerMother min value must be an integer.',
    ):
        IntegerMother.create(min=IntegerMother.invalid_type())


@mark.unit_testing
def test_integer_mother_create_method_min_greater_than_max() -> None:
    """
    Check that IntegerMother create method raises a ValueError when the provided min is greater than max.
    """
    min_value = IntegerMother.negative()
    max_value = IntegerMother.positive()

    with assert_raises(
        expected_exception=ValueError,
        match='IntegerMother min value must be less than or equal to max value.',
    ):
        IntegerMother.create(min=max_value, max=min_value)


@mark.unit_testing
def test_integer_mother_positive_method_happy_path() -> None:
    """
    Check that IntegerMother positive method returns a positive integer.
    """
    value = IntegerMother.positive()

    assert type(value) is int
    assert 0 < value <= 100


@mark.unit_testing
def test_integer_mother_positive_method_invalid_max_type() -> None:
    """
    Check that IntegerMother positive method raises a TypeError when the provided max is not an integer.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='IntegerMother max value must be an integer.',
    ):
        IntegerMother.positive(max=IntegerMother.invalid_type())


@mark.unit_testing
def test_integer_mother_positive_method_max_value() -> None:
    """
    Check that IntegerMother positive method max parameter is the maximum permitted value.
    """
    IntegerMother.positive(max=1)


@mark.unit_testing
def test_integer_mother_positive_method_max_random_value() -> None:
    """
    Check that IntegerMother positive method max parameter is a random positive integer.
    """
    max_value = IntegerMother.positive()

    IntegerMother.positive(max=max_value)


@mark.unit_testing
def test_integer_mother_positive_method_max_not_greater_than_zero_value() -> None:
    """
    Check that IntegerMother positive method raises a ValueError when the provided max is not greater than 0.
    """
    with assert_raises(
        expected_exception=ValueError,
        match='IntegerMother min value must be less than or equal to max value.',
    ):
        IntegerMother.positive(max=0)


@mark.unit_testing
def test_integer_mother_positive_method_max_not_greater_than_zero_random_value() -> None:
    """
    Check that IntegerMother positive method raises a ValueError when the provided max is not greater than 0.
    """
    max_value = IntegerMother.negative_or_zero()

    with assert_raises(
        expected_exception=ValueError,
        match='IntegerMother min value must be less than or equal to max value.',
    ):
        IntegerMother.positive(max=max_value)


@mark.unit_testing
def test_integer_mother_positive_or_zero_method_happy_path() -> None:
    """
    Check that IntegerMother positive_or_zero method returns a random integer between 0 and 100.
    """
    value = IntegerMother.positive_or_zero()

    assert type(value) is int
    assert 0 <= value <= 100


@mark.unit_testing
def test_integer_mother_positive_or_zero_method_invalid_max_type() -> None:
    """
    Test IntegerMother negative method.
    """
    value = IntegerMother.negative()

    assert type(value) is int
    assert -100 <= value < 0


@mark.unit_testing
def test_integer_mother_negative_method_invalid_min_type() -> None:
    """
    Check that IntegerMother negative method raises a TypeError when the provided min is not an integer.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='IntegerMother min value must be an integer.',
    ):
        IntegerMother.negative(min=IntegerMother.invalid_type())


@mark.unit_testing
def test_integer_mother_negative_method_min_value() -> None:
    """
    Check that IntegerMother negative method min parameter is the minimum permitted value.
    """
    IntegerMother.negative(min=-1)


@mark.unit_testing
def test_integer_mother_negative_method_min_random_value() -> None:
    """
    Check that IntegerMother negative method min parameter is a random negative integer.
    """
    min_value = IntegerMother.negative()

    IntegerMother.negative(min=min_value)


@mark.unit_testing
def test_integer_mother_negative_method_min_greater_than_zero() -> None:
    """
    Check that IntegerMother negative method raises a ValueError when the provided min is greater than or equal to 0.
    """
    min_value = IntegerMother.positive_or_zero()

    with assert_raises(
        expected_exception=ValueError,
        match='IntegerMother min value must be less than or equal to max value.',
    ):
        IntegerMother.negative(min=min_value)


@mark.unit_testing
def test_integer_mother_negative_or_zero_method_happy_path() -> None:
    """
    Check that IntegerMother negative_or_zero method returns a random integer between -100 and 0.
    """
    value = IntegerMother.negative_or_zero()

    assert type(value) is int
    assert -100 <= value <= 0


@mark.unit_testing
def test_integer_mother_negative_or_zero_method_invalid_min_type() -> None:
    """
    Check that IntegerMother negative_or_zero method raises a TypeError when the provided min is not an integer.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='IntegerMother min value must be an integer.',
    ):
        IntegerMother.negative_or_zero(min=IntegerMother.invalid_type())


@mark.unit_testing
def test_integer_mother_negative_or_zero_method_min_value() -> None:
    """
    Check that IntegerMother negative_or_zero method min parameter is the minimum permitted value.
    """
    IntegerMother.negative_or_zero(min=-1)


@mark.unit_testing
def test_integer_mother_negative_or_zero_method_min_random_value() -> None:
    """
    Check that IntegerMother negative_or_zero method min parameter is a random negative integer.
    """
    min_value = IntegerMother.negative_or_zero()

    IntegerMother.negative_or_zero(min=min_value)


@mark.unit_testing
def test_integer_mother_out_of_range_method_happy_path() -> None:
    """
    Check that IntegerMother out_of_range method returns a random integer value that is either less than min_value or
    greater than max_value.
    """
    min_value = IntegerMother.negative()
    max_value = IntegerMother.positive()

    value = IntegerMother.out_of_range(min=min_value, max=max_value)

    assert type(value) is int
    assert value < min_value or value > max_value
    assert value != min_value and value != max_value


@mark.unit_testing
def test_integer_mother_out_of_range_method_invalid_min_type() -> None:
    """
    Check that IntegerMother out_of_range method raises a TypeError when the provided min is not an integer.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='IntegerMother min value must be an integer.',
    ):
        IntegerMother.out_of_range(min=IntegerMother.invalid_type())


@mark.unit_testing
def test_integer_mother_out_of_range_method_invalid_max_type() -> None:
    """
    Check that IntegerMother out_of_range method raises a TypeError when the provided max is not an integer.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='IntegerMother max value must be an integer.',
    ):
        IntegerMother.out_of_range(max=IntegerMother.invalid_type())


@mark.unit_testing
def test_integer_mother_out_of_range_method_min_greater_than_max() -> None:
    """
    Check that IntegerMother out_of_range method raises a ValueError when the provided min is greater than max.
    """
    min_value = IntegerMother.positive()
    max_value = IntegerMother.negative()

    with assert_raises(
        expected_exception=ValueError,
        match='IntegerMother min value must be less than or equal to max value.',
    ):
        IntegerMother.out_of_range(min=min_value, max=max_value)


@mark.unit_testing
def test_integer_mother_out_of_range_method_invalid_range_type() -> None:
    """
    Check that IntegerMother out_of_range method raises a TypeError when the provided range is not an integer.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='IntegerMother range must be an integer.',
    ):
        IntegerMother.out_of_range(range=IntegerMother.invalid_type())


@mark.unit_testing
def test_integer_mother_out_of_range_method_negative_range_value() -> None:
    """
    Check that IntegerMother out_of_range method raises a ValueError when the provided range is the minimum permitted
    value.
    """
    with assert_raises(
        expected_exception=ValueError,
        match='IntegerMother range must be greater than 0.',
    ):
        IntegerMother.out_of_range(range=0)


@mark.unit_testing
def test_integer_mother_out_of_range_method_negative_random_range_value() -> None:
    """
    Check that IntegerMother out_of_range method raises a ValueError when the provided range is a random negative value.
    """
    with assert_raises(
        expected_exception=ValueError,
        match='IntegerMother range must be greater than 0.',
    ):
        IntegerMother.out_of_range(range=IntegerMother.negative_or_zero())


@mark.unit_testing
def test_integer_mother_create_method_invalid_type() -> None:
    """
    Check that IntegerMother create method raises a TypeError when the provided value is not an integer.
    """
    assert type(IntegerMother.invalid_type()) is not int
