"""
BoolMother module.
"""

from sys import version_info

if version_info >= (3, 12):
    from typing import override  # pragma: no cover
else:
    from typing_extensions import override  # pragma: no cover

from ..base_mother import BaseMother


class BoolMother(BaseMother[bool]):
    """
    BoolMother class.

    Example:
    ```python
    from object_mother_pattern.mothers import BoolMother

    boolean = BoolMother.create()
    print(boolean)
    # >>> True
    ```
    """

    _type: type = bool

    @classmethod
    @override
    def create(cls, *, value: bool | None = None) -> bool:
        """
        Create a random boolean value.

        Args:
            value (bool | None, optional): Bool value. Defaults to None.

        Raises:
            TypeError: If value is not a boolean.

        Returns:
            bool: Random boolean.

        Example:
        ```python
        from object_mother_pattern.mothers import BoolMother

        boolean = BoolMother.create()
        print(boolean)
        # >>> True
        ```
        """
        if value is not None and type(value) is not bool:
            raise TypeError('BoolMother value must be a boolean.')

        if value is not None:
            return value

        return cls._random().pybool()
