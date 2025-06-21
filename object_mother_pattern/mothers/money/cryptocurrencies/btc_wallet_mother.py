"""
BtcWalletMother module.
"""

from sys import version_info

if version_info >= (3, 12):
    from typing import override  # pragma: no cover
else:
    from typing_extensions import override  # pragma: no cover

from random import choice, choices
from typing import assert_never

from object_mother_pattern.models import BaseMother
from object_mother_pattern.mothers import StringCase
from object_mother_pattern.mothers.primitives.string_mother import StringMother

from .utils import get_bip39_words


class BtcWalletMother(BaseMother[str]):
    """
    BtcWalletMother class is responsible for creating random BTC wallet addresses values.

    Example:
    ```python
    from object_mother_pattern.mothers.money.cryptocurrencies import BtcWalletMother

    wallet = BtcWalletMother.create()
    print(wallet)
    # >>> envelope company have recall achieve possible decline picture again erupt strategy meat
    ```
    """

    @classmethod
    @override
    def create(
        cls,
        *,
        value: str | None = None,
        word_number: int = 12,
        string_case: StringCase | None = None,
    ) -> str:
        """
        Create a random BTC wallet address value. If a specific wallet address value is provided via `value`, it is
        returned after validation. Otherwise, a random wallet address value (separated by spaces) is generated of the
        provided `word_number` length.

        Args:
            value (str | None, optional): Specific value to return. Defaults to None.
            word_number (int, optional): The number of words of the wallet address. Must be >= 1. Defaults to 12.
            string_case (StringCase | None, optional): The case of the wallet address. Defaults to None.

        Raises:
            TypeError: If the provided `value` is not a string.
            TypeError: If `word_number` is not an integer.
            TypeError: If `word_number` is not greater than 0.
            TypeError: If `string_case` is not a StringCase.

        Returns:
            str: A randomly generated BTC wallet address value (separated by spaces).

        Example:
        ```python
        from object_mother_pattern.mothers.money.cryptocurrencies import BtcWalletMother

        wallet = BtcWalletMother.create()
        print(wallet)
        # >>> envelope company have recall achieve possible decline picture again erupt strategy meat
        ```
        """
        if value is not None:
            if type(value) is not str:
                raise TypeError('BtcWalletMother value must be a string.')

            return value

        if type(word_number) is not int:
            raise TypeError('BtcWalletMother word_number must be an integer.')

        if word_number < 1:
            raise ValueError('BtcWalletMother word_number must be greater than or equal to 1.')

        if string_case is None:
            string_case = StringCase(value=choice(seq=tuple(StringCase)))  # noqa: S311

        if type(string_case) is not StringCase:
            raise TypeError('BtcWalletMother string_case must be a StringCase.')

        wallet = ' '.join(choices(population=get_bip39_words(), k=word_number))  # noqa: S311

        match string_case:
            case StringCase.LOWERCASE:
                wallet = wallet.lower()

            case StringCase.UPPERCASE:
                wallet = wallet.upper()

            case StringCase.MIXEDCASE:
                wallet = ''.join(choice(seq=(char.upper(), char.lower())) for char in wallet)  # noqa: S311

            case _:  # pragma: no cover
                assert_never(string_case)

        return wallet

    @classmethod
    def invalid_value(cls) -> str:
        """
        Create an invalid BTC wallet value.

        Returns:
            str: Invalid BTC wallet string.
        """
        return StringMother.invalid_value()
