"""
IpNetworkMother module.
"""

from sys import version_info

if version_info >= (3, 12):
    from typing import override  # pragma: no cover
else:
    from typing_extensions import override  # pragma: no cover

from object_mother_pattern.models import BaseMother
from object_mother_pattern.mothers.internet.ipv4_network_mother import Ipv4NetworkMother
from object_mother_pattern.mothers.internet.ipv6_network_mother import Ipv6NetworkMother
from object_mother_pattern.mothers.primitives.boolean_mother import BooleanMother
from object_mother_pattern.mothers.primitives.string_mother import StringMother


class IpNetworkMother(BaseMother[str]):
    """
    IpNetworkMother class is responsible for creating random IP network values, balancing between IPv4 and IPv6
    networks.

    Example:
    ```python
    from object_mother_pattern.mothers.internet import IpNetworkMother

    network = IpNetworkMother.create()
    print(network)
    # >>> 139.104.0.0/13
    ```
    """

    @classmethod
    @override
    def create(cls, *, value: str | None = None) -> str:
        """
        Create a random IP network value (IPv4 or IPv6). If a specific IP network value is provided via `value`, it is
        returned after validation. Otherwise, a random IP network value is generated.

        Args:
            value (str | None, optional): Specific value to return. Defaults to None.

        Raises:
            TypeError: If the provided `value` is not a string.

        Returns:
            str: A randomly generated IP network value.

        Example:
        ```python
        from object_mother_pattern.mothers.internet import IpNetworkMother

        network = IpNetworkMother.create()
        print(network)
        # >>> 139.104.0.0/13
        ```
        """
        if value is not None:
            if type(value) is not str:
                raise TypeError('IpNetworkMother value must be a string.')

            return value

        if BooleanMother.create():
            return Ipv4NetworkMother.create()  # pragma: no cover

        return Ipv6NetworkMother.create()  # pragma: no cover

    @classmethod
    def invalid_value(cls) -> str:
        """
        Create an invalid IP network value.

        Returns:
            str: Invalid IP network string.
        """
        return StringMother.invalid_value()
