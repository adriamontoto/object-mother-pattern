"""
Test module for the HttpHttpsUrlMother class.
"""

from pytest import mark, raises as assert_raises
from value_object_pattern.usables.internet.uri import HttpHttpsUrlValueObject

from object_mother_pattern.mothers.internet import HttpHttpsUrlMother


@mark.unit_testing
def test_http_https_url_mother_create_method_happy_path() -> None:
    """
    Check that HttpHttpsUrlMother create method returns a valid HTTP or HTTPS URL.
    """
    value = HttpHttpsUrlMother.create()

    assert type(value) is str
    assert HttpHttpsUrlValueObject(value=value).scheme in ('http', 'https')


@mark.unit_testing
def test_http_https_url_mother_create_method_value() -> None:
    """
    Check that HttpHttpsUrlMother create method returns the provided value.
    """
    value = HttpHttpsUrlMother.create()

    assert HttpHttpsUrlMother.create(value=value) == value


@mark.unit_testing
def test_http_https_url_mother_create_method_invalid_value_type() -> None:
    """
    Check that HttpHttpsUrlMother create method raises a TypeError when the provided value is not a string.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='HttpHttpsUrlMother value must be a string.',
    ):
        HttpHttpsUrlMother.create(value=HttpHttpsUrlMother.invalid_type())


@mark.unit_testing
def test_http_https_url_mother_create_method_with_domain_host_type() -> None:
    """
    Check that HttpHttpsUrlMother create method returns a valid HTTP or HTTPS URL with a domain host.
    """
    value = HttpHttpsUrlMother.create(host_type='domain')

    assert HttpHttpsUrlValueObject(value=value).scheme in ('http', 'https')


@mark.unit_testing
def test_http_https_url_mother_invalid_type_method() -> None:
    """
    Check that HttpHttpsUrlMother invalid_type method returns a non-string value.
    """
    assert type(HttpHttpsUrlMother.invalid_type()) is not str


@mark.unit_testing
def test_http_https_url_mother_invalid_value_method() -> None:
    """
    Check that HttpHttpsUrlMother invalid_value method returns an invalid HTTP or HTTPS URL.
    """
    value = HttpHttpsUrlMother.invalid_value()

    assert type(value) is str
    assert not value.isprintable()
