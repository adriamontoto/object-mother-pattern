"""
HostMother module.
"""

from sys import version_info

if version_info >= (3, 12):
    from typing import override  # pragma: no cover
else:
    from typing_extensions import override  # pragma: no cover


from random import choice

from object_mother_pattern.models import BaseMother
from object_mother_pattern.mothers import StringCase
from object_mother_pattern.mothers.primitives.string_mother import StringMother

from .domain_mother import DomainMother
from .ipv4_address_mother import Ipv4AddressMother
from .ipv6_address_mother import Ipv6AddressMother


class HostMother(BaseMother[str]):
    """
    HostMother class is responsible for creating random host values.

    Generated hosts match the host value object rules: a host can be a domain, an IPv4 address, or an IPv6
    address.

    Example:
    ```python
    from object_mother_pattern.mothers.internet import HostMother

    host = HostMother.create()
    print(host)
    # >>> 203.0.113.10
    ```
    """

    @classmethod
    @override
    def create(cls, *, value: str | None = None) -> str:
        """
        Create a random host value.

        If a specific host value is provided via `value`, it is returned after type validation. Otherwise, a random host
        is generated from one of the supported host families: domain, IPv4 address, or IPv6 address.

        Args:
            value (str | None, optional): Specific value to return. Defaults to None.

        Raises:
            TypeError: If the provided `value` is not a string.

        Returns:
            str: A randomly generated host value.

        Example:
        ```python
        from object_mother_pattern.mothers.internet import HostMother

        host = HostMother.create()
        print(host)
        # >>> api.example.com
        ```
        """
        if value is not None:
            if type(value) is not str:
                raise TypeError('HostMother value must be a string.')

            return value

        return choice(seq=(cls.domain, cls.ipv4_address, cls.ipv6_address))()  # noqa: S311

    @classmethod
    def domain(cls) -> str:
        """
        Create a random domain host value.

        Returns:
            str: A randomly generated domain.

        Example:
        ```python
        from object_mother_pattern.mothers.internet import HostMother

        host = HostMother.domain()
        print(host)
        # >>> web.service.io
        ```
        """
        return DomainMother.create(string_case=StringCase.LOWERCASE)

    @classmethod
    def ipv4_address(cls) -> str:
        """
        Create a random IPv4 address host value.

        Returns:
            str: A randomly generated IPv4 address.

        Example:
        ```python
        from object_mother_pattern.mothers.internet import HostMother

        host = HostMother.ipv4_address()
        print(host)
        # >>> 198.51.100.42
        ```
        """
        return Ipv4AddressMother.create()

    @classmethod
    def ipv6_address(cls) -> str:
        """
        Create a random IPv6 address host value.

        Returns:
            str: A randomly generated IPv6 address.

        Example:
        ```python
        from object_mother_pattern.mothers.internet import HostMother

        host = HostMother.ipv6_address()
        print(host)
        # >>> 2001:db8:85a3::8a2e:370:7334
        ```
        """
        return Ipv6AddressMother.create()

    @classmethod
    def invalid_value(cls) -> str:
        """
        Create an invalid host value.

        Returns:
            str: Invalid host string.
        """
        return StringMother.invalid_value()
