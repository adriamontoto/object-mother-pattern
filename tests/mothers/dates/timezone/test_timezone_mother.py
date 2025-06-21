"""
Test module for the TimezoneMother class.
"""

from datetime import tzinfo
from zoneinfo import ZoneInfo, available_timezones

from pytest import mark, raises as assert_raises

from object_mother_pattern.mothers.dates import StringTimezoneMother, TimezoneMother


@mark.unit_testing
def test_timezone_mother_happy_path() -> None:
    """
    Test TimezoneMother happy path.
    """
    value = TimezoneMother.create()

    assert isinstance(value, tzinfo)
    assert str(value) in available_timezones()


@mark.unit_testing
def test_timezone_mother_value() -> None:
    """
    Test TimezoneMother create method with value.
    """
    value = ZoneInfo(StringTimezoneMother.create())

    assert TimezoneMother.create(value=value) == value


@mark.unit_testing
def test_timezone_mother_invalid_type() -> None:
    """
    Test TimezoneMother create method with invalid type.
    """
    assert not isinstance(TimezoneMother.invalid_type(), tzinfo)


@mark.unit_testing
def test_timezone_mother_invalid_value_type() -> None:
    """
    Test TimezoneMother create method with invalid value type.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='TimezoneMother value must be a tzinfo.',
    ):
        TimezoneMother.create(value=TimezoneMother.invalid_type())
