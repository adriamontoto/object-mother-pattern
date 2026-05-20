"""
Test module for the ListMother class.
"""

from pytest import mark, raises as assert_raises

from object_mother_pattern.models import ListMother
from object_mother_pattern.mothers import IntegerMother, StringMother


@mark.unit_testing
def test_list_mother_create_method_happy_path() -> None:
    """
    Check that ListMother create method returns a list within bounds.
    """
    value = ListMother.create(min_length=1, max_length=3, item_mother=IntegerMother.create)

    assert type(value) is list
    assert 1 <= len(value) <= 3
    assert all(type(item) is int for item in value)


@mark.unit_testing
def test_list_mother_create_method_default_items() -> None:
    """
    Check that ListMother can create lists without an item mother.
    """
    value: list[object] = ListMother.create(min_length=2, max_length=2)

    assert value == [None, None]


@mark.unit_testing
def test_list_mother_create_method_with_string_item_mother() -> None:
    """
    Check that ListMother can create items using another mother.
    """
    value = ListMother.create(min_length=3, max_length=3, item_mother=StringMother.create)

    assert type(value) is list
    assert len(value) == 3
    assert all(type(item) is str for item in value)


@mark.unit_testing
def test_list_mother_create_method_with_value() -> None:
    """
    Check that ListMother create method returns the provided list.
    """
    value = [IntegerMother.create()]

    assert ListMother.create(value=value) is value


@mark.unit_testing
def test_list_mother_create_method_invalid_value_type() -> None:
    """
    Check that ListMother validates provided value type.
    """
    with assert_raises(expected_exception=TypeError, match='ListMother value must be a list.'):
        ListMother.create(value=ListMother.invalid_type(remove_types=(list,)))


@mark.unit_testing
def test_list_mother_create_method_invalid_length_types() -> None:
    """
    Check that ListMother validates length parameter types.
    """
    with assert_raises(expected_exception=TypeError, match='ListMother min_length must be an integer.'):
        ListMother.create(min_length=IntegerMother.invalid_type())

    with assert_raises(expected_exception=TypeError, match='ListMother max_length must be an integer.'):
        ListMother.create(max_length=IntegerMother.invalid_type())


@mark.unit_testing
def test_list_mother_create_method_invalid_length_bounds() -> None:
    """
    Check that ListMother validates length bounds.
    """
    with assert_raises(
        expected_exception=ValueError, match='ListMother min_length must be greater than or equal to 0.'
    ):
        ListMother.create(min_length=-1)

    with assert_raises(
        expected_exception=ValueError, match='ListMother max_length must be greater than or equal to 0.'
    ):
        ListMother.create(max_length=-1)

    with assert_raises(
        expected_exception=ValueError,
        match='ListMother min_length must be less than or equal to max_length.',
    ):
        ListMother.create(min_length=2, max_length=1)


@mark.unit_testing
def test_list_mother_create_method_invalid_item_mother_type() -> None:
    """
    Check that ListMother validates item_mother type.
    """
    with assert_raises(expected_exception=TypeError, match='ListMother item_mother must be callable.'):
        ListMother.create(item_mother=ListMother.invalid_type())


@mark.unit_testing
def test_list_mother_empty_method_happy_path() -> None:
    """
    Check that ListMother empty method returns an empty list.
    """
    assert ListMother.empty() == []


@mark.unit_testing
def test_list_mother_of_length_method_happy_path() -> None:
    """
    Check that ListMother of_length method returns a list with the requested length.
    """
    value = ListMother.of_length(length=3, item_mother=IntegerMother.create)

    assert len(value) == 3
    assert all(type(item) is int for item in value)
