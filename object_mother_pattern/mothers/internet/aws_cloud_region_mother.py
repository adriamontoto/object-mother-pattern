"""
AwsCloudRegionMother module.
"""

from functools import lru_cache
from random import choice
from re import DOTALL, findall
from sys import version_info
from urllib.request import urlopen

if version_info >= (3, 12):
    from typing import override  # pragma: no cover
else:
    from typing_extensions import override  # pragma: no cover

from object_mother_pattern.mothers.base_mother import BaseMother


@lru_cache(maxsize=1)
def get_aws_cloud_regions() -> tuple[str]:
    """
    Get AWS cloud regions.

    Returns:
        tuple[str]: The AWS cloud regions.

    References:
        AWS Cloud Regions: https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions.html#available-regions
    """
    url = 'https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions.html#available-regions'
    with urlopen(url=url) as response:  # noqa: S310
        content = response.read().decode('utf-8')

    pattern = r'<tr>\s*<td[^>]*tabindex="-1">(.*?)</td>\s*<td[^>]*tabindex="-1">.*?</td>\s*<td[^>]*tabindex="-1">.*?</td>\s*</tr>'  # noqa: E501
    region_codes = findall(pattern=pattern, string=content, flags=DOTALL)

    return tuple(region_code.lower() for region_code in region_codes)


class AwsCloudRegionMother(BaseMother[str]):
    """
    AwsCloudRegionMother class is responsible for creating random AWS cloud region values.

    References:
        AWS Cloud Regions: https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions.html#available-regions

    Example:
    ```python
    from object_mother_pattern.mothers.internet import AwsCloudRegionMother

    region = AwsCloudRegionMother.create()
    print(region)
    # >>> us-east-1
    ```
    """

    _type: type = str

    @classmethod
    @override
    def create(cls, *, value: str | None = None) -> str:
        """
        Create a random AWS cloud region value. If a specific AWS cloud region value is provided via `value`, it is
        returned after validation. Otherwise, a random AWS cloud region value is generated.

        Args:
            value (str | None, optional): Specific value to return. Defaults to None.

        Raises:
            TypeError: If the provided `value` is not a string.

        Returns:
            str: A randomly AWS cloud region value.

        Example:
        ```python
        from object_mother_pattern.mothers.internet import AwsCloudRegionMother

        region = AwsCloudRegionMother.create()
        print(region)
        # >>> us-east-1
        ```
        """
        if value is not None:
            if type(value) is not str:
                raise TypeError('AwsCloudRegionMother value must be a string.')

            return value

        return choice(seq=get_aws_cloud_regions())  # noqa: S311
