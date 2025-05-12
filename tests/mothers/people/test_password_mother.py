"""
Test module for the PasswordMother class.
"""

from pytest import mark, raises as assert_raises

from object_mother_pattern.mothers import BooleanMother, IntegerMother, StringMother
from object_mother_pattern.mothers.people import PasswordMother
from object_mother_pattern.mothers.primitives.utils.alphabets import (
    ALPHABET_LOWERCASE_BASIC,
    SUPER_SPECIAL_CHARS,
)


@mark.unit_testing
def test_password_mother_happy_path() -> None:
    """
    Test PasswordMother create method happy path with default parameters.
    """
    value = PasswordMother.create()

    assert type(value) is str
    assert len(value) == 12


@mark.unit_testing
def test_password_mother_create_with_value() -> None:
    """
    Test PasswordMother create method with specific value.
    """
    value = PasswordMother.create()

    assert PasswordMother.create(value=value) == value


@mark.unit_testing
def test_password_mother_invalid_value_type() -> None:
    """
    Test PasswordMother create method with invalid value type.
    """
    with assert_raises(expected_exception=TypeError, match='PasswordMother value must be a string.'):
        PasswordMother.create(value=PasswordMother.invalid_type())


@mark.unit_testing
def test_password_mother_create_with_custom_counts() -> None:
    """
    Test PasswordMother create method with custom character counts.
    """
    lowercase_count = IntegerMother.positive()
    uppercase_count = IntegerMother.positive()
    digits_count = IntegerMother.positive()
    special_characters_count = IntegerMother.positive()
    super_special_characters_count = IntegerMother.positive()
    length = (
        lowercase_count + uppercase_count + digits_count + special_characters_count + super_special_characters_count
    )

    value = PasswordMother.create(
        lowercase_count=lowercase_count,
        uppercase_count=uppercase_count,
        digits_count=digits_count,
        special_characters_count=special_characters_count,
        super_special_characters_count=super_special_characters_count,
    )

    assert type(value) is str
    assert len(value) == length


@mark.unit_testing
def test_password_mother_create_sample_size_greater_than_sequence_length() -> None:
    """
    Test PasswordMother create method with sample_size greater than sequence length.
    """
    lowercase_count = IntegerMother.create(min=len(ALPHABET_LOWERCASE_BASIC))

    with assert_raises(
        expected_exception=ValueError,
        match='PasswordMother sample_size must be less than or equal to the length of the sequence.',
    ):
        PasswordMother.create(
            lowercase_count=lowercase_count,
            lowercase_alphabet=ALPHABET_LOWERCASE_BASIC,
            uppercase_count=0,
            digits_count=0,
            special_characters_count=0,
            super_special_characters_count=0,
            exclude_duplicates=True,
        )


@mark.unit_testing
def test_password_mother_create_sample_size_greater_than_sequence_length_with_duplicates() -> None:
    """
    Test PasswordMother create method with sample_size greater than sequence length and duplicates allowed.
    """
    lowercase_count = IntegerMother.create(min=len(ALPHABET_LOWERCASE_BASIC))

    value = PasswordMother.create(
        lowercase_count=lowercase_count,
        lowercase_alphabet=ALPHABET_LOWERCASE_BASIC,
        uppercase_count=0,
        digits_count=0,
        special_characters_count=0,
        super_special_characters_count=0,
        exclude_duplicates=False,
    )

    assert type(value) is str
    assert len(value) == lowercase_count


@mark.unit_testing
def test_password_mother_invalid_lowercase_count_type() -> None:
    """
    Test PasswordMother create method with invalid lowercase_count type.
    """
    with assert_raises(expected_exception=TypeError, match='PasswordMother lowercase_count value must be an integer.'):
        PasswordMother.create(lowercase_count=IntegerMother.invalid_type())


@mark.unit_testing
def test_password_mother_invalid_uppercase_count_type() -> None:
    """
    Test PasswordMother create method with invalid uppercase_count type.
    """
    with assert_raises(expected_exception=TypeError, match='PasswordMother uppercase_count value must be an integer.'):
        PasswordMother.create(uppercase_count=IntegerMother.invalid_type())


@mark.unit_testing
def test_password_mother_invalid_digits_count_type() -> None:
    """
    Test PasswordMother create method with invalid digits_count type.
    """
    with assert_raises(expected_exception=TypeError, match='PasswordMother digits_count value must be an integer.'):
        PasswordMother.create(digits_count=IntegerMother.invalid_type())


@mark.unit_testing
def test_password_mother_invalid_special_characters_count_type() -> None:
    """
    Test PasswordMother create method with invalid special_characters_count type.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='PasswordMother special_characters_count value must be an integer.',
    ):
        PasswordMother.create(special_characters_count=IntegerMother.invalid_type())


@mark.unit_testing
def test_password_mother_invalid_super_special_characters_count_type() -> None:
    """
    Test PasswordMother create method with invalid super_special_characters_count type.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='PasswordMother super_special_characters_count value must be an integer.',
    ):
        PasswordMother.create(super_special_characters_count=IntegerMother.invalid_type())


