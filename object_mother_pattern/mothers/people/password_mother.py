"""
PasswordMother module.
"""

from sys import version_info

if version_info >= (3, 12):
    from typing import override  # pragma: no cover
else:
    from typing_extensions import override  # pragma: no cover

from random import choice, choices, randint, sample

from object_mother_pattern.models import BaseMother
from object_mother_pattern.mothers.primitives.string_mother import StringMother
from object_mother_pattern.mothers.primitives.utils.alphabets import (
    ALPHABET_LOWERCASE_BASIC,
    ALPHABET_UPPERCASE_BASIC,
    DIGITS_BASIC,
    SPECIAL_CHARS,
    SUPER_SPECIAL_CHARS,
)


class PasswordMother(BaseMother[str]):
    """
    PasswordMother class is responsible for creating random password values.

    Example:
    ```python
    from object_mother_pattern.mothers.people import PasswordMother

    password = PasswordMother.create()
    print(password)
    # >>> xR#x^rX262;F
    ```
    """

    @classmethod
    @override
    def create(  # noqa: C901
        cls,
        *,
        value: str | None = None,
        lowercase_count: int = 3,
        lowercase_alphabet: str = ALPHABET_LOWERCASE_BASIC,
        uppercase_count: int = 3,
        uppercase_alphabet: str = ALPHABET_UPPERCASE_BASIC,
        digits_count: int = 3,
        digits_alphabet: str = DIGITS_BASIC,
        special_characters_count: int = 3,
        special_characters_alphabet: str = SPECIAL_CHARS,
        super_special_characters_count: int = 0,
        super_special_characters_alphabet: str = SUPER_SPECIAL_CHARS,
        exclude_duplicates: bool = False,
    ) -> str:
        """
        Generate a random password based on the provided parameters. If a specific password value is provided via
        `value`, it is returned after validation. Otherwise, a random password is generated based on the specified
        counts and alphabets for lowercase letters, uppercase letters, digits, special characters, and super special
        characters.

        Args:
            value (str | None, optional): Specific password value to return. Defaults to None.
            lowercase_count (int, optional): Number of lowercase letters in the password. Must be >= 0. Defaults to 3.
            lowercase_alphabet (str, optional): Alphabet to use for lowercase letters. Defaults to
            ALPHABET_LOWERCASE_BASIC.
            uppercase_count (int, optional): Number of uppercase letters in the password. Must be >= 0. Defaults to 3.
            uppercase_alphabet (str, optional): Alphabet to use for uppercase letters. Defaults to
            ALPHABET_UPPERCASE_BASIC.
            digits_count (int, optional): Number of digits in the password. Must be >= 0. Defaults to 3.
            digits_alphabet (str, optional): Alphabet to use for digits. Defaults to DIGITS_BASIC.
            special_characters_count (int, optional): Number of special characters in the password. Must be >= 0.
            Defaults to 3.
            special_characters_alphabet (str, optional): Alphabet to use for special characters. Defaults to
            SPECIAL_CHARS.
            super_special_characters_count (int, optional): Number of super special characters in the password. Must be
            >= 0. Defaults to 0.
            super_special_characters_alphabet (str, optional): Alphabet to use for super special characters. Defaults
            to SUPER_SPECIAL_CHARS.
            exclude_duplicates (bool, optional): Whether to exclude duplicate characters in the password. Defaults to
            False.

        Raises:
            TypeError: If `value` is not a string.
            TypeError: If `lowercase_count` is not an integer.
            ValueError: If `lowercase_count` is negative.
            TypeError: If `lowercase_alphabet` is not a string.
            TypeError: If `uppercase_count` is not an integer.
            ValueError: If `uppercase_count` is negative.
            TypeError: If `uppercase_alphabet` is not a string.
            TypeError: If `digits_count` is not an integer.
            ValueError: If `digits_count` is negative.
            TypeError: If `digits_alphabet` is not a string.
            TypeError: If `special_characters_count` is not an integer.
            ValueError: If `special_characters_count` is negative.
            TypeError: If `special_characters_alphabet` is not a string.
            TypeError: If `super_special_characters_count` is not an integer.
            ValueError: If `super_special_characters_count` is negative.
            TypeError: If `super_special_characters_alphabet` is not a string.
            TypeError: If `exclude_duplicates` is not a boolean.
            ValueError: If password length is greater than the alphabet length.

        Returns:
            str: Randomly generated password based on the specified parameters.

        Example:
        ```python
        from object_mother_pattern.mothers.people import PasswordMother

        password = PasswordMother.create()
        print(password)
        # >>> xR#x^rX262;F
        ```
        """
        if value is not None:
            if type(value) is not str:
                raise TypeError('PasswordMother value must be a string.')

            return value

        if type(lowercase_count) is not int:
            raise TypeError('PasswordMother lowercase_count value must be an integer.')

        if lowercase_count < 0:
            raise ValueError('PasswordMother lowercase_count value must be greater than or equal to 0.')

        if type(lowercase_alphabet) is not str:
            raise TypeError('PasswordMother lowercase_alphabet value must be a string.')

        if type(uppercase_count) is not int:
            raise TypeError('PasswordMother uppercase_count value must be an integer.')

        if uppercase_count < 0:
            raise ValueError('PasswordMother uppercase_count value must be greater than or equal to 0.')

        if type(uppercase_alphabet) is not str:
            raise TypeError('PasswordMother uppercase_alphabet value must be a string.')

        if type(digits_count) is not int:
            raise TypeError('PasswordMother digits_count value must be an integer.')

        if digits_count < 0:
            raise ValueError('PasswordMother digits_count value must be greater than or equal to 0.')

        if type(digits_alphabet) is not str:
            raise TypeError('PasswordMother digits_alphabet value must be a string.')

        if type(special_characters_count) is not int:
            raise TypeError('PasswordMother special_characters_count value must be an integer.')

        if special_characters_count < 0:
            raise ValueError('PasswordMother special_characters_count value must be greater than or equal to 0.')

        if type(special_characters_alphabet) is not str:
            raise TypeError('PasswordMother special_characters_alphabet value must be a string.')

        if type(super_special_characters_count) is not int:
            raise TypeError('PasswordMother super_special_characters_count value must be an integer.')

        if super_special_characters_count < 0:
            raise ValueError('PasswordMother super_special_characters_count value must be greater than or equal to 0.')

        if type(super_special_characters_alphabet) is not str:
            raise TypeError('PasswordMother super_special_characters_alphabet value must be a string.')

        if type(exclude_duplicates) is not bool:
            raise TypeError('PasswordMother exclude_duplicates value must be a boolean.')

        password_alphabet = ''  # nosec: B105
        password_alphabet += (
            cls._random_sample(
                sequence=lowercase_alphabet,
                sample_size=lowercase_count,
                unique=exclude_duplicates,
            )
            if lowercase_count > 0
            else ''
        )

        password_alphabet += (
            cls._random_sample(
                sequence=uppercase_alphabet,
                sample_size=uppercase_count,
                unique=exclude_duplicates,
            )
            if uppercase_count > 0
            else ''
        )

        password_alphabet += (
            cls._random_sample(
                sequence=digits_alphabet,
                sample_size=digits_count,
                unique=exclude_duplicates,
            )
            if digits_count > 0
            else ''
        )

        password_alphabet += (
            cls._random_sample(
                sequence=special_characters_alphabet,
                sample_size=special_characters_count,
                unique=exclude_duplicates,
            )
            if special_characters_count > 0
            else ''
        )

        password_alphabet += (
            cls._random_sample(
                sequence=super_special_characters_alphabet,
                sample_size=super_special_characters_count,
                unique=exclude_duplicates,
            )
            if super_special_characters_count > 0
            else ''
        )

        return cls._random_sample(sequence=password_alphabet, sample_size=len(password_alphabet), unique=True)

    @classmethod
    def random_length(
        cls,
        *,
        min_length: int = 8,
        max_length: int = 16,
        exclude_super_special: bool = False,
        exclude_duplicates: bool = False,
    ) -> str:
        """
        Generate a random password with a random length between `min_length` and `max_length`.

        Args:
            min_length (int, optional): Minimum length of the password. Must be > 0. Defaults to 8.
            max_length (int, optional): Maximum length of the password. Must be > 0 and >= `min_length`. Defaults to 16.
            exclude_super_special (bool, optional): Whether to exclude super special characters in the password.
            Defaults to False.
            exclude_duplicates (bool, optional): Whether to exclude duplicate characters in the password. Defaults to
            False

        Raises:
            TypeError: If `min_length` is not an integer.
            ValueError: If `min_length` is less than or equal to 0.
            TypeError: If `max_length` is not an integer.
            ValueError: If `max_length` is less than or equal to 0.
            ValueError: If `min_length` is greater than `max_length`.
            TypeError: If `exclude_super_special` is not a boolean.
            TypeError: If `exclude_duplicates` is not a boolean.

        Returns:
            str: Randomly generated password with a random length between `min_length` and `max_length`.

        Example:
        ```python
        from object_mother_pattern.mothers.people import PasswordMother

        password = PasswordMother.random_length(min_length=8, max_length=16)
        print(password)
        # >>> &8I_0,[xS*Qpl 6;
        ```
        """
        if type(min_length) is not int:
            raise TypeError('PasswordMother min_length value must be an integer.')

        if min_length <= 0:
            raise ValueError('PasswordMother min_length value must be greater than 0.')

        if type(max_length) is not int:
            raise TypeError('PasswordMother max_length value must be an integer.')

        if max_length <= 0:
            raise ValueError('PasswordMother max_length value must be greater than 0.')

        if min_length > max_length:
            raise ValueError('PasswordMother min_length value must be less than or equal to max_length.')

        if type(exclude_super_special) is not bool:
            raise TypeError('PasswordMother exclude_super_special value must be a boolean.')

        if type(exclude_duplicates) is not bool:
            raise TypeError('PasswordMother exclude_duplicates value must be a boolean.')

        char_counts = cls._distribute_characters(
            length=randint(a=min_length, b=max_length),  # noqa: S311
            exclude_super_special=exclude_super_special,
        )

        return cls.create(
            lowercase_count=char_counts['lowercase'],
            uppercase_count=char_counts['uppercase'],
            digits_count=char_counts['digits'],
            special_characters_count=char_counts['special'],
            super_special_characters_count=char_counts['super_special'],
            exclude_duplicates=exclude_duplicates,
        )

    @classmethod
    def of_length(cls, *, length: int, exclude_super_special: bool = False, exclude_duplicates: bool = False) -> str:
        """
        Generate a random password of a specific length `length`.

        Args:
            length (int): Length of the password. Must be > 0.
            exclude_super_special (bool, optional): Whether to exclude super special characters in the password.
            Defaults to False.
            exclude_duplicates (bool, optional): Whether to exclude duplicate characters in the password. Defaults to
            False

        Raises:
            TypeError: If `length` is not an integer.
            ValueError: If `length` is less than or equal to 0.
            TypeError: If `exclude_super_special` is not a boolean.
            TypeError: If `exclude_duplicates` is not a boolean.

        Returns:
            str: Randomly generated password of the specified length.

        Example:
        ```python
        from object_mother_pattern.mothers.people import PasswordMother

        password = PasswordMother.of_length(length=12)
        print(password)
        # >>> xR#x^rX262;F
        ```
        """
        if type(length) is not int:
            raise TypeError('PasswordMother length value must be an integer.')

        if length <= 0:
            raise ValueError('PasswordMother length value must be greater than 0.')

        return cls.random_length(
            min_length=length,
            max_length=length,
            exclude_super_special=exclude_super_special,
            exclude_duplicates=exclude_duplicates,
        )

    @classmethod
    def _distribute_characters(cls, *, length: int, exclude_super_special: bool = False) -> dict[str, int]:
        """
        Distribute characters among different character types for password generation.

        Args:
            length (int): Total password length to distribute.
            exclude_super_special (bool, optional): Whether to exclude super special characters in the password.
            Defaults to False.

        Returns:
            dict[str, int]: Dictionary with counts for each character type.
        """
        min_type_count = min(1, length // 4)  # At least one of each if length allows
        remaining_length = length - (min_type_count * 4)

        char_counts = {
            'lowercase': min_type_count,
            'uppercase': min_type_count,
            'digits': min_type_count,
            'special': min_type_count,
            'super_special': 0,
        }

        char_types = ['lowercase', 'uppercase', 'digits', 'special']
        if not exclude_super_special:
            char_types.append('super_special')

        for _ in range(remaining_length):
            char_type = choice(seq=char_types)  # noqa: S311
            char_counts[char_type] += 1

        return char_counts

    @classmethod
    def _random_sample(cls, *, sequence: str, sample_size: int, unique: bool = False) -> str:
        """
        Generate a random sample of size `sample_size` from the given sequence `sequence`.

        Args:
            sequence (str): The sequence to sample from.
            sample_size (int): The size of the final sample.
            unique (bool, optional): Whether to add unique characters to the final sample. Defaults to False.

        Raises:
            ValueError: If `sample_size` is greater than the length of `sequence`.

        Returns:
            str: Random sample from the provided sequence `sequence`.
        """
        if unique:
            if sample_size > len(sequence):
                raise ValueError('PasswordMother sample_size must be less than or equal to the length of the sequence.')

            return ''.join(sample(population=sequence, k=sample_size))

        return ''.join(choices(population=sequence, k=sample_size))  # noqa: S311

    @classmethod
    def invalid_value(cls) -> str:
        """
        Create an invalid string value.

        Returns:
            str: Invalid string.
        """
        return StringMother.invalid_value()
