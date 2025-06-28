"""
StringMother module.
"""

from sys import version_info

if version_info >= (3, 12):
    from typing import override  # pragma: no cover
else:
    from typing_extensions import override  # pragma: no cover

from random import choice, randint

from object_mother_pattern.models import BaseMother

from .utils.alphabets import ALPHABET_BASIC, ALPHABET_LOWERCASE_BASIC, ALPHABET_UPPERCASE_BASIC, DIGITS_BASIC


class StringMother(BaseMother[str]):
    """
    StringMother class.

    Example:
    ```python
    from object_mother_pattern import StringMother

    string = StringMother.create()
    print(string)
    # >>> zFUmlsODZqzwyGjrOOqBtYzNwlJdOETalkXbuSegoQpgEnYQTCDeoifWrTQXMm
    ```
    """

    @classmethod
    @override
    def create(
        cls,
        *,
        value: str | None = None,
        min_length: int = 1,
        max_length: int = 128,
        characters: str = ALPHABET_BASIC,
    ) -> str:
        """
        Create a random string value. If a specific string value is provided via `value`, it is returned after
        validation. Otherwise, a random string value is generated with the provided `min_length`, `max_length` (both
        included), and `characters`.

        Args:
            value (str | None, optional): String value. Defaults to None.
            min_length (int, optional): Minimum length of the string. Must be >= 0. Defaults to 1.
            max_length (int, optional): Maximum length of the string. Must be >= 0 and >= `min_length`. Defaults to 128.
            characters (str, optional): Characters to use for the string. Must not be empty. Defaults to ALPHABET_BASIC.

        Raises:
            TypeError: If `value` is not a string.
            TypeError: If `min_length` is not an integer.
            TypeError: If `max_length` is not an integer.
            ValueError: If `min_length` is less than 0.
            ValueError: If `max_length` is less than 0.
            ValueError: If `min_length` is greater than `max_length`.
            TypeError: If `characters` is not a string.
            ValueError: If `characters` is empty.

        Returns:
            str: Random string value of length between `min_length` and `max_length` (inclusive) and using the provided
            `characters`.

        Example:
        ```python
        from object_mother_pattern import StringMother

        string = StringMother.create()
        print(string)
        # >>> zFUmlsODZqzwyGjrOOqBtYzNwlJdOETalkXbuSegoQpgEnYQTCDeoifWrTQXMm
        ```
        """
        if value is not None:
            if type(value) is not str:
                raise TypeError('StringMother value must be a string.')

            return value

        if type(min_length) is not int:
            raise TypeError('StringMother min_length must be an integer.')

        if type(max_length) is not int:
            raise TypeError('StringMother max_length must be an integer.')

        if min_length < 0:
            raise ValueError('StringMother min_length must be greater than or equal to 0.')

        if max_length < 0:
            raise ValueError('StringMother max_length must be greater than or equal to 0.')

        if min_length > max_length:
            raise ValueError('StringMother min_length must be less than or equal to max_length.')

        if type(characters) is not str:
            raise TypeError('StringMother characters must be a string.')

        if not characters:
            raise ValueError('StringMother characters must not be empty.')

        length = randint(a=min_length, b=max_length)  # noqa: S311
        return ''.join(choice(seq=characters) for _ in range(length))  # noqa: S311

    @classmethod
    def empty(cls) -> str:
        """
        Create an empty string value.

        Returns:
            str: Empty string.

        Example:
        ```python
        from object_mother_pattern import StringMother

        string = StringMother.empty()
        print(string)
        # >>>
        ```
        """
        return ''

    @classmethod
    def lowercase(cls, *, min_length: int = 1, max_length: int = 128) -> str:
        """
        Create a random string value with only lowercase characters of length between `min_length` and `max_length`.

        Args:
            min_length (int, optional): Minimum length of the string. Must be >= 0. Defaults to 1.
            max_length (int, optional): Maximum length of the string. Must be >= 0 and >= `min_length`. Defaults to 128.

        Raises:
            TypeError: If `min_length` is not an integer.
            TypeError: If `max_length` is not an integer.
            ValueError: If `min_length` is less than 0.
            ValueError: If `max_length` is less than 0.
            ValueError: If `min_length` is greater than `max_length`.

        Returns:
            str: Random string with only lowercase characters of length between `min_length` and `max_length`.

        Example:
        ```python
        from object_mother_pattern import StringMother

        string = StringMother.lowercase(min_length=8, max_length=32)
        print(string)
        # >>> tfkryxuftaewzbc
        ```
        """
        return cls.create(min_length=min_length, max_length=max_length, characters=ALPHABET_LOWERCASE_BASIC)

    @classmethod
    def uppercase(cls, *, min_length: int = 1, max_length: int = 128) -> str:
        """
        Create a random string value with only uppercase characters of length between `min_length` and `max_length`.

        Args:
            min_length (int, optional): Minimum length of the string. Must be >= 0. Defaults to 1.
            max_length (int, optional): Maximum length of the string. Must be >= 0 and >= `min_length`. Defaults to 128.

        Raises:
            TypeError: If `min_length` is not an integer.
            TypeError: If `max_length` is not an integer.
            ValueError: If `min_length` is less than 0.
            ValueError: If `max_length` is less than 0.
            ValueError: If `min_length` is greater than `max_length`.

        Returns:
            str: Random string with only uppercase characters of length between `min_length` and `max_length`.

        Example:
        ```python
        from object_mother_pattern import StringMother

        string = StringMother.uppercase(min_length=8, max_length=32)
        print(string)
        # >>> TFRYXUFTAEWZBC
        ```
        """
        return cls.create(min_length=min_length, max_length=max_length, characters=ALPHABET_UPPERCASE_BASIC)

    @classmethod
    def titlecase(cls, *, min_length: int = 1, max_length: int = 128) -> str:
        """
        Create a random string value with only titlecase characters of length between `min_length` and `max_length`.

        Args:
            min_length (int, optional): Minimum length of the string. Must be >= 0. Defaults to 1.
            max_length (int, optional): Maximum length of the string. Must be >= 0 and >= `min_length`. Defaults to 128.

        Raises:
            TypeError: If `min_length` is not an integer.
            TypeError: If `max_length` is not an integer.
            ValueError: If `min_length` is less than 0.
            ValueError: If `max_length` is less than 0.
            ValueError: If `min_length` is greater than `max_length`.

        Returns:
            str: Random string with only titlecase characters of length between `min_length` and `max_length`.

        Example:
        ```python
        from object_mother_pattern import StringMother

        string = StringMother.titlecase(min_length=8, max_length=32)
        print(string)
        # >>> Taknabjoqndabq
        ```
        """
        return cls.create(
            min_length=min_length,
            max_length=max_length,
            characters=ALPHABET_LOWERCASE_BASIC,
        ).title()

    @classmethod
    def mixedcase(cls, *, min_length: int = 1, max_length: int = 128) -> str:
        """
        Create a random string value with only mixedcase characters of length between `min_length` and `max_length`.

        Args:
            min_length (int, optional): Minimum length of the string. Must be >= 0. Defaults to 1.
            max_length (int, optional): Maximum length of the string. Must be >= 0 and >= `min_length`. Defaults to 128.

        Raises:
            TypeError: If `min_length` is not an integer.
            TypeError: If `max_length` is not an integer.
            ValueError: If `min_length` is less than 0.
            ValueError: If `max_length` is less than 0.
            ValueError: If `min_length` is greater than `max_length`.

        Returns:
            str: Random string with only mixedcase characters of length between `min_length` and `max_length`.

        Example:
        ```python
        from object_mother_pattern import StringMother

        string = StringMother.mixedcase(min_length=8, max_length=32)
        print(string)
        # >>> TfkrYRxUFTaEwZbC
        ```
        """
        return cls.create(
            min_length=min_length,
            max_length=max_length,
            characters=ALPHABET_LOWERCASE_BASIC + ALPHABET_UPPERCASE_BASIC,
        )

    @classmethod
    def of_length(cls, *, length: int) -> str:
        """
        Create a string value of a specific length, using all characters (lowercase, uppercase, and digits) of length
        `length`.

        Args:
            length (int): Length of the string. Must be >= 0.

        Raises:
            TypeError: If `length` is not an integer.
            ValueError: If `length` is less than 0.

        Returns:
            str: Random string value of a specific length of length `length`.

        Example:
        ```python
        from object_mother_pattern import StringMother

        string = StringMother.of_length(length=10)
        print(string)
        # >>> TfkrYRxUFT
        ```
        """
        return cls.create(min_length=length, max_length=length)

    @classmethod
    def alpha(cls, *, min_length: int = 1, max_length: int = 128) -> str:
        """
        Create a random string with only alphabetic characters (lowercase and uppercase, no digits or special
        characters) of length between `min_length` and `max_length`.

        Args:
            min_length (int, optional): Minimum length of the string. Must be >= 0. Defaults to 1.
            max_length (int, optional): Maximum length of the string. Must be >= 0 and >= `min_length`. Defaults to 128.

        Raises:
            TypeError: If `min_length` is not an integer.
            TypeError: If `max_length` is not an integer.
            ValueError: If `min_length` is less than 0.
            ValueError: If `max_length` is less than 0.
            ValueError: If `min_length` is greater than `max_length`.

        Returns:
            str: Random string with only alphabetic characters of length between `min_length` and `max_length`.

        Example:
        ```python
        from object_mother_pattern import StringMother

        string = StringMother.alpha(min_length=8, max_length=32)
        print(string)
        # >>> TfkrYRxUFTaEwZbC
        ```
        """
        return cls.create(
            min_length=min_length,
            max_length=max_length,
            characters=ALPHABET_LOWERCASE_BASIC + ALPHABET_UPPERCASE_BASIC,
        )

    @classmethod
    def alphanumeric(cls, *, min_length: int = 1, max_length: int = 128) -> str:
        """
        Create a random string value with only alphanumeric characters (lowercase, uppercase, and digits, no special
        characters) of length between `min_length` and `max_length`.

        Args:
            min_length (int, optional): Minimum length of the string. Must be >= 0. Defaults to 1.
            max_length (int, optional): Maximum length of the string. Must be >= 0 and >= `min_length`. Defaults to 128.

        Raises:
            TypeError: If `min_length` is not an integer.
            TypeError: If `max_length` is not an integer.
            ValueError: If `min_length` is less than 0.
            ValueError: If `max_length` is less than 0.
            ValueError: If `min_length` is greater than `max_length`.

        Returns:
            str: Random string with only alphanumeric characters of length between `min_length` and `max_length`.

        Example:
        ```python
        from object_mother_pattern import StringMother

        string = StringMother.alphanumeric(min_length=8, max_length=32)
        print(string)
        # >>> L1LTw68dgl8tSS0apNwGKMrwmh
        ```
        """
        return cls.create(min_length=min_length, max_length=max_length, characters=ALPHABET_BASIC)

    @classmethod
    def numeric(cls, *, min_length: int = 1, max_length: int = 128) -> str:
        """
        Create a random string with only numeric characters of length between `min_length` and `max_length`.

        Args:
            min_length (int, optional): Minimum length of the string. Must be >= 0. Defaults to 1.
            max_length (int, optional): Maximum length of the string. Must be >= 0 and >= `min_length`. Defaults to 128.

        Raises:
            TypeError: If `min_length` is not an integer.
            TypeError: If `max_length` is not an integer.
            ValueError: If `min_length` is less than 0.
            ValueError: If `max_length` is less than 0.
            ValueError: If `min_length` is greater than `max_length`.

        Returns:
            str: Random string with only numeric characters of length between `min_length` and `max_length`.

        Example:
        ```python
        from object_mother_pattern import StringMother

        string = StringMother.numeric(min_length=8, max_length=32)
        print(string)
        # >>> 715166264316
        ```
        """
        return cls.create(min_length=min_length, max_length=max_length, characters=DIGITS_BASIC)

    @classmethod
    def not_trimmed(cls, *, min_length: int = 2, max_length: int = 128) -> str:
        """
        Create a random string value of length between `min_length` and `max_length` (inclusive) that is not trimmed,
        it will include leading or trailing spaces, or both.

        Args:
            min_length (int, optional): Minimum length of the string. Must be >= 0. Defaults to 2.
            max_length (int, optional): Maximum length of the string. Must be >= 2 and >= `min_length`. Defaults to 128.

        Raises:
            TypeError: If `min_length` is not an integer.
            TypeError: If `max_length` is not an integer.
            ValueError: If `min_length` is less than 2.
            ValueError: If `max_length` is less than 2.
            ValueError: If `min_length` is greater than `max_length`.

        Returns:
            str: Random string value that is not trimmed.

        Example:
        ```python
        from object_mother_pattern import StringMother

        string = StringMother.not_trimmed(min_length=8, max_length=32)
        print(string)
        # >>>   TfkrYRxUFT
        ```
        """
        if type(min_length) is not int:
            raise TypeError('StringMother min_length must be an integer.')

        if type(max_length) is not int:
            raise TypeError('StringMother max_length must be an integer.')

        if min_length < 2:
            raise ValueError('StringMother min_length must be greater than or equal to 2.')

        if max_length < 2:
            raise ValueError('StringMother max_length must be greater than or equal to 2.')

        if min_length > max_length:
            raise ValueError('StringMother min_length must be less than or equal to max_length.')

        total_length = randint(a=min_length, b=max_length)  # noqa: S311
        total_spaces = randint(a=1, b=total_length - 1)  # noqa: S311
        leading_spaces = randint(a=0, b=total_spaces)  # noqa: S311
        trailing_spaces = total_spaces - leading_spaces

        core_length = total_length - total_spaces  # ≥ 1 by construction
        core_string = cls.create(min_length=core_length, max_length=core_length)

        return (' ' * leading_spaces) + core_string + (' ' * trailing_spaces)

    @classmethod
    def invalid_value(cls, *, length: int = 8) -> str:
        """
        Create an invalid string value.

        Args:
            length (int, optional): Length of the string. Must be >= 0. Defaults to 8.

        Raises:
            TypeError: If `length` is not an integer.
            ValueError: If `length` is less than 0.

        Returns:
            str: Invalid string.
        """
        if type(length) is not int:
            raise TypeError('StringMother length must be an integer.')

        if length < 0:
            raise ValueError('StringMother length must be greater than or equal to 0.')

        non_printable_chars = ''.join(chr(i) for i in range(0, 8))

        return ''.join(choice(seq=non_printable_chars) for _ in range(length))  # noqa: S311
