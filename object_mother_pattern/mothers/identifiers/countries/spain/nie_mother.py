"""
NieMother module for Spanish Foreign Identity Number (NIE).
"""

from sys import version_info

if version_info >= (3, 12):
    from typing import override  # pragma: no cover
else:
    from typing_extensions import override  # pragma: no cover

from random import choice, randint
from typing import ClassVar, assert_never

from object_mother_pattern.models import BaseMother
from object_mother_pattern.mothers import StringCase
from object_mother_pattern.mothers.primitives.string_mother import StringMother


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

    _NIE_LETTERS: str = 'TRWAGMYFPDXBNJZSQVHLCKE'
    _NIE_PREFIXES: ClassVar[dict[str, int]] = {'X': 0, 'Y': 1, 'Z': 2}
    _MIN_NUMBER: int = 0
    _MAX_NUMBER: int = 9999999

    @classmethod
    @override
    def create(cls, *, value: str | None = None, string_case: StringCase | None = None) -> str:
        """
        Create a random valid Spanish NIE. If a specific NIE value is provided via `value`,
        it is returned after validation. Otherwise, a random valid NIE is generated.

        Args:
            value (str | None, optional): Specific NIE value to return. Defaults to None.
            string_case (StringCase | None, optional): The case of the NIE letters. Defaults to None (random case).

        Raises:
            TypeError: If the provided `value` is not a string.
            TypeError: If the provided `string_case` is not a StringCase.

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

        if string_case is None:
            string_case = StringCase(value=choice(seq=tuple(StringCase)))  # noqa: S311

        if type(string_case) is not StringCase:
            raise TypeError('NieMother string_case must be a StringCase')

        prefix = choice(seq=tuple(cls._NIE_PREFIXES.keys()))  # noqa: S311
        prefix_num = cls._NIE_PREFIXES[prefix]
        number = randint(a=cls._MIN_NUMBER, b=cls._MAX_NUMBER)  # noqa: S311
        letter = cls._NIE_LETTERS[(prefix_num * 10000000 + number) % 23]

        nie = f'{prefix}{number:07d}{letter}'
        match string_case:
            case StringCase.LOWERCASE:
                nie = nie.lower()

            case StringCase.UPPERCASE:
                nie = nie.upper()

            case StringCase.MIXEDCASE:
                nie = ''.join(choice(seq=(char.upper(), char.lower())) for char in nie)  # noqa: S311

            case _:  # pragma: no cover
                assert_never(string_case)

        return nie

    @classmethod
    def invalid_value(cls) -> str:
        """
        Create an invalid NIE value.

        Returns:
            str: Invalid NIE string.
        """
        return StringMother.invalid_value()
