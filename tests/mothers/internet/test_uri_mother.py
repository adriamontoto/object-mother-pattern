"""
Test module for the UriMother class.
"""

from ipaddress import ip_address
from urllib.parse import urlsplit

from pytest import mark, raises as assert_raises
from value_object_pattern.usables.internet.uri import UrlValueObject

from object_mother_pattern.mothers.internet import UriMother


@mark.unit_testing
def test_uri_mother_create_method_happy_path() -> None:
    """
    Check that UriMother create method returns a valid URI.
    """
    value = UriMother.create()
    parts = urlsplit(url=value)

    assert type(value) is str
    assert UrlValueObject(value=value).scheme
    assert parts.path.count('/') == 2
    assert '&' in parts.query
    assert len(parts.fragment) >= 3


@mark.unit_testing
def test_uri_mother_create_method_value() -> None:
    """
    Check that UriMother create method returns the provided value.
    """
    value = UriMother.create()

    assert UriMother.create(value=value) == value


@mark.unit_testing
def test_uri_mother_create_method_invalid_value_type() -> None:
    """
    Check that UriMother create method raises a TypeError when the provided value is not a string.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='UriMother value must be a string.',
    ):
        UriMother.create(value=UriMother.invalid_type())


@mark.unit_testing
def test_uri_mother_create_method_with_domain_host_type() -> None:
    """
    Check that UriMother create method returns a URI with a domain host when host_type is domain.
    """
    value = UriMother.create(host_type='domain')
    host = urlsplit(url=value).netloc

    assert UrlValueObject(value=value).scheme
    assert '.' in host
    assert ':' not in host


@mark.unit_testing
def test_uri_mother_create_method_with_ip_host_type() -> None:
    """
    Check that UriMother create method returns a URI with an IP host when host_type is ip.
    """
    value = UriMother.create(host_type='ip')
    host = urlsplit(url=value).netloc

    assert UrlValueObject(value=value).scheme
    assert ip_address(address=host).version in (4, 6)


@mark.unit_testing
def test_uri_mother_create_method_with_ipv4_host_type() -> None:
    """
    Check that UriMother create method returns a URI with an IPv4 host when host_type is ipv4.
    """
    value = UriMother.create(host_type='ipv4')
    host = urlsplit(url=value).netloc

    assert UrlValueObject(value=value).scheme
    assert ip_address(address=host).version == 4


@mark.unit_testing
def test_uri_mother_create_method_with_ipv6_host_type() -> None:
    """
    Check that UriMother create method returns a URI with an IPv6 host when host_type is ipv6.
    """
    value = UriMother.create(host_type='ipv6')
    host = urlsplit(url=value).netloc

    assert UrlValueObject(value=value).scheme
    assert ip_address(address=host).version == 6


@mark.unit_testing
def test_uri_mother_create_method_invalid_host_type_type() -> None:
    """
    Check that UriMother create method raises a TypeError when host_type is not a string.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='UriMother host_type must be a string.',
    ):
        UriMother.create(host_type=UriMother.invalid_type())


@mark.unit_testing
def test_uri_mother_create_method_invalid_host_type_value() -> None:
    """
    Check that UriMother create method raises a ValueError when host_type is invalid.
    """
    with assert_raises(
        expected_exception=ValueError,
        match='UriMother host_type must be one of domain, ip, ipv4, or ipv6.',
    ):
        UriMother.create(host_type='hostname')


@mark.unit_testing
def test_uri_mother_with_scheme_method() -> None:
    """
    Check that UriMother with_scheme method returns a URI with the provided scheme.
    """
    value = UriMother.with_scheme(scheme='git+ssh')
    parts = urlsplit(url=value)

    assert parts.scheme == 'git+ssh'
    assert UrlValueObject(value=value).scheme == 'git+ssh'
    assert parts.query
    assert parts.fragment


@mark.unit_testing
def test_uri_mother_with_scheme_method_invalid_type() -> None:
    """
    Check that UriMother with_scheme method raises a TypeError when scheme is not a string.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='UriMother scheme must be a string.',
    ):
        UriMother.with_scheme(scheme=UriMother.invalid_type())


@mark.unit_testing
def test_uri_mother_with_scheme_method_invalid_value() -> None:
    """
    Check that UriMother with_scheme method raises a ValueError when scheme is invalid.
    """
    with assert_raises(
        expected_exception=ValueError,
        match='UriMother scheme must start with a letter',
    ):
        UriMother.with_scheme(scheme='1http')


@mark.unit_testing
def test_uri_mother_with_domain_method() -> None:
    """
    Check that UriMother with_domain method returns a URI with a domain host.
    """
    value = UriMother.with_domain()
    host = urlsplit(url=value).netloc

    assert UrlValueObject(value=value).scheme
    assert '.' in host
    assert ':' not in host


@mark.unit_testing
def test_uri_mother_with_ipv4_address_method() -> None:
    """
    Check that UriMother with_ipv4_address method returns a URI with an IPv4 host.
    """
    value = UriMother.with_ipv4_address()
    host = urlsplit(url=value).netloc

    assert UrlValueObject(value=value).scheme
    assert host.count('.') == 3
    assert ':' not in host


@mark.unit_testing
def test_uri_mother_with_ipv6_address_method() -> None:
    """
    Check that UriMother with_ipv6_address method returns a URI with an IPv6 host.
    """
    value = UriMother.with_ipv6_address()
    host = urlsplit(url=value).netloc

    assert UrlValueObject(value=value).scheme
    assert ':' in host


@mark.unit_testing
def test_uri_mother_with_query_method() -> None:
    """
    Check that UriMother with_query method returns a URI with a query string.
    """
    value = UriMother.with_query()
    url = UrlValueObject(value=value)

    assert url.query is not None
    assert '&' in url.query


@mark.unit_testing
def test_uri_mother_with_fragment_method() -> None:
    """
    Check that UriMother with_fragment method returns a URI with a fragment section.
    """
    value = UriMother.with_fragment()
    url = UrlValueObject(value=value)

    assert url.fragment is not None
    assert len(url.fragment) >= 3


@mark.unit_testing
def test_uri_mother_with_query_and_fragment_method() -> None:
    """
    Check that UriMother with_query_and_fragment method returns a URI with query and fragment parts.
    """
    value = UriMother.with_query_and_fragment()
    url = UrlValueObject(value=value)

    assert url.query is not None
    assert url.fragment is not None


@mark.unit_testing
def test_uri_mother_invalid_type_method() -> None:
    """
    Check that UriMother invalid_type method returns a non-string value.
    """
    assert type(UriMother.invalid_type()) is not str


@mark.unit_testing
def test_uri_mother_invalid_value_method() -> None:
    """
    Check that UriMother invalid_value method returns an invalid URI.
    """
    value = UriMother.invalid_value()

    assert type(value) is str
    assert not value.isprintable()
