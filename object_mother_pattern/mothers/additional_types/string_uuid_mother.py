"""
StringUUIDMother module.
"""

from random import choice
from sys import version_info

if version_info >= (3, 12):
    from typing import override  # pragma: no cover
else:
    from typing_extensions import override  # pragma: no cover

from object_mother_pattern.mothers.base_mother import BaseMother


class StringUUIDMother(BaseMother[str]):
    """
    StringUUIDMother class.

    Example:
    ```python
    from object_mother_pattern.mothers import StringUUIDMother

    uuid = StringUUIDMother.create()
    print(uuid)
    # >>> 3e9e0f3a-64a3-474f-9127-368e723f389f
    ```
    """

    _type: type = str

    @classmethod
    @override
    def create(cls, *, value: str | None = None) -> str:
        """
        Create a random string UUID. If a value is provided, it will be returned.

        Args:
            value (str | None, optional): String UUID value. Defaults to None.

        Raises:
            TypeError: If value is not a string UUID.

        Returns:
            str: Random universally unique identifier.

        Example:
        ```python
        from object_mother_pattern.mothers import StringUUIDMother

        uuid = StringUUIDMother.create()
        print(uuid)
        # >>> 3e9e0f3a-64a3-474f-9127-368e723f389f
        ```
        """
        if value is not None:
            if type(value) is not str:
                raise TypeError('StringUUIDMother value must be a string.')

            return value

        return str(object=cls._random().uuid4())

    @classmethod
    def invalid_value(cls) -> str:
        """
        Create an invalid string value.

        Returns:
            str: Invalid string.
        """
        non_printable_chars = ''.join(chr(i) for i in range(32))

        return ''.join(choice(seq=non_printable_chars) for _ in range(10))
