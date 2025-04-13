"""
BtcWalletMother module.
"""

from random import choices
from sys import version_info

if version_info >= (3, 12):
    from typing import override  # pragma: no cover
else:
    from typing_extensions import override  # pragma: no cover

from enum import StrEnum, unique
from random import choice
from typing import assert_never

from object_mother_pattern.mothers.base_mother import BaseMother

from .utils import get_bip39_words


@unique
class BtcWalletCase(StrEnum):
    """
    Type of BTC wallet address cases.
    """

    LOWERCASE = 'lowercase'
    UPPERCASE = 'uppercase'
    MIXED = 'mixed'


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

    _type: type = str

    @classmethod
    @override
    def create(cls, *, value: str | None = None, word_number: int = 12) -> str:
        """
        Create a random BTC wallet address value. If a specific wallet address value is provided via `value`, it is
        returned after validation. Otherwise, a random wallet address value (separated by spaces) is generated of the
        provided `word_number` length.

        Args:
            value (str | None, optional): Specific value to return. Defaults to None.
            word_number (int, optional): The number of words of the wallet address. Must be >= 1. Defaults to 12.

        Raises:
            TypeError: If the provided `value` is not a string.
            TypeError: If `word_number` is not an integer.
            TypeError: If `word_number` is not greater than 0.

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

        wallet = ' '.join(choices(population=get_bip39_words(), k=word_number))  # noqa: S311

        wallet_case = BtcWalletCase(value=choice(seq=tuple(BtcWalletCase)))  # noqa: S311
        match wallet_case:
            case BtcWalletCase.LOWERCASE:
                wallet = wallet.lower()

            case BtcWalletCase.UPPERCASE:
                wallet = wallet.upper()

            case BtcWalletCase.MIXED:
                wallet = ''.join(choice(seq=(char.upper(), char.lower())) for char in wallet)  # noqa: S311

            case _:
                assert_never(wallet)

        return wallet