@mark.unit_testing
def test_password_mother_invalid_lowercase_alphabet_type() -> None:
    """
    Test PasswordMother create method with invalid lowercase_alphabet type.
    """
    with assert_raises(expected_exception=TypeError, match='PasswordMother lowercase_alphabet value must be a string.'):
        PasswordMother.create(lowercase_alphabet=StringMother.invalid_type())


@mark.unit_testing
def test_password_mother_invalid_uppercase_alphabet_type() -> None:
    """
    Test PasswordMother create method with invalid uppercase_alphabet type.
    """
    with assert_raises(expected_exception=TypeError, match='PasswordMother uppercase_alphabet value must be a string.'):
        PasswordMother.create(uppercase_alphabet=StringMother.invalid_type())


@mark.unit_testing
def test_password_mother_invalid_digits_alphabet_type() -> None:
    """
    Test PasswordMother create method with invalid digits_alphabet type.
    """
    with assert_raises(expected_exception=TypeError, match='PasswordMother digits_alphabet value must be a string.'):
        PasswordMother.create(digits_alphabet=StringMother.invalid_type())


@mark.unit_testing
def test_password_mother_invalid_special_characters_alphabet_type() -> None:
    """
    Test PasswordMother create method with invalid special_characters_alphabet type.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='PasswordMother special_characters_alphabet value must be a string.',
    ):
        PasswordMother.create(special_characters_alphabet=StringMother.invalid_type())


@mark.unit_testing
def test_password_mother_invalid_super_special_characters_alphabet_type() -> None:
    """
    Test PasswordMother create method with invalid super_special_characters_alphabet type.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='PasswordMother super_special_characters_alphabet value must be a string.',
    ):
        PasswordMother.create(super_special_characters_alphabet=StringMother.invalid_type())


@mark.unit_testing
def test_password_mother_invalid_exclude_duplicates_type() -> None:
    """
    Test PasswordMother create method with invalid exclude_duplicates type.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='PasswordMother exclude_duplicates value must be a boolean.',
    ):
        PasswordMother.create(exclude_duplicates=BooleanMother.invalid_type())


@mark.unit_testing
def test_password_mother_negative_lowercase_count() -> None:
    """
    Test PasswordMother create method with negative lowercase_count.
    """
    with assert_raises(
        expected_exception=ValueError,
        match='PasswordMother lowercase_count value must be greater than or equal to 0.',
    ):
        PasswordMother.create(lowercase_count=IntegerMother.negative())


@mark.unit_testing
def test_password_mother_negative_uppercase_count() -> None:
    """
    Test PasswordMother create method with negative uppercase_count.
    """
    with assert_raises(
        expected_exception=ValueError,
        match='PasswordMother uppercase_count value must be greater than or equal to 0.',
    ):
        PasswordMother.create(uppercase_count=IntegerMother.negative())


@mark.unit_testing
def test_password_mother_negative_digits_count() -> None:
    """
    Test PasswordMother create method with negative digits_count.
    """
    with assert_raises(
        expected_exception=ValueError,
        match='PasswordMother digits_count value must be greater than or equal to 0.',
    ):
        PasswordMother.create(digits_count=IntegerMother.negative())


@mark.unit_testing
def test_password_mother_negative_special_characters_count() -> None:
    """
    Test PasswordMother create method with negative special_characters_count.
    """
    with assert_raises(
        expected_exception=ValueError,
        match='PasswordMother special_characters_count value must be greater than or equal to 0.',
    ):
        PasswordMother.create(special_characters_count=IntegerMother.negative())


@mark.unit_testing
def test_password_mother_negative_super_special_characters_count() -> None:
    """
    Test PasswordMother create method with negative super_special_characters_count.
    """
    with assert_raises(
        expected_exception=ValueError,
        match='PasswordMother super_special_characters_count value must be greater than or equal to 0.',
    ):
        PasswordMother.create(super_special_characters_count=IntegerMother.negative())


@mark.unit_testing
def test_password_mother_random_length_happy_path() -> None:
    """
    Test PasswordMother random_length method happy path.
    """
    min_length = IntegerMother.create(min=0, max=16)
    max_length = IntegerMother.create(min=16, max=32)
    value = PasswordMother.random_length(min_length=min_length, max_length=max_length)

    assert type(value) is str
    assert min_length <= len(value) <= max_length


@mark.unit_testing
def test_password_mother_random_length_exclude_super_special() -> None:
    """
    Test PasswordMother random_length method with exclude_super_special.
    """
    min_length = IntegerMother.create(min=0, max=16)
    max_length = IntegerMother.create(min=16, max=32)
    value = PasswordMother.random_length(min_length=min_length, max_length=max_length, exclude_super_special=True)

    assert type(value) is str
    assert min_length <= len(value) <= max_length
    assert not any(char in value for char in SUPER_SPECIAL_CHARS)


@mark.unit_testing
def test_password_mother_random_length_invalid_min_length_type() -> None:
    """
    Test PasswordMother random_length method with invalid min_length type.
    """
    with assert_raises(expected_exception=TypeError, match='PasswordMother min_length value must be an integer.'):
        PasswordMother.random_length(min_length=IntegerMother.invalid_type())


@mark.unit_testing
def test_password_mother_random_length_invalid_max_length_type() -> None:
    """
    Test PasswordMother random_length method with invalid max_length type.
    """
    with assert_raises(expected_exception=TypeError, match='PasswordMother max_length value must be an integer.'):
        PasswordMother.random_length(max_length=IntegerMother.invalid_type())


@mark.unit_testing
def test_password_mother_random_length_min_length_less_than_or_equal_to_zero() -> None:
    """
    Test PasswordMother random_length method with min_length <= 0.
    """
    with assert_raises(expected_exception=ValueError, match='PasswordMother min_length value must be greater than 0.'):
        PasswordMother.random_length(min_length=IntegerMother.create(max=0))


@mark.unit_testing
def test_password_mother_random_length_max_length_less_than_or_equal_to_zero() -> None:
    """
    Test PasswordMother random_length method with max_length <= 0.
    """
    with assert_raises(expected_exception=ValueError, match='PasswordMother max_length value must be greater than 0.'):
        PasswordMother.random_length(max_length=IntegerMother.create(max=0))


@mark.unit_testing
def test_password_mother_random_length_min_length_greater_than_max_length() -> None:
    """
    Test PasswordMother random_length method with min_length > max_length.
    """
    min_length = IntegerMother.create(min=16, max=32)
    max_length = IntegerMother.create(min=1, max=15)

    with assert_raises(
        expected_exception=ValueError,
        match='PasswordMother min_length value must be less than or equal to max_length.',
    ):
        PasswordMother.random_length(min_length=min_length, max_length=max_length)


@mark.unit_testing
def test_password_mother_random_length_invalid_exclude_duplicates_type() -> None:
    """
    Test PasswordMother random_length method with invalid exclude_duplicates type.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='PasswordMother exclude_duplicates value must be a boolean.',
    ):
        PasswordMother.random_length(exclude_duplicates=BooleanMother.invalid_type())


