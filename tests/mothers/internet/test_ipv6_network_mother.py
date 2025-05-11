"""
Test module for the Ipv6NetworkMother class.
"""

from ipaddress import IPv6Network

from pytest import mark, raises as assert_raises

from object_mother_pattern.mothers.internet import Ipv6NetworkMother


@mark.unit_testing
def test_ipv6_network_mother_happy_path() -> None:
    """
    Test Ipv6NetworkMother happy path.
    """
    value = Ipv6NetworkMother.create()

    IPv6Network(address=value)


@mark.unit_testing
def test_ipv6_network_mother_value() -> None:
    """
    Test Ipv6NetworkMother create method with value.
    """
    value = Ipv6NetworkMother.create()

    assert Ipv6NetworkMother.create(value=value) == value


@mark.unit_testing
def test_ipv6_network_mother_invalid_value_type() -> None:
    """
    Test Ipv6NetworkMother create method with invalid value type.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='Ipv6NetworkMother value must be a string.',
    ):
        Ipv6NetworkMother.create(value=Ipv6NetworkMother.invalid_type())


@mark.unit_testing
def test_ipv6_network_mother_invalid_type() -> None:
    """
    Test Ipv6NetworkMother create method with invalid type.
    """
    assert type(Ipv6NetworkMother.invalid_type()) is not str


@mark.unit_testing
def test_ipv6_network_mother_invalid_value() -> None:
    """
    Test Ipv6NetworkMother invalid_value method.
    """
    value = Ipv6NetworkMother.invalid_value()

    assert type(value) is str
    assert not value.isprintable()
