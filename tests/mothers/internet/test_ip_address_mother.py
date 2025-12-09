"""
Test module for the IpAddressMother class.
"""

from ipaddress import ip_address

from pytest import mark, raises as assert_raises

from object_mother_pattern.mothers.internet import IpAddressMother


@mark.unit_testing
def test_ip_address_mother_happy_path() -> None:
    """
    Test IpAddressMother happy path.
    """
    value = IpAddressMother.create()

    ip_address(address=value)


@mark.unit_testing
def test_ip_address_mother_value() -> None:
    """
    Test IpAddressMother create method with value.
    """
    value = IpAddressMother.create()

    assert IpAddressMother.create(value=value) == value


@mark.unit_testing
def test_ip_address_mother_invalid_value_type() -> None:
    """
    Test IpAddressMother create method with invalid value type.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='IpAddressMother value must be a string.',
    ):
        IpAddressMother.create(value=IpAddressMother.invalid_type())


@mark.unit_testing
def test_ip_address_mother_invalid_type() -> None:
    """
    Test IpAddressMother create method with invalid type.
    """
    assert type(IpAddressMother.invalid_type()) is not str


@mark.unit_testing
def test_ip_address_mother_invalid_value() -> None:
    """
    Test IpAddressMother invalid_value method.
    """
    value = IpAddressMother.invalid_value()

    assert type(value) is str
    assert not value.isprintable()
