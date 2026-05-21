"""
Base class for enum object mothers.
"""

from sys import version_info

if version_info >= (3, 12):
    from typing import override  # pragma: no cover
else:
    from typing_extensions import override  # pragma: no cover


from abc import ABC
from datetime import date, datetime
from enum import Enum
from inspect import isclass
from random import choice
from typing import Any, Generic, Iterable, TypeVar, get_args, get_origin
from uuid import UUID, uuid4

from faker import Faker

E = TypeVar('E', bound=Enum)


class EnumerationMother(ABC, Generic[E]):  # noqa: UP046
    """
    Generate valid values from a concrete `Enum` type.

    Subclasses declare the enum they create through `EnumerationMother[MyEnum]`. `create()` can return a provided enum
    value after validation, select a random enum member, or select a random member while excluding specific values.

    ***This class is supposed to be subclassed and not instantiated directly***.

    Example:
    ```python
    from enum import Enum, unique

    from object_mother_pattern.models import EnumerationMother


    @unique
    class ColorEnumeration(Enum):
        RED = 1
        GREEN = 2
        BLUE = 3


    class ColorMother(EnumerationMother[ColorEnumeration]):
        pass


    color_mother = ColorMother()

    color = color_mother.create()
    print(color)
    # >>> Color.GREEN
    ```
    """

    _enumeration: type[E]

    @override
    def __init_subclass__(cls, **kwargs: Any) -> None:
        """
        Capture and validate the enum type declared by a concrete mother.

        Args:
            **kwargs: Keyword arguments forwarded to the parent class hook.

        Raises:
            TypeError: If the class parameter is not an `Enum` subclass.
            TypeError: If the subclass is not parameterized with `EnumerationMother[E]`.
        """
        super().__init_subclass__(**kwargs)

        for base in getattr(cls, '__orig_bases__', ()):
            if get_origin(tp=base) is EnumerationMother:
                enumeration, *_ = get_args(tp=base)

                if not (isclass(object=enumeration) and issubclass(enumeration, Enum)):
                    raise TypeError(f'EnumerationMother[...] <<<{enumeration}>>> must be an Enum subclass. Got <<<{type(enumeration).__name__}>>> type.')  # noqa: E501  # fmt: skip

                cls._enumeration = enumeration  # type: ignore[assignment]
                return

        raise TypeError('EnumerationMother must be parameterized, e.g. "class ColorMother(EnumerationMother[ColorEnumeration])".')  # noqa: E501  # fmt: skip

    @classmethod
    def create(cls, *, value: E | None = None, exclude: Iterable[E] | None = None) -> E:
        """
        Create an enum member from the configured enum class.

        If `value` is provided, it is validated and returned. Otherwise, a random enum member is selected from the
        configured enumeration after removing any values passed through `exclude`.

        Args:
            value: Specific enum value to return.
            exclude: Enum values to exclude from random selection.

        Raises:
            TypeError: If the provided `value` is not an instance of the enumeration class.
            TypeError: If any value in `exclude` is not an instance of the enumeration class.
            ValueError: If all enumeration values are excluded.

        Returns:
            E: Valid enum member from the configured enum.

        Example:
        ```python
        from enum import Enum, unique

        from object_mother_pattern.models import EnumerationMother


        @unique
        class ColorEnumeration(Enum):
            RED = 1
            GREEN = 2
            BLUE = 3


        class ColorMother(EnumerationMother[ColorEnumeration]):
            pass


        color_mother = ColorMother()

        color = color_mother.create()
        print(color)
        # >>> Color.GREEN
        ```
        """
        if value is not None:
            if not isinstance(value, cls._enumeration):
                raise TypeError(f'{cls._enumeration.__name__}Mother value must be an instance of <<<{cls._enumeration.__name__}>>> type.')  # noqa: E501  # fmt: skip

            return value

        available_values: tuple[E, ...] = tuple(cls._enumeration)

        if exclude is not None:
            exclude_set = set()
            for excluded_value in exclude:
                if not isinstance(excluded_value, cls._enumeration):
                    raise TypeError(f'{cls._enumeration.__name__}Mother exclude values must be instances of <<<{cls._enumeration.__name__}>>> type.')  # noqa: E501  # fmt: skip

                exclude_set.add(excluded_value)

            available_values = tuple(value for value in available_values if value not in exclude_set)

            if not available_values:
                raise ValueError(f'{cls._enumeration.__name__}Mother cannot exclude all enumeration values.')

        return choice(seq=available_values)  # noqa: S311

    @staticmethod
    def invalid_type(remove_types: Iterable[type[Any]] | None = None) -> Any:  # noqa: C901
        """
        Generate a value with a type that should be invalid for enum mothers.

        This helper is intended for negative-path tests that verify enum validation rejects non-enum inputs.

        Args:
            remove_types: Candidate types to exclude from the generated invalid values.

        Returns:
            Any: Value whose type differs from the excluded types.
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
