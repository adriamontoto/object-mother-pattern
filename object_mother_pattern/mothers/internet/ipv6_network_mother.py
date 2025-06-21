"""
Ipv6NetworkMother module.
"""

from sys import version_info

if version_info >= (3, 12):
    from typing import override  # pragma: no cover
else:
    from typing_extensions import override  # pragma: no cover

from object_mother_pattern.models import BaseMother
from object_mother_pattern.mothers.primitives.string_mother import StringMother


class Ipv6NetworkMother(BaseMother[str]):
    """
    Ipv6NetworkMother class is responsible for creating random IPv6 network values.

    Example:
    ```python
    from object_mother_pattern.mothers.internet import Ipv6NetworkMother

    network = Ipv6NetworkMother.create()
    print(network)
    # >>> bc70:4687:255a:44f6:b000::/68
    ```
    """

    @classmethod
    @override
    def create(cls, *, value: str | None = None) -> str:
        """
        Create a random IPv6 network value. If a specific IPv6 network value is provided via `value`, it is returned
        after validation. Otherwise, a random IPv6 network value is generated.

        Args:
            value (str | None, optional): Specific value to return. Defaults to None.

        Raises:
            TypeError: If the provided `value` is not a string.

        Returns:
            str: A randomly generated IPv6 network value.

        Example:
        ```python
        from object_mother_pattern.mothers.internet import Ipv6NetworkMother

        network = Ipv6NetworkMother.create()
        print(network)
        # >>> bc70:4687:255a:44f6:b000::/68
        ```
        """
        if value is not None:
            if type(value) is not str:
                raise TypeError('Ipv6NetworkMother value must be a string.')

            return value

        return cls._random().ipv6(network=True)

    @classmethod
    def invalid_value(cls) -> str:
        """
        Create an invalid IPv6 network value.

        Returns:
            str: Invalid IPv6 network string.
        """
        return StringMother.invalid_value()
