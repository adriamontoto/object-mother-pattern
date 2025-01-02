"""
Test module for the StringDatetimeMother class.
"""

from datetime import UTC, datetime

from dateutil.relativedelta import relativedelta
from pytest import raises as assert_raises

from object_mother_pattern.mothers import DatetimeMother, IntegerMother, StringDatetimeMother


def test_string_datetime_mother_happy_path() -> None:
    """
    Test StringDatetimeMother happy path.
    """
    value = StringDatetimeMother.create()

    assert type(value) is str
    datetime.fromisoformat(value)


def test_string_datetime_mother_value() -> None:
    """
    Test StringDatetimeMother create method with value.
    """
    value = StringDatetimeMother.create()

    assert StringDatetimeMother.create(value=value) == value


def test_string_datetime_mother_invalid_type() -> None:
    """
    Test StringDatetimeMother create method with invalid type.
    """
    assert type(StringDatetimeMother.invalid_type()) is not str


def test_string_datetime_mother_invalid_value_type() -> None:
    """
    Test StringDatetimeMother create method with invalid value type.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='StringDatetimeMother value must be a string.',
    ):
        StringDatetimeMother.create(value=StringDatetimeMother.invalid_type())


# E       AssertionError: Regex pattern did not match.
# E        Regex: 'DatetimeMother end_datetime must be a date.'
# E        Input: "can't compare offset-naive and offset-aware datetimes"


# tests/mothers/additional_types/test_string_datetime_mother.py:123: AssertionError
def test_string_datetime_mother_invalid_start_datetime_type() -> None:
    """
    Test StringDatetimeMother create method with invalid start_datetime type.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='DatetimeMother start_datetime must be a datetime.',
    ):
        StringDatetimeMother.create(start_datetime=StringDatetimeMother.invalid_type())


def test_string_datetime_mother_invalid_end_datetime_type() -> None:
    """
    Test StringDatetimeMother create method with invalid end_datetime type.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='DatetimeMother end_datetime must be a date.',
    ):
        StringDatetimeMother.create(end_datetime=StringDatetimeMother.invalid_type())


def test_string_datetime_mother_start_datetime_greater_than_end_datetime() -> None:
    """
    Test StringDatetimeMother create method with start_datetime greater than end_datetime.
    """
    start_datetime = DatetimeMother.create(
        start_datetime=datetime.now(tz=UTC),
        end_datetime=datetime.now(tz=UTC) + relativedelta(years=100),
    )
    end_datetime = DatetimeMother.create(
        start_datetime=datetime.now(tz=UTC) - relativedelta(years=100),
        end_datetime=datetime.now(tz=UTC),
    )

    with assert_raises(
        expected_exception=ValueError,
        match='DatetimeMother end_datetime must be older than start_datetime.',
    ):
        StringDatetimeMother.create(start_datetime=start_datetime, end_datetime=end_datetime)


def test_string_datetime_mother_out_of_range_method_happy_path() -> None:
    """
    Test StringDatetimeMother happy path.
    """
    start_datetime = datetime.now(tz=UTC) - relativedelta(years=100)
    end_datetime = datetime.now(tz=UTC)

    value = StringDatetimeMother.out_of_range(start_datetime=start_datetime, end_datetime=end_datetime)

    assert type(value) is str
    assert (
        start_datetime >= datetime.fromisoformat(value) <= end_datetime
        or start_datetime <= datetime.fromisoformat(value) >= end_datetime
    )


# E       AssertionError: Regex pattern did not match.
# E        Regex: 'DatetimeMother end_datetime must be a date.'
# E        Input: "can't compare offset-naive and offset-aware datetimes"


# tests/mothers/additional_types/test_string_datetime_mother.py:123: AssertionError
def test_string_datetime_mother_out_of_range_method_invalid_start_datetime_type() -> None:
    """
    Test StringDatetimeMother create method with invalid start_datetime type.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='DatetimeMother start_datetime must be a date.',
    ):
        StringDatetimeMother.out_of_range(start_datetime=StringDatetimeMother.invalid_type())


# E       AssertionError: Regex pattern did not match.
# E        Regex: 'DatetimeMother end_datetime must be a date.'
# E        Input: "can't compare offset-naive and offset-aware datetimes"


# tests/mothers/additional_types/test_string_datetime_mother.py:123: AssertionError
def test_string_datetime_mother_out_of_range_method_invalid_end_datetime_type() -> None:
    """
    Test StringDatetimeMother create method with invalid end_datetime type.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='DatetimeMother end_datetime must be a date.',
    ):
        StringDatetimeMother.out_of_range(end_datetime=StringDatetimeMother.invalid_type())


def test_string_datetime_mother_out_of_range_method_invalid_range_type() -> None:
    """
    Test StringDatetimeMother create method with invalid range type.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='DatetimeMother range must be an integer.',
    ):
        StringDatetimeMother.out_of_range(range=IntegerMother.invalid_type())


def test_string_datetime_mother_out_of_range_method_invalid_range_value() -> None:
    """
    Test StringDatetimeMother create method with invalid range value.
    """
    with assert_raises(
        expected_exception=ValueError,
        match='DatetimeMother range must be a positive integer.',
    ):
        StringDatetimeMother.out_of_range(range=IntegerMother.negative())


def test_string_datetime_mother_out_of_range_method_start_datetime_greater_than_end_datetime() -> None:
    """
    Test StringDatetimeMother create method with start_datetime greater than end_datetime.
    """
    start_datetime = DatetimeMother.create(
        start_datetime=datetime.now(tz=UTC),
        end_datetime=datetime.now(tz=UTC) + relativedelta(years=100),
    )
    end_datetime = DatetimeMother.create(
        start_datetime=datetime.now(tz=UTC) - relativedelta(years=100),
        end_datetime=datetime.now(tz=UTC),
    )

    with assert_raises(
        expected_exception=ValueError,
        match='DatetimeMother end_datetime must be older than start_datetime.',
    ):
        StringDatetimeMother.out_of_range(start_datetime=start_datetime, end_datetime=end_datetime)