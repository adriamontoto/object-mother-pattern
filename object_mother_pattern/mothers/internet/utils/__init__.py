from functools import lru_cache


@lru_cache(maxsize=1)
def get_aws_cloud_regions() -> tuple[str, ...]:
    """
    Get AWS cloud regions from the official AWS documentation.

    Returns:
        tuple[str, ...]: The AWS regions in lower case.

    References:
        AWS Cloud Regions: https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions.html#available-regions
    """
    with open(file='object_mother_pattern/mothers/internet/utils/aws_regions.txt') as file:
        lines = file.read().splitlines()
        filtered_lines = tuple(line for line in lines if line.strip() and not line.strip().startswith('#'))

        return filtered_lines
