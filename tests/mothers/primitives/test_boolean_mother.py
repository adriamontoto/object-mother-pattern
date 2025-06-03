"""
Test module for the BooleanMother class.
"""

from math import inf, nextafter

from pytest import mark, raises as assert_raises

from object_mother_pattern.mothers import BooleanMother, FloatMother


@mark.unit_testing
def test_boolean_mother_create_method_happy_path() -> None:
    """
    Check that BooleanMother create method returns a boolean value.
    """
    value = BooleanMother.create()

    assert type(value) is bool


@mark.unit_testing
def test_boolean_mother_create_method_value() -> None:
    """
    Check that BooleanMother create method returns the provided value.
    """
    value = BooleanMother.create()

    assert BooleanMother.create(value=value) == value


@mark.unit_testing
def test_boolean_mother_create_method_invalid_value_type() -> None:
    """
    Check that BooleanMother create method raises a TypeError when the provided value is not a boolean.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='BooleanMother value must be a boolean.',
    ):
        BooleanMother.create(value=BooleanMother.invalid_type())


@mark.unit_testing
def test_boolean_mother_create_method_probability_true_hundred_percent() -> None:
    """
    Check that BooleanMother create method returns True when the probability of True is 1.0.
    """
    value = BooleanMother.create(probabilty_true=1.0)

    assert value


@mark.unit_testing
def test_boolean_mother_create_method_probability_true_zero_percent() -> None:
    """
    Check that BooleanMother create method returns True when the probability of True is 0.0.
    """
    value = BooleanMother.create(probabilty_true=0.0)

    assert not value


@mark.unit_testing
def test_boolean_mother_create_method_invalid_probability_true_type() -> None:
    """
    Check that BooleanMother create method raises a TypeError when the provided probability is not a float.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='BooleanMother probabilty_true must be a float.',
    ):
        BooleanMother.create(probabilty_true=FloatMother.invalid_type())


@mark.unit_testing
def test_boolean_mother_create_method_negative_probability_true() -> None:
    """
    Check that BooleanMother create method raises a ValueError when the provided probability is less than 0.0.
    """
    with assert_raises(
        expected_exception=ValueError,
        match='BooleanMother probabilty_true must be greater than or equal to 0.0.',
    ):
        BooleanMother.create(probabilty_true=nextafter(0.0, -inf))


@mark.unit_testing
def test_boolean_mother_create_method_random_negative_probability_true() -> None:
    """
    Check that BooleanMother create method raises a ValueError when the provided probability is less than 0.0.
    """
    with assert_raises(
        expected_exception=ValueError,
        match='BooleanMother probabilty_true must be greater than or equal to 0.0.',
    ):
        BooleanMother.create(probabilty_true=FloatMother.create(max=nextafter(0.0, -inf)))


@mark.unit_testing
def test_boolean_mother_create_method_greater_than_one_probability_true() -> None:
    """
    Check that BooleanMother create method raises a ValueError when the provided probability is more than 1.0.
    """
    with assert_raises(
        expected_exception=ValueError,
        match='BooleanMother probabilty_true must be less than or equal to 1.0.',
    ):
        BooleanMother.create(probabilty_true=nextafter(1.0, inf))


@mark.unit_testing
def test_boolean_mother_create_method_random_positive_probability_true() -> None:
    """
    Check that BooleanMother create method raises a ValueError when the provided probability is more than 1.0.
    """
    with assert_raises(
        expected_exception=ValueError,
        match='BooleanMother probabilty_true must be less than or equal to 1.0.',
    ):
        BooleanMother.create(probabilty_true=FloatMother.create(min=nextafter(1.0, inf), max=inf))


@mark.unit_testing
def test_boolean_mother_true_method_happy_path() -> None:
    """
    Check that BooleanMother true method returns True.
    """
    assert BooleanMother.true() is True


@mark.unit_testing
def test_boolean_mother_false_method_happy_path() -> None:
    """
    Check that BooleanMother false method returns False.
    """
    assert BooleanMother.false() is False


@mark.unit_testing
def test_boolean_mother_invalid_type_method() -> None:
    """
    Check that BooleanMother invalid_type method returns a value that is not a boolean.
    """
    assert type(BooleanMother.invalid_type()) is not bool
