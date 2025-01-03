"""
NameMother module.
"""

from random import choice, randint
from sys import version_info

if version_info >= (3, 12):
    from typing import override  # pragma: no cover
else:
    from typing_extensions import override  # pragma: no cover

from object_mother_pattern.mothers.primitives.string_mother import StringMother


class NameMother(StringMother):
    """
    NameMother class.
    """

    @classmethod
    @override
    def create(cls, *, value: str | None = None, min_length: int = 3, max_length: int = 128) -> str:
        """
        Create a random name between the min and max length, both inclusive.

        Args:
            min_length (int, optional): Minimum name length. Defaults to 3.
            max_length (int, optional): Maximum name length. Defaults to 128.

        Raises:
            TypeError: If value is not a string.
            TypeError: If min_length is not an integer.
            TypeError: If max_length is not an integer.
            ValueError: If min_length is less than 3.
            ValueError: If max_length is less than 3.
            ValueError: If min_length is greater than max_length.

        Returns:
            str: The randomized name.
        """
        if value is not None and type(value) is not str:
            raise TypeError('NameMother value must be a string.')

        if type(min_length) is not int:
            raise TypeError('NameMother min_length must be an integer.')

        if type(max_length) is not int:
            raise TypeError('NameMother max_length must be an integer.')

        if min_length < 3:
            raise ValueError('NameMother min_length must be greater than or equal to 3.')

        if max_length < 3:
            raise ValueError('NameMother max_length must be greater than or equal to 3.')

        if min_length > max_length:
            raise ValueError('NameMother min_length must be less than or equal to max_length.')

        if value is not None:
            return value

        length = randint(a=min_length, b=max_length)

        name = cls._random().name()
        while len(name) < length:
            name += cls._random().name()  # pragma: no cover

        name = name[:length]
        if name != name.strip():
            name = name[:-1] + cls._random().lexify(text='?')  # pragma: no cover

        return choice(seq=(name.lower(), name.upper(), name.title()))
