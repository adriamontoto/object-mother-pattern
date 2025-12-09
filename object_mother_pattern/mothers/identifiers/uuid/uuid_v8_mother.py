"""
UuidV8Mother module.
"""

from sys import version_info

if version_info >= (3, 12):
    from typing import override  # pragma: no cover
else:
    from typing_extensions import override  # pragma: no cover

if version_info >= (3, 14):
    from uuid import uuid8  # pragma: no cover
else:
    from uuid6 import uuid8  # type: ignore  # pragma: no cover

from uuid import UUID

from object_mother_pattern.models import BaseMother


class UuidV8Mother(BaseMother[UUID]):
    """
    UuidV8Mother class is responsible for creating random UUID8 (random) values.

    Example:
    ```python
    from object_mother_pattern.mothers.identifiers import UuidV8Mother

    uuid = UuidV8Mother.create()
    print(uuid)
    # >>> 1f6b82d1-1a39-4607-8a28-4dd1453104d3
    ```
    """

    @classmethod
    @override
    def create(cls, *, value: UUID | None = None) -> UUID:
        """
        Create a random UUID8 value. If a specific UUID value is provided via `value`, it is returned after validation.
        Otherwise, the method generates a random UUID8.

        Args:
            value (UUID | None, optional): Specific value to return. Defaults to None.

        Raises:
            TypeError: If the provided `value` is not a UUID.
            TypeError: If the provided `value` is not a UUID8.

        Returns:
            UUID: A random UUID8 (random) value.

        Example:
        ```python
        from object_mother_pattern.mothers.identifiers import UuidV8Mother

        uuid = UuidV8Mother.create()
        print(uuid)
        # >>> 1f6b82d1-1a39-4607-8a28-4dd1453104d3
        ```
        """
        if value is not None:
            if not isinstance(value, UUID):
                raise TypeError('UuidV8Mother value must be a UUID.')

            if value.version != 8:
                raise TypeError('UuidV8Mother value must be a UUID8.')

            return value

        return uuid8()
