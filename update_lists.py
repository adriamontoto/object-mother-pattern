"""
Update the lists used in the Object Mother Pattern package.
"""

from urllib.request import urlopen


def update_bip39_words() -> None:
    """
    Retrieve BIP39 words from Bitcoin and update the local BIP39 file.

    References:
        Bip39 Words: https://github.com/bitcoin/bips/blob/master/bip-0039/english.txt
    """
    url = 'https://raw.githubusercontent.com/bitcoin/bips/refs/heads/master/bip-0039/english.txt'
    with urlopen(url=url) as response:  # noqa: S310
        lines = response.read().decode('utf-8').splitlines()

    bip39_words = tuple(line.strip().lower() for line in lines if line and not line.startswith('#'))

    path = 'object_mother_pattern/mothers/money/cryptocurrencies/utils/bip39_words.txt'
    with open(file=path, mode='w', encoding='utf-8') as file:
        file.writelines(f'{word}\n' for word in bip39_words)


def update_tld_domains() -> None:
    """
    Retrieve top-level domains from IANA and update the local TLD file.

    References:
        TLD Domains: https://data.iana.org/TLD/tlds-alpha-by-domain.txt
    """
    url = 'https://data.iana.org/TLD/tlds-alpha-by-domain.txt'
    with urlopen(url=url) as response:  # noqa: S310
        lines = response.read().decode('utf-8').splitlines()

    tld_domains = tuple(line.strip().lower() for line in lines if line and not line.startswith('#'))

    path = 'object_mother_pattern/mothers/internet/utils/tld_domains.txt'
    with open(file=path, mode='w', encoding='utf-8') as file:
        file.writelines(f'{domain}\n' for domain in tld_domains)


if __name__ == '__main__':
    update_bip39_words()
    update_tld_domains()
