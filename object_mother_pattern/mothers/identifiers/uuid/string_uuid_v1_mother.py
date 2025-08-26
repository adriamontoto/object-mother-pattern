"""
StringUuidV1Mother module.
"""

from sys import version_info

if version_info >= (3, 12):
    from typing import override  # pragma: no cover
else:
    from typing_extensions import override  # pragma: no cover


from object_mother_pattern.models import BaseMother
from object_mother_pattern.mothers.primitives import StringMother

from .uuid_v1_mother import UuidV1Mother


class StringUuidV1Mother(BaseMother[str]):
    """
    StringUuidV1Mother class is responsible for creating random string UUID1 values.

    Example:
    ```python
    from object_mother_pattern.mothers.identifiers import StringUuidV1Mother

    uuid = StringUuidV1Mother.create()
    print(uuid)
    # >>> 26afb422-824d-11f0-9bbf-325096b39f47
    ```
    """

    @classmethod
    @override
    def create(cls, *, value: str | None = None) -> str:
        """
        Create a random string UUID value. If a specific string UUID value is provided via `value`, it is returned after
        validation. Otherwise, the method generates a random string UUID.

        Args:
            value (str | None, optional): Specific value to return. Defaults to None.

        Raises:
            TypeError: If the provided `value` is not a string.

        Returns:
            str: A random string universally unique identifier value.

        Example:
        ```python
        from object_mother_pattern.mothers.identifiers import StringUuidV1Mother

        uuid = StringUuidV1Mother.create()
        print(uuid)
        # >>> 26afb422-824d-11f0-9bbf-325096b39f47
        ```
        """
        if value is not None:
            if type(value) is not str:
                raise TypeError('StringUuidV1Mother value must be a string.')

            return value

        return str(UuidV1Mother.create())

    @classmethod
    def invalid_value(cls) -> str:
        """
        Create an invalid string value.

        Returns:
            str: Invalid string.
        """
        return StringMother.invalid_value()
