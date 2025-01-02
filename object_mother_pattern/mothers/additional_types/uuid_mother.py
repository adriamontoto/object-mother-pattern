"""
UUIDMother module.
"""

from sys import version_info
from uuid import UUID

if version_info >= (3, 12):
    from typing import override  # pragma: no cover
else:
    from typing_extensions import override  # pragma: no cover

from object_mother_pattern.mothers.base_mother import BaseMother


class UUIDMother(BaseMother[UUID]):
    """
    UUIDMother class.

    Example:
    ```python
    from object_mother_pattern.mothers import UUIDMother

    uuid = UUIDMother.create()
    print(uuid)
    # >>> 3e9e0f3a-64a3-474f-9127-368e723f389f
    ```
    """

    _type: type = UUID

    @classmethod
    @override
    def create(cls, *, value: UUID | None = None) -> UUID:
        """
        Create a random UUID. If a value is provided, it will be returned.

        Args:
            value (UUID | None, optional): UUID value. Defaults to None.

        Raises:
            TypeError: If value is not a UUID.

        Returns:
            UUID: Random universally unique identifier.

        Example:
        ```python
        from object_mother_pattern.mothers import UUIDMother

        uuid = UUIDMother.create()
        print(uuid)
        # >>> 3e9e0f3a-64a3-474f-9127-368e723f389f
        ```
        """
        if value is not None:
            if type(value) is not UUID:
                raise TypeError('UUIDMother value must be a UUID.')

            return value

        return cls._random().uuid4(cast_to=None)  # type: ignore[return-value]
