"""
PassportMother module for Spanish passport values.
"""

from sys import version_info

if version_info >= (3, 12):
    from typing import override  # pragma: no cover
else:
    from typing_extensions import override  # pragma: no cover


from random import choice
from typing import assert_never

from object_mother_pattern.models import BaseMother
from object_mother_pattern.mothers import StringCase
from object_mother_pattern.mothers.primitives.string_mother import StringMother


class PassportMother(BaseMother[str]):
    """
    PassportMother class is responsible for creating valid Spanish passport values.

    Example:
    ```python
    from object_mother_pattern.mothers.identifiers.countries.spain import PassportMother

    passport = PassportMother.create()
    print(passport)
    # >>> AB123456
    ```
    """

    @classmethod
    @override
    def create(cls, *, value: str | None = None, string_case: StringCase | None = None) -> str:
        """
        Create a random valid Spanish passport.

        Args:
            value (str | None, optional): Specific passport value to return. Defaults to None.
            string_case (StringCase | None, optional): Case of passport letters. Defaults to None.

        Raises:
            TypeError: If the provided `value` is not a string.
            TypeError: If `string_case` is not a StringCase.

        Returns:
            str: A valid Spanish passport.

        Example:
        ```python
        from object_mother_pattern.mothers.identifiers.countries.spain import PassportMother

        passport = PassportMother.create()
        print(passport)
        # >>> ABC123456
        ```
        """
        if value is not None:
            if type(value) is not str:
                raise TypeError('PassportMother value must be a string.')

            return value

        if string_case is None:
            string_case = StringCase(value=choice(seq=tuple(StringCase)))  # noqa: S311

        if type(string_case) is not StringCase:
            raise TypeError('PassportMother string_case must be a StringCase.')

        passport = (f'{StringMother.uppercase(min_length=2, max_length=3)}{StringMother.numeric(min_length=6, max_length=6)}')  # noqa: E501  # fmt: skip
        match string_case:
            case StringCase.LOWERCASE:
                passport = passport.lower()

            case StringCase.UPPERCASE:
                passport = passport.upper()

            case StringCase.MIXEDCASE:
                passport = ''.join(choice(seq=(char.upper(), char.lower())) for char in passport)  # noqa: S311

            case _:  # pragma: no cover
                assert_never(string_case)

        return passport

    @classmethod
    def invalid_value(cls) -> str:
        """
        Create an invalid Spanish passport value.

        Returns:
            str: Invalid Spanish passport string.
        """
        return StringMother.invalid_value()
