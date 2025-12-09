"""
UuidV7Mother module.
"""

from sys import version_info

if version_info >= (3, 12):
    from typing import override  # pragma: no cover
else:
    from typing_extensions import override  # pragma: no cover

if version_info >= (3, 14):
    from uuid import uuid7  # pragma: no cover
else:
    from uuid6 import uuid7  # type: ignore  # pragma: no cover


from uuid import UUID

from object_mother_pattern.models import BaseMother


class UuidV7Mother(BaseMother[UUID]):
    """
    UuidV7Mother class is responsible for creating random UUID7 (random) values.

    Example:
    ```python
    from object_mother_pattern.mothers.identifiers import UuidV7Mother

    uuid = UuidV7Mother.create()
    print(uuid)
    # >>> 019afedd-025c-7f00-b22f-796d93c9b9cb
    ```
    """

    @classmethod
    @override
    def create(cls, *, value: UUID | None = None) -> UUID:
        """
        Create a random UUID7 value. If a specific UUID value is provided via `value`, it is returned after validation.
        Otherwise, the method generates a random UUID7.

        Args:
            value (UUID | None, optional): Specific value to return. Defaults to None.

        Raises:
            TypeError: If the provided `value` is not a UUID.
            TypeError: If the provided `value` is not a UUID7.

        Returns:
            UUID: A random UUID7 (random) value.

        Example:
        ```python
        from object_mother_pattern.mothers.identifiers import UuidV7Mother

        uuid = UuidV7Mother.create()
        print(uuid)
        # >>> 019afedd-025c-7f00-b22f-796d93c9b9cb
        ```
        """
        if value is not None:
            if not isinstance(value, UUID):
                raise TypeError('UuidV7Mother value must be a UUID.')

            if value.version != 7:
                raise TypeError('UuidV7Mother value must be a UUID7.')

            return value

        return uuid7()
