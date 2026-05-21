"""
Test module for the HttpUrlMother class.
"""

from pytest import mark, raises as assert_raises
from value_object_pattern.usables.internet.uri import HttpUrlValueObject

from object_mother_pattern.mothers.internet import HttpUrlMother


@mark.unit_testing
def test_http_url_mother_create_method_happy_path() -> None:
    """
    Check that HttpUrlMother create method returns a valid HTTP URL.
    """
    value = HttpUrlMother.create()

    assert type(value) is str
    assert HttpUrlValueObject(value=value).scheme == 'http'


@mark.unit_testing
def test_http_url_mother_create_method_value() -> None:
    """
    Check that HttpUrlMother create method returns the provided value.
    """
    value = HttpUrlMother.create()

    assert HttpUrlMother.create(value=value) == value


@mark.unit_testing
def test_http_url_mother_create_method_invalid_value_type() -> None:
    """
    Check that HttpUrlMother create method raises a TypeError when the provided value is not a string.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='HttpUrlMother value must be a string.',
    ):
        HttpUrlMother.create(value=HttpUrlMother.invalid_type())


@mark.unit_testing
def test_http_url_mother_create_method_with_ipv4_host_type() -> None:
    """
    Check that HttpUrlMother create method returns a valid HTTP URL with an IPv4 host.
    """
    value = HttpUrlMother.create(host_type='ipv4')

    assert HttpUrlValueObject(value=value).scheme == 'http'


@mark.unit_testing
def test_http_url_mother_invalid_type_method() -> None:
    """
    Check that HttpUrlMother invalid_type method returns a non-string value.
    """
    assert type(HttpUrlMother.invalid_type()) is not str


@mark.unit_testing
def test_http_url_mother_invalid_value_method() -> None:
    """
    Check that HttpUrlMother invalid_value method returns an invalid HTTP URL.
    """
    value = HttpUrlMother.invalid_value()

    assert type(value) is str
    assert not value.isprintable()
