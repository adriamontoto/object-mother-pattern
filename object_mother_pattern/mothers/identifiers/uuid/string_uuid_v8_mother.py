"""
StringUuidV8Mother module.
"""

from sys import version_info

if version_info >= (3, 12):
    from typing import override  # pragma: no cover
else:
    from typing_extensions import override  # pragma: no cover

from uuid import UUID

from object_mother_pattern.models import BaseMother
from object_mother_pattern.mothers.primitives import StringMother

from .uuid_v8_mother import UuidV8Mother


class StringUuidV8Mother(BaseMother[str]):
    """
    StringUuidV8Mother class is responsible for creating random string UUID8 values.

    Example:
    ```python
    from object_mother_pattern.mothers.identifiers import StringUuidV8Mother

    uuid = StringUuidV8Mother.create()
    print(uuid)
    # >>> 1f6b82d1-1a39-4607-8a28-4dd1453104d3
    ```
    """

    @classmethod
    @override
    def create(cls, *, value: str | None = None) -> str:
        """
        Create a random string UUID value. If a specific string UUID value is provided via `value`, it is returned after
        validation. Otherwise, the method generates a random string UUID.

        Args:
            value (str | None, optional): Specific value to return. Defaults to None.

        Raises:
            TypeError: If the provided `value` is not a string.
            TypeError: If the provided `value` is not a valid UUID string.
            TypeError: If the provided `value` is not a UUID8.

        Returns:
            str: A random string universally unique identifier value.

        Example:
        ```python
        from object_mother_pattern.mothers.identifiers import StringUuidV8Mother

        uuid = StringUuidV8Mother.create()
        print(uuid)
        # >>> 1f6b82d1-1a39-4607-8a28-4dd1453104d3
        ```
        """
        if value is not None:
            if type(value) is not str:
                raise TypeError('StringUuidV8Mother value must be a string.')

            try:
                UUID(value)

            except Exception as exception:
                raise TypeError('StringUuidV8Mother value must be a UUID.') from exception

            return str(UuidV8Mother.create(value=UUID(value)))

        return str(UuidV8Mother.create())

    @classmethod
    def invalid_value(cls) -> str:
        """
        Create an invalid string value.

        Returns:
            str: Invalid string.
        """
        return StringMother.invalid_value()
