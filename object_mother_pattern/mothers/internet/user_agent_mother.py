"""
UserAgentMother module.
"""

from sys import version_info

if version_info >= (3, 12):
    from typing import override  # pragma: no cover
else:
    from typing_extensions import override  # pragma: no cover

from random import randint

from object_mother_pattern.models import BaseMother
from object_mother_pattern.mothers.primitives.string_mother import StringMother


class UserAgentMother(BaseMother[str]):
    """
    UserAgentMother class is responsible for creating random user agent values.

    Example:
    ```python
    from object_mother_pattern.mothers.internet import UserAgentMother

    agent = UserAgentMother.create()
    print(agent)
    # >>> Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.1 (KHTML, like Gecko) Chrome/44.0.865.0 Safari/536.1
    ```
    """

    @classmethod
    @override
    def create(cls, *, value: str | None = None, min_length: int = 64, max_length: int = 256) -> str:
        """
        Create a random user agent value. If a specific user agent value is provided via `value`, it is returned after
        validation. Otherwise, a random user agent value is generated within the provided range of `min_length` and
        `max_length` (both included).

        Args:
            value (str | None, optional): Specific value to return. Defaults to None.
            min_length (int, optional): Minimum length of the user agent. Must be >= 1. Defaults to 64.
            max_length (int, optional): Maximum length of the user agent. Must be >= 1 and >= `min_length`. Defaults to
            256.

        Raises:
            TypeError: If the provided `value` is not a string.
            TypeError: If `min_length` is not an integer.
            TypeError: If `max_length` is not an integer.
            ValueError: If `min_length` is not greater than 0.
            ValueError: If `max_length` is not greater than 0.
            ValueError: If `min_length` is greater than `max_length`.

        Returns:
            str: A randomly generated user agent value in the provided range.

        Example:
        ```python
        from object_mother_pattern.mothers.internet import UserAgentMother

        agent = UserAgentMother.create()
        print(agent)
        # >>> Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.1 (KHTML, like Gecko) Chrome/44.0.865.0 Safari/536.1
        ```
        """
        if value is not None:
            if type(value) is not str:
                raise TypeError('UserAgentMother value must be a string.')

            return value

        if type(min_length) is not int:
            raise TypeError('UserAgentMother min_length must be an integer.')

        if type(max_length) is not int:
            raise TypeError('UserAgentMother max_length must be an integer.')

        if min_length < 1:
            raise ValueError('UserAgentMother min_length must be greater than or equal to 1.')

        if max_length < 1:
            raise ValueError('UserAgentMother max_length must be greater than or equal to 1.')

        if min_length > max_length:
            raise ValueError('UserAgentMother min_length must be less than or equal to max_length.')

        length = randint(a=min_length, b=max_length)  # noqa: S311

        user_agent = cls._random().user_agent()
        while len(user_agent) < length:
            user_agent += cls._random().user_agent()

        user_agent = user_agent[:length]
        if user_agent != user_agent.strip():
            user_agent = user_agent[:-1] + cls._random().lexify(text='?').lower()  # pragma: no cover

        return user_agent[:length]

    @classmethod
    def of_length(cls, *, length: int) -> str:
        """
        Create a random user agent value of a specific `length`.

        Args:
            length (int): Length of the user agent. Must be >= 1.

        Raises:
            TypeError: If `length` is not an integer.
            ValueError: If `length` is not greater than 0.

        Returns:
            str: A randomly generated user agent value of the provided length.

        Example:
        ```python
        from object_mother_pattern.mothers.internet import UserAgentMother

        agent = UserAgentMother.of_length(length=100)
        print(agent)
        # >>> Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.1 (KHTML, like Gecko) Chrome/44.0.865.0 Safari/536.1
        ```
        """
        return cls.create(min_length=length, max_length=length)

    @classmethod
    def invalid_value(cls) -> str:
        """
        Create an invalid user agent value.

        Returns:
            str: Invalid user agent string.
        """
        return StringMother.invalid_value()
