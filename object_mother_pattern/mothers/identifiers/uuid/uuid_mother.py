"""
UuidMother module.
"""

from sys import version_info

if version_info >= (3, 12):
    from typing import override  # pragma: no cover
else:
    from typing_extensions import override  # pragma: no cover

from random import choice
from uuid import UUID

from object_mother_pattern.models import BaseMother

from .uuid_v4_mother import UuidV4Mother


class UuidMother(BaseMother[UUID]):
    """
    UuidMother class is responsible for creating random universally unique identifier values.

    Example:
    ```python
    from object_mother_pattern import UuidMother

    uuid = UuidMother.create()
    print(uuid)
    # >>> 3e9e0f3a-64a3-474f-9127-368e723f389f
    ```
    """

    @classmethod
    @override
    def create(cls, *, value: UUID | None = None) -> UUID:
        """
        Create a random UUID value. If a specific UUID value is provided via `value`, it is returned after validation.\
        Otherwise, the method generates a random UUID.

        Args:
            value (UUID | None, optional): Specific value to return. Defaults to None.

        Raises:
            TypeError: If the provided `value` is not a UUID.

        Returns:
            UUID: A random universally unique identifier value.

        Example:
        ```python
        from object_mother_pattern.mothers.identifiers import UuidMother

        uuid = UuidMother.create()
        print(uuid)
        # >>> 3e9e0f3a-64a3-474f-9127-368e723f389f
        ```
        """
        if value is not None:
            if type(value) is not UUID:
                raise TypeError('UuidMother value must be a UUID.')

            return value

        uuid_generators = [
            UuidV4Mother.create,
        ]

        return choice(seq=uuid_generators)()  # noqa: S311
