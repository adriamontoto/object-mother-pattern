"""
StringMother module.
"""

from random import choice
from sys import version_info

if version_info >= (3, 12):
    from typing import override  # pragma: no cover
else:
    from typing_extensions import override  # pragma: no cover

from object_mother_pattern.mothers.base_mother import BaseMother


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
    def create(cls, *, value: str | None = None, min_length: int = 1, max_length: int = 128) -> str:
        """
        Create a random string value.

        Args:
            value (str | None, optional): String value. Defaults to None.

        Raises:
            TypeError: If value is not a string.
            TypeError: If min_length is not an integer.
            TypeError: If max_length is not an integer.
            ValueError: If min_length is less than 1.
            ValueError: If max_length is less than 1.
            ValueError: If min_length is greater than max_length.

        Returns:
            str: Random string.

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

        return cls._random().pystr(min_chars=min_length, max_chars=max_length)

    @classmethod
    def of_length(cls, *, length: int) -> str:
        """
        Create a string of a specific length.

        Args:
            length (int): Length of the string.

        Raises:
            TypeError: If length is not a string.
            ValueError: If length is less than 1.

        Returns:
            str: String of a specific length.

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
    def invalid_value(cls) -> str:
        """
        Create an invalid string value.

        Returns:
            str: Invalid string.
        """
        non_printable_chars = ''.join(chr(i) for i in range(32))

        return ''.join(choice(seq=non_printable_chars) for _ in range(10))
