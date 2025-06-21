"""
Ipv6AddressMother module.
"""

from sys import version_info

if version_info >= (3, 12):
    from typing import override  # pragma: no cover
else:
    from typing_extensions import override  # pragma: no cover

from object_mother_pattern.models import BaseMother
from object_mother_pattern.mothers.primitives.string_mother import StringMother


class Ipv6AddressMother(BaseMother[str]):
    """
    Ipv6AddressMother class is responsible for creating random IPv6 address values.

    Example:
    ```python
    from object_mother_pattern.mothers.internet import Ipv6AddressMother

    ip = Ipv6AddressMother.create()
    print(ip)
    # >>> 108.61.183.60
    ```
    """

    @classmethod
    @override
    def create(cls, *, value: str | None = None) -> str:
        """
        Create a random IPv6 address value. If a specific IPv6 address value is provided via `value`, it is returned
        after validation. Otherwise, a random IPv6 address value is generated.

        Args:
            value (str | None, optional): Specific value to return. Defaults to None.

        Raises:
            TypeError: If the provided `value` is not a string.

        Returns:
            str: A randomly generated IPv6 address value.

        Example:
        ```python
        from object_mother_pattern.mothers.internet import Ipv6AddressMother

        ip = Ipv6AddressMother.create()
        print(ip)
        # >>> c5d1:d2d4:2ce5:bc68:538b:a8fb:eff:3fe9
        ```
        """
        if value is not None:
            if type(value) is not str:
                raise TypeError('Ipv6AddressMother value must be a string.')

            return value

        return cls._random().ipv6()

    @classmethod
    def unspecified(cls) -> str:
        """
        Create a string IPv6 unspecified address value `::`.

        Returns:
            str: A IPv6 unspecified address string.

        Example:
        ```python
        from object_mother_pattern.mothers.internet import Ipv6AddressMother

        ip = Ipv6AddressMother.unspecified()
        print(ip)
        # >>> ::
        ```
        """
        return '::'

    @classmethod
    def loopback(cls) -> str:
        """
        Create a string IPv6 loopback address value `::1`.

        Returns:
            str: A IPv6 loopback address string.

        Example:
        ```python
        from object_mother_pattern.mothers.internet import Ipv6AddressMother

        ip = Ipv6AddressMother.loopback()
        print(ip)
        # >>> ::1
        ```
        """
        return '::1'

    @classmethod
    def invalid_value(cls) -> str:
        """
        Create an invalid IPv6 address value.

        Returns:
            str: Invalid IPv6 address string.
        """
        return StringMother.invalid_value()
