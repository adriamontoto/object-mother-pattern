"""
ListMother module.
"""

from collections.abc import Callable
from random import randint
from sys import version_info
from typing import Any, TypeVar, cast

if version_info >= (3, 12):
    from typing import override  # pragma: no cover
else:
    from typing_extensions import override  # pragma: no cover

from .base_mother import BaseMother

T = TypeVar('T')


class ListMother(BaseMother[list[T]]):
    """
    ListMother class is responsible for creating random list values.

    Example:
    ```python
    from object_mother_pattern.models import ListMother
    from object_mother_pattern.mothers import IntegerMother

    values = ListMother.create(min_length=2, max_length=5, item_mother=IntegerMother.create)
    print(values)
    # >>> [13, -42, 8]
    ```
    """

    @classmethod
    @override
    def create(
        cls,
        *,
        value: list[T] | None = None,
        min_length: int = 0,
        max_length: int = 10,
        item_mother: Callable[[], T] | None = None,
    ) -> list[T]:
        """
        Create a random list value. If a specific list value is provided via `value`, it is returned after validation.
        Otherwise, a random list value is generated with the provided length bounds.

        Args:
            value (list[T] | None, optional): Specific list value to return. Defaults to None.
            min_length (int, optional): Minimum length of the list. Must be >= 0. Defaults to 0.
            max_length (int, optional): Maximum length of the list. Must be >= 0 and >= `min_length`. Defaults to 10.
            item_mother (Callable[[], T] | None, optional): Mother callable used to create each item. Defaults to None.

        Raises:
            TypeError: If the provided `value` is not a list.
            TypeError: If `min_length` is not an integer.
            TypeError: If `max_length` is not an integer.
            ValueError: If `min_length` is less than 0.
            ValueError: If `max_length` is less than 0.
            ValueError: If `min_length` is greater than `max_length`.
            TypeError: If `item_mother` is not callable.

        Returns:
            list[T]: Random list value of length between `min_length` and `max_length`.

        Example:
        ```python
        from object_mother_pattern.models import ListMother
        from object_mother_pattern.mothers import StringMother

        values = ListMother.create(min_length=2, max_length=4, item_mother=StringMother.create)
        print(values)
        # >>> ['alpha', 'beta', 'gamma']
        ```
        """
        if value is not None:
            if type(value) is not list:
                raise TypeError('ListMother value must be a list.')

            return value

        if type(min_length) is not int:
            raise TypeError('ListMother min_length must be an integer.')

        if type(max_length) is not int:
            raise TypeError('ListMother max_length must be an integer.')

        if min_length < 0:
            raise ValueError('ListMother min_length must be greater than or equal to 0.')

        if max_length < 0:
            raise ValueError('ListMother max_length must be greater than or equal to 0.')

        if min_length > max_length:
            raise ValueError('ListMother min_length must be less than or equal to max_length.')

        if item_mother is not None and not callable(item_mother):
            raise TypeError('ListMother item_mother must be callable.')

        length = randint(a=min_length, b=max_length)  # noqa: S311
        if item_mother is None:
            return cast('list[T]', [None for _ in range(length)])

        return [item_mother() for _ in range(length)]

    @classmethod
    def empty(cls) -> list[Any]:
        """
        Create an empty list.

        Returns:
            list[Any]: Empty list.

        Example:
        ```python
        from object_mother_pattern.models import ListMother

        values = ListMother.empty()
        print(values)
        # >>> []
        ```
        """
        return []

    @classmethod
    def of_length(cls, *, length: int, item_mother: Callable[[], T] | None = None) -> list[T]:
        """
        Create a list with a specific length.

        Args:
            length (int): Exact length of the list. Must be >= 0.
            item_mother (Callable[[], T] | None, optional): Mother callable used to create each item. Defaults to None.

        Raises:
            TypeError: If `length` is not an integer.
            ValueError: If `length` is less than 0.
            TypeError: If `item_mother` is not callable.

        Returns:
            list[T]: Random list value with exactly `length` items.

        Example:
        ```python
        from object_mother_pattern.models import ListMother
        from object_mother_pattern.mothers import IntegerMother

        values = ListMother.of_length(length=3, item_mother=IntegerMother.create)
        print(values)
        # >>> [7, -1, 42]
        ```
        """
        return cls.create(min_length=length, max_length=length, item_mother=item_mother)
