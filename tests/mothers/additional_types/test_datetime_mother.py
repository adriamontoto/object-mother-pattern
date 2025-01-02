"""
Test module for the DatetimeMother class.
"""

from datetime import UTC, datetime

from dateutil.relativedelta import relativedelta
from pytest import raises as assert_raises

from object_mother_pattern.mothers import DatetimeMother, IntegerMother


def test_datetime_mother_happy_path() -> None:
    """
    Test DatetimeMother happy path.
    """
    value = DatetimeMother.create()

    assert type(value) is datetime


def test_datetime_mother_value() -> None:
    """
    Test DatetimeMother create method with value.
    """
    value = DatetimeMother.create()

    assert DatetimeMother.create(value=value) == value


def test_datetime_mother_invalid_type() -> None:
    """
    Test DatetimeMother create method with invalid type.
    """
    assert type(DatetimeMother.invalid_type()) is not datetime


def test_datetime_mother_invalid_value_type() -> None:
    """
    Test DatetimeMother create method with invalid value type.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='DatetimeMother value must be a date.',
    ):
        DatetimeMother.create(value=DatetimeMother.invalid_type())


def test_datetime_mother_invalid_start_datetime_type() -> None:
    """
    Test DatetimeMother create method with invalid start_datetime type.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='DatetimeMother start_datetime must be a date.',
    ):
        DatetimeMother.create(start_datetime=DatetimeMother.invalid_type())


def test_datetime_mother_invalid_end_datetime_type() -> None:
    """
    Test DatetimeMother create method with invalid end_datetime type.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='DatetimeMother end_datetime must be a date.',
    ):
        DatetimeMother.create(end_datetime=DatetimeMother.invalid_type())


def test_datetime_mother_start_datetime_greater_than_end_datetime() -> None:
    """
    Test DatetimeMother create method with start_datetime greater than end_datetime.
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
        DatetimeMother.create(start_datetime=start_datetime, end_datetime=end_datetime)


def test_datetime_mother_out_of_range_method_happy_path() -> None:
    """
    Test DatetimeMother happy path.
    """
    start_datetime = datetime.now(tz=UTC) - relativedelta(years=100)
    end_datetime = datetime.now(tz=UTC)

    value = DatetimeMother.out_of_range(start_datetime=start_datetime, end_datetime=end_datetime)

    assert type(value) is datetime
    assert start_datetime >= value <= end_datetime or start_datetime <= value >= end_datetime


def test_datetime_mother_out_of_range_method_invalid_start_datetime_type() -> None:
    """
    Test DatetimeMother create method with invalid start_datetime type.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='DatetimeMother start_datetime must be a date.',
    ):
        DatetimeMother.out_of_range(start_datetime=DatetimeMother.invalid_type())


def test_datetime_mother_out_of_range_method_invalid_end_datetime_type() -> None:
    """
    Test DatetimeMother create method with invalid end_datetime type.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='DatetimeMother end_datetime must be a date.',
    ):
        DatetimeMother.out_of_range(end_datetime=DatetimeMother.invalid_type())


def test_datetime_mother_out_of_range_method_invalid_range_type() -> None:
    """
    Test DatetimeMother create method with invalid range type.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='DatetimeMother range must be an integer.',
    ):
        DatetimeMother.out_of_range(range=IntegerMother.invalid_type())


def test_datetime_mother_out_of_range_method_invalid_range_value() -> None:
    """
    Test DatetimeMother create method with invalid range value.
    """
    with assert_raises(
        expected_exception=ValueError,
        match='DatetimeMother range must be a positive integer.',
    ):
        DatetimeMother.out_of_range(range=IntegerMother.negative())


def test_datetime_mother_out_of_range_method_start_datetime_greater_than_end_datetime() -> None:
    """
    Test DatetimeMother create method with start_datetime greater than end_datetime.
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
        DatetimeMother.out_of_range(start_datetime=start_datetime, end_datetime=end_datetime)
