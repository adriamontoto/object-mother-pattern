"""
Test module for the StringTimezoneMother class.
"""

from zoneinfo import available_timezones

from pytest import mark, raises as assert_raises

from object_mother_pattern.mothers.dates import StringTimezoneMother


@mark.unit_testing
def test_string_timezone_mother_happy_path() -> None:
    """
    Test StringTimezoneMother happy path.
    """
    value = StringTimezoneMother.create()

    assert type(value) is str
    assert value in available_timezones()


@mark.unit_testing
def test_string_timezone_mother_value() -> None:
    """
    Test StringTimezoneMother create method with value.
    """
    value = StringTimezoneMother.create()

    assert StringTimezoneMother.create(value=value) == value


@mark.unit_testing
def test_string_timezone_mother_invalid_type() -> None:
    """
    Test StringTimezoneMother create method with invalid type.
    """
    assert type(StringTimezoneMother.invalid_type()) is not str


@mark.unit_testing
def test_string_timezone_mother_invalid_value_type() -> None:
    """
    Test StringTimezoneMother create method with invalid value type.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='StringTimezoneMother value must be a string.',
    ):
        StringTimezoneMother.create(value=StringTimezoneMother.invalid_type())
