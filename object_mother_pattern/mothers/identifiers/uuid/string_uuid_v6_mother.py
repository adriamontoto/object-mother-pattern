"""
StringUuidV6Mother module.
"""

from sys import version_info

if version_info >= (3, 12):
    from typing import override  # pragma: no cover
else:
    from typing_extensions import override  # pragma: no cover

from uuid import UUID

from object_mother_pattern.models import BaseMother
from object_mother_pattern.mothers.primitives import StringMother

from .uuid_v6_mother import UuidV6Mother


class StringUuidV6Mother(BaseMother[str]):
    """
    StringUuidV6Mother class is responsible for creating random string UUID6 values.

    Example:
    ```python
    from object_mother_pattern.mothers.identifiers import StringUuidV6Mother

    uuid = StringUuidV6Mother.create()
    print(uuid)
    # >>> 1f0d455c-76e5-6210-b032-46ef6b2a93e1
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
            TypeError: If the provided `value` is not a UUID6.

        Returns:
            str: A random string universally unique identifier value.

        Example:
        ```python
        from object_mother_pattern.mothers.identifiers import StringUuidV6Mother

        uuid = StringUuidV6Mother.create()
        print(uuid)
        # >>> 1f0d455c-76e5-6210-b032-46ef6b2a93e1
        ```
        """
        if value is not None:
            if type(value) is not str:
                raise TypeError('StringUuidV6Mother value must be a string.')

            try:
                UUID(value)

            except Exception as exception:
                raise TypeError('StringUuidV6Mother value must be a UUID.') from exception

            return str(UuidV6Mother.create(value=UUID(value)))

        return str(UuidV6Mother.create())

    @classmethod
    def invalid_value(cls) -> str:
        """
        Create an invalid string value.

        Returns:
            str: Invalid string.
        """
        return StringMother.invalid_value()
