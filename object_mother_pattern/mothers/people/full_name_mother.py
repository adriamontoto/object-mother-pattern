"""
FullNameMother module.
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


class FullNameMother(BaseMother[str]):
    """
    FullNameMother class is responsible for creating random full name values.

    Example:
    ```python
    from object_mother_pattern.mothers.people import FullNameMother

    name = FullNameMother.create()
    print(name)
    # >>> Brady Warrenbruce Jacobso
    ```
    """

    @classmethod
    @override
    def create(  # noqa: C901
        cls,
        *,
        value: str | None = None,
        min_length: int = 3,
        max_length: int = 128,
        string_case: StringCase | None = None,
    ) -> str:
        """
        Create a random string full name value. If a specific string full name value is provided via `value`, it is
        returned after validation. Otherwise, a random string full name value is generated within the provided range of
        `min_length` and `max_length` (both included).

        Args:
            value (str | None, optional): Specific value to return. Defaults to None.
            min_length (int, optional): Minimum length of the full name. Must be >= 1. Defaults to 3.
            max_length (int, optional): Maximum length of the full name. Must be >= 1 and >= `min_length`. Defaults to
            128.
            string_case (StringCase | None, optional): The case of the full name. Defaults to None (randomly chosen).

        Raises:
            TypeError: If the provided `value` is not a string.
            TypeError: If `min_length` is not an integer.
            TypeError: If `max_length` is not an integer.
            ValueError: If `min_length` is not greater than 0.
            ValueError: If `max_length` is not greater than 0.
            ValueError: If `min_length` is greater than `max_length`.
            TypeError: If `string_case` is not a StringCase.

        Returns:
            str: A randomly generated full name value in the provided range.

        Example:
        ```python
        from object_mother_pattern.mothers.people import FullNameMother

        name = FullNameMother.create()
        print(name)
        # >>> Brady Warrenbruce Jacobso
        ```
        """
        if value is not None:
            if type(value) is not str:
                raise TypeError('FullNameMother value must be a string.')

            return value

        if type(min_length) is not int:
            raise TypeError('FullNameMother min_length must be an integer.')

        if type(max_length) is not int:
            raise TypeError('FullNameMother max_length must be an integer.')

        if min_length < 1:
            raise ValueError('FullNameMother min_length must be greater than or equal to 1.')

        if max_length < 1:
            raise ValueError('FullNameMother max_length must be greater than or equal to 1.')

        if min_length > max_length:
            raise ValueError('FullNameMother min_length must be less than or equal to max_length.')

        if string_case is None:
            string_case = StringCase(value=choice(seq=tuple(StringCase)))  # noqa: S311

        if type(string_case) is not StringCase:
            raise TypeError('FullNameMother string_case must be a StringCase.')

        length = randint(a=min_length, b=max_length)  # noqa: S311

        name = cls._random().name()
        while len(name) < length:
            name += cls._random().name()

        name = name[:length]
        if name != name.strip():
            name = name[:-1] + cls._random().lexify(text='?').lower()  # pragma: no cover

        match string_case:
            case StringCase.LOWERCASE:
                name = name.lower()

            case StringCase.UPPERCASE:
                name = name.upper()

            case StringCase.MIXEDCASE:
                name = ''.join(choice((char.upper(), char.lower())) for char in name)  # noqa: S311

            case _:  # pragma: no cover
                assert_never(string_case)

        return name

    @classmethod
    def of_length(cls, *, length: int) -> str:
        """
        Create a random string full name value of a specific `length`.

        Args:
            length (int): Length of the full name. Must be >= 1.

        Raises:
            TypeError: If `length` is not an integer.
            ValueError: If `length` is not greater than 0.

        Returns:
            str: A randomly generated full name value of the provided length.

        Example:
        ```python
        from object_mother_pattern.mothers.people import FullNameMother

        name = FullNameMother.of_length(length=5)
        print(name)
        # >>> Leslie
        ```
        """
        return cls.create(min_length=length, max_length=length)

    @classmethod
    def invalid_value(cls) -> str:
        """
        Create an invalid string full name value.

        Returns:
            str: Invalid string full name string.
        """
        return StringMother.invalid_value()
