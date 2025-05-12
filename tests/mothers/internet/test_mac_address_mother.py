"""
Test module for the MacAddressMother class.
"""

from pytest import mark, raises as assert_raises

from object_mother_pattern.mothers import StringMother
from object_mother_pattern.mothers.internet import MacAddressMother
from object_mother_pattern.mothers.internet.mac_address_mother import MacAddressCase, MacAddressFormat


@mark.unit_testing
def test_mac_address_mother_happy_path() -> None:
    """
    Test MacAddressMother happy path.
    """
    value = MacAddressMother.create()

    assert type(value) is str
    assert len(value) == 12 or len(value) == 14 or len(value) == 17


@mark.unit_testing
def test_mac_address_mother_value() -> None:
    """
    Test MacAddressMother create method with value.
    """
    value = MacAddressMother.create()

    assert MacAddressMother.create(value=value) == value


@mark.unit_testing
def test_mac_address_mother_invalid_value_type() -> None:
    """
    Test MacAddressMother create method with invalid value type.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='MacAddressMother value must be a string.',
    ):
        MacAddressMother.create(value=MacAddressMother.invalid_type())


@mark.unit_testing
def test_mac_address_mother_lowercase_case() -> None:
    """
    Test MacAddressMother create method with lowercase case.
    """
    value = MacAddressMother.create(mac_case=MacAddressCase.LOWERCASE)

    assert value.islower() or value == '00:00:00:00:00:00'


@mark.unit_testing
def test_mac_address_mother_uppercase_case() -> None:
    """
    Test MacAddressMother create method with uppercase case.
    """
    value = MacAddressMother.create(mac_case=MacAddressCase.UPPERCASE)

    assert value.isupper() or value == '00:00:00:00:00:00'


@mark.unit_testing
def test_mac_address_mother_mixed_case() -> None:
    """
    Test MacAddressMother create method with mixed case.
    """
    value = MacAddressMother.create(mac_case=MacAddressCase.MIXED)

    assert any(char.islower() or char.isupper() for char in value) or value == '00:00:00:00:00:00'


@mark.unit_testing
def test_mac_address_mother_invalid_case() -> None:
    """
    Test MacAddressMother create method with invalid case.
    """
    with assert_raises(
        expected_exception=ValueError,
        match='MacAddressMother mac_case must be a MacAddressCase.',
    ):
        MacAddressMother.create(mac_case=StringMother.invalid_type())


@mark.unit_testing
def test_mac_address_mother_raw_format() -> None:
    """
    Test MacAddressMother create method with raw format.
    """
    value = MacAddressMother.create(mac_format=MacAddressFormat.RAW)

    assert len(value) == 12
    assert all(char.isalnum() for char in value)
    assert all(separator not in value for separator in (':', '-', ' ', '.', ' '))


@mark.unit_testing
def test_mac_address_mother_universal_format() -> None:
    """
    Test MacAddressMother create method with universal format.
    """
    value = MacAddressMother.create(mac_format=MacAddressFormat.UNIVERSAL)

    assert len(value) == 17
    assert value.count(':') == 5
    assert all(char.isalnum() or char == ':' for char in value)


@mark.unit_testing
def test_mac_address_mother_windows_format() -> None:
    """
    Test MacAddressMother create method with windows format.
    """
    value = MacAddressMother.create(mac_format=MacAddressFormat.WINDOWS)

    assert len(value) == 17
    assert value.count('-') == 5
    assert all(char.isalnum() or char == '-' for char in value)


@mark.unit_testing
def test_mac_address_mother_cisco_format() -> None:
    """
    Test MacAddressMother create method with cisco format.
    """
    value = MacAddressMother.create(mac_format=MacAddressFormat.CISCO)

    assert value.count('.') == 2
    assert all(char.isalnum() or char == '.' for char in value)


@mark.unit_testing
def test_mac_address_mother_space_format() -> None:
    """
    Test MacAddressMother create method with space format.
    """
    value = MacAddressMother.create(mac_format=MacAddressFormat.SPACE)

    assert len(value) == 17
    assert value.count(' ') == 5
    assert all(char.isalnum() or char == ' ' for char in value)


@mark.unit_testing
def test_mac_address_mother_null_format() -> None:
    """
    Test MacAddressMother create method with null format.
    """
    value = MacAddressMother.create(mac_format=MacAddressFormat.NULL)

    assert value == '00:00:00:00:00:00'


@mark.unit_testing
def test_mac_address_mother_broadcast_format() -> None:
    """
    Test MacAddressMother create method with broadcast format.
    """
    value = MacAddressMother.create(mac_format=MacAddressFormat.BROADCAST)

    assert value.upper() == 'FF:FF:FF:FF:FF:FF'


@mark.unit_testing
def test_mac_address_mother_invalid_format() -> None:
    """
    Test MacAddressMother create method with invalid format.
    """
    with assert_raises(
        expected_exception=ValueError,
        match='MacAddressMother mac_format must be a MacAddressFormat.',
    ):
        MacAddressMother.create(mac_format=StringMother.invalid_type())


@mark.unit_testing
def test_mac_address_mother_lowercase_method() -> None:
    """
    Test MacAddressMother lowercase method.
    """
    value = MacAddressMother.lowercase()

    assert type(value) is str
    assert value.islower() or value == '00:00:00:00:00:00'


@mark.unit_testing
def test_mac_address_mother_uppercase_method() -> None:
    """
    Test MacAddressMother uppercase method.
    """
    value = MacAddressMother.uppercase()

    assert type(value) is str
    assert value.isupper() or value == '00:00:00:00:00:00'


@mark.unit_testing
def test_mac_address_mother_mixed_method() -> None:
    """
    Test MacAddressMother mixed method.
    """
    value = MacAddressMother.mixed()

    assert type(value) is str
    assert any(char.islower() or char.isupper() for char in value) or value == '00:00:00:00:00:00'


@mark.unit_testing
def test_mac_address_mother_raw_format_method() -> None:
    """
    Test MacAddressMother raw_format method.
    """
    value = MacAddressMother.raw_format()

    assert type(value) is str
    assert len(value) == 12
    assert all(char.isalnum() for char in value)
    assert all(separator not in value for separator in (':', '-', ' ', '.', ' '))


@mark.unit_testing
def test_mac_address_mother_universal_format_method() -> None:
    """
    Test MacAddressMother universal_format method.
    """
    value = MacAddressMother.universal_format()

    assert type(value) is str
    assert len(value) == 17
    assert value.count(':') == 5
    assert all(char.isalnum() or char == ':' for char in value)


@mark.unit_testing
def test_mac_address_mother_windows_format_method() -> None:
    """
    Test MacAddressMother windows_format method.
    """
    value = MacAddressMother.windows_format()

    assert type(value) is str
    assert len(value) == 17
    assert value.count('-') == 5
    assert all(char.isalnum() or char == '-' for char in value)


@mark.unit_testing
def test_mac_address_mother_cisco_format_method() -> None:
    """
    Test MacAddressMother cisco_format method.
    """
    value = MacAddressMother.cisco_format()

    assert type(value) is str
    assert len(value) == 14
    assert value.count('.') == 2
    assert all(char.isalnum() or char == '.' for char in value)


@mark.unit_testing
def test_mac_address_mother_space_format_method() -> None:
    """
    Test MacAddressMother space_format method.
    """
    value = MacAddressMother.space_format()

    assert type(value) is str
    assert len(value) == 17
    assert value.count(' ') == 5
    assert all(char.isalnum() or char == ' ' for char in value)


@mark.unit_testing
def test_mac_address_mother_null_method() -> None:
    """
    Test MacAddressMother null method.
    """
    value = MacAddressMother.null()

    assert type(value) is str
    assert value == '00:00:00:00:00:00'


@mark.unit_testing
def test_mac_address_mother_broadcast_method() -> None:
    """
    Test MacAddressMother broadcast method.
    """
    value = MacAddressMother.broadcast()

    assert type(value) is str
    assert value == 'FF:FF:FF:FF:FF:FF'


@mark.unit_testing
def test_mac_address_mother_invalid_value_method() -> None:
    """
    Test MacAddressMother invalid_value method.
    """
    value = MacAddressMother.invalid_value()

    assert type(value) is str
    assert not value.isprintable()


@mark.unit_testing
def test_mac_address_mother_invalid_type_method() -> None:
    """
    Test MacAddressMother invalid_type method.
    """
    value = MacAddressMother.invalid_type()

    assert type(value) is not str
