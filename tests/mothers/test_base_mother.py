"""
Test module for the BaseMother class.
"""

from re import escape

from pytest import mark, raises as assert_raises

from object_mother_pattern.models import BaseMother


@mark.unit_testing
def test_base_mother_cannot_be_instantiated() -> None:
    """
    Test BaseMother cannot be instantiated.
    """
    with assert_raises(
        expected_exception=TypeError,
        match=r"Can't instantiate abstract class BaseMother with.*",
    ):
        BaseMother()  # type: ignore[abstract]


@mark.unit_testing
def test_base_mother_init_with_invalid_type() -> None:
    """
    Test BaseMother initialization with invalid type.
    """
    value = BaseMother.invalid_type(remove_types=(list, set, tuple, dict))

    with assert_raises(
        expected_exception=TypeError,
        match=r'BaseMother\[.*\] <<<.*>>> must be a type. Got <<<.*>>> type.',
    ):

        class BooleanMother(BaseMother[value]):  # type: ignore[valid-type]
            pass


@mark.unit_testing
def test_base_mother_init_without_parameterization() -> None:
    """
    Test BaseMother initialization without parameterization.
    """
    with assert_raises(
        expected_exception=TypeError,
        match=escape(pattern='BaseMother must be parameterized, e.g. "class BooleanMother(BaseMother[bool])".'),
    ):

        class BooleanMother(BaseMother):  # type: ignore[type-arg]
            pass
