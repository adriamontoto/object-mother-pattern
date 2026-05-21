"""
HttpsUrlMother module.
"""

from sys import version_info

if version_info >= (3, 12):
    from typing import override  # pragma: no cover
else:
    from typing_extensions import override  # pragma: no cover


from object_mother_pattern.models import BaseMother
from object_mother_pattern.mothers.primitives.string_mother import StringMother

from .url_mother import UrlMother


class HttpsUrlMother(BaseMother[str]):
    """
    HttpsUrlMother class is responsible for creating random HTTPS URL values.

    Example:
    ```python
    from object_mother_pattern.mothers.internet import HttpsUrlMother

    url = HttpsUrlMother.create()
    print(url)
    # >>> https://example.com/orders/list
    ```
    """

    @classmethod
    @override
    def create(cls, *, value: str | None = None, host_type: str | None = None) -> str:
        """
        Create a random HTTPS URL value.

        If a specific HTTPS URL value is provided via `value`, it is returned after type validation. Otherwise, a random
        URL with the `https` scheme is generated.

        Args:
            value (str | None, optional): Specific value to return. Defaults to None.
            host_type (str | None, optional): Host type to use. Accepted values are `domain`, `ip`, `ipv4`, and `ipv6`.
                Defaults to None.

        Raises:
            TypeError: If the provided `value` is not a string.
            TypeError: If `host_type` is not a string.
            ValueError: If `host_type` is not one of `domain`, `ip`, `ipv4`, or `ipv6`.

        Returns:
            str: A randomly generated HTTPS URL value.

        Example:
        ```python
        from object_mother_pattern.mothers.internet import HttpsUrlMother

        url = HttpsUrlMother.create()
        print(url)
        # >>> https://api.example.dev/v1/orders
        ```
        """
        if value is not None:
            if type(value) is not str:
                raise TypeError('HttpsUrlMother value must be a string.')

            return value

        return UrlMother.with_scheme(scheme='https', host_type=host_type)

    @classmethod
    def invalid_value(cls) -> str:
        """
        Create an invalid HTTPS URL value.

        Returns:
            str: Invalid HTTPS URL string.
        """
        return StringMother.invalid_value()
