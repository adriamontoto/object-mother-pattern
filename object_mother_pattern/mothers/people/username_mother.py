"""
UsernameMother module.
"""

from random import choice, randint
from sys import version_info

if version_info >= (3, 12):
    from typing import override  # pragma: no cover
else:
    from typing_extensions import override  # pragma: no cover

from object_mother_pattern.models import BaseMother
from object_mother_pattern.mothers.primitives.string_mother import StringMother


class UsernameMother(BaseMother[str]):
    """
    UsernameMother class is responsible for creating random username values.

    Example:
    ```python
    from object_mother_pattern.mothers.people import UsernameMother

    username = UsernameMother.create()
    print(username)
    # >>> rickydavila
    ```
    """

    @classmethod
    @override
    def create(  # noqa: C901
        cls,
        *,
        value: str | None = None,
        min_length: int = 3,
        max_length: int = 32,
        separators: str = '_',
    ) -> str:
        """
        Create a random string username value. If a specific string username value is provided via `value`, it is
        returned after validation. Otherwise, a random string username value is generated within the provided range of
        `min_length` and `max_length` (both included), additionally can use `separators` to add some characters between
        the words. All alphanumeric characters are allowed + the provided `separators`.

        Args:
            value (str | None, optional): Specific value to return. Defaults to None.
            min_length (int, optional): Minimum length of the username. Must be >= 1. Defaults to 3.
            max_length (int, optional): Maximum length of the username. Must be >= 1 and >= `min_length`. Defaults to
            32.
            separators (str, optional): Separator characters to use in the username. Defaults to '._-'.

        Raises:
            TypeError: If the provided `value` is not a string.
            TypeError: If `min_length` is not an integer.
            TypeError: If `max_length` is not an integer.
            TypeError: If `separators` is not a string.
            ValueError: If `min_length` is not greater than 0.
            ValueError: If `max_length` is not greater than 0.
            ValueError: If `min_length` is greater than `max_length`.

        Returns:
            str: A randomly generated username value in the provided range.

        Example:
        ```python
        from object_mother_pattern.mothers.people import UsernameMother

        username = UsernameMother.create()
        print(username)
        # >>> rickydavila
        ```
        """
        if value is not None:
            if type(value) is not str:
                raise TypeError('UsernameMother value must be a string.')

            return value

        if type(min_length) is not int:
            raise TypeError('UsernameMother min_length must be an integer.')

        if type(max_length) is not int:
            raise TypeError('UsernameMother max_length must be an integer.')

        if type(separators) is not str:
            raise TypeError('UsernameMother separator must be a string.')

        if min_length < 1:
            raise ValueError('UsernameMother min_length must be greater than or equal to 1.')

        if max_length < 1:
            raise ValueError('UsernameMother max_length must be greater than or equal to 1.')

        if min_length > max_length:
            raise ValueError('UsernameMother min_length must be less than or equal to max_length.')

        length = randint(a=min_length, b=max_length)  # noqa: S311

        username = cls._random().user_name()
        while len(username) < length:
            separator = choice(seq=separators)  # noqa: S311  # pragma: no cover
            username += separator + cls._random().user_name()  # pragma: no cover

        username = username[:length]
        if username[-1] in separators:
            username = username[:-1] + cls._random().lexify(text='?').lower()  # pragma: no cover

        return username

    @classmethod
    def of_length(cls, *, length: int) -> str:
        """
        Create a random string username value of a specific `length`. All alphanumeric characters are allowed + the
        provided `separators`.

        Args:
            length (int): Length of the username. Must be >= 1.

        Raises:
            TypeError: If `length` is not an integer.
            ValueError: If `length` is not greater than 0.

        Returns:
            str: A randomly generated username value of the provided length.

        Example:
        ```python
        from object_mother_pattern.mothers.people import UsernameMother

        username = UsernameMother.of_length(length=5)
        print(username)
        # >>> mvill
        ```
        """
        return cls.create(min_length=length, max_length=length)

    @classmethod
    def invalid_value(cls) -> str:
        """
        Create an invalid string username value.

        Returns:
            str: Invalid string username string.
        """
        return StringMother.invalid_value()
