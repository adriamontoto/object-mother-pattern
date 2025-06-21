"""
Test module for the BytesMother class.
"""

from pytest import mark, raises as assert_raises

from object_mother_pattern.mothers import BytesMother, IntegerMother


@mark.unit_testing
def test_bytes_mother_create_method_happy_path() -> None:
    """
    Check that BytesMother create method returns a bytes value with a length between 0 and 128.
    """
    value = BytesMother.create()

    assert type(value) is bytes
    assert 0 <= len(value) <= 128


@mark.unit_testing
def test_bytes_mother_create_method_value() -> None:
    """
    Check that BytesMother create method returns the provided value.
    """
    value = BytesMother.create()

    assert BytesMother.create(value=value) == value


@mark.unit_testing
def test_bytes_mother_create_method_invalid_value_type() -> None:
    """
    Check that BytesMother create method raises a TypeError when the provided value is not a value of type bytes.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='BytesMother value must be bytes.',
    ):
        BytesMother.create(value=BytesMother.invalid_type())


@mark.unit_testing
def test_bytes_mother_create_method_min_length_value() -> None:
    """
    Check that BytesMother create method min_length parameter is the minimum permitted value.
    """
    BytesMother.create(min_length=0)


@mark.unit_testing
def test_bytes_mother_create_method_min_length_random_value() -> None:
    """
    Check that BytesMother create method min_length parameter is a random positive integer.
    """
    min_length = IntegerMother.positive()

    BytesMother.create(min_length=min_length)


@mark.unit_testing
def test_bytes_mother_create_method_invalid_min_length_type() -> None:
    """
    Check that BytesMother create method raises a TypeError when the provided min_length is not an integer.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='BytesMother min_length must be an integer.',
    ):
        BytesMother.create(min_length=IntegerMother.invalid_type())


@mark.unit_testing
def test_bytes_mother_create_method_min_length_negative_value() -> None:
    """
    Check that BytesMother create method raises a ValueError when the provided min_length is negative.
    """
    with assert_raises(
        expected_exception=ValueError,
        match='BytesMother min_length must be greater than or equal to 0.',
    ):
        BytesMother.create(min_length=-1)


@mark.unit_testing
def test_bytes_mother_create_method_min_length_random_negative_value() -> None:
    """
    Check that BytesMother create method raises a ValueError when the provided min_length is a random negative value.
    """
    with assert_raises(
        expected_exception=ValueError,
        match='BytesMother min_length must be greater than or equal to 0.',
    ):
        BytesMother.create(min_length=IntegerMother.negative())


@mark.unit_testing
def test_bytes_mother_create_method_max_length_value() -> None:
    """
    Check that BytesMother create method max_length parameter is the minimum permitted value.
    """
    BytesMother.create(max_length=1)


@mark.unit_testing
def test_bytes_mother_create_method_max_length_random_value() -> None:
    """
    Check that BytesMother create method max_length parameter is a random positive integer.
    """
    max_length = IntegerMother.positive()

    BytesMother.create(max_length=max_length)


@mark.unit_testing
def test_bytes_mother_create_method_invalid_max_length_type() -> None:
    """
    Check that BytesMother create method raises a TypeError when the provided max_length is not an integer.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='BytesMother max_length must be an integer.',
    ):
        BytesMother.create(max_length=IntegerMother.invalid_type())


@mark.unit_testing
def test_bytes_mother_create_method_max_length_negative_value() -> None:
    """
    Check that BytesMother create method raises a ValueError when the provided max_length is negative.
    """
    with assert_raises(
        expected_exception=ValueError,
        match='BytesMother max_length must be greater than or equal to 0.',
    ):
        BytesMother.create(max_length=-1)


@mark.unit_testing
def test_bytes_mother_create_method_max_length_random_negative_value() -> None:
    """
    Check that BytesMother create method raises a ValueError when the provided max_length is a random negative value.
    """
    with assert_raises(
        expected_exception=ValueError,
        match='BytesMother max_length must be greater than or equal to 0.',
    ):
        BytesMother.create(max_length=IntegerMother.negative())


@mark.unit_testing
def test_bytes_mother_create_method_min_length_greater_than_max_length() -> None:
    """
    Check that BytesMother create method raises a ValueError when the provided min_length is greater than max_length.
    """
    min_length = IntegerMother.create(min=0, max=15)
    max_length = IntegerMother.create(min=16, max=32)

    with assert_raises(
        expected_exception=ValueError,
        match='BytesMother min_length must be less than or equal to max_length.',
    ):
        BytesMother.create(min_length=max_length, max_length=min_length)


@mark.unit_testing
def test_bytes_mother_empty_method_happy_path() -> None:
    """
    Check that BytesMother empty method returns an empty bytes value.
    """
    value = BytesMother.empty()

    assert type(value) is bytes
    assert len(value) == 0


@mark.unit_testing
def test_bytes_mother_of_length_method_happy_path() -> None:
    """
    Check that BytesMother of_length method returns a bytes value with a length equal to the provided length.
    """
    length = IntegerMother.positive_or_zero()
    value = BytesMother.of_length(length=length)

    assert type(value) is bytes
    assert len(value) == length


@mark.unit_testing
def test_bytes_mother_of_length_method_invalid_length_type() -> None:
    """
    Check that BytesMother of_length method raises a TypeError when the provided length is not an integer.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='BytesMother length must be an integer.',
    ):
        BytesMother.of_length(length=IntegerMother.invalid_type())


@mark.unit_testing
def test_bytes_mother_of_length_method_length_value() -> None:
    """
    Check that BytesMother of_length method returns a bytes value with a length equal to 1.
    """
    BytesMother.of_length(length=1)


@mark.unit_testing
def test_bytes_mother_of_length_method_length_negative_value() -> None:
    """
    Check that BytesMother of_length method raises a ValueError when the provided length is less than 0.
    """
    with assert_raises(
        expected_exception=ValueError,
        match='BytesMother length must be greater than or equal to 1.',
    ):
        BytesMother.of_length(length=0)


@mark.unit_testing
def test_bytes_mother_of_length_method_length_value_random_negative() -> None:
    """
    Check that BytesMother of_length method raises a ValueError when the provided length is a random negative value.
    """
    with assert_raises(
        expected_exception=ValueError,
        match='BytesMother length must be greater than or equal to 1.',
    ):
        BytesMother.of_length(length=IntegerMother.negative())


@mark.unit_testing
def test_bytes_mother_invalid_type_method() -> None:
    """
    Test BytesMother create method with invalid type.
    """
    assert type(BytesMother.invalid_type()) is not bytes
