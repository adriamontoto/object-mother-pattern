"""
Test module for the Ipv4AddressMother class.
"""

from ipaddress import IPv4Address

from pytest import mark, raises as assert_raises

from object_mother_pattern.mothers.internet import Ipv4AddressMother


@mark.unit_testing
def test_ipv4_address_mother_happy_path() -> None:
    """
    Test Ipv4AddressMother happy path.
    """
    value = Ipv4AddressMother.create()

    IPv4Address(address=value)


@mark.unit_testing
def test_ipv4_address_mother_value() -> None:
    """
    Test Ipv4AddressMother create method with value.
    """
    value = Ipv4AddressMother.create()

    assert Ipv4AddressMother.create(value=value) == value


@mark.unit_testing
def test_ipv4_address_mother_invalid_value_type() -> None:
    """
    Test Ipv4AddressMother create method with invalid value type.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='Ipv4AddressMother value must be a string.',
    ):
        Ipv4AddressMother.create(value=Ipv4AddressMother.invalid_type())


@mark.unit_testing
def test_ipv4_address_mother_invalid_type() -> None:
    """
    Test Ipv4AddressMother create method with invalid type.
    """
    assert type(Ipv4AddressMother.invalid_type()) is not str


@mark.unit_testing
def test_ipv4_address_mother_invalid_value() -> None:
    """
    Test Ipv4AddressMother invalid_value method.
    """
    value = Ipv4AddressMother.invalid_value()

    assert type(value) is str
    assert not value.isprintable()


@mark.unit_testing
def test_ipv4_address_mother_public() -> None:
    """
    Test Ipv4AddressMother public method.
    """
    value = Ipv4AddressMother.public()

    ip = IPv4Address(address=value)
    assert not ip.is_loopback
    assert not ip.is_multicast
    assert not ip.is_unspecified
    assert not ip.is_private


@mark.unit_testing
def test_ipv4_address_mother_private() -> None:
    """
    Test Ipv4AddressMother private method.
    """
    value = Ipv4AddressMother.private()

    assert IPv4Address(address=value).is_private


@mark.unit_testing
def test_ipv4_address_mother_unspecified() -> None:
    """
    Test Ipv4AddressMother unspecified method.
    """
    value = Ipv4AddressMother.unspecified()

    assert value == '0.0.0.0'  # noqa: S104


@mark.unit_testing
def test_ipv4_address_mother_loopback() -> None:
    """
    Test Ipv4AddressMother loopback method.
    """
    value = Ipv4AddressMother.loopback()

    assert value == '127.0.0.1'


@mark.unit_testing
def test_ipv4_address_mother_broadcast() -> None:
    """
    Test Ipv4AddressMother broadcast method.
    """
    value = Ipv4AddressMother.broadcast()

    assert value == '255.255.255.255'
