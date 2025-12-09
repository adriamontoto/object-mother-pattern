"""
Test module for the IpNetworkMother class.
"""

from ipaddress import ip_network

from pytest import mark, raises as assert_raises

from object_mother_pattern.mothers.internet import IpNetworkMother


@mark.unit_testing
def test_ip_network_mother_happy_path() -> None:
    """
    Test IpNetworkMother happy path.
    """
    value = IpNetworkMother.create()

    ip_network(address=value)


@mark.unit_testing
def test_ip_network_mother_value() -> None:
    """
    Test IpNetworkMother create method with value.
    """
    value = IpNetworkMother.create()

    assert IpNetworkMother.create(value=value) == value


@mark.unit_testing
def test_ip_network_mother_invalid_value_type() -> None:
    """
    Test IpNetworkMother create method with invalid value type.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='IpNetworkMother value must be a string.',
    ):
        IpNetworkMother.create(value=IpNetworkMother.invalid_type())


@mark.unit_testing
def test_ip_network_mother_invalid_type() -> None:
    """
    Test IpNetworkMother create method with invalid type.
    """
    assert type(IpNetworkMother.invalid_type()) is not str


@mark.unit_testing
def test_ip_network_mother_invalid_value() -> None:
    """
    Test IpNetworkMother invalid_value method.
    """
    value = IpNetworkMother.invalid_value()

    assert type(value) is str
    assert not value.isprintable()
