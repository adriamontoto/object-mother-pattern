"""
Test module for the NieMother class.
"""

from re import Pattern, compile as re_compile

from pytest import mark, raises as assert_raises

from object_mother_pattern.mothers import StringCase, StringMother
from object_mother_pattern.mothers.identifiers.countries.spain import NieMother

_NIE_REGEX: Pattern[str] = re_compile(pattern=r'^([XYZxyz])(\d{7})([A-Za-z])$')


@mark.unit_testing
def test_nie_mother_happy_path() -> None:
    """
    Test NieMother happy path.
    """
    value = NieMother.create()

    assert _NIE_REGEX.match(string=value) is not None


@mark.unit_testing
def test_nie_mother_value() -> None:
    """
    Test NieMother create method with value.
    """
    value = NieMother.create()

    assert NieMother.create(value=value) == value


@mark.unit_testing
def test_nie_mother_invalid_value_type() -> None:
    """
    Test NieMother create method with invalid value type.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='NieMother value must be a string.',
    ):
        NieMother.create(value=NieMother.invalid_type())


@mark.unit_testing
def test_nie_mother_lowercase_case() -> None:
    """
    Test NieMother create method with lowercase case.
    """
    value = NieMother.create(string_case=StringCase.LOWERCASE)

    assert value.islower()


@mark.unit_testing
def test_nie_mother_uppercase_case() -> None:
    """
    Test NieMother create method with uppercase case.
    """
    value = NieMother.create(string_case=StringCase.UPPERCASE)

    assert value.isupper()


@mark.unit_testing
def test_nie_mother_mixed_case() -> None:
    """
    Test NieMother create method with mixed case.
    """
    value = NieMother.create(string_case=StringCase.MIXEDCASE)

    assert all(char.islower() or char.isupper() or char.isdigit() for char in value)


@mark.unit_testing
def test_nie_mother_invalid_case() -> None:
    """
    Test NieMother create method with invalid case.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='NieMother string_case must be a StringCase.',
    ):
        NieMother.create(string_case=StringMother.invalid_type())


@mark.unit_testing
def test_nie_mother_invalid_type() -> None:
    """
    Test NieMother create method with invalid type.
    """
    assert type(NieMother.invalid_type()) is not str


@mark.unit_testing
def test_nie_mother_invalid_value() -> None:
    """
    Test NieMother invalid_value method.
    """
    invalid_nie = NieMother.invalid_value()

    assert type(invalid_nie) is str
    assert not invalid_nie.isprintable()
