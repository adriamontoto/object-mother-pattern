"""
Test module for the NameMother class.
"""

from pytest import raises as assert_raises

from object_mother_pattern.mothers import IntegerMother, NameMother


def test_name_mother_happy_path() -> None:
    """
    Test NameMother happy path.
    """
    value = NameMother.create()

    assert type(value) is str
    assert 3 <= len(value) <= 128


def test_name_mother_value() -> None:
    """
    Test NameMother create method with value.
    """
    value = NameMother.create()

    assert NameMother.create(value=value) == value


def test_name_mother_of_length_method() -> None:
    """
    Test NameMother of_length method.
    """
    text_length = IntegerMother.create(min=3, max=128)
    value = NameMother.of_length(length=text_length)

    assert type(value) is str
    assert len(value) == text_length


def test_name_mother_invalid_type() -> None:
    """
    Test NameMother create method with invalid type.
    """
    assert type(NameMother.invalid_type()) is not str


def test_name_mother_invalid_value_type() -> None:
    """
    Test NameMother create method with invalid value type.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='NameMother value must be a string.',
    ):
        NameMother.create(value=NameMother.invalid_type())


def test_name_mother_invalid_min_length_type() -> None:
    """
    Test NameMother create method with invalid min length type.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='NameMother min_length must be an integer.',
    ):
        NameMother.create(min_length=IntegerMother.invalid_type())


def test_name_mother_invalid_max_length_type() -> None:
    """
    Test NameMother create method with invalid max length type.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='NameMother max_length must be an integer.',
    ):
        NameMother.create(max_length=IntegerMother.invalid_type())


def test_name_mother_min_length_less_than_three() -> None:
    """
    Test NameMother create method with min less than 3.
    """
    with assert_raises(
        expected_exception=ValueError,
        match='NameMother min_length must be greater than or equal to 3.',
    ):
        NameMother.create(min_length=IntegerMother.negative())


def test_name_mother_max_length_less_than_three() -> None:
    """
    Test NameMother create method with max less than 3.
    """
    with assert_raises(
        expected_exception=ValueError,
        match='NameMother max_length must be greater than or equal to 3.',
    ):
        NameMother.create(max_length=IntegerMother.negative())


def test_name_mother_min_length_greater_than_max_length() -> None:
    """
    Test NameMother create method with min greater than max.
    """
    min_value = IntegerMother.create(min=1, max=1024)
    max_value = IntegerMother.create(min=1025, max=2048)

    with assert_raises(
        expected_exception=ValueError,
        match='NameMother min_length must be less than or equal to max_length.',
    ):
        NameMother.create(min_length=max_value, max_length=min_value)
