"""
EnumerationMother module.
"""

from enum import Enum
from random import choice
from typing import Any, Generic, Iterable, TypeVar

from object_mother_pattern.mothers.base_mother import BaseMother

E = TypeVar('E', bound=Enum)


class EnumerationMother(Generic[E]):
    """
    EnumerationMother class is responsible for creating random enum values.

    ***This class is supposed to be subclassed and not instantiated directly***.

    Example:
    ```python
    from enum import Enum, unique

    from object_mother_pattern.mothers import EnumerationMother


    @unique
    class ColorEnumeration(Enum):
        RED = 1
        GREEN = 2
        BLUE = 3


    color = EnumerationMother.create(enumeration=ColorEnumeration)
    print(color)
    # >>> Color.GREEN
    ```
    """

    @classmethod
    def create(cls, *, enumeration: type[E], value: E | None = None) -> E:
        """
        Given an enumeration, create a random enumeration value from the provided `enumeration` class. If a specific
        value is provided, it is returned after ensuring it is a member of the `enumeration`.

        Args:
            enumeration (type[E]): The enumeration class to generate a value from.
            value (E | None, optional): Specific enumeration value to return. Defaults to None.

        Raises:
            TypeError: If the provided `value` is not an instance of the `enumeration` class.
            TypeError: If the provided `enumeration` is not a subclass of Enum.

        Returns:
            E: A randomly generated enumeration value from the provided `enumeration` class.

        Example:
        ```python
        from enum import Enum, unique

        from object_mother_pattern.mothers import EnumerationMother


        @unique
        class ColorEnumeration(Enum):
            RED = 1
            GREEN = 2
            BLUE = 3


        color = EnumerationMother.create(enumeration=ColorEnumeration)
        print(color)
        # >>> Color.GREEN
        ```
        """
        if value is not None:
            if type(value) is not enumeration:
                raise TypeError(f'{enumeration.__name__}Mother value must be an instance of {enumeration.__name__}.')

            return value

        if not issubclass(enumeration, Enum):
            raise TypeError(f'{enumeration.__name__} enumeration must be a subclass of Enum.')

        return choice(seq=tuple(enumeration))  # noqa: S311

    @classmethod
    def invalid_type(cls, remove_types: Iterable[type[Any]] | None = None) -> Any:
        """
        Create an invalid type.

        Args:
            remove_types (Iterable[type[Any]] | None, optional): Iterable of types to remove. Defaults to None.

        Returns:
            Any: Invalid type.
        """
        return BaseMother.invalid_type(remove_types=remove_types)
