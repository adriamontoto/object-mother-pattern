"""
AwsCloudRegionMother module.
"""

from sys import version_info

if version_info >= (3, 12):
    from typing import override  # pragma: no cover
else:
    from typing_extensions import override  # pragma: no cover

from random import choice

from object_mother_pattern.models import BaseMother
from object_mother_pattern.mothers.primitives.string_mother import StringMother

from .utils import get_aws_cloud_regions


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

    @classmethod
    def invalid_value(cls) -> str:
        """
        Create an invalid AWS cloud region value.

        Returns:
            str: Invalid AWS cloud region string.
        """
        return StringMother.invalid_value()
