"""
Test module for the Ipv4NetworkMother class.
"""

from ipaddress import IPv4Network

from pytest import mark, raises as assert_raises

from object_mother_pattern.mothers.internet import Ipv4NetworkMother


@mark.unit_testing
def test_ipv4_network_mother_happy_path() -> None:
    """
    Test Ipv4NetworkMother happy path.
    """
    value = Ipv4NetworkMother.create()

    IPv4Network(address=value)


@mark.unit_testing
def test_ipv4_network_mother_value() -> None:
    """
    Test Ipv4NetworkMother create method with value.
    """
    value = Ipv4NetworkMother.create()

    assert Ipv4NetworkMother.create(value=value) == value


@mark.unit_testing
def test_ipv4_network_mother_invalid_value_type() -> None:
    """
    Test Ipv4NetworkMother create method with invalid value type.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='Ipv4NetworkMother value must be a string.',
    ):
        Ipv4NetworkMother.create(value=Ipv4NetworkMother.invalid_type())


@mark.unit_testing
def test_ipv4_network_mother_invalid_type() -> None:
    """
    Test Ipv4NetworkMother create method with invalid type.
    """
    assert type(Ipv4NetworkMother.invalid_type()) is not str


@mark.unit_testing
def test_ipv4_network_mother_invalid_value() -> None:
    """
    Test Ipv4NetworkMother invalid_value method.
    """
    value = Ipv4NetworkMother.invalid_value()

    assert type(value) is str
    assert not value.isprintable()
