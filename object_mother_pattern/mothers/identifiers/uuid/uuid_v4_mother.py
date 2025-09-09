"""
UuidV4Mother module.
"""

from sys import version_info

if version_info >= (3, 12):
    from typing import override  # pragma: no cover
else:
    from typing_extensions import override  # pragma: no cover

from uuid import UUID, uuid4

from object_mother_pattern.models import BaseMother


class UuidV4Mother(BaseMother[UUID]):
    """
    UuidV4Mother class is responsible for creating random UUID4 (random) values.

    Example:
    ```python
    from object_mother_pattern.mothers.identifiers import UuidV4Mother

    uuid = UuidV4Mother.create()
    print(uuid)
    # >>> 3e9e0f3a-64a3-474f-9127-368e723f389f
    ```
    """

    @classmethod
    @override
    def create(cls, *, value: UUID | None = None) -> UUID:
        """
        Create a random UUID4 value. If a specific UUID value is provided via `value`, it is returned after validation.
        Otherwise, the method generates a random UUID4.

        Args:
            value (UUID | None, optional): Specific value to return. Defaults to None.

        Raises:
            TypeError: If the provided `value` is not a UUID.

        Returns:
            UUID: A random UUID4 (random) value.

        Example:
        ```python
        from object_mother_pattern.mothers.identifiers import UuidV4Mother

        uuid = UuidV4Mother.create()
        print(uuid)
        # >>> 3e9e0f3a-64a3-474f-9127-368e723f389f
        ```
        """
        if value is not None:
            if type(value) is not UUID:
                raise TypeError('UuidV4Mother value must be a UUID.')

            return value

        return uuid4()
