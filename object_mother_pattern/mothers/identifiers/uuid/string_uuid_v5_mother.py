"""
StringUuidV5Mother module.
"""

from sys import version_info

if version_info >= (3, 12):
    from typing import override  # pragma: no cover
else:
    from typing_extensions import override  # pragma: no cover

from uuid import UUID

from object_mother_pattern.models import BaseMother
from object_mother_pattern.mothers.primitives import StringMother

from .uuid_v5_mother import UuidV5Mother


class StringUuidV5Mother(BaseMother[str]):
    """
    StringUuidV5Mother class is responsible for creating random string UUID5 values.

    Example:
    ```python
    from object_mother_pattern.mothers.identifiers import StringUuidV5Mother

    uuid = StringUuidV5Mother.create()
    print(uuid)
    # >>> cfbff0d1-9375-5685-968c-48ce8b15ae17
    ```
    """

    @classmethod
    @override
    def create(cls, *, value: str | None = None, namespace: UUID | None = None, name: str | None = None) -> str:
        """
        Create a random string UUID5 value. If a specific string UUID value is provided via `value`, it is returned
        after validation. Otherwise, the method generates a random string UUID5 using the provided namespace and name.

        Args:
            value (str | None, optional): Specific value to return. Defaults to None.
            namespace (UUID | None, optional): UUID namespace for generation. Defaults to namespace.
            name (str | None, optional): Name for UUID generation. Defaults to a random string.

        Raises:
            TypeError: If the provided `value` is not a string.
            TypeError: If the provided `namespace` is not a UUID.
            TypeError: If the provided `name` is not a string.

        Returns:
            str: A random string UUID5 value.

        Example:
        ```python
        from object_mother_pattern.mothers.identifiers import StringUuidV5Mother

        uuid = StringUuidV5Mother.create()
        print(uuid)
        # >>> cfbff0d1-9375-5685-968c-48ce8b15ae17
        ```
        """
        if value is not None:
            if type(value) is not str:
                raise TypeError('StringUuidV5Mother value must be a string.')

            return value

        return str(UuidV5Mother.create(namespace=namespace, name=name))

    @classmethod
    def invalid_value(cls) -> str:
        """
        Create an invalid string value.

        Returns:
            str: Invalid string.
        """
        return StringMother.invalid_value()
