"""
KeyMother module.
"""

from sys import version_info

if version_info >= (3, 12):
    from typing import override  # pragma: no cover
else:
    from typing_extensions import override  # pragma: no cover


from random import choice, randint, sample

from object_mother_pattern.models import BaseMother
from object_mother_pattern.mothers.primitives.string_mother import StringMother


class KeyMother(BaseMother[str]):
    """
    KeyMother class is responsible for creating random key values.

    A generated key follows the format:
    - lowercase letters and digits
    - optional separators between groups (`.` or `-`)
    - no leading/trailing separators
    - no consecutive separators

    Example:
    ```python
    from object_mother_pattern.mothers.internet import KeyMother

    key = KeyMother.create()
    print(key)
    # >>> user.profile-1
    ```
    """

    _ALPHANUMERIC: str = 'abcdefghijklmnopqrstuvwxyz0123456789'
    _SEPARATORS: str = '.-'

    @classmethod
    @override
    def create(
        cls,
        *,
        value: str | None = None,
        min_length: int = 3,
        max_length: int = 64,
    ) -> str:
        """
        Create a random key value. If a specific key value is provided via `value`, it is returned after validation.
        Otherwise, a random key value is generated within the provided range of `min_length` and `max_length` (both
        included).

        Args:
            value (str | None, optional): Specific value to return. Defaults to None.
            min_length (int, optional): Minimum length of the key. Must be >= 1. Defaults to 3.
            max_length (int, optional): Maximum length of the key. Must be >= 1 and >= `min_length`. Defaults to 64.

        Raises:
            TypeError: If the provided `value` is not a string.
            TypeError: If `min_length` is not an integer.
            TypeError: If `max_length` is not an integer.
            ValueError: If `min_length` is less than 1.
            ValueError: If `max_length` is less than 1.
            ValueError: If `min_length` is greater than `max_length`.

        Returns:
            str: A randomly generated key value.

        Example:
        ```python
        from object_mother_pattern.mothers.internet import KeyMother

        key = KeyMother.create()
        print(key)
        # >>> user.profile-1
        ```
        """
        if value is not None:
            if type(value) is not str:
                raise TypeError('KeyMother value must be a string.')

            return value

        if type(min_length) is not int:
            raise TypeError('KeyMother min_length must be an integer.')

        if type(max_length) is not int:
            raise TypeError('KeyMother max_length must be an integer.')

        if min_length < 1:
            raise ValueError('KeyMother min_length must be greater than or equal to 1.')

        if max_length < 1:
            raise ValueError('KeyMother max_length must be greater than or equal to 1.')

        if min_length > max_length:
            raise ValueError('KeyMother min_length must be less than or equal to max_length.')

        total_length = randint(a=min_length, b=max_length)  # noqa: S311
        separator_count = cls._separator_count(total_length=total_length)
        total_segments = separator_count + 1
        total_alphanumeric = total_length - separator_count
        segment_lengths = cls._segment_lengths(
            total_alphanumeric=total_alphanumeric,
            total_segments=total_segments,
        )

        key = ''
        for index, segment_length in enumerate(segment_lengths):
            key += ''.join(choice(seq=cls._ALPHANUMERIC) for _ in range(segment_length))  # noqa: S311

            if index < separator_count:
                key += choice(seq=cls._SEPARATORS)  # noqa: S311

        return key

    @classmethod
    def of_length(cls, *, length: int) -> str:
        """
        Create a random key value of a specific `length`.

        Args:
            length (int): Length of the key. Must be >= 1.

        Returns:
            str: A randomly generated key value with the provided length.

        Example:
        ```python
        from object_mother_pattern.mothers.internet import KeyMother

        key = KeyMother.of_length(length=12)
        print(key)
        # >>> account-id.4
        ```
        """
        return cls.create(min_length=length, max_length=length)

    @classmethod
    def _separator_count(cls, *, total_length: int) -> int:
        """
        Generate the number of separators for a key with `total_length`.

        Args:
            total_length (int): Total target key length.

        Returns:
            int: Number of separators to use.
        """
        max_separators = (total_length - 1) // 2

        if max_separators == 0:
            return 0

        return randint(a=0, b=max_separators)  # noqa: S311

    @classmethod
    def _segment_lengths(cls, *, total_alphanumeric: int, total_segments: int) -> tuple[int, ...]:
        """
        Split `total_alphanumeric` characters into `total_segments` positive segment lengths.

        Args:
            total_alphanumeric (int): Total number of alphanumeric characters.
            total_segments (int): Number of segments to generate.

        Returns:
            tuple[int, ...]: Segment lengths.
        """
        if total_segments == 1:
            return (total_alphanumeric,)

        split_points = sample(population=range(1, total_alphanumeric), k=total_segments - 1)  # noqa: S311
        split_points.sort()
        boundaries = [0, *split_points, total_alphanumeric]

        return tuple(boundaries[index + 1] - boundaries[index] for index in range(total_segments))

    @classmethod
    def invalid_value(cls) -> str:
        """
        Create an invalid key value.

        Returns:
            str: Invalid key string.
        """
        return StringMother.invalid_value()
