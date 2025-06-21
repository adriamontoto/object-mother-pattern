"""
BaseMother module.
"""

from sys import version_info

if version_info >= (3, 12):
    from typing import override  # pragma: no cover
else:
    from typing_extensions import override  # pragma: no cover

from abc import ABC, abstractmethod
from datetime import date, datetime
from inspect import isclass
from random import choice
from typing import Any, Generic, Iterable, TypeVar, get_args, get_origin
from uuid import UUID, uuid4

from faker import Faker

T = TypeVar('T')


class BaseMother(ABC, Generic[T]):  # noqa: UP046
    """
    BaseMother class.

    ***This class is abstract and should not be instantiated directly***.
    """

    _type: type

    @override
    def __init_subclass__(cls, **kwargs: Any) -> None:
        """
        Initializes the class.

        Args:
            **kwargs (Any): Keyword arguments.

        Raises:
            TypeError: If the class parameter is not a type.
            TypeError: If the class is not parameterized.
        """
        super().__init_subclass__(**kwargs)

        for base in getattr(cls, '__orig_bases__', ()):
            if get_origin(tp=base) is BaseMother:
                mother_type, *_ = get_args(tp=base)

                if not isclass(object=mother_type):
                    raise TypeError(f'BaseMother[...] <<<{mother_type}>>> must be a type. Got <<<{type(mother_type).__name__}>>> type.')  # noqa: E501  # fmt: skip

                cls._type = mother_type
                return

        raise TypeError('BaseMother must be parameterized, e.g. "class BooleanMother(BaseMother[bool])".')

    @classmethod
    def _random(cls) -> Faker:
        """
        Get a Faker instance.

        Returns:
            Faker: Faker instance.
        """
        return Faker(use_weighting=False)

    @classmethod
    @abstractmethod
    def create(cls, *, value: T | None = None) -> T:
        """
        Create a random T value. If a specific T value is provided via `value`, it is returned after validation.
        Otherwise, a random T value is generated.

        Args:
            value (T | None, optional): A specific T value to return. Defaults to None.

        Returns:
            T: A randomly generated T value.
        """

    @classmethod
    def invalid_type(cls, *, remove_types: Iterable[type[Any]] | None = None) -> Any:  # noqa: C901
        """
        Create an invalid type.

        Args:
            remove_types (Iterable[type[Any]] | None, optional): Iterable of types to remove. Defaults to None.

        Returns:
            Any: Invalid type.
        """
        faker = Faker()

        remove_types = set() if remove_types is None else set(remove_types)
        if hasattr(cls, '_type'):
            remove_types.add(cls._type)

        types: list[Any] = []
        if int not in remove_types:
            types.append(faker.pyint())

        if float not in remove_types:
            types.append(faker.pyfloat())

        if bool not in remove_types:
            types.append(faker.pybool())

        if str not in remove_types:
            types.append(faker.pystr())

        if bytes not in remove_types:
            types.append(faker.pystr().encode())

        if list not in remove_types:
            types.append(faker.pylist())  #  pragma: no cover

        if set not in remove_types:
            types.append(faker.pyset())  #  pragma: no cover

        if tuple not in remove_types:
            types.append(faker.pytuple())  #  pragma: no cover

        if dict not in remove_types:
            types.append(faker.pydict())  #  pragma: no cover

        if datetime not in remove_types:
            types.append(faker.date_time())

        if date not in remove_types:
            types.append(faker.date_object())

        if UUID not in remove_types:
            types.append(uuid4())

        return choice(seq=types)  # noqa: S311
