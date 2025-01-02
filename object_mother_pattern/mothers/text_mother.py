"""
TextMother module.
"""

from random import choice, randint
from sys import version_info

if version_info >= (3, 12):
    from typing import override  # pragma: no cover
else:
    from typing_extensions import override  # pragma: no cover

from object_mother_pattern.mothers.primitives.string_mother import StringMother


class TextMother(StringMother):
    """
    TextMother class.
    """

    @classmethod
    @override
    def create(cls, *, value: str | None = None, min_length: int = 1, max_length: int = 1024) -> str:  # noqa: C901
        """
        Create a random text between the min and max length, both inclusive.

        Args:
            min_length (int, optional): Minimum text length. Defaults to 1.
            max_length (int, optional): Maximum text length. Defaults to 1024.

        Raises:
            TypeError: If value is not a string.
            TypeError: If min_length is not an integer.
            TypeError: If max_length is not an integer.
            ValueError: If min_length is less than 0.
            ValueError: If max_length is less than 0.
            ValueError: If min_length is greater than max_length.

        Returns:
            str: The randomized text.
        """
        if value is not None and type(value) is not str:
            raise TypeError('TextMother value must be a string.')

        if type(min_length) is not int:
            raise TypeError('TextMother min_length must be an integer.')

        if type(max_length) is not int:
            raise TypeError('TextMother max_length must be an integer.')

        if min_length < 0:
            raise ValueError('TextMother min_length must be greater than or equal to 0.')

        if max_length < 0:
            raise ValueError('TextMother max_length must be greater than or equal to 0.')

        if min_length > max_length:
            raise ValueError('TextMother min_length must be less than or equal to max_length.')

        if value is not None:
            return value

        length = randint(a=min_length, b=max_length)
        if length == 0:
            return ''

        if length == 1:
            return '.'

        text = cls._random().text(max_nb_chars=20) if length < 5 else cls._random().text(max_nb_chars=length)
        while len(text) < length:
            text += cls._random().text(max_nb_chars=20) if length < 5 else cls._random().text(max_nb_chars=length)

        text = text[:length]
        text = text.replace('.', ' ')

        # Remove spaces at the end of the text due to the string cut
        if text[-2] == ' ':
            text = text[:-2] + cls._random().lexify(text='?') + text[-1]  # pragma: no cover

        text = text[:-1] + '.'

        return choice(seq=(text.lower(), text.upper(), text.title()))
