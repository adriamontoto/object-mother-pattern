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

from .uuid_v1_mother import UuidV1Mother
from .uuid_v3_mother import UuidV3Mother
from .uuid_v4_mother import UuidV4Mother
from .uuid_v5_mother import UuidV5Mother


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
    def create(cls, *, value: UUID | None = None, exclude_versions: set[int] | None = None) -> UUID:
        """
        Create a random UUID value. If a specific UUID value is provided via `value`, it is returned after validation.
        Otherwise, the method generates a random UUID.

        Args:
            value (UUID | None, optional): Specific value to return. Defaults to None.
            exclude_versions (set[int] | None, optional): Specific UUID versions to exclude. Defaults to no exclusions.

        Raises:
            TypeError: If the provided `value` is not a UUID.
            TypeError: If the provided `exclude_versions` is not a set.
            ValueError: If the provided `exclude_versions` is not a subset of {1, 3, 4, 5}.

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

        if exclude_versions is None:
            exclude_versions = set()

        if type(exclude_versions) is not set:
            raise TypeError('UuidMother exclude_versions must be a set')

        all_versions = {1, 3, 4, 5}
        if not exclude_versions.issubset(all_versions):
            raise ValueError(f'UuidMother exclude_versions must be a subset of {all_versions}')

        uuid_generators = {
            1: UuidV1Mother.create,
            3: UuidV3Mother.create,
            4: UuidV4Mother.create,
            5: UuidV5Mother.create,
        }

        allowed_versions = all_versions - exclude_versions
        allowed_generators = [uuid_generators[version] for version in allowed_versions]

        return choice(seq=allowed_generators)()  # type: ignore[operator, no-any-return]  # noqa: S311
