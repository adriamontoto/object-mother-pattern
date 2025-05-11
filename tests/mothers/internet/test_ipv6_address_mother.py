"""
Test module for the Ipv6AddressMother class.
"""

from ipaddress import IPv6Address

from pytest import mark, raises as assert_raises

from object_mother_pattern.mothers.internet import Ipv6AddressMother


@mark.unit_testing
def test_ipv6_address_mother_happy_path() -> None:
    """
    Test Ipv6AddressMother happy path.
    """
    value = Ipv6AddressMother.create()

    IPv6Address(address=value)


@mark.unit_testing
def test_ipv6_address_mother_value() -> None:
    """
    Test Ipv6AddressMother create method with value.
    """
    value = Ipv6AddressMother.create()

    assert Ipv6AddressMother.create(value=value) == value


@mark.unit_testing
def test_ipv6_address_mother_invalid_value_type() -> None:
    """
    Test Ipv6AddressMother create method with invalid value type.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='Ipv6AddressMother value must be a string.',
    ):
        Ipv6AddressMother.create(value=Ipv6AddressMother.invalid_type())


@mark.unit_testing
def test_ipv6_address_mother_invalid_type() -> None:
    """
    Test Ipv6AddressMother create method with invalid type.
    """
    assert type(Ipv6AddressMother.invalid_type()) is not str


@mark.unit_testing
def test_ipv6_address_mother_invalid_value() -> None:
    """
    Test Ipv6AddressMother invalid_value method.
    """
    value = Ipv6AddressMother.invalid_value()

    assert type(value) is str
    assert not value.isprintable()


@mark.unit_testing
def test_ipv6_address_mother_unspecified() -> None:
    """
    Test Ipv6AddressMother unspecified method.
    """
    value = Ipv6AddressMother.unspecified()

    assert value == '::'


@mark.unit_testing
def test_ipv6_address_mother_loopback() -> None:
    """
    Test Ipv6AddressMother loopback method.
    """
    value = Ipv6AddressMother.loopback()

    assert value == '::1'
