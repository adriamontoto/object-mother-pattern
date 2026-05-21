"""
NifMother module for Spanish company NIF values.
"""

from sys import version_info

if version_info >= (3, 12):
    from typing import override  # pragma: no cover
else:
    from typing_extensions import override  # pragma: no cover


from random import choice
from typing import ClassVar, assert_never

from object_mother_pattern.models import BaseMother
from object_mother_pattern.mothers import StringCase
from object_mother_pattern.mothers.primitives.string_mother import StringMother


class NifMother(BaseMother[str]):
    """
    NifMother class is responsible for creating valid Spanish company NIF values.

    Example:
    ```python
    from object_mother_pattern.mothers.identifiers.countries.spain import NifMother

    nif = NifMother.create()
    print(nif)
    # >>> A58818501
    ```
    """

    _CONTROL_LETTERS: str = 'JABCDEFGHI'
    _DIGIT_CONTROL_FIRST_LETTERS: ClassVar[tuple[str, ...]] = ('A', 'B', 'E', 'H')
    _LETTER_CONTROL_FIRST_LETTERS: ClassVar[tuple[str, ...]] = ('P', 'Q', 'S')
    _DIGIT_OR_LETTER_CONTROL_FIRST_LETTERS: ClassVar[tuple[str, ...]] = (
        'C',
        'D',
        'F',
        'G',
        'J',
        'N',
        'R',
        'U',
        'V',
        'W',
    )
    _FIRST_LETTERS: ClassVar[tuple[str, ...]] = (
        *_DIGIT_CONTROL_FIRST_LETTERS,
        *_LETTER_CONTROL_FIRST_LETTERS,
        *_DIGIT_OR_LETTER_CONTROL_FIRST_LETTERS,
    )

    @classmethod
    @override
    def create(
        cls,
        *,
        value: str | None = None,
        string_case: StringCase | None = None,
        first_letter: str | None = None,
    ) -> str:
        """
        Create a random valid Spanish company NIF.

        Args:
            value (str | None, optional): Specific NIF value to return. Defaults to None.
            string_case (StringCase | None, optional): Case of NIF letters. Defaults to None.
            first_letter (str | None, optional): Entity type first letter to use. Defaults to None.

        Raises:
            TypeError: If the provided `value` is not a string.
            TypeError: If `string_case` is not a StringCase.
            TypeError: If `first_letter` is not a string.
            ValueError: If `first_letter` is not a valid NIF first letter.

        Returns:
            str: A valid Spanish company NIF.

        Example:
        ```python
        from object_mother_pattern.mothers.identifiers.countries.spain import NifMother

        nif = NifMother.create(first_letter='A')
        print(nif)
        # >>> A58818501
        ```
        """
        if value is not None:
            if type(value) is not str:
                raise TypeError('NifMother value must be a string.')

            return value

        string_case = cls._string_case(string_case=string_case)
        first_letter = cls._first_letter(first_letter=first_letter)
        number = StringMother.numeric(min_length=7, max_length=7)
        nif = f'{first_letter}{number}{cls._control_character(first_letter=first_letter, number=number)}'

        return cls._render_case(value=nif, string_case=string_case)

    @classmethod
    def _string_case(cls, *, string_case: StringCase | None) -> StringCase:
        """
        Resolve and validate the requested NIF string case.

        Args:
            string_case (StringCase | None): Requested string case.

        Raises:
            TypeError: If `string_case` is not a StringCase.

        Returns:
            StringCase: Resolved string case.
        """
        if string_case is None:
            string_case = StringCase(value=choice(seq=tuple(StringCase)))  # noqa: S311

        if type(string_case) is not StringCase:
            raise TypeError('NifMother string_case must be a StringCase.')

        return string_case

    @classmethod
    def _first_letter(cls, *, first_letter: str | None) -> str:
        """
        Resolve and validate the NIF entity type first letter.

        Args:
            first_letter (str | None): Requested first letter.

        Raises:
            TypeError: If `first_letter` is not a string.
            ValueError: If `first_letter` is not a valid NIF first letter.

        Returns:
            str: Resolved uppercase first letter.
        """
        if first_letter is None:
            first_letter = choice(seq=cls._FIRST_LETTERS)  # noqa: S311

        if type(first_letter) is not str:
            raise TypeError('NifMother first_letter must be a string.')

        first_letter = first_letter.upper()
        if first_letter not in cls._FIRST_LETTERS:
            raise ValueError('NifMother first_letter must be a valid Spanish company NIF first letter.')

        return first_letter

    @classmethod
    def _control_character(cls, *, first_letter: str, number: str) -> str:
        """
        Calculate the NIF control character for the provided first letter and number.

        Args:
            first_letter (str): NIF first letter.
            number (str): Seven-digit NIF number section.

        Returns:
            str: NIF control character.
        """
        total = sum(
            (
                sum(divmod(int(digit) * 2, 10)),
                int(digit),
            )[index % 2]
            for index, digit in enumerate(number)
        )
        control_value = (10 - total % 10) % 10
        control_digit = str(control_value)
        control_letter = cls._CONTROL_LETTERS[control_value]

        if first_letter in cls._DIGIT_CONTROL_FIRST_LETTERS:
            control_character = control_digit

        elif first_letter in cls._LETTER_CONTROL_FIRST_LETTERS:
            control_character = control_letter

        else:
            control_character = choice(seq=(control_digit, control_letter))  # noqa: S311

        return control_character

    @classmethod
    def _render_case(cls, *, value: str, string_case: StringCase) -> str:
        """
        Render the NIF value using the requested string case.

        Args:
            value (str): NIF value to render.
            string_case (StringCase): Requested string case.

        Returns:
            str: Rendered NIF value.
        """
        match string_case:
            case StringCase.LOWERCASE:
                value = value.lower()

            case StringCase.UPPERCASE:
                value = value.upper()

            case StringCase.MIXEDCASE:
                value = ''.join(choice(seq=(char.upper(), char.lower())) for char in value)  # noqa: S311

            case _:  # pragma: no cover
                assert_never(string_case)

        return value

    @classmethod
    def invalid_value(cls) -> str:
        """
        Create an invalid Spanish company NIF value.

        Returns:
            str: Invalid Spanish company NIF string.
        """
        return StringMother.invalid_value()
