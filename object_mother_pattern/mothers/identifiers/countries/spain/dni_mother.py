"""
DniMother module for Spanish National Identity Document (DNI).
"""

from enum import StrEnum, unique
from random import choice, randint
from sys import version_info
from typing import assert_never

if version_info >= (3, 12):
    from typing import override  # pragma: no cover
else:
    from typing_extensions import override  # pragma: no cover

from object_mother_pattern.mothers import BaseMother, StringMother


@unique
class DniCase(StrEnum):
    """
    Type of DNI letter cases.
    """

    LOWERCASE = 'lowercase'
    UPPERCASE = 'uppercase'


class DniMother(BaseMother[str]):
    """
    DniMother class is responsible for creating valid Spanish National Identity Document (DNI) values.

    A valid Spanish DNI consists of 8 digits followed by a letter. The letter is calculated using
    a specific algorithm and serves as a validation check digit.

    Example:
    ```python
    from object_mother_pattern.mothers.identifiers.countries.spain import DniMother

    dni = DniMother.create()
    print(dni)
    # >>> 52714561X
    ```
    """

    _type: type = str
    _DNI_LETTERS: str = 'TRWAGMYFPDXBNJZSQVHLCKE'
    _MIN_NUMBER: int = 0
    _MAX_NUMBER: int = 99999999

    @classmethod
    @override
    def create(cls, *, value: str | None = None, dni_case: DniCase | None = None) -> str:
        """
        Create a random valid Spanish DNI. If a specific DNI value is provided via `value`, it is returned after
        validation. Otherwise, a random valid DNI is generated.

        Args:
            value (str | None, optional): Specific DNI value to return. Defaults to None.
            dni_case (DniCase | None, optional): The case of the DNI letter. Defaults to None (random case).

        Raises:
            TypeError: If the provided `value` is not a string.
            TypeError: If the provided `dni_case` is not a DniCase.

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

        if dni_case is None:
            dni_case = DniCase(value=choice(seq=tuple(DniCase)))  # noqa: S311

        if type(dni_case) is not DniCase:
            raise TypeError('DniMother dni_case must be a DniCase')

        number = randint(a=cls._MIN_NUMBER, b=cls._MAX_NUMBER)  # noqa: S311
        letter = cls._DNI_LETTERS[number % 23]

        match dni_case:
            case DniCase.LOWERCASE:
                letter = letter.lower()

            case DniCase.UPPERCASE:
                letter = letter.upper()

            case _:  # pragma: no cover
                assert_never(dni_case)

        return f'{number:08d}{letter}'

    @classmethod
    def invalid_value(cls) -> str:
        """
        Create an invalid DNI value.

        Returns:
            str: Invalid DNI string.
        """
        return StringMother.invalid_value()
