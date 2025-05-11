"""
Test module for the IntegerMother class.
"""

from pytest import mark, raises as assert_raises

from object_mother_pattern.mothers import IntegerMother


@mark.unit_testing
def test_integer_mother_happy_path() -> None:
    """
    Test IntegerMother happy path.
    """
    value = IntegerMother.create()

    assert type(value) is int
    assert -100 <= value <= 100


@mark.unit_testing
def test_integer_mother_value() -> None:
    """
    Test IntegerMother create method with value.
    """
    value = IntegerMother.create()

    assert IntegerMother.create(value=value) == value


@mark.unit_testing
def test_integer_mother_invalid_type() -> None:
    """
    Test IntegerMother create method with invalid type.
    """
    assert type(IntegerMother.invalid_type()) is not int


@mark.unit_testing
def test_integer_mother_same_min_max() -> None:
    """
    Test IntegerMother create method with same min and max.
    """
    value = IntegerMother.create()

    assert IntegerMother.create(min=value, max=value) == value


@mark.unit_testing
def test_integer_mother_invalid_value_type() -> None:
    """
    Test IntegerMother create method with invalid value type.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='IntegerMother value must be an integer.',
    ):
        IntegerMother.create(value=IntegerMother.invalid_type())


@mark.unit_testing
def test_integer_mother_invalid_min_type() -> None:
    """
    Test IntegerMother create method with invalid min type.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='IntegerMother min value must be an integer.',
    ):
        IntegerMother.create(min=IntegerMother.invalid_type())


@mark.unit_testing
def test_integer_mother_invalid_max_type() -> None:
    """
    Test IntegerMother create method with invalid max type.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='IntegerMother max value must be an integer.',
    ):
        IntegerMother.create(max=IntegerMother.invalid_type())


@mark.unit_testing
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


@mark.unit_testing
def test_integer_mother_positive() -> None:
    """
    Test IntegerMother positive method.
    """
    value = IntegerMother.positive()

    assert type(value) is int
    assert value > 0


@mark.unit_testing
def test_integer_mother_positive_invalid_max_type() -> None:
    """
    Test IntegerMother positive method with invalid max type.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='IntegerMother max value must be an integer.',
    ):
        IntegerMother.positive(max=IntegerMother.invalid_type())


@mark.unit_testing
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


@mark.unit_testing
def test_integer_mother_negative() -> None:
    """
    Test IntegerMother negative method.
    """
    value = IntegerMother.negative()

    assert type(value) is int
    assert value < 0


@mark.unit_testing
def test_integer_mother_negative_invalid_min_type() -> None:
    """
    Test IntegerMother negative method with invalid min type.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='IntegerMother min value must be an integer.',
    ):
        IntegerMother.negative(min=IntegerMother.invalid_type())


@mark.unit_testing
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


@mark.unit_testing
def test_integer_mother_out_of_range() -> None:
    """
    Test IntegerMother out_of_range method.
    """
    min_value = IntegerMother.create(max=0)
    max_value = IntegerMother.create(min=0)
    range_value = IntegerMother.create(min=0)

    value = IntegerMother.out_of_range(min=min_value, max=max_value, range=range_value)

    assert type(value) is int
    assert value < min_value or value > max_value
    assert (min_value - range_value <= value <= min_value) or (max_value <= value <= max_value + range_value)


@mark.unit_testing
def test_integer_mother_out_of_range_invalid_min_type() -> None:
    """
    Test IntegerMother out_of_range method with invalid min type.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='IntegerMother min value must be an integer.',
    ):
        IntegerMother.out_of_range(min=IntegerMother.invalid_type())


@mark.unit_testing
def test_integer_mother_out_of_range_invalid_max_type() -> None:
    """
    Test IntegerMother out_of_range method with invalid max type.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='IntegerMother max value must be an integer.',
    ):
        IntegerMother.out_of_range(max=IntegerMother.invalid_type())


@mark.unit_testing
def test_integer_mother_out_of_range_min_greater_than_max() -> None:
    """
    Test IntegerMother out_of_range method with min greater than max.
    """
    min_value = IntegerMother.positive()
    max_value = IntegerMother.negative()

    with assert_raises(
        expected_exception=ValueError,
        match='IntegerMother min value must be less than or equal to max value.',
    ):
        IntegerMother.out_of_range(min=min_value, max=max_value)


@mark.unit_testing
def test_integer_mother_out_of_range_invalid_range_type() -> None:
    """
    Test IntegerMother out_of_range method with invalid range type.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='IntegerMother range must be an integer.',
    ):
        IntegerMother.out_of_range(range=IntegerMother.invalid_type())


@mark.unit_testing
def test_integer_mother_out_of_range_negative_range() -> None:
    """
    Test IntegerMother out_of_range method with negative range.
    """
    with assert_raises(
        expected_exception=ValueError,
        match='IntegerMother range must be a positive integer.',
    ):
        IntegerMother.out_of_range(range=IntegerMother.negative())
