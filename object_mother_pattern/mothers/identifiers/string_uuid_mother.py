"""
StringUuidMother module.
"""

from sys import version_info

if version_info >= (3, 12):
    from typing import override  # pragma: no cover
else:
    from typing_extensions import override  # pragma: no cover

from object_mother_pattern.mothers import StringMother
from object_mother_pattern.mothers.base_mother import BaseMother


class StringUuidMother(BaseMother[str]):
    """
    StringUuidMother class is responsible for creating random string universally unique identifier values.

    Example:
    ```python
    from object_mother_pattern.mothers import StringUuidMother

    uuid = StringUuidMother.create()
    print(uuid)
    # >>> 3e9e0f3a-64a3-474f-9127-368e723f389f
    ```
    """

    _type: type = str

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
        from object_mother_pattern.mothers import StringUuidMother

        uuid = StringUuidMother.create()
        print(uuid)
        # >>> 3e9e0f3a-64a3-474f-9127-368e723f389f
        ```
        """
        if value is not None:
            if type(value) is not str:
                raise TypeError('StringUuidMother value must be a string.')

            return value

        return str(object=cls._random().uuid4())

    @classmethod
    def invalid_value(cls) -> str:
        """
        Create an invalid string value.

        Returns:
            str: Invalid string.
        """
        return StringMother.invalid_value()
