"""
Test module for the DictMother class.
"""

from collections.abc import Callable, Hashable
from typing import cast

from pytest import mark, raises as assert_raises

from object_mother_pattern.models import DictMother
from object_mother_pattern.mothers import IntegerMother, StringMother


def _unhashable_key() -> list[object]:
    """
    Create an unhashable key candidate for DictMother tests.
    """
    return []


def _same_key() -> str:
    """
    Create the same key on every call for DictMother duplicate-key tests.
    """
    return 'same-key'


@mark.unit_testing
def test_dict_mother_create_method_happy_path() -> None:
    """
    Check that DictMother create method returns a dictionary within bounds.
    """
    value = DictMother.create(
        min_length=1,
        max_length=3,
        key_mother=StringMother.snake_case,
        value_mother=IntegerMother.create,
    )

    assert type(value) is dict
    assert 1 <= len(value) <= 3
    assert all(type(key) is str for key in value)
    assert all(type(item) is int for item in value.values())


@mark.unit_testing
def test_dict_mother_create_method_default_keys_and_values() -> None:
    """
    Check that DictMother can create dictionaries without key or value mothers.
    """
    value: dict[object, object] = DictMother.create(min_length=2, max_length=2)

    assert value == {0: None, 1: None}


@mark.unit_testing
def test_dict_mother_create_method_with_value() -> None:
    """
    Check that DictMother create method returns the provided dictionary.
    """
    value = {StringMother.snake_case(): IntegerMother.create()}

    assert DictMother.create(value=value) is value


@mark.unit_testing
def test_dict_mother_create_method_invalid_value_type() -> None:
    """
    Check that DictMother validates provided value type.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='DictMother value must be a dictionary.',
    ):
        DictMother.create(value=DictMother.invalid_type(remove_types=(dict,)))


@mark.unit_testing
def test_dict_mother_create_method_invalid_min_length_type() -> None:
    """
    Check that DictMother validates min_length type.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='DictMother min_length must be an integer.',
    ):
        DictMother.create(min_length=IntegerMother.invalid_type())


@mark.unit_testing
def test_dict_mother_create_method_invalid_max_length_type() -> None:
    """
    Check that DictMother validates max_length type.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='DictMother max_length must be an integer.',
    ):
        DictMother.create(max_length=IntegerMother.invalid_type())


@mark.unit_testing
def test_dict_mother_create_method_negative_min_length() -> None:
    """
    Check that DictMother validates negative min_length.
    """
    with assert_raises(
        expected_exception=ValueError,
        match='DictMother min_length must be greater than or equal to 0.',
    ):
        DictMother.create(min_length=-1)


@mark.unit_testing
def test_dict_mother_create_method_negative_max_length() -> None:
    """
    Check that DictMother validates negative max_length.
    """
    with assert_raises(
        expected_exception=ValueError,
        match='DictMother max_length must be greater than or equal to 0.',
    ):
        DictMother.create(max_length=-1)


@mark.unit_testing
def test_dict_mother_create_method_min_length_greater_than_max_length() -> None:
    """
    Check that DictMother validates inconsistent length bounds.
    """
    with assert_raises(
        expected_exception=ValueError,
        match='DictMother min_length must be less than or equal to max_length.',
    ):
        DictMother.create(min_length=2, max_length=1)


@mark.unit_testing
def test_dict_mother_create_method_invalid_key_mother_type() -> None:
    """
    Check that DictMother validates key_mother type.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='DictMother key_mother must be callable.',
    ):
        DictMother.create(key_mother=DictMother.invalid_type())


@mark.unit_testing
def test_dict_mother_create_method_invalid_value_mother_type() -> None:
    """
    Check that DictMother validates value_mother type.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='DictMother value_mother must be callable.',
    ):
        DictMother.create(value_mother=DictMother.invalid_type())


@mark.unit_testing
def test_dict_mother_create_method_unhashable_key_mother_value() -> None:
    """
    Check that DictMother validates generated key hashability.
    """
    key_mother = cast('Callable[[], Hashable]', _unhashable_key)

    with assert_raises(
        expected_exception=TypeError,
        match='DictMother key_mother must create hashable keys.',
    ):
        DictMother.create(min_length=1, max_length=1, key_mother=key_mother)


@mark.unit_testing
def test_dict_mother_create_method_repeated_key_mother_value() -> None:
    """
    Check that DictMother rejects key mothers that cannot create enough unique keys.
    """
    with assert_raises(
        expected_exception=ValueError,
        match='DictMother key_mother must create enough unique keys.',
    ):
        DictMother.create(min_length=2, max_length=2, key_mother=_same_key)


@mark.unit_testing
def test_dict_mother_empty_method_happy_path() -> None:
    """
    Check that DictMother empty method returns an empty dictionary.
    """
    assert DictMother.empty() == {}


@mark.unit_testing
def test_dict_mother_of_length_method_happy_path() -> None:
    """
    Check that DictMother of_length method returns a dictionary with the requested length.
    """
    value = DictMother.of_length(
        length=3,
        key_mother=StringMother.snake_case,
        value_mother=IntegerMother.create,
    )

    assert len(value) == 3
    assert all(type(key) is str for key in value)
    assert all(type(item) is int for item in value.values())
