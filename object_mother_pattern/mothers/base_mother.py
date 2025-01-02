"""
BaseMother module.
"""

from abc import ABC, abstractmethod
from datetime import date, datetime
from random import choice
from typing import Any, Generic, Iterable, TypeVar
from uuid import UUID, uuid4

from faker import Faker

T = TypeVar('T')


class BaseMother(ABC, Generic[T]):
    """
    BaseMother class.
    """

    _type: type

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
        Create a random T. If a value is provided, it will be returned.

        Args:
            value (T | None, optional): T value. Defaults to None.

        Returns:
            T: Random T.
        """

    @classmethod
    def invalid_type(cls, remove_types: Iterable[type[Any]] | None = None) -> Any:  # noqa: C901
        """
        Create an invalid type.

        Args:
            remove_types (Iterable[type[Any]], optional): Iterable of types to remove. Defaults to None.

        Returns:
            Any: Invalid type.
        """
        faker = Faker()

        remove_types = set() if remove_types is None else set(remove_types)
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

        return choice(seq=types)
