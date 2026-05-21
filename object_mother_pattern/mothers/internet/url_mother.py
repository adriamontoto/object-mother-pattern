"""
UrlMother module.
"""

from sys import version_info

if version_info >= (3, 12):
    from typing import override  # pragma: no cover
else:
    from typing_extensions import override  # pragma: no cover


from random import choice
from re import Pattern, compile as re_compile
from typing import Final

from object_mother_pattern.models import BaseMother
from object_mother_pattern.mothers import StringMother

from .host_mother import HostMother
from .ipv4_address_mother import Ipv4AddressMother
from .ipv6_address_mother import Ipv6AddressMother
from .key_mother import KeyMother
from .slug_mother import SlugMother


class UrlMother(BaseMother[str]):
    """
    UrlMother class is responsible for creating random URL values.

    Generated URLs include a scheme, a host, two slug path sections, two query parameters, and a fragment section.

    Example:
    ```python
    from object_mother_pattern.mothers.internet import UrlMother

    url = UrlMother.create()
    print(url)
    # >>> https://example.com/catalog/item
    ```
    """

    _SCHEME_REGEX: Final[Pattern[str]] = re_compile(pattern=r'^[a-zA-Z][a-zA-Z0-9+\-.]+$')
    _SCHEMES: Final[tuple[str, ...]] = ('http', 'https', 'ftp', 'sftp', 'git+ssh', 'webdav', 's3')

    @classmethod
    @override
    def create(cls, *, value: str | None = None, host_type: str | None = None) -> str:
        """
        Create a random URL value.

        If a specific URL value is provided via `value`, it is returned after type validation. Otherwise, a complete
        random URL is generated with a random valid scheme, selected host type, slug path, query, and fragment.

        Args:
            value (str | None, optional): Specific value to return. Defaults to None.
            host_type (str | None, optional): Host type to use. Accepted values are `domain`, `ip`, `ipv4`, and `ipv6`.
                Defaults to None.

        Raises:
            TypeError: If the provided `value` is not a string.
            TypeError: If `host_type` is not a string.
            ValueError: If `host_type` is not one of `domain`, `ip`, `ipv4`, or `ipv6`.

        Returns:
            str: A randomly generated URL value.

        Example:
        ```python
        from object_mother_pattern.mothers.internet import UrlMother

        url = UrlMother.create()
        print(url)
        # >>> ftp://files.example.net/releases/latest
        ```
        """
        if value is not None:
            if type(value) is not str:
                raise TypeError('UrlMother value must be a string.')

            return value

        return cls.with_scheme(scheme=choice(seq=cls._SCHEMES), host_type=host_type)  # noqa: S311

    @classmethod
    def with_scheme(cls, *, scheme: str, host_type: str | None = None) -> str:
        """
        Create a random URL value with a specific scheme.

        Args:
            scheme (str): Scheme to use in the generated URL.
            host_type (str | None, optional): Host type to use. Accepted values are `domain`, `ip`, `ipv4`, and `ipv6`.
                Defaults to None.

        Raises:
            TypeError: If `scheme` is not a string.
            ValueError: If `scheme` is not a valid URL scheme.
            TypeError: If `host_type` is not a string.
            ValueError: If `host_type` is not one of `domain`, `ip`, `ipv4`, or `ipv6`.

        Returns:
            str: A randomly generated URL value with the provided scheme.

        Example:
        ```python
        from object_mother_pattern.mothers.internet import UrlMother

        url = UrlMother.with_scheme(scheme='s3')
        print(url)
        # >>> s3://bucket.example/files/index?version=v1&format=json#metadata
        ```
        """
        if type(scheme) is not str:
            raise TypeError('UrlMother scheme must be a string.')

        if cls._SCHEME_REGEX.fullmatch(string=scheme) is None:
            raise ValueError('UrlMother scheme must start with a letter and contain only letters, digits, +, -, or .')

        if host_type is not None and type(host_type) is not str:
            raise TypeError('UrlMother host_type must be a string.')

        if host_type is None:
            host = choice(  # noqa: S311
                seq=(
                    HostMother.domain(),
                    Ipv4AddressMother.create(),
                    Ipv6AddressMother.create(),
                ),
            )

        elif host_type == 'domain':
            host = HostMother.domain()

        elif host_type == 'ip':
            host = choice(seq=(Ipv4AddressMother.create(), Ipv6AddressMother.create()))  # noqa: S311

        elif host_type == 'ipv4':
            host = Ipv4AddressMother.create()

        elif host_type == 'ipv6':
            host = Ipv6AddressMother.create()

        else:
            raise ValueError('UrlMother host_type must be one of domain, ip, ipv4, or ipv6.')

        return (
            f'{scheme}://{host}'
            f'/{SlugMother.create(min_length=3, max_length=12)}/{SlugMother.create(min_length=3, max_length=12)}'
            f'?{KeyMother.create(min_length=3, max_length=12)}={SlugMother.create(min_length=3, max_length=12)}'
            f'&{KeyMother.create(min_length=3, max_length=12)}={SlugMother.create(min_length=3, max_length=12)}'
            f'#{SlugMother.create(min_length=3, max_length=20)}'
        )

    @classmethod
    def with_domain(cls) -> str:
        """
        Create a random URL value with a domain host.

        Returns:
            str: A randomly generated complete URL value with a domain host.

        Example:
        ```python
        from object_mother_pattern.mothers.internet import UrlMother

        url = UrlMother.with_domain()
        print(url)
        # >>> https://api.example.com/users/list?page=one&sort=latest#results
        ```
        """
        return cls.create(host_type='domain')

    @classmethod
    def with_ipv4_address(cls) -> str:
        """
        Create a random URL value with an IPv4 address host.

        Returns:
            str: A randomly generated complete URL value with an IPv4 address host.

        Example:
        ```python
        from object_mother_pattern.mothers.internet import UrlMother

        url = UrlMother.with_ipv4_address()
        print(url)
        # >>> http://192.0.2.20/api/v1?version=v1&format=json#status
        ```
        """
        return cls.create(host_type='ipv4')

    @classmethod
    def with_ipv6_address(cls) -> str:
        """
        Create a random URL value with an IPv6 address host.

        Returns:
            str: A randomly generated complete URL value with an IPv6 address host.

        Example:
        ```python
        from object_mother_pattern.mothers.internet import UrlMother

        url = UrlMother.with_ipv6_address()
        print(url)
        # >>> https://2001:db8::1/api/v1?version=v1&format=json#status
        ```
        """
        return cls.create(host_type='ipv6')

    @classmethod
    def with_query(cls) -> str:
        """
        Create a random URL value with a query string.

        Returns:
            str: A randomly generated URL value with a query string.

        Example:
        ```python
        from object_mother_pattern.mothers.internet import UrlMother

        url = UrlMother.with_query()
        print(url)
        # >>> https://example.com/search/items?page=one&sort=latest#results
        ```
        """
        return cls.create()

    @classmethod
    def with_fragment(cls) -> str:
        """
        Create a random URL value with a fragment section.

        Returns:
            str: A randomly generated URL value with a fragment.

        Example:
        ```python
        from object_mother_pattern.mothers.internet import UrlMother

        url = UrlMother.with_fragment()
        print(url)
        # >>> https://example.com/docs/intro?topic=start#overview
        ```
        """
        return cls.create()

    @classmethod
    def with_query_and_fragment(cls) -> str:
        """
        Create a random URL value with a query string and fragment section.

        Returns:
            str: A randomly generated URL value with a query string and fragment.

        Example:
        ```python
        from object_mother_pattern.mothers.internet import UrlMother

        url = UrlMother.with_query_and_fragment()
        print(url)
        # >>> https://example.com/docs/api?version=v1#methods
        ```
        """
        return cls.create()

    @classmethod
    def invalid_value(cls) -> str:
        """
        Create an invalid URL value.

        Returns:
            str: Invalid URL string.
        """
        return StringMother.invalid_value()
