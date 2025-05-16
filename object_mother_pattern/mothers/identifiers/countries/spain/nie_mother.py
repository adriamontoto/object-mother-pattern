"""
NieMother module for Spanish Foreign Identity Number (NIE).
"""

from enum import StrEnum, unique
from random import choice, randint
from sys import version_info
from typing import ClassVar, assert_never

if version_info >= (3, 12):
    from typing import override  # pragma: no cover
else:
    from typing_extensions import override  # pragma: no cover

from object_mother_pattern.mothers import BaseMother, StringMother


@unique
class NieCase(StrEnum):
    """
    Type of NIE letter cases.
    """

    LOWERCASE = 'lowercase'
    UPPERCASE = 'uppercase'
    MIXEDCASE = 'mixedcase'


class NieMother(BaseMother[str]):
    """
    NieMother class is responsible for creating valid Spanish Foreign Identity Number (NIE) values. A valid Spanish NIE
    consists of an initial letter (X, Y, or Z), followed by 7 digits, and a final check letter. The check letter is
    calculated using the same algorithm as the DNI.

    Example:
    ```python
    from object_mother_pattern.mothers.identifiers.countries.spain import NieMother

    nie = NieMother.create()
    print(nie)
    # >>> X1234567L
    ```
    """

    _type: type = str
    _NIE_LETTERS: str = 'TRWAGMYFPDXBNJZSQVHLCKE'
    _NIE_PREFIXES: ClassVar[dict[str, int]] = {'X': 0, 'Y': 1, 'Z': 2}
    _MIN_NUMBER: int = 0
    _MAX_NUMBER: int = 9999999

    @classmethod
    @override
    def create(cls, *, value: str | None = None, nie_case: NieCase | None = None) -> str:
        """
        Create a random valid Spanish NIE. If a specific NIE value is provided via `value`,
        it is returned after validation. Otherwise, a random valid NIE is generated.

        Args:
            value (str | None, optional): Specific NIE value to return. Defaults to None.
            nie_case (NieCase | None, optional): The case of the NIE letters. Defaults to None (random case).

        Raises:
            TypeError: If the provided `value` is not a string.
            TypeError: If the provided `nie_case` is not a NieCase.

        Returns:
            str: A valid Spanish NIE.

        Example:
        ```python
        from object_mother_pattern.mothers.identifiers.countries.spain import NieMother

        nie = NieMother.create()
        print(nie)
        # >>> X1234567L
        ```
        """
        if value is not None:
            if type(value) is not str:
                raise TypeError('NieMother value must be a string')

            return value

        if nie_case is None:
            nie_case = NieCase(value=choice(seq=tuple(NieCase)))  # noqa: S311

        if type(nie_case) is not NieCase:
            raise TypeError('NieMother nie_case must be a NieCase')

        prefix = choice(seq=tuple(cls._NIE_PREFIXES.keys()))  # noqa: S311
        prefix_num = cls._NIE_PREFIXES[prefix]
        number = randint(a=cls._MIN_NUMBER, b=cls._MAX_NUMBER)  # noqa: S311
        letter = cls._NIE_LETTERS[(prefix_num * 10000000 + number) % 23]

        nie = f'{prefix}{number:07d}{letter}'
        match nie_case:
            case NieCase.LOWERCASE:
                nie = nie.lower()

            case NieCase.UPPERCASE:
                nie = nie.upper()

            case NieCase.MIXEDCASE:
                nie = ''.join(choice(seq=(char.upper(), char.lower())) for char in nie)  # noqa: S311

            case _:  # pragma: no cover
                assert_never(nie_case)

        return nie

    @classmethod
    def invalid_value(cls) -> str:
        """
        Create an invalid NIE value.

        Returns:
            str: Invalid NIE string.
        """
        return StringMother.invalid_value()
