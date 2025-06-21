"""
TextMother module.
"""

from sys import version_info

if version_info >= (3, 12):
    from typing import override  # pragma: no cover
else:
    from typing_extensions import override  # pragma: no cover

from random import choice, randint
from typing import assert_never

from object_mother_pattern.models import BaseMother
from object_mother_pattern.mothers import StringCase
from object_mother_pattern.mothers.primitives.string_mother import StringMother


class TextMother(BaseMother[str]):
    """
    TextMother class is responsible for creating random text values.

    Example:
    ```python
    from object_mother_pattern.mothers.extra import TextMother

    text = TextMother.create()
    print(text)
    # >>> Policy Writer Media Something  Drug Television Blue Buy
    # >>> Less Explain Most Recently Movie  Less Try Board Care Would
    # >>> Would Stuff Thought Keep Mention Fast Government  Note Some Process
    # >>> Official Experience Risk Hair  Either Oil Could Also Physical
    # >>> College Anything Current Tell Mrs Mrs Station
    # >>> Network Leader Wide Language  Fall Water Cover Yes
    # >>> Second Remain If Hit  Evening Money Person Four
    # >>> Without Cultural Community  Expert Blood Effect Picture Fly Laugh Seek
    # >>> Data Off Late Usually Chair Well Situation  Wish Carry Traditional Involve Left Set Car
    # >>> Show Security Build Two Approach Situation Good Page Magazine Process Tablek.
    ```
    """

    @classmethod
    @override
    def create(  # noqa: C901
        cls,
        *,
        value: str | None = None,
        min_length: int = 1,
        max_length: int = 1024,
        string_case: StringCase | None = None,
    ) -> str:
        """
        Create a random text. If a specific text value is provided via `value`, it is returned after
        validation. Otherwise, a random string value is generated with the provided `min_length`, `max_length` (both
        included). If `string_case` is None, a random case is chosen from the available StringCase options.

        Args:
            value (str | None, optional): Text value. Defaults to None.
            min_length (int, optional): Minimum length of the text. Must be >= 1. Defaults to 1.
            max_length (int, optional): Maximum length of the text. Must be >= 1 and >= `min_length`. Defaults to 1024.
            string_case (StringCase | None, optional): The case of the text. Defaults to None.

        Raises:
            TypeError: If `value` is not a string.
            TypeError: If `min_length` is not an integer.
            TypeError: If `max_length` is not an integer.
            ValueError: If `min_length` is less than 1.
            ValueError: If `max_length` is less than 1.
            ValueError: If `min_length` is greater than `max_length`.
            TypeError: If `string_case` is not a StringCase.

        Returns:
            str: Random text value of length between `min_length` and `max_length` (inclusive).

        Example:
        ```python
        from object_mother_pattern.mothers.extra import TextMother

        text = TextMother.create()
        print(text)
        # >>> Policy Writer Media Something  Drug Television Blue Buy
        # >>> Less Explain Most Recently Movie  Less Try Board Care Would
        # >>> Would Stuff Thought Keep Mention Fast Government  Note Some Process
        # >>> Official Experience Risk Hair  Either Oil Could Also Physical
        # >>> College Anything Current Tell Mrs Mrs Station
        # >>> Network Leader Wide Language  Fall Water Cover Yes
        # >>> Second Remain If Hit  Evening Money Person Four
        # >>> Without Cultural Community  Expert Blood Effect Picture Fly Laugh Seek
        # >>> Data Off Late Usually Chair Well Situation  Wish Carry Traditional Involve Left Set Car
        # >>> Show Security Build Two Approach Situation Good Page Magazine Process Tablek.
        ```
        """
        if value is not None:
            if type(value) is not str:
                raise TypeError('TextMother value must be a string.')

            return value

        if type(min_length) is not int:
            raise TypeError('TextMother min_length must be an integer.')

        if type(max_length) is not int:
            raise TypeError('TextMother max_length must be an integer.')

        if min_length < 1:
            raise ValueError('TextMother min_length must be greater than or equal to 1.')

        if max_length < 1:
            raise ValueError('TextMother max_length must be greater than or equal to 1.')

        if min_length > max_length:
            raise ValueError('TextMother min_length must be less than or equal to max_length.')

        if string_case is None:
            string_case = StringCase(value=choice(seq=tuple(StringCase)))  # noqa: S311

        if type(string_case) is not StringCase:
            raise TypeError('TextMother string_case must be a StringCase.')

        length = randint(a=min_length, b=max_length)  # noqa: S311

        text = cls._random().text(max_nb_chars=20) if length < 5 else cls._random().text(max_nb_chars=length)
        while len(text) < length:
            text += cls._random().text(max_nb_chars=20) if length < 5 else cls._random().text(max_nb_chars=length)

        text = text[:length]

        # Remove spaces at the end of the text due to the string cut
        if length > 1 and text[-2] == ' ':
            text = text[:-2] + cls._random().lexify(text='?') + text[-1]  # pragma: no cover

        text = text[:-1] + '.'

        match string_case:
            case StringCase.LOWERCASE:
                text = text.lower()

            case StringCase.UPPERCASE:
                text = text.upper()

            case StringCase.MIXEDCASE:
                text = ''.join(choice(seq=(char.upper(), char.lower())) for char in text)  # noqa: S311

            case _:  # pragma: no cover
                assert_never(string_case)

        return text  # noqa: S311

    @classmethod
    def empty(cls) -> str:
        """
        Create an empty string value.

        Returns:
            str: Empty string.

        Example:
        ```python
        from object_mother_pattern.mothers import StringMother

        string = StringMother.empty()
        print(string)
        # >>>
        ```
        """
        return ''

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
        from object_mother_pattern.mothers.extra import TextMother

        text = TextMother.of_length(length=10)
        print(text)
        # >>> SOUTHERNT.
        ```
        """
        return cls.create(min_length=length, max_length=length)

    @classmethod
    def invalid_value(cls) -> str:
        """
        Create an invalid text value.

        Returns:
            str: Invalid text string.
        """
        return StringMother.invalid_value()
