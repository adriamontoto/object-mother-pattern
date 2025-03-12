"""
StringMother module.
"""

from random import choice, randint
from sys import version_info

if version_info >= (3, 12):
    from typing import override  # pragma: no cover
else:
    from typing_extensions import override  # pragma: no cover

from object_mother_pattern.mothers.base_mother import BaseMother

from .utils.alphabets import (
    ALPHABET_BASIC,
    ALPHABET_LOWERCASE_BASIC,
    ALPHABET_UPPERCASE_BASIC,
    DIGITS_BASIC,
)


class StringMother(BaseMother[str]):
    """
    StringMother class.

    Example:
    ```python
    from object_mother_pattern.mothers import StringMother

    string = StringMother.create()
    print(string)
    # >>> 'zFUmlsODZqzwyGjrOOqBtYzNwlJdOETalkXbuSegoQpgEnYQTCDeoifWrTQXMm'
    ```
    """

    _type: type = str

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
        Create a random string value of length between min_length and max_length (inclusive) and using the provided
        characters. If a value is provided, it will be returned.

        Args:
            value (str | None, optional): String value. Defaults to None.
            min_length (int, optional): Minimum length of the string. Defaults to 1.
            max_length (int, optional): Maximum length of the string. Defaults to 128.
            characters (str, optional): Characters to use for the string. Defaults to ALPHABET_BASIC.

        Raises:
            TypeError: If value is not a string.
            TypeError: If min_length is not an integer.
            TypeError: If max_length is not an integer.
            ValueError: If min_length is less than 1.
            ValueError: If max_length is less than 1.
            ValueError: If min_length is greater than max_length.
            TypeError: If characters is not a string.
            ValueError: If characters is empty.

        Returns:
            str: Random string value.

        Example:
        ```python
        from object_mother_pattern.mothers import StringMother

        string = StringMother.create()
        print(string)
        # >>> 'zFUmlsODZqzwyGjrOOqBtYzNwlJdOETalkXbuSegoQpgEnYQTCDeoifWrTQXMm'
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

        if min_length < 1:
            raise ValueError('StringMother min_length must be greater than 0.')

        if max_length < 1:
            raise ValueError('StringMother max_length must be greater than 0.')

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
        """
        return ''

    @classmethod
    def lower(cls, *, min_length: int = 1, max_length: int = 128) -> str:
        """
        Create a random string value with only lowercase characters of length between min_length and max_length.

        Args:
            min_length (int, optional): Minimum length of the string. Defaults to 1.
            max_length (int, optional): Maximum length of the string. Defaults to 128.

        Raises:
            TypeError: If min_length is not an integer.
            TypeError: If max_length is not an integer.
            ValueError: If min_length is less than 1.
            ValueError: If max_length is less than 1.
            ValueError: If min_length is greater than max_length.

        Returns:
            str: Random string with only lowercase characters.

        Example:
        ```python
        from object_mother_pattern.mothers import StringMother

        string = StringMother.lower(min_length=8, max_length=32)
        print(string)
        # >>> 'tfkryxuftaewzbc'
        ```
        """
        return cls.create(min_length=min_length, max_length=max_length, characters=ALPHABET_LOWERCASE_BASIC)

    @classmethod
    def upper(cls, *, min_length: int = 1, max_length: int = 128) -> str:
        """
        Create a random string value with only uppercase characters of length between min_length and max_length.

        Args:
            min_length (int, optional): Minimum length of the string. Defaults to 1.
            max_length (int, optional): Maximum length of the string. Defaults to 128.

        Raises:
            TypeError: If min_length is not an integer.
            TypeError: If max_length is not an integer.
            ValueError: If min_length is less than 1.
            ValueError: If max_length is less than 1.
            ValueError: If min_length is greater than max_length.

        Returns:
            str: Random string with only uppercase characters.

        Example:
        ```python
        from object_mother_pattern.mothers import StringMother

        string = StringMother.upper(min_length=8, max_length=32)
        print(string)
        # >>> 'TFRYXUFTAEWZBC'
        ```
        """
        return cls.create(min_length=min_length, max_length=max_length, characters=ALPHABET_UPPERCASE_BASIC)

    @classmethod
    def of_length(cls, *, length: int) -> str:
        """
        Create a string value of a specific length, using all characters (lowercase, uppercase, and digits).

        Args:
            length (int): Length of the string.

        Raises:
            TypeError: If length is not a string.
            ValueError: If length is less than 1.

        Returns:
            str: Random string value of a specific length.

        Example:
        ```python
        from object_mother_pattern.mothers import StringMother

        string = StringMother.of_length(length=10)
        print(string)
        # >>> 'TfkrYRxUFT'
        ```
        """
        return cls.create(min_length=length, max_length=length)

    @classmethod
    def alpha(cls, *, min_length: int = 1, max_length: int = 128) -> str:
        """
        Create a random string with only alphabetic characters (lowercase and uppercase, no digits or special
        characters) of length between min_length and max_length.

        Args:
            min_length (int, optional): Minimum length of the string. Defaults to 1.
            max_length (int, optional): Maximum length of the string. Defaults to 128.

        Raises:
            TypeError: If min_length is not an integer.
            TypeError: If max_length is not an integer.
            ValueError: If min_length is less than 1.
            ValueError: If max_length is less than 1.
            ValueError: If min_length is greater than max_length.

        Returns:
            str: Random string with only alphabetic characters.

        Example:
        ```python
        from object_mother_pattern.mothers import StringMother

        string = StringMother.alpha(min_length=8, max_length=32)
        print(string)
        # >>> 'TfkrYRxUFTaEwZbC'
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
        characters) of length between min_length and max_length.

        Args:
            min_length (int, optional): Minimum length of the string. Defaults to 1.
            max_length (int, optional): Maximum length of the string. Defaults to 128.

        Raises:
            TypeError: If min_length is not an integer.
            TypeError: If max_length is not an integer.
            ValueError: If min_length is less than 1.
            ValueError: If max_length is less than 1.
            ValueError: If min_length is greater than max_length.

        Returns:
            str: Random string with only alphanumeric characters.

        Example:
        ```python
        from object_mother_pattern.mothers import StringMother

        string = StringMother.alphanumeric(min_length=8, max_length=32)
        print(string)
        # >>> 'L1LTw68dgl8tSS0apNwGKMrwmh'
        ```
        """
        return cls.create(min_length=min_length, max_length=max_length, characters=ALPHABET_BASIC)

    # TODO:
    @classmethod
    def base32(cls, *, min_length: int = 1, max_length: int = 128) -> str:
        """
        Create a random string with only base32 characters `abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ234567`
        of length between min_length and max_length.

        Args:
            min_length (int, optional): Minimum length of the string. Defaults to 1.
            max_length (int, optional): Maximum length of the string. Defaults to 128.

        Raises:
            TypeError: If min_length is not an integer.
            TypeError: If max_length is not an integer.
            ValueError: If min_length is less than 1.
            ValueError: If max_length is less than 1.
            ValueError: If min_length is greater than max_length.

        Returns:
            str: Random string with only base32 characters.

        Example:
        ```python
        from object_mother_pattern.mothers import StringMother

        string = StringMother.base32(min_length=8, max_length=32)
        print(string)
        # >>> 'rR6axEdGpVfjdPhYIGBOzBY'
        ```
        """
        raise NotImplementedError()

    # TODO:
    @classmethod
    def base56(cls, *, min_length: int = 1, max_length: int = 128) -> str:
        """
        Create a random string with only base56 characters `abcdefghijkmnpqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ23456789`
        of length between min_length and max_length.

        Args:
            min_length (int, optional): Minimum length of the string. Defaults to 1.
            max_length (int, optional): Maximum length of the string. Defaults to 128.

        Raises:
            TypeError: If min_length is not an integer.
            TypeError: If max_length is not an integer.
            ValueError: If min_length is less than 1.
            ValueError: If max_length is less than 1.
            ValueError: If min_length is greater than max_length.

        Returns:
            str: Random string with only base56 characters.

        Example:
        ```python
        from object_mother_pattern.mothers import StringMother

        string = StringMother.base56(min_length=8, max_length=32)
        print(string)
        # >>> 'UFyTHGQz'
        ```
        """
        raise NotImplementedError()

    # TODO:
    @classmethod
    def base58(cls, *, min_length: int = 1, max_length: int = 128) -> str:
        """
        Create a random string with only base58 characters `abcdefghijkmnopqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ123456789`
        of length between min_length and max_length.

        Args:
            min_length (int, optional): Minimum length of the string. Defaults to 1.
            max_length (int, optional): Maximum length of the string. Defaults to 128.

        Raises:
            TypeError: If min_length is not an integer.
            TypeError: If max_length is not an integer.
            ValueError: If min_length is less than 1.
            ValueError: If max_length is less than 1.
            ValueError: If min_length is greater than max_length.

        Returns:
            str: Random string with only base58 characters.

        Example:
        ```python
        from object_mother_pattern.mothers import StringMother

        string = StringMother.base58(min_length=8, max_length=32)
        print(string)
        # >>> 'X2S3nqEykSPBHLVvV'
        ```
        """
        raise NotImplementedError()

    # TODO:
    @classmethod
    def base64(cls, *, min_length: int = 1, max_length: int = 128) -> str:
        """
        Create a random string with only base64 characters
        `abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789+/` of length between min_length and max_length.
        It can include one or two `=` characters at the end.

        Args:
            min_length (int, optional): Minimum length of the string. Defaults to 1.
            max_length (int, optional): Maximum length of the string. Defaults to 128.

        Raises:
            TypeError: If min_length is not an integer.
            TypeError: If max_length is not an integer.
            ValueError: If min_length is less than 1.
            ValueError: If max_length is less than 1.
            ValueError: If min_length is greater than max_length.

        Returns:
            str: Random string with only base64 characters.

        Example:
        ```python
        from object_mother_pattern.mothers import StringMother

        string = StringMother.base64(min_length=8, max_length=32)
        print(string)
        # >>> 'bg8+/izreZ=='
        ```
        """
        raise NotImplementedError()

    @classmethod
    def digit(cls, *, min_length: int = 1, max_length: int = 128) -> str:
        """
        Create a random string with only digit characters of length between min_length and max_length.

        Args:
            min_length (int, optional): Minimum length of the string. Defaults to 1.
            max_length (int, optional): Maximum length of the string. Defaults to 128.

        Raises:
            TypeError: If min_length is not an integer.
            TypeError: If max_length is not an integer.
            ValueError: If min_length is less than 1.
            ValueError: If max_length is less than 1.
            ValueError: If min_length is greater than max_length.

        Returns:
            str: Random string with only digit characters.

        Example:
        ```python
        from object_mother_pattern.mothers import StringMother

        string = StringMother.digit(min_length=8, max_length=32)
        print(string)
        # >>> '9583332687'
        ```
        """
        return cls.create(min_length=min_length, max_length=max_length, characters=DIGITS_BASIC)

    # TODO:
    @classmethod
    def hexadecimal(cls, *, min_length: int = 1, max_length: int = 128, include_prefix: bool | None = None) -> str:
        """
        Create a random string with only hexadecimal characters `abcdefABCDEF0123456789` of length between min_length
        and max_length. If include_prefix is True, the `0x` or `0X` prefix will be included. If include_prefix is
        False, the prefix will not be included. If include_prefix is None, the prefix may or may not be included.

        Args:
            min_length (int, optional): Minimum length of the string. Defaults to 1.
            max_length (int, optional): Maximum length of the string. Defaults to 128.
            include_prefix (bool | None, optional): Include the `0x` or `0X` prefix. Defaults to None.

        Raises:
            TypeError: If include_prefix is not a boolean or None.
            TypeError: If min_length is not an integer.
            TypeError: If max_length is not an integer.
            ValueError: If min_length is less than 1.
            ValueError: If max_length is less than 1.
            ValueError: If min_length is greater than max_length.

        Returns:
            str: Random string with only hexadecimal characters.

        Example:
        ```python
        from object_mother_pattern.mothers import StringMother

        string = StringMother.hexadecimal(min_length=8, max_length=32)
        print(string)
        # >>> '0x5781ebb1caf8'
        ```
        """
        raise NotImplementedError()

    # TODO:
    @classmethod
    def printable(cls, *, min_length: int = 1, max_length: int = 128) -> str:
        """
        Create a random string value of length between min_length and max_length (inclusive) that is printable.

        Args:
            min_length (int, optional): Minimum length of the string. Defaults to 1.
            max_length (int, optional): Maximum length of the string. Defaults to 128.

        Raises:
            TypeError: If min_length is not an integer.
            TypeError: If max_length is not an integer.
            ValueError: If min_length is less than 1.
            ValueError: If max_length is less than 1.
            ValueError: If min_length is greater than max_length.

        Returns:
            str: Random string value that is printable.

        Example:
        ```python
        from object_mother_pattern.mothers import StringMother

        string = StringMother.printable(min_length=8, max_length=32)
        print(string)
        # >>> 'TfkrYRxUFTaEwZbC'
        ```
        """
        raise NotImplementedError()

    # TODO:
    @classmethod
    def not_trimmed(cls, *, min_length: int = 1, max_length: int = 128) -> str:
        """
        Create a random string value of length between min_length and max_length (inclusive) that is not trimmed, it
        can include leading and trailing spaces.

        Args:
            min_length (int, optional): Minimum length of the string. Defaults to 1.
            max_length (int, optional): Maximum length of the string. Defaults to 128.

        Raises:
            TypeError: If min_length is not an integer.
            TypeError: If max_length is not an integer.
            ValueError: If min_length is less than 1.
            ValueError: If max_length is less than 1.
            ValueError: If min_length is greater than max_length.

        Returns:
            str: Random string value that is not trimmed.

        Example:
        ```python
        from object_mother_pattern.mothers import StringMother

        string = StringMother.not_trimmed(min_length=8, max_length=32)
        print(string)
        # >>> '  TfkrYRxUFT'
        ```
        """
        raise NotImplementedError()

    @classmethod
    def invalid_value(cls) -> str:
        """
        Create an invalid string value.

        Returns:
            str: Invalid string.
        """
        non_printable_chars = ''.join(chr(i) for i in range(32))
        return ''.join(choice(seq=non_printable_chars) for _ in range(10))  # noqa: S311
