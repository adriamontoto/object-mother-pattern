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
