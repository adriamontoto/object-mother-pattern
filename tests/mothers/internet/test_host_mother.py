"""
Test module for the HostMother class.
"""

from ipaddress import ip_address

from pytest import mark, raises as assert_raises
from value_object_pattern.usables.internet import HostValueObject

from object_mother_pattern.mothers.internet import HostMother


@mark.unit_testing
def test_host_mother_create_method_happy_path() -> None:
    """
    Check that HostMother create method returns a valid host.
    """
    value = HostMother.create()

    assert type(value) is str
    assert HostValueObject(value=value).value


@mark.unit_testing
def test_host_mother_create_method_value() -> None:
    """
    Check that HostMother create method returns the provided value.
    """
    value = HostMother.create()

    assert HostMother.create(value=value) == value


@mark.unit_testing
def test_host_mother_create_method_invalid_value_type() -> None:
    """
    Check that HostMother create method raises a TypeError when the provided value is not a string.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='HostMother value must be a string.',
    ):
        HostMother.create(value=HostMother.invalid_type())


@mark.unit_testing
def test_host_mother_hostname_method() -> None:
    """
    Check that HostMother hostname method returns a valid hostname host.
    """
    value = HostMother.hostname()

    assert type(value) is str
    assert HostValueObject(value=value).value == value.lower()


@mark.unit_testing
def test_host_mother_ipv4_address_method() -> None:
    """
    Check that HostMother ipv4_address method returns a valid IPv4 host.
    """
    value = HostMother.ipv4_address()

    assert type(value) is str
    assert ip_address(address=value).version == 4
    assert HostValueObject(value=value).value == value


@mark.unit_testing
def test_host_mother_ipv6_address_method() -> None:
    """
    Check that HostMother ipv6_address method returns a valid IPv6 host.
    """
    value = HostMother.ipv6_address()

    assert type(value) is str
    assert ip_address(address=value).version == 6
    assert HostValueObject(value=value).value


@mark.unit_testing
def test_host_mother_invalid_type_method() -> None:
    """
    Check that HostMother invalid_type method returns a non-string value.
    """
    assert type(HostMother.invalid_type()) is not str


@mark.unit_testing
def test_host_mother_invalid_value_method() -> None:
    """
    Check that HostMother invalid_value method returns an invalid host.
    """
    value = HostMother.invalid_value()

    assert type(value) is str
    assert not value.isprintable()
