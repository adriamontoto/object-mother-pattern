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
    BooleanMother class is responsible for creating random boolean values.

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
        Create a boolean value. If a specific boolean value is provided via `value`, it is returned after validation.
        Otherwise, a random boolean is generated.

        Args:
            value (bool | None, optional): A specific boolean value to return. Defaults to None.

        Raises:
            TypeError: If the provided `value` is not a boolean.

        Returns:
            bool: A randomly generated boolean value.

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
        Return a true boolean value.

        Returns:
            bool: True boolean value.

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
        Return a false boolean value.

        Returns:
            bool: False boolean value.

        Example:
        ```python
        from object_mother_pattern.mothers import BooleanMother

        boolean = BooleanMother.false()
        print(boolean)
        # >>> False
        ```
        """
        return False
