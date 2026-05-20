"""
IbanMother module.
"""

from sys import version_info

if version_info >= (3, 12):
    from typing import override  # pragma: no cover
else:
    from typing_extensions import override  # pragma: no cover

from random import randint
from string import ascii_uppercase, digits
from typing import ClassVar

from object_mother_pattern.models import BaseMother
from object_mother_pattern.mothers.primitives.string_mother import StringMother


class IbanMother(BaseMother[str]):
    """
    IbanMother generates IBAN numbers with correct check digits.
    """

    _COUNTRY_LENGTHS: ClassVar[dict[str, int]] = {
        'AL': 28,
        'AT': 20,
        'BA': 20,
        'BE': 16,
        'BG': 22,
        'CH': 21,
        'CY': 28,
        'CZ': 24,
        'DE': 22,
        'DK': 18,
        'EE': 20,
        'ES': 24,
        'FI': 18,
        'FR': 27,
        'GB': 22,
        'GI': 23,
        'GR': 27,
        'HR': 21,
        'HU': 28,
        'IE': 22,
        'IL': 23,
        'IS': 26,
        'IT': 27,
        'KW': 30,
        'KZ': 20,
        'LB': 28,
        'LI': 21,
        'LT': 20,
        'LU': 20,
        'LV': 21,
        'MC': 27,
        'ME': 22,
        'MK': 19,
        'MT': 31,
        'NL': 18,
        'NO': 15,
        'PL': 28,
        'PT': 25,
        'RO': 24,
        'RS': 22,
        'SA': 24,
        'SE': 24,
        'SI': 19,
        'SK': 24,
        'TR': 26,
        'UA': 29,
    }

    _BBAN_CHARS: str = ascii_uppercase + digits

    @classmethod
    @override
    def create(cls, *, value: str | None = None, country_code: str | None = None) -> str:
        """
        Create a random IBAN or return the provided value.
        """
        if value is not None:
            if type(value) is not str:
                raise TypeError('IbanMother value must be a string.')
            return value

        code = cls._pick_country(country_code)
        length = cls._COUNTRY_LENGTHS[code]
        bban_length = length - 4

        bban = ''.join(cls._random_bban_char() for _ in range(bban_length))
        checksum = cls._compute_checksum(code=code, bban=bban)

        return f'{code}{checksum}{bban}'

    @classmethod
    def invalid_value(cls) -> str:
        """
        Create an invalid IBAN value.
        """
        return StringMother.invalid_value()

    @classmethod
    def _pick_country(cls, country_code: str | None) -> str:
        """
        Pick and validate the country code used to generate an IBAN.

        Args:
            country_code (str | None): Optional country code to force.

        Raises:
            TypeError: If `country_code` is not a string.
            ValueError: If `country_code` is not supported.

        Returns:
            str: Supported uppercase country code.
        """
        if country_code is None:
            keys = tuple(cls._COUNTRY_LENGTHS.keys())
            index = randint(0, len(keys) - 1)  # noqa: S311
            return keys[index]

        if type(country_code) is not str:
            raise TypeError('IbanMother country_code must be a string.')

        code = country_code.upper()
        if code not in cls._COUNTRY_LENGTHS:
            raise ValueError(f'IbanMother country_code must be one of {sorted(cls._COUNTRY_LENGTHS)}.')
        return code

    @classmethod
    def _compute_checksum(cls, *, code: str, bban: str) -> str:
        """
        Compute IBAN checksum using the mod-97 algorithm.

        Args:
            code (str): Two-letter country code.
            bban (str): Basic bank account number.

        Returns:
            str: Two-digit IBAN checksum.
        """
        rearranged = f'{bban}{code}00'
        remainder = 0
        for char in rearranged:
            numeric = str(ord(char) - 55) if char.isalpha() else char
            for digit in numeric:
                remainder = (remainder * 10 + int(digit)) % 97

        checksum_value = 98 - remainder
        return f'{checksum_value:02d}'

    @classmethod
    def _random_bban_char(cls) -> str:
        """
        Create a random BBAN character.

        Returns:
            str: Random character allowed in the generated BBAN.
        """
        index = randint(0, len(cls._BBAN_CHARS) - 1)  # noqa: S311
        return cls._BBAN_CHARS[index]
