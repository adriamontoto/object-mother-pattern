"""
StringUuidMother module.
"""

from sys import version_info

if version_info >= (3, 12):
    from typing import override  # pragma: no cover
else:
    from typing_extensions import override  # pragma: no cover


from object_mother_pattern.models import BaseMother
from object_mother_pattern.mothers.primitives import StringMother

from .uuid_mother import UuidMother


class StringUuidMother(BaseMother[str]):
    """
    StringUuidMother class is responsible for creating random string universally unique identifier values.

    Example:
    ```python
    from object_mother_pattern.mothers.identifiers import StringUuidMother

    uuid = StringUuidMother.create()
    print(uuid)
    # >>> 3e9e0f3a-64a3-474f-9127-368e723f389f
    ```
    """

    @classmethod
    @override
    def create(cls, *, value: str | None = None, exclude_versions: set[int] | None = None) -> str:
        """
        Create a random string UUID value. If a specific string UUID value is provided via `value`, it is returned after
        validation. Otherwise, the method generates a random string UUID.

        Args:
            value (str | None, optional): Specific value to return. Defaults to None.
            exclude_versions (set[int] | None, optional): Specific UUID versions to exclude. Defaults to no exclusions.

        Raises:
            TypeError: If the provided `value` is not a string.

        Returns:
            str: A random string universally unique identifier value (UUID1, UUID2, UUID3, UUID4, or UUID5).

        Example:
        ```python
        from object_mother_pattern.mothers.identifiers import StringUuidMother

        uuid = StringUuidMother.create()
        print(uuid)
        # >>> 3e9e0f3a-64a3-474f-9127-368e723f389f
        ```
        """
        if value is not None:
            if type(value) is not str:
                raise TypeError('StringUuidMother value must be a string.')

            return value

        return str(UuidMother.create(exclude_versions=exclude_versions))

    @classmethod
    def invalid_value(cls) -> str:
        """
        Create an invalid string value.

        Returns:
            str: Invalid string.
        """
        return StringMother.invalid_value()
