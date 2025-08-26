"""
IpAddressMother module.
"""

from sys import version_info

if version_info >= (3, 12):
    from typing import override  # pragma: no cover
else:
    from typing_extensions import override  # pragma: no cover

from object_mother_pattern.models import BaseMother
from object_mother_pattern.mothers.internet.ipv4_address_mother import Ipv4AddressMother
from object_mother_pattern.mothers.internet.ipv6_address_mother import Ipv6AddressMother
from object_mother_pattern.mothers.primitives.boolean_mother import BooleanMother
from object_mother_pattern.mothers.primitives.string_mother import StringMother


class IpAddressMother(BaseMother[str]):
    """
    IpAddressMother class is responsible for creating random IP address values, balancing between IPv4 and IPv6
    addresses.

    Example:
    ```python
    from object_mother_pattern.mothers.internet import IpAddressMother

    ip = IpAddressMother.create()
    print(ip)
    # >>> f1e2:8560:2a7d:dca2:9fbd:c6d9:7660:32d0
    ```
    """

    @classmethod
    @override
    def create(cls, *, value: str | None = None) -> str:
        """
        Create a random IP address value (IPv4 or IPv6). If a specific IP address value is provided via `value`, it is
        returned after validation. Otherwise, a random IP address value is generated.

        Args:
            value (str | None, optional): Specific value to return. Defaults to None.

        Raises:
            TypeError: If the provided `value` is not a string.

        Returns:
            str: A randomly generated IP address value.

        Example:
        ```python
        from object_mother_pattern.mothers.internet import IpAddressMother

        ip = IpAddressMother.create()
        print(ip)
        # >>> f1e2:8560:2a7d:dca2:9fbd:c6d9:7660:32d0
        ```
        """
        if value is not None:
            if type(value) is not str:
                raise TypeError('IpAddressMother value must be a string.')

            return value

        if BooleanMother.create():
            return Ipv4AddressMother.create()

        return Ipv6AddressMother.create()

    @classmethod
    def invalid_value(cls) -> str:
        """
        Create an invalid IP address value.

        Returns:
            str: Invalid IP address string.
        """
        return StringMother.invalid_value()
