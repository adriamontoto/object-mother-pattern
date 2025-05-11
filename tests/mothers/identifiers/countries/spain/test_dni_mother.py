"""
Test module for the DniMother class.
"""

from re import Pattern, compile as re_compile

from pytest import mark, raises as assert_raises

from object_mother_pattern.mothers import StringMother
from object_mother_pattern.mothers.identifiers.countries.spain import DniMother
from object_mother_pattern.mothers.identifiers.countries.spain.dni_mother import DniCase

_DNI_REGEX: Pattern[str] = re_compile(pattern=r'^(\d{8})([A-Za-z])$')


@mark.unit_testing
def test_dni_mother_happy_path() -> None:
    """
    Test DniMother happy path.
    """
    value = DniMother.create()

    assert _DNI_REGEX.match(string=value) is not None


@mark.unit_testing
def test_dni_mother_value() -> None:
    """
    Test DniMother create method with value.
    """
    value = DniMother.create()

    assert DniMother.create(value=value) == value


@mark.unit_testing
def test_dni_mother_invalid_value_type() -> None:
    """
    Test DniMother create method with invalid value type.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='DniMother value must be a string',
    ):
        DniMother.create(value=DniMother.invalid_type())


@mark.unit_testing
def test_dni_mother_lowercase_case() -> None:
    """
    Test DniMother create method with lowercase case.
    """
    value = DniMother.create(dni_case=DniCase.LOWERCASE)

    assert value.islower()


@mark.unit_testing
def test_dni_mother_uppercase_case() -> None:
    """
    Test DniMother create method with uppercase case.
    """
    value = DniMother.create(dni_case=DniCase.UPPERCASE)

    assert value.isupper()


@mark.unit_testing
def test_dni_mother_invalid_case() -> None:
    """
    Test DniMother create method with invalid case.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='DniMother dni_case must be a DniCase',
    ):
        DniMother.create(dni_case=StringMother.invalid_type())


@mark.unit_testing
def test_dni_mother_invalid_type() -> None:
    """
    Test DniMother create method with invalid type.
    """
    assert type(DniMother.invalid_type()) is not str


@mark.unit_testing
def test_dni_mother_invalid_value() -> None:
    """
    Test DniMother invalid_value method.
    """
    invalid_dni = DniMother.invalid_value()

    assert type(invalid_dni) is str
    assert not invalid_dni.isprintable()
