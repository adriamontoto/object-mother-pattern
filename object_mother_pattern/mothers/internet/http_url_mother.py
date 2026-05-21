"""
HttpUrlMother module.
"""

from sys import version_info

if version_info >= (3, 12):
    from typing import override  # pragma: no cover
else:
    from typing_extensions import override  # pragma: no cover


from object_mother_pattern.models import BaseMother
from object_mother_pattern.mothers.primitives.string_mother import StringMother

from .url_mother import UrlMother


class HttpUrlMother(BaseMother[str]):
    """
    HttpUrlMother class is responsible for creating random HTTP URL values.

    Example:
    ```python
    from object_mother_pattern.mothers.internet import HttpUrlMother

    url = HttpUrlMother.create()
    print(url)
    # >>> http://example.com/orders/list
    ```
    """

    @classmethod
    @override
    def create(cls, *, value: str | None = None, host_type: str | None = None) -> str:
        """
        Create a random HTTP URL value.

        If a specific HTTP URL value is provided via `value`, it is returned after type validation. Otherwise, a random
        URL with the `http` scheme is generated.

        Args:
            value (str | None, optional): Specific value to return. Defaults to None.
            host_type (str | None, optional): Host type to use. Accepted values are `domain`, `ip`, `ipv4`, and `ipv6`.
                Defaults to None.

        Raises:
            TypeError: If the provided `value` is not a string.
            TypeError: If `host_type` is not a string.
            ValueError: If `host_type` is not one of `domain`, `ip`, `ipv4`, or `ipv6`.

        Returns:
            str: A randomly generated HTTP URL value.

        Example:
        ```python
        from object_mother_pattern.mothers.internet import HttpUrlMother

        url = HttpUrlMother.create()
        print(url)
        # >>> http://api.example.dev/v1/orders
        ```
        """
        if value is not None:
            if type(value) is not str:
                raise TypeError('HttpUrlMother value must be a string.')

            return value

        return UrlMother.with_scheme(scheme='http', host_type=host_type)

    @classmethod
    def invalid_value(cls) -> str:
        """
        Create an invalid HTTP URL value.

        Returns:
            str: Invalid HTTP URL string.
        """
        return StringMother.invalid_value()
