from functools import lru_cache
from importlib.resources import files


@lru_cache(maxsize=1)
def get_aws_cloud_regions() -> tuple[str, ...]:
    """
    Get AWS cloud regions from the official AWS documentation.

    Returns:
        tuple[str, ...]: The AWS regions in lower case.

    References:
        AWS Cloud Regions: https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions.html#available-regions
    """
    lines = (
        files('object_mother_pattern.mothers.internet.utils')
        .joinpath('aws_regions.txt')
        .read_text(encoding='utf-8')
        .splitlines()
    )
    filtered_lines = tuple(line for line in lines if not line.startswith('#') and (_line := line.strip().lower()))

    return filtered_lines


@lru_cache(maxsize=1)
def get_tld_dict() -> dict[int, tuple[str, ...]]:
    """
    Get top level domains from IANA in a dictionary sorted by domain length.

    Returns:
        dict[int, tuple[str, ...]]: The top level domains in lower case sorted by domain length.

    References:
        TLD Domains: https://data.iana.org/TLD/tlds-alpha-by-domain.txt
    """
    lines = (
        files('object_mother_pattern.mothers.internet.utils')
        .joinpath('tld_domains.txt')
        .read_text(encoding='utf-8')
        .splitlines()
    )

    temp: dict[int, list[str]] = {}
    tlds = tuple(line for line in lines if not line.startswith('#') and (_line := line.strip().lower()))
    for tld in tlds:
        key = len(tld)
        temp.setdefault(key, []).append(tld)

    return {key: tuple(value) for key, value in temp.items()}


@lru_cache(maxsize=1)
def get_label_dict() -> dict[int, tuple[str, ...]]:
    """
    Get labels from a list of words in a dictionary sorted by label length.

    Returns:
        dict[int, tuple[str, ...]]: The labels in lower case sorted by label length.

    References:
        Words: https://www.mit.edu/~ecprice/wordlist.10000
    """
    lines = (
        files('object_mother_pattern.mothers.internet.utils')
        .joinpath('words.txt')
        .read_text(encoding='utf-8')
        .splitlines()
    )

    temp: dict[int, list[str]] = {}
    labels = tuple(line for line in lines if not line.startswith('#') and (_line := line.strip().lower()))
    for label in labels:
        key = len(label)
        temp.setdefault(key, []).append(label)

    return {key: tuple(value) for key, value in temp.items()}
