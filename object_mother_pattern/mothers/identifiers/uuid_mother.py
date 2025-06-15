"""
UuidMother module.
"""

from sys import version_info
from uuid import UUID, uuid4

if version_info >= (3, 12):
    from typing import override  # pragma: no cover
else:
    from typing_extensions import override  # pragma: no cover

from object_mother_pattern.mothers.base_mother import BaseMother


class UuidMother(BaseMother[UUID]):
    """
    UuidMother class is responsible for creating random universally unique identifier values.

    Example:
    ```python
    from object_mother_pattern.mothers import UuidMother

    uuid = UuidMother.create()
    print(uuid)
    # >>> 3e9e0f3a-64a3-474f-9127-368e723f389f
    ```
    """

    @classmethod
    @override
    def create(cls, *, value: UUID | None = None) -> UUID:
        """
        Create a random UUID value. If a specific UUID value is provided via `value`, it is returned after validation.
        Otherwise, the method generates a random UUID.

        Args:
            value (UUID | None, optional): Specific value to return. Defaults to None.

        Raises:
            TypeError: If the provided `value` is not a UUID.

        Returns:
            UUID: A random universally unique identifier value.

        Example:
        ```python
        from object_mother_pattern.mothers import UuidMother

        uuid = UuidMother.create()
        print(uuid)
        # >>> 3e9e0f3a-64a3-474f-9127-368e723f389f
        ```
        """
        if value is not None:
            if type(value) is not UUID:
                raise TypeError('UuidMother value must be a UUID.')

            return value

        return uuid4()
