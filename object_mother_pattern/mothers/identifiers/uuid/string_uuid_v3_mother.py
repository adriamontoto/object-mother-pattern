"""
StringUuidV3Mother module.
"""

from sys import version_info

if version_info >= (3, 12):
    from typing import override  # pragma: no cover
else:
    from typing_extensions import override  # pragma: no cover

from uuid import UUID

from object_mother_pattern.models import BaseMother
from object_mother_pattern.mothers.primitives import StringMother

from .uuid_v3_mother import UuidV3Mother


class StringUuidV3Mother(BaseMother[str]):
    """
    StringUuidV3Mother class is responsible for creating random string UUID3 values.

    Example:
    ```python
    from object_mother_pattern.mothers.identifiers import StringUuidV3Mother

    uuid = StringUuidV3Mother.create()
    print(uuid)
    # >>> 9073926b-929f-31c2-abc9-fad77ae3e8eb
    ```
    """

    @classmethod
    @override
    def create(cls, *, value: str | None = None, namespace: UUID | None = None, name: str | None = None) -> str:
        """
        Create a random string UUID3 value. If a specific string UUID value is provided via `value`, it is returned
        after validation. Otherwise, the method generates a random string UUID3 using the provided namespace and name.

        Args:
            value (str | None, optional): Specific value to return. Defaults to None.
            namespace (UUID | None, optional): UUID namespace for generation. Defaults to namespace.
            name (str | None, optional): Name for UUID generation. Defaults to a random string.

        Raises:
            TypeError: If the provided `value` is not a string.
            TypeError: If the provided `namespace` is not a UUID.
            TypeError: If the provided `name` is not a string.

        Returns:
            str: A random string UUID3 value.

        Example:
        ```python
        from object_mother_pattern.mothers.identifiers import StringUuidV3Mother

        uuid = StringUuidV3Mother.create()
        print(uuid)
        # >>> 9073926b-929f-31c2-abc9-fad77ae3e8eb
        ```
        """
        if value is not None:
            if type(value) is not str:
                raise TypeError('StringUuidV3Mother value must be a string.')

            return value

        return str(UuidV3Mother.create(namespace=namespace, name=name))

    @classmethod
    def invalid_value(cls) -> str:
        """
        Create an invalid string value.

        Returns:
            str: Invalid string.
        """
        return StringMother.invalid_value()
