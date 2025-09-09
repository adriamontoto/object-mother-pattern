"""
UuidV5Mother module.
"""

from sys import version_info

if version_info >= (3, 12):
    from typing import override  # pragma: no cover
else:
    from typing_extensions import override  # pragma: no cover

from random import choice
from uuid import NAMESPACE_DNS, NAMESPACE_OID, NAMESPACE_URL, NAMESPACE_X500, UUID, uuid5

from object_mother_pattern.models import BaseMother
from object_mother_pattern.mothers import StringMother


class UuidV5Mother(BaseMother[UUID]):
    """
    UuidV5Mother class is responsible for creating random UUID5 (namespace) values.

    Example:
    ```python
    from object_mother_pattern.mothers.identifiers import UuidV5Mother

    uuid = UuidV5Mother.create()
    print(uuid)
    # >>> cfbff0d1-9375-5685-968c-48ce8b15ae17
    ```
    """

    @classmethod
    @override
    def create(cls, *, value: UUID | None = None, namespace: UUID | None = None, name: str | None = None) -> UUID:
        """
        Create a random UUID5 value. If a specific UUID value is provided via `value`, it is returned after validation.
        Otherwise, the method generates a random UUID5 using the provided namespace and name.

        Args:
            value (UUID | None, optional): Specific value to return. Defaults to None.
            namespace (UUID | None, optional): UUID namespace for generation. Defaults to namespace.
            name (str | None, optional): Name for UUID generation. Defaults to a random string.

        Raises:
            TypeError: If the provided `value` is not a UUID.
            TypeError: If the provided `namespace` is not a UUID.
            TypeError: If the provided `name` is not a string.

        Returns:
            UUID: A random UUID5 (namespace) value.

        Example:
        ```python
        from object_mother_pattern.mothers.identifiers import UuidV5Mother

        uuid = UuidV5Mother.create()
        print(uuid)
        # >>> cfbff0d1-9375-5685-968c-48ce8b15ae17
        ```
        """
        if value is not None:
            if type(value) is not UUID:
                raise TypeError('UuidV5Mother value must be a UUID.')

            return value

        if namespace is None:
            namespace = choice((NAMESPACE_DNS, NAMESPACE_OID, NAMESPACE_URL, NAMESPACE_X500))  # noqa: S311

        if type(namespace) is not UUID:
            raise TypeError('UuidV5Mother namespace must be a UUID.')

        if name is None:
            name = StringMother.create()

        if type(name) is not str:
            raise TypeError('UuidV5Mother name must be a string.')

        return uuid5(namespace=namespace, name=name)
