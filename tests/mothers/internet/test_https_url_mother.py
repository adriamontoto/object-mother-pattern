"""
Test module for the HttpsUrlMother class.
"""

from pytest import mark, raises as assert_raises
from value_object_pattern.usables.internet.uri import HttpsUrlValueObject

from object_mother_pattern.mothers.internet import HttpsUrlMother


@mark.unit_testing
def test_https_url_mother_create_method_happy_path() -> None:
    """
    Check that HttpsUrlMother create method returns a valid HTTPS URL.
    """
    value = HttpsUrlMother.create()

    assert type(value) is str
    assert HttpsUrlValueObject(value=value).scheme == 'https'


@mark.unit_testing
def test_https_url_mother_create_method_value() -> None:
    """
    Check that HttpsUrlMother create method returns the provided value.
    """
    value = HttpsUrlMother.create()

    assert HttpsUrlMother.create(value=value) == value


@mark.unit_testing
def test_https_url_mother_create_method_invalid_value_type() -> None:
    """
    Check that HttpsUrlMother create method raises a TypeError when the provided value is not a string.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='HttpsUrlMother value must be a string.',
    ):
        HttpsUrlMother.create(value=HttpsUrlMother.invalid_type())


@mark.unit_testing
def test_https_url_mother_create_method_with_ipv6_host_type() -> None:
    """
    Check that HttpsUrlMother create method returns a valid HTTPS URL with an IPv6 host.
    """
    value = HttpsUrlMother.create(host_type='ipv6')

    assert HttpsUrlValueObject(value=value).scheme == 'https'


@mark.unit_testing
def test_https_url_mother_invalid_type_method() -> None:
    """
    Check that HttpsUrlMother invalid_type method returns a non-string value.
    """
    assert type(HttpsUrlMother.invalid_type()) is not str


@mark.unit_testing
def test_https_url_mother_invalid_value_method() -> None:
    """
    Check that HttpsUrlMother invalid_value method returns an invalid HTTPS URL.
    """
    value = HttpsUrlMother.invalid_value()

    assert type(value) is str
    assert not value.isprintable()
