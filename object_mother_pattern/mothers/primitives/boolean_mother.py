"""
BooleanMother module.
"""

from sys import version_info

if version_info >= (3, 12):
    from typing import override  # pragma: no cover
else:
    from typing_extensions import override  # pragma: no cover

from random import choice

from object_mother_pattern.mothers.base_mother import BaseMother


class BooleanMother(BaseMother[bool]):
    """
    BooleanMother class.

    Example:
    ```python
    from object_mother_pattern.mothers import BooleanMother

    boolean = BooleanMother.create()
    print(boolean)
    # >>> True
    ```
    """

    _type: type = bool

    @classmethod
    @override
    def create(cls, *, value: bool | None = None) -> bool:
        """
        Create a random boolean value. If a value is provided, it will be returned.

        Args:
            value (bool | None, optional): Bool value. Defaults to None.

        Raises:
            TypeError: If value is not a boolean.

        Returns:
            bool: Random boolean.

        Example:
        ```python
        from object_mother_pattern.mothers import BooleanMother

        boolean = BooleanMother.create()
        print(boolean)
        # >>> True
        ```
        """
        if value is not None:
            if type(value) is not bool:
                raise TypeError('BooleanMother value must be a boolean.')

            return value

        return choice(seq=(True, False))  # noqa: S311

    @classmethod
    def true(cls) -> bool:
        """
        Return True.

        Returns:
            bool: True.

        Example:
        ```python
        from object_mother_pattern.mothers import BooleanMother

        boolean = BooleanMother.true()
        print(boolean)
        # >>> True
        ```
        """
        return True

    @classmethod
    def false(cls) -> bool:
        """
        Return False.

        Returns:
            bool: False.

        Example:
        ```python
        from object_mother_pattern.mothers import BooleanMother

        boolean = BooleanMother.false()
        print(boolean)
        # >>> False
        ```
        """
        return False
