"""
DniMother module for Spanish National Identity Document (DNI).
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


class DniMother(BaseMother[str]):
    """
    DniMother class is responsible for creating valid Spanish National Identity Document (DNI) values. A valid Spanish
    DNI consists of 8 digits followed by a letter. The letter is calculated using a specific algorithm and serves as a
    validation check digit.

    Example:
    ```python
    from object_mother_pattern.mothers.identifiers.countries.spain import DniMother

    dni = DniMother.create()
    print(dni)
    # >>> 52714561X
    ```
    """

    _DNI_LETTERS: str = 'TRWAGMYFPDXBNJZSQVHLCKE'
    _MIN_NUMBER: int = 0
    _MAX_NUMBER: int = 99999999

    @classmethod
    @override
    def create(cls, *, value: str | None = None, string_case: StringCase | None = None) -> str:
        """
        Create a random valid Spanish DNI. If a specific DNI value is provided via `value`, it is returned after
        validation. Otherwise, a random valid DNI is generated.

        Args:
            value (str | None, optional): Specific DNI value to return. Defaults to None.
            string_case (StringCase | None, optional): The case of the DNI letter. Defaults to None (random case).

        Raises:
            TypeError: If the provided `value` is not a string.
            TypeError: If the provided `string_case` is not a StringCase.

        Returns:
            str: A valid Spanish DNI.

        Example:
        ```python
        from object_mother_pattern.mothers.identifiers.countries.spain import DniMother

        dni = DniMother.create()
        print(dni)
        # >>> 52714561X
        ```
        """
        if value is not None:
            if type(value) is not str:
                raise TypeError('DniMother value must be a string')

            return value

        if string_case is None:
            string_case = StringCase(value=choice(seq=tuple(StringCase)))  # noqa: S311

        if type(string_case) is not StringCase:
            raise TypeError('DniMother string_case must be a StringCase')

        number = randint(a=cls._MIN_NUMBER, b=cls._MAX_NUMBER)  # noqa: S311
        letter = cls._DNI_LETTERS[number % 23]

        match string_case:
            case StringCase.LOWERCASE:
                letter = letter.lower()

            case StringCase.UPPERCASE:
                letter = letter.upper()

            case StringCase.MIXEDCASE:
                letter = ''.join(choice(seq=(char.upper(), char.lower())) for char in letter)  # noqa: S311

            case _:  # pragma: no cover
                assert_never(string_case)

        return f'{number:08d}{letter}'

    @classmethod
    def invalid_value(cls) -> str:
        """
        Create an invalid DNI value.

        Returns:
            str: Invalid DNI string.
        """
        return StringMother.invalid_value()
