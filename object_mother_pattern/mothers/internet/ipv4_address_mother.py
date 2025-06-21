"""
Ipv4AddressMother module.
"""

from sys import version_info

if version_info >= (3, 12):
    from typing import override  # pragma: no cover
else:
    from typing_extensions import override  # pragma: no cover

from object_mother_pattern.models import BaseMother
from object_mother_pattern.mothers.primitives.string_mother import StringMother


class Ipv4AddressMother(BaseMother[str]):
    """
    Ipv4AddressMother class is responsible for creating random IPv4 address values.

    Example:
    ```python
    from object_mother_pattern.mothers.internet import Ipv4AddressMother

    ip = Ipv4AddressMother.create()
    print(ip)
    # >>> 108.61.183.60
    ```
    """

    @classmethod
    @override
    def create(cls, *, value: str | None = None) -> str:
        """
        Create a random IPv4 address value. If a specific IPv4 address value is provided via `value`, it is returned
        after validation. Otherwise, a random IPv4 address value is generated.

        Args:
            value (str | None, optional): Specific value to return. Defaults to None.

        Raises:
            TypeError: If the provided `value` is not a string.

        Returns:
            str: A randomly generated IPv4 address value.

        Example:
        ```python
        from object_mother_pattern.mothers.internet import Ipv4AddressMother

        ip = Ipv4AddressMother.create()
        print(ip)
        # >>> 108.61.183.60
        ```
        """
        if value is not None:
            if type(value) is not str:
                raise TypeError('Ipv4AddressMother value must be a string.')

            return value

        return cls._random().ipv4()

    @classmethod
    def public(cls) -> str:
        """
        Create a random string IPv4 public address value.

        Returns:
            str: A randomly string IPv4 public address value.

        Example:
        ```python
        from object_mother_pattern.mothers.internet import Ipv4AddressMother

        ip = Ipv4AddressMother.public()
        print(ip)
        # >>> 67.137.90.113
        ```
        """
        return cls._random().ipv4_public()

    @classmethod
    def private(cls) -> str:
        """
        Create a random string IPv4 private address value (RFC 1918).

        Returns:
            str: A randomly string IPv4 private address value.

        References:
            RFC 1918: https://www.rfc-editor.org/rfc/rfc1918

        Example:
        ```python
        from object_mother_pattern.mothers.internet import Ipv4AddressMother

        ip = Ipv4AddressMother.private()
        print(ip)
        # >>> 192.168.73.117
        ```
        """
        return cls._random().ipv4_private()

    @classmethod
    def unspecified(cls) -> str:
        """
        Create a string IPv4 unspecified address value `0.0.0.0`.

        Returns:
            str: A IPv4 unspecified address string.

        Example:
        ```python
        from object_mother_pattern.mothers.internet import Ipv4AddressMother

        ip = Ipv4AddressMother.unspecified()
        print(ip)
        # >>> 0.0.0.0
        ```
        """
        return '0.0.0.0'  # noqa: S104

    @classmethod
    def loopback(cls) -> str:
        """
        Create a string IPv4 loopback address value `127.0.0.1`.

        Returns:
            str: A IPv4 loopback address string.

        Example:
        ```python
        from object_mother_pattern.mothers.internet import Ipv4AddressMother

        ip = Ipv4AddressMother.loopback()
        print(ip)
        # >>> 127.0.0.1
        ```
        """
        return '127.0.0.1'

    @classmethod
    def broadcast(cls) -> str:
        """
        Create a string IPv4 broadcast address value `255.255.255.255`.

        Returns:
            str: A IPv4 broadcast address string.

        Example:
        ```python
        from object_mother_pattern.mothers.internet import Ipv4AddressMother

        ip = Ipv4AddressMother.broadcast()
        print(ip)
        # >>> 255.255.255.255
        ```
        """
        return '255.255.255.255'

    @classmethod
    def invalid_value(cls) -> str:
        """
        Create an invalid IPv4 address value.

        Returns:
            str: Invalid IPv4 address string.
        """
        return StringMother.invalid_value()
