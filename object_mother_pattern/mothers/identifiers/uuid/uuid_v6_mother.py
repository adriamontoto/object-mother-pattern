"""
UuidV6Mother module.
"""

from sys import version_info

if version_info >= (3, 12):
    from typing import override  # pragma: no cover
else:
    from typing_extensions import override  # pragma: no cover

if version_info >= (3, 14):
    from uuid import uuid6  # pragma: no cover
else:
    from uuid6 import uuid6  # type: ignore  # pragma: no cover

from uuid import UUID

from object_mother_pattern.models import BaseMother


class UuidV6Mother(BaseMother[UUID]):
    """
    UuidV6Mother class is responsible for creating random UUID6 (random) values.

    Example:
    ```python
    from object_mother_pattern.mothers.identifiers import UuidV6Mother

    uuid = UuidV6Mother.create()
    print(uuid)
    # >>> 1f0d455c-76e5-6210-b032-46ef6b2a93e1
    ```
    """

    @classmethod
    @override
    def create(cls, *, value: UUID | None = None) -> UUID:
        """
        Create a random UUID6 value. If a specific UUID value is provided via `value`, it is returned after validation.
        Otherwise, the method generates a random UUID6.

        Args:
            value (UUID | None, optional): Specific value to return. Defaults to None.

        Raises:
            TypeError: If the provided `value` is not a UUID.
            TypeError: If the provided `value` is not a UUID6.

        Returns:
            UUID: A random UUID6 (random) value.

        Example:
        ```python
        from object_mother_pattern.mothers.identifiers import UuidV6Mother

        uuid = UuidV6Mother.create()
        print(uuid)
        # >>> 1f0d455c-76e5-6210-b032-46ef6b2a93e1
        ```
        """
        if value is not None:
            if not isinstance(value, UUID):
                raise TypeError('UuidV6Mother value must be a UUID.')

            if value.version != 6:
                raise TypeError('UuidV6Mother value must be a UUID6.')

            return value

        return uuid6()
