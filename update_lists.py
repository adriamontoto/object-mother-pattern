"""
Update the lists used in the Object Mother Pattern package.
"""

from datetime import UTC, datetime
from re import DOTALL, findall
from urllib.request import urlopen


def add_updated_date_comment(file_path: str) -> None:
    """
    Automatically add a comment indicating the last updated date to the first line of the specified file.

    Args:
        file_path (str): The path of the file to be updated.
    """
    now = datetime.now(tz=UTC).isoformat()

    with open(file=file_path, mode='r+', encoding='utf-8') as file:
        content = file.read()
        file.seek(0)
        file.write(f'# This file was automatically updated using "update_lists.py" on {now}\n\n{content}')
        file.truncate()


def update_aws_cloud_regions() -> None:
    """
    Retrieve AWS cloud regions from the official AWS documentation and update the local AWS regions file..

    References:
        AWS Cloud Regions: https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions.html#available-regions
    """
    url = 'https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions.html#available-regions'
    with urlopen(url=url) as response:  # noqa: S310
        content = response.read().decode('utf-8')

    pattern = r'<tr>\s*<td[^>]*tabindex="-1">(.*?)</td>\s*<td[^>]*tabindex="-1">.*?</td>\s*<td[^>]*tabindex="-1">.*?</td>\s*</tr>'  # noqa: E501
    aws_regions = tuple(region_code.lower() for region_code in findall(pattern=pattern, string=content, flags=DOTALL))

    path = 'object_mother_pattern/mothers/internet/utils/aws_regions.txt'
    with open(file=path, mode='w', encoding='utf-8') as file:
        file.writelines(f'{word}\n' for word in aws_regions)

    add_updated_date_comment(file_path=path)


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

    add_updated_date_comment(file_path=path)


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

    add_updated_date_comment(file_path=path)


def update_word_list() -> None:
    """
    Retrieve a list of 10000 words.

    References:
        Words: https://www.mit.edu/~ecprice/wordlist.10000
    """
    url = 'https://www.mit.edu/~ecprice/wordlist.10000'
    with urlopen(url=url) as response:  # noqa: S310
        lines = response.read().decode('utf-8').splitlines()

    words = tuple(line.strip().lower() for line in lines if line)

    path = 'object_mother_pattern/mothers/internet/utils/words.txt'
    with open(file=path, mode='w', encoding='utf-8') as file:
        file.writelines(f'{word}\n' for word in words)

    add_updated_date_comment(file_path=path)


if __name__ == '__main__':
    update_aws_cloud_regions()
    update_bip39_words()
    update_tld_domains()
    update_word_list()