@mark.unit_testing
def test_password_mother_random_length_invalid_exclude_super_special_type() -> None:
    """
    Test PasswordMother random_length method with invalid exclude_super_special type.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='PasswordMother exclude_super_special value must be a boolean.',
    ):
        PasswordMother.random_length(exclude_super_special=BooleanMother.invalid_type())


@mark.unit_testing
def test_password_mother_of_length_happy_path() -> None:
    """
    Test PasswordMother of_length method happy path.
    """
    length = IntegerMother.positive()
    value = PasswordMother.of_length(length=length)

    assert type(value) is str
    assert len(value) == length


@mark.unit_testing
def test_password_mother_of_length_invalid_length_type() -> None:
    """
    Test PasswordMother of_length method with invalid length type.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='PasswordMother length value must be an integer.',
    ):
        PasswordMother.of_length(length=IntegerMother.invalid_type())


@mark.unit_testing
def test_password_mother_of_length_invalid_exclude_super_special_type() -> None:
    """
    Test PasswordMother of_length method with invalid exclude_super_special type.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='PasswordMother exclude_super_special value must be a boolean.',
    ):
        PasswordMother.of_length(length=IntegerMother.positive(), exclude_super_special=BooleanMother.invalid_type())


@mark.unit_testing
def test_password_mother_of_length_invalid_exclude_duplicates_type() -> None:
    """
    Test PasswordMother of_length method with invalid exclude_duplicates type.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='PasswordMother exclude_duplicates value must be a boolean.',
    ):
        PasswordMother.of_length(length=IntegerMother.positive(), exclude_duplicates=BooleanMother.invalid_type())


@mark.unit_testing
def test_password_mother_of_length_length_less_than_or_equal_to_zero() -> None:
    """
    Test PasswordMother of_length method with length <= 0.
    """
    with assert_raises(
        expected_exception=ValueError,
        match='PasswordMother length value must be greater than 0.',
    ):
        PasswordMother.of_length(length=IntegerMother.create(max=0))


@mark.unit_testing
def test_password_mother_of_length_exclude_super_special() -> None:
    """
    Test PasswordMother of_length method with exclude_super_special.
    """
    length = IntegerMother.positive()
    value = PasswordMother.of_length(length=length, exclude_super_special=True)

    assert type(value) is str
    assert len(value) == length
    assert not any(char in value for char in SUPER_SPECIAL_CHARS)


@mark.unit_testing
def test_password_mother_invalid_type() -> None:
    """
    Test PasswordMother invalid_type method.
    """
    value = PasswordMother.invalid_type()

    assert type(value) is not str


@mark.unit_testing
def test_password_mother_invalid_value() -> None:
    """
    Test PasswordMother invalid_value method.
    """
    value = PasswordMother.invalid_value()

    assert type(value) is str
    assert not value.isprintable()
