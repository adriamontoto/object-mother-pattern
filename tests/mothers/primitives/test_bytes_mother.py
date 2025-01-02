"""
Test module for the BytesMother class.
"""

from pytest import raises as assert_raises

from object_mother_pattern.mothers import BytesMother, IntegerMother


def test_bytes_mother_happy_path() -> None:
    """
    Test BytesMother happy path.
    """
    value = BytesMother.create()

    assert type(value) is bytes


def test_bytes_mother_value() -> None:
    """
    Test BytesMother create method with value.
    """
    value = BytesMother.create()

    assert BytesMother.create(value=value) == value


def test_bytes_mother_invalid_type() -> None:
    """
    Test BytesMother create method with invalid type.
    """
    assert type(BytesMother.invalid_type()) is not bytes


def test_bytes_mother_invalid_value_type() -> None:
    """
    Test BytesMother create method with invalid value type.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='BytesMother value must be bytes.',
    ):
        BytesMother.create(value=BytesMother.invalid_type())


def test_bytes_mother_invalid_min_length_type() -> None:
    """
    Test BytesMother create method with invalid min_length type.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='BytesMother min_length must be an integer.',
    ):
        BytesMother.create(min_length=IntegerMother.invalid_type())


def test_bytes_mother_invalid_min_length_value() -> None:
    """
    Test BytesMother create method with invalid min_length value.
    """
    with assert_raises(
        expected_exception=ValueError,
        match='BytesMother min_length must be greater than 0.',
    ):
        BytesMother.create(min_length=IntegerMother.negative())


def test_bytes_mother_invalid_max_length_type() -> None:
    """
    Test BytesMother create method with invalid max_length type.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='BytesMother max_length must be an integer.',
    ):
        BytesMother.create(max_length=IntegerMother.invalid_type())


def test_bytes_mother_invalid_max_length_value() -> None:
    """
    Test BytesMother create method with invalid max_length value.
    """
    with assert_raises(
        expected_exception=ValueError,
        match='BytesMother max_length must be greater than 0.',
    ):
        BytesMother.create(max_length=IntegerMother.negative())


def test_bytes_mother_min_length_greater_than_max_length() -> None:
    """
    Test BytesMother create method with min_length greater than max_length.
    """
    min_value = IntegerMother.create(min=0)
    max_value = IntegerMother.create(min=1000, max=2000)

    with assert_raises(
        expected_exception=ValueError,
        match='BytesMother min_length must be less than or equal to max_length.',
    ):
        BytesMother.create(min_length=max_value, max_length=min_value)


def test_bytes_mother_of_length() -> None:
    """
    Test BytesMother of_length method.
    """
    length = IntegerMother.create(min=0)
    value = BytesMother.of_length(length=length)

    assert len(value) == length


def test_bytes_mother_of_length_invalid_length_type() -> None:
    """
    Test BytesMother of_length method with invalid length type.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='BytesMother min_length must be an integer.',
    ):
        BytesMother.of_length(length=IntegerMother.invalid_type())


def test_bytes_mother_of_length_invalid_length_value() -> None:
    """
    Test BytesMother of_length method with invalid length value.
    """
    with assert_raises(
        expected_exception=ValueError,
        match='BytesMother min_length must be greater than 0.',
    ):
        BytesMother.of_length(length=IntegerMother.negative())
