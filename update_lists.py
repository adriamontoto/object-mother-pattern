"""
Update the lists used in the Object Mother Pattern package.
"""

from datetime import UTC, datetime
from pathlib import Path
from re import DOTALL, findall
from urllib.request import urlopen


def write_if_changed(path: str, lines: tuple[str, ...]) -> None:
    """
    Write list content to a file only when the body has changed to avoid noisy commits. Preserves the existing file
    when no changes are detected.

    Args:
        path (str): The file path to update.
        lines (tuple[str, ...]): The lines to write to the file.
    """
    header_prefix = '# This file was automatically updated using "update_lists.py" on '
    new_body = '\n'.join(lines) + '\n'
    file_path = Path(path)

    current_text = file_path.read_text(encoding='utf-8')
    _, _, existing_body = current_text.partition('\n')
    if existing_body[1:] == new_body:
        return

    now = datetime.now(tz=UTC).isoformat()
    new_text = f'{header_prefix}{now}\n\n{new_body}'
    file_path.write_text(new_text, encoding='utf-8')


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
    write_if_changed(path=path, lines=aws_regions)


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
    write_if_changed(path=path, lines=bip39_words)


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
    write_if_changed(path=path, lines=tld_domains)


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
    write_if_changed(path=path, lines=words)


if __name__ == '__main__':
    update_aws_cloud_regions()
    update_bip39_words()
    update_tld_domains()
    update_word_list()
