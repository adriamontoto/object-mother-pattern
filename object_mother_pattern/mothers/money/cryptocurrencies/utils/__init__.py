from functools import lru_cache


@lru_cache(maxsize=1)
def get_bip39_words() -> tuple[str, ...]:
    """
    Get BIP39 words.

    Returns:
        tuple[str, ...]: The BIP39 word list.

    References:
        BIP39 Words: https://github.com/bitcoin/bips/blob/master/bip-0039/english.txt
    """
    with open(file='object_mother_pattern/mothers/money/cryptocurrencies/utils/bip39_words.txt') as file:
        return tuple(file.read().splitlines())
