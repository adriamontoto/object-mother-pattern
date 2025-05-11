"""
EnumerationMother module.
"""

from datetime import date, datetime
from enum import Enum
from random import choice
from typing import Any, Generic, Iterable, TypeVar
from uuid import UUID, uuid4

from faker import Faker

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


    color_mother = EnumerationMother(enumeration=ColorEnumeration)

    color = color_mother.create()
    print(color)
    # >>> Color.GREEN
    ```
    """

    _enumeration: type[E]

    def __init__(self, *, enumeration: type[E]) -> None:
        """
        Initialize the EnumerationMother with the specified enumeration class `enumeration`.

        Args:
            enumeration (type[E]): The enumeration class to generate values from.

        Raises:
            TypeError: If the provided `enumeration` is not a subclass of Enum.

        Example:
        ```python
        from enum import Enum, unique

        from object_mother_pattern.mothers import EnumerationMother


        @unique
        class ColorEnumeration(Enum):
            RED = 1
            GREEN = 2
            BLUE = 3


        color_mother = EnumerationMother(enumeration=ColorEnumeration)

        color = color_mother.create()
        print(color)
        # >>> Color.GREEN
        ```
        """
        if type(enumeration) is not type(Enum):
            raise TypeError('EnumerationMother enumeration must be a subclass of Enum.')

        self._enumeration = enumeration

    def create(self, *, value: E | None = None) -> E:
        """
        Create a random enumeration value from the enumeration class. If a specific
        value is provided, it is returned after ensuring it is a member of the enumeration.

        Args:
            value (E | None, optional): Specific enumeration value to return. Defaults to None.

        Raises:
            TypeError: If the provided `value` is not an instance of the enumeration class.

        Returns:
            E: A randomly generated enumeration value from the enumeration class.

        Example:
        ```python
        from enum import Enum, unique

        from object_mother_pattern.mothers import EnumerationMother


        @unique
        class ColorEnumeration(Enum):
            RED = 1
            GREEN = 2
            BLUE = 3


        color_mother = EnumerationMother(enumeration=ColorEnumeration)

        color = color_mother.create()
        print(color)
        # >>> Color.GREEN
        ```
        """
        if value is not None:
            if type(value) is not self._enumeration:
                raise TypeError(f'{self._enumeration.__name__}Mother value must be an instance of {self._enumeration.__name__}.')  # noqa: E501  # fmt: skip

            return value

        return choice(seq=tuple(self._enumeration))  # noqa: S311

    @staticmethod
    def invalid_type(remove_types: Iterable[type[Any]] | None = None) -> Any:  # noqa: C901
        """
        Create an invalid type.

        Args:
            remove_types (Iterable[type[Any]] | None, optional): Iterable of types to remove. Defaults to None.

        Returns:
            Any: Invalid type.
        """
        faker = Faker()

        remove_types = set() if remove_types is None else set(remove_types)

        types: list[Any] = []
        if int not in remove_types:
            types.append(faker.pyint())  # pragma: no cover

        if float not in remove_types:
            types.append(faker.pyfloat())  # pragma: no cover

        if bool not in remove_types:
            types.append(faker.pybool())  # pragma: no cover

        if str not in remove_types:
            types.append(faker.pystr())  # pragma: no cover

        if bytes not in remove_types:
            types.append(faker.pystr().encode())  # pragma: no cover

        if list not in remove_types:
            types.append(faker.pylist())  # pragma: no cover

        if set not in remove_types:
            types.append(faker.pyset())  # pragma: no cover

        if tuple not in remove_types:
            types.append(faker.pytuple())  # pragma: no cover

        if dict not in remove_types:
            types.append(faker.pydict())  # pragma: no cover

        if datetime not in remove_types:
            types.append(faker.date_time())  # pragma: no cover

        if date not in remove_types:
            types.append(faker.date_object())  # pragma: no cover

        if UUID not in remove_types:
            types.append(uuid4())  # pragma: no cover

        return choice(seq=types)  # noqa: S311
