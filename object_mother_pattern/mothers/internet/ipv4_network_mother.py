"""
Ipv4NetworkMother module.
"""

from sys import version_info

if version_info >= (3, 12):
    from typing import override  # pragma: no cover
else:
    from typing_extensions import override  # pragma: no cover

from object_mother_pattern.models import BaseMother
from object_mother_pattern.mothers.primitives.string_mother import StringMother


class Ipv4NetworkMother(BaseMother[str]):
    """
    Ipv4NetworkMother class is responsible for creating random IPv4 network values.

    Example:
    ```python
    from object_mother_pattern.mothers.internet import Ipv4NetworkMother

    network = Ipv4NetworkMother.create()
    print(network)
    # >>> 139.104.0.0/13
    ```
    """

    @classmethod
    @override
    def create(cls, *, value: str | None = None) -> str:
        """
        Create a random IPv4 network value. If a specific IPv4 network value is provided via `value`, it is returned
        after validation. Otherwise, a random IPv4 network value is generated.

        Args:
            value (str | None, optional): Specific value to return. Defaults to None.

        Raises:
            TypeError: If the provided `value` is not a string.

        Returns:
            str: A randomly generated IPv4 network value.

        Example:
        ```python
        from object_mother_pattern.mothers.internet import Ipv4NetworkMother

        network = Ipv4NetworkMother.create()
        print(network)
        # >>> 139.104.0.0/13
        ```
        """
        if value is not None:
            if type(value) is not str:
                raise TypeError('Ipv4NetworkMother value must be a string.')

            return value

        return cls._random().ipv4(network=True)

    @classmethod
    def invalid_value(cls) -> str:
        """
        Create an invalid IPv4 network value.

        Returns:
            str: Invalid IPv4 network string.
        """
        return StringMother.invalid_value()
