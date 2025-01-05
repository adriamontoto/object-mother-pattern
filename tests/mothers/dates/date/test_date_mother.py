"""
Test module for the DateMother class.
"""

from datetime import UTC, date, datetime

from dateutil.relativedelta import relativedelta
from pytest import raises as assert_raises

from object_mother_pattern.mothers import DateMother, IntegerMother


def test_date_mother_happy_path() -> None:
    """
    Test DateMother happy path.
    """
    value = DateMother.create()

    assert type(value) is date


def test_date_mother_value() -> None:
    """
    Test DateMother create method with value.
    """
    value = DateMother.create()

    assert DateMother.create(value=value) == value


def test_date_mother_invalid_type() -> None:
    """
    Test DateMother create method with invalid type.
    """
    assert type(DateMother.invalid_type()) is not date


def test_date_mother_invalid_value_type() -> None:
    """
    Test DateMother create method with invalid value type.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='DateMother value must be a date.',
    ):
        DateMother.create(value=DateMother.invalid_type())


def test_date_mother_invalid_start_date_type() -> None:
    """
    Test DateMother create method with invalid start_date type.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='DateMother start_date must be a date.',
    ):
        DateMother.create(start_date=DateMother.invalid_type())


def test_date_mother_invalid_end_date_type() -> None:
    """
    Test DateMother create method with invalid end_date type.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='DateMother end_date must be a date.',
    ):
        DateMother.create(end_date=DateMother.invalid_type())


def test_date_mother_start_date_greater_than_end_date() -> None:
    """
    Test DateMother create method with start_date greater than end_date.
    """
    start_date = DateMother.create(
        start_date=datetime.now(tz=UTC).date(),
        end_date=datetime.now(tz=UTC).date() + relativedelta(years=100),
    )
    end_date = DateMother.create(
        start_date=datetime.now(tz=UTC).date() - relativedelta(years=100),
        end_date=datetime.now(tz=UTC).date(),
    )

    with assert_raises(
        expected_exception=ValueError,
        match='DateMother end_date must be older than start_date.',
    ):
        DateMother.create(start_date=start_date, end_date=end_date)


def test_date_mother_out_of_range_method_happy_path() -> None:
    """
    Test DateMother happy path.
    """
    start_date = datetime.now(tz=UTC).date() - relativedelta(years=100)
    end_date = datetime.now(tz=UTC).date()

    value = DateMother.out_of_range(start_date=start_date, end_date=end_date)

    assert type(value) is date
    assert start_date >= value <= end_date or start_date <= value >= end_date


def test_date_mother_out_of_range_method_invalid_start_date_type() -> None:
    """
    Test DateMother create method with invalid start_date type.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='DateMother start_date must be a date.',
    ):
        DateMother.out_of_range(start_date=DateMother.invalid_type())


def test_date_mother_out_of_range_method_invalid_end_date_type() -> None:
    """
    Test DateMother create method with invalid end_date type.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='DateMother end_date must be a date.',
    ):
        DateMother.out_of_range(end_date=DateMother.invalid_type())


def test_date_mother_out_of_range_method_invalid_range_type() -> None:
    """
    Test DateMother create method with invalid range type.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='DateMother range must be an integer.',
    ):
        DateMother.out_of_range(range=IntegerMother.invalid_type())


def test_date_mother_out_of_range_method_invalid_range_value() -> None:
    """
    Test DateMother create method with invalid range value.
    """
    with assert_raises(
        expected_exception=ValueError,
        match='DateMother range must be a positive integer.',
    ):
        DateMother.out_of_range(range=IntegerMother.negative())


def test_date_mother_out_of_range_method_start_date_greater_than_end_date() -> None:
    """
    Test DateMother create method with start_date greater than end_date.
    """
    start_date = DateMother.create(
        start_date=datetime.now(tz=UTC).date(),
        end_date=datetime.now(tz=UTC).date() + relativedelta(years=100),
    )
    end_date = DateMother.create(
        start_date=datetime.now(tz=UTC).date() - relativedelta(years=100),
        end_date=datetime.now(tz=UTC).date(),
    )

    with assert_raises(
        expected_exception=ValueError,
        match='DateMother end_date must be older than start_date.',
    ):
        DateMother.out_of_range(start_date=start_date, end_date=end_date)
