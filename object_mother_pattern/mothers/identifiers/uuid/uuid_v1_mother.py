"""
UuidV1Mother module.
"""

from sys import version_info

if version_info >= (3, 12):
    from typing import override  # pragma: no cover
else:
    from typing_extensions import override  # pragma: no cover

from uuid import UUID, uuid1

from object_mother_pattern.models import BaseMother


class UuidV1Mother(BaseMother[UUID]):
    """
    UuidV1Mother class is responsible for creating random UUID1 (random) values.

    Example:
    ```python
    from object_mother_pattern.mothers.identifiers import UuidV1Mother

    uuid = UuidV1Mother.create()
    print(uuid)
    # >>> 26afb422-824d-11f0-9bbf-325096b39f47
    ```
    """

    @classmethod
    @override
    def create(cls, *, value: UUID | None = None) -> UUID:
        """
        Create a random UUID1 value. If a specific UUID value is provided via `value`, it is returned after validation.
        Otherwise, the method generates a random UUID1.

        Args:
            value (UUID | None, optional): Specific value to return. Defaults to None.

        Raises:
            TypeError: If the provided `value` is not a UUID.

        Returns:
            UUID: A random UUID1 (random) value.

        Example:
        ```python
        from object_mother_pattern.mothers.identifiers import UuidV1Mother

        uuid = UuidV1Mother.create()
        print(uuid)
        # >>> 26afb422-824d-11f0-9bbf-325096b39f47
        ```
        """
        if value is not None:
            if type(value) is not UUID:
                raise TypeError('UuidV1Mother value must be a UUID.')

            return value

        return uuid1()
