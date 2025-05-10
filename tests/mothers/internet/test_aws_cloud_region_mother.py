"""
Test module for the AwsCloudRegionMother class.
"""

from pytest import mark, raises as assert_raises

from object_mother_pattern.mothers.internet import AwsCloudRegionMother
from object_mother_pattern.mothers.internet.utils import get_aws_cloud_regions


@mark.unit_testing
def test_aws_cloud_region_mother_happy_path() -> None:
    """
    Test AwsCloudRegionMother happy path.
    """
    value = AwsCloudRegionMother.create()
    aws_regions = get_aws_cloud_regions()

    assert type(value) is str
    assert value in aws_regions


@mark.unit_testing
def test_aws_cloud_region_mother_value() -> None:
    """
    Test AwsCloudRegionMother create method with value.
    """
    value = AwsCloudRegionMother.create()

    assert AwsCloudRegionMother.create(value=value) == value


@mark.unit_testing
def test_aws_cloud_region_mother_invalid_type() -> None:
    """
    Test AwsCloudRegionMother create method with invalid type.
    """
    assert type(AwsCloudRegionMother.invalid_type()) is not str


@mark.unit_testing
def test_aws_cloud_region_mother_invalid_value() -> None:
    """
    Test AwsCloudRegionMother invalid_value method.
    """
    value = AwsCloudRegionMother.invalid_value()

    assert type(value) is str
    assert not value.isprintable()


@mark.unit_testing
def test_aws_cloud_region_mother_invalid_value_type() -> None:
    """
    Test AwsCloudRegionMother create method with invalid value type.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='AwsCloudRegionMother value must be a string.',
    ):
        AwsCloudRegionMother.create(value=AwsCloudRegionMother.invalid_type())
