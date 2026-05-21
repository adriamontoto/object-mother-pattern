"""
DictMother module.
"""

from sys import version_info

if version_info >= (3, 12):
    from typing import override  # pragma: no cover
else:
    from typing_extensions import override  # pragma: no cover


from collections.abc import Callable, Hashable
from random import randint
from typing import Any, TypeVar, cast

from .base_mother import BaseMother

K = TypeVar('K', bound=Hashable)
V = TypeVar('V')


class DictMother(BaseMother[dict[K, V]]):
    """
    DictMother class is responsible for creating random dictionary values.

    Example:
    ```python
    from object_mother_pattern.models import DictMother
    from object_mother_pattern.mothers import IntegerMother, StringMother

    values = DictMother.create(
        min_length=2,
        max_length=5,
        key_mother=StringMother.snake_case,
        value_mother=IntegerMother.create,
    )
    print(values)
    # >>> {'first_key': 13, 'second_key': -42}
    ```
    """

    @classmethod
    @override
    def create(
        cls,
        *,
        value: dict[K, V] | None = None,
        min_length: int = 0,
        max_length: int = 10,
        key_mother: Callable[[], K] | None = None,
        value_mother: Callable[[], V] | None = None,
    ) -> dict[K, V]:
        """
        Create a random dictionary value. If a specific dictionary value is provided via `value`, it is returned after
        validation. Otherwise, a random dictionary value is generated with the provided length bounds.

        Args:
            value (dict[K, V] | None, optional): Specific dictionary value to return. Defaults to None.
            min_length (int, optional): Minimum length of the dictionary. Must be >= 0. Defaults to 0.
            max_length (int, optional): Maximum length of the dictionary. Must be >= 0 and >= `min_length`. Defaults to
                10.
            key_mother (Callable[[], K] | None, optional): Mother callable used to create each key. Defaults to None.
            value_mother (Callable[[], V] | None, optional): Mother callable used to create each value. Defaults to
                None.

        Raises:
            TypeError: If the provided `value` is not a dictionary.
            TypeError: If `min_length` is not an integer.
            TypeError: If `max_length` is not an integer.
            ValueError: If `min_length` is less than 0.
            ValueError: If `max_length` is less than 0.
            ValueError: If `min_length` is greater than `max_length`.
            TypeError: If `key_mother` is not callable.
            TypeError: If `value_mother` is not callable.
            TypeError: If `key_mother` creates unhashable keys.
            ValueError: If `key_mother` cannot create enough unique keys.

        Returns:
            dict[K, V]: Random dictionary value of length between `min_length` and `max_length`.

        Example:
        ```python
        from object_mother_pattern.models import DictMother
        from object_mother_pattern.mothers import IntegerMother, StringMother

        values = DictMother.create(
            min_length=2,
            max_length=4,
            key_mother=StringMother.snake_case,
            value_mother=IntegerMother.create,
        )
        print(values)
        # >>> {'first_key': 13, 'second_key': -42}
        ```
        """
        if value is not None:
            return cls._provided_value(value=value)

        cls._ensure_lengths(min_length=min_length, max_length=max_length)
        cls._ensure_mothers(key_mother=key_mother, value_mother=value_mother)

        length = randint(a=min_length, b=max_length)  # noqa: S311
        return cls._build(length=length, key_mother=key_mother, value_mother=value_mother)

    @classmethod
    def _provided_value(cls, *, value: dict[K, V]) -> dict[K, V]:
        """
        Validate and return a provided dictionary value.

        Args:
            value (dict[K, V]): Specific dictionary value to return.

        Raises:
            TypeError: If `value` is not a dictionary.

        Returns:
            dict[K, V]: The provided dictionary value.
        """
        if type(value) is not dict:
            raise TypeError('DictMother value must be a dictionary.')

        return value

    @classmethod
    def _ensure_lengths(cls, *, min_length: int, max_length: int) -> None:
        """
        Validate dictionary length bounds.

        Args:
            min_length (int): Minimum length of the dictionary.
            max_length (int): Maximum length of the dictionary.

        Raises:
            TypeError: If `min_length` is not an integer.
            TypeError: If `max_length` is not an integer.
            ValueError: If `min_length` is less than 0.
            ValueError: If `max_length` is less than 0.
            ValueError: If `min_length` is greater than `max_length`.
        """
        if type(min_length) is not int:
            raise TypeError('DictMother min_length must be an integer.')

        if type(max_length) is not int:
            raise TypeError('DictMother max_length must be an integer.')

        if min_length < 0:
            raise ValueError('DictMother min_length must be greater than or equal to 0.')

        if max_length < 0:
            raise ValueError('DictMother max_length must be greater than or equal to 0.')

        if min_length > max_length:
            raise ValueError('DictMother min_length must be less than or equal to max_length.')

    @classmethod
    def _ensure_mothers(
        cls,
        *,
        key_mother: Callable[[], K] | None,
        value_mother: Callable[[], V] | None,
    ) -> None:
        """
        Validate dictionary key and value mother callables.

        Args:
            key_mother (Callable[[], K] | None): Mother callable used to create dictionary keys.
            value_mother (Callable[[], V] | None): Mother callable used to create dictionary values.

        Raises:
            TypeError: If `key_mother` is not callable.
            TypeError: If `value_mother` is not callable.
        """
        if key_mother is not None and not callable(key_mother):
            raise TypeError('DictMother key_mother must be callable.')

        if value_mother is not None and not callable(value_mother):
            raise TypeError('DictMother value_mother must be callable.')

    @classmethod
    def _build(
        cls,
        *,
        length: int,
        key_mother: Callable[[], K] | None,
        value_mother: Callable[[], V] | None,
    ) -> dict[K, V]:
        """
        Build a dictionary using the provided exact length and optional mothers.

        Args:
            length (int): Exact number of dictionary items to create.
            key_mother (Callable[[], K] | None): Mother callable used to create dictionary keys.
            value_mother (Callable[[], V] | None): Mother callable used to create dictionary values.

        Raises:
            TypeError: If `key_mother` creates unhashable keys.
            ValueError: If `key_mother` cannot create enough unique keys.

        Returns:
            dict[K, V]: Generated dictionary value.
        """
        values: dict[K, V] = {}
        attempts = 0
        max_attempts = max(length * 10, 100)

        while len(values) < length:
            attempts += 1
            if attempts > max_attempts:
                raise ValueError('DictMother key_mother must create enough unique keys.')

            key = cast('K', len(values)) if key_mother is None else key_mother()
            cls._ensure_hashable_key(key=key)

            if key in values:
                continue

            values[key] = cast('V', None) if value_mother is None else value_mother()

        return values

    @classmethod
    def _ensure_hashable_key(cls, *, key: K) -> None:
        """
        Validate that a generated key can be used in a dictionary.

        Args:
            key (K): Generated key to validate.

        Raises:
            TypeError: If `key` is not hashable.
        """
        try:
            hash(key)
        except TypeError as exception:
            raise TypeError('DictMother key_mother must create hashable keys.') from exception

    @classmethod
    def empty(cls) -> dict[Any, Any]:
        """
        Create an empty dictionary.

        Returns:
            dict[Any, Any]: Empty dictionary.

        Example:
        ```python
        from object_mother_pattern.models import DictMother

        values = DictMother.empty()
        print(values)
        # >>> {}
        ```
        """
        return {}

    @classmethod
    def of_length(
        cls,
        *,
        length: int,
        key_mother: Callable[[], K] | None = None,
        value_mother: Callable[[], V] | None = None,
    ) -> dict[K, V]:
        """
        Create a dictionary with a specific length.

        Args:
            length (int): Exact length of the dictionary. Must be >= 0.
            key_mother (Callable[[], K] | None, optional): Mother callable used to create each key. Defaults to None.
            value_mother (Callable[[], V] | None, optional): Mother callable used to create each value. Defaults to
                None.

        Raises:
            TypeError: If `length` is not an integer.
            ValueError: If `length` is less than 0.
            TypeError: If `key_mother` is not callable.
            TypeError: If `value_mother` is not callable.
            TypeError: If `key_mother` creates unhashable keys.
            ValueError: If `key_mother` cannot create enough unique keys.

        Returns:
            dict[K, V]: Random dictionary value with exactly `length` items.

        Example:
        ```python
        from object_mother_pattern.models import DictMother
        from object_mother_pattern.mothers import IntegerMother, StringMother

        values = DictMother.of_length(
            length=3,
            key_mother=StringMother.snake_case,
            value_mother=IntegerMother.create,
        )
        print(values)
        # >>> {'first_key': 13, 'second_key': -42, 'third_key': 8}
        ```
        """
        return cls.create(
            min_length=length,
            max_length=length,
            key_mother=key_mother,
            value_mother=value_mother,
        )
