"""
StringUuidV4Mother module.
"""

from sys import version_info

if version_info >= (3, 12):
    from typing import override  # pragma: no cover
else:
    from typing_extensions import override  # pragma: no cover

from uuid import uuid4

from object_mother_pattern.models import BaseMother
from object_mother_pattern.mothers.primitives import StringMother


class StringUuidV4Mother(BaseMother[str]):
    """
    StringUuidV4Mother class is responsible for creating random string UUID4 values.

    Example:
    ```python
    from object_mother_pattern.mothers.identifiers import StringUuidV4Mother

    uuid = StringUuidV4Mother.create()
    print(uuid)
    # >>> 3e9e0f3a-64a3-474f-9127-368e723f389f
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
        from object_mother_pattern.mothers.identifiers import StringUuidV4Mother

        uuid = StringUuidV4Mother.create()
        print(uuid)
        # >>> 3e9e0f3a-64a3-474f-9127-368e723f389f
        ```
        """
        if value is not None:
            if type(value) is not str:
                raise TypeError('StringUuidV4Mother value must be a string.')

            return value

        return str(object=uuid4())

    @classmethod
    def invalid_value(cls) -> str:
        """
        Create an invalid string value.

        Returns:
            str: Invalid string.
        """
        return StringMother.invalid_value()
