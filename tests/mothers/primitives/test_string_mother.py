"""
Test module for the StringMother class.
"""

from pytest import mark, raises as assert_raises

from object_mother_pattern.mothers import IntegerMother, StringMother


@mark.unit_testing
def test_string_mother_create_method_happy_path() -> None:
    """
    Check that StringMother create method returns a string value with a length between 1 and 128.
    """
    value = StringMother.create()

    assert type(value) is str
    assert 1 <= len(value) <= 128


@mark.unit_testing
def test_string_mother_create_method_value() -> None:
    """
    Check that StringMother create method returns the provided value.
    """
    value = StringMother.create()

    assert StringMother.create(value=value) == value


@mark.unit_testing
def test_string_mother_create_method_invalid_value_type() -> None:
    """
    Check that StringMother create method raises a TypeError when the provided value is not a string.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='StringMother value must be a string.',
    ):
        StringMother.create(value=StringMother.invalid_type())


@mark.unit_testing
def test_string_mother_create_method_min_length_value() -> None:
    """
    Check that StringMother create method min_length parameter is the minimum permitted value.
    """
    StringMother.create(min_length=0)


@mark.unit_testing
def test_string_mother_create_method_min_length_random_value() -> None:
    """
    Check that StringMother create method min_length parameter is a random positive integer.
    """
    min_length = IntegerMother.positive()

    StringMother.create(min_length=min_length)


@mark.unit_testing
def test_string_mother_create_method_invalid_min_length_type() -> None:
    """
    Check that StringMother create method raises a TypeError when the provided min_length is not an integer.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='StringMother min_length must be an integer.',
    ):
        StringMother.create(min_length=IntegerMother.invalid_type())


@mark.unit_testing
def test_string_mother_create_method_invalid_max_length_type() -> None:
    """
    Check that StringMother create method raises a TypeError when the provided max_length is not an integer.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='StringMother max_length must be an integer.',
    ):
        StringMother.create(max_length=IntegerMother.invalid_type())


@mark.unit_testing
def test_string_mother_create_method_min_length_negative_value() -> None:
    """
    Check that StringMother create method raises a ValueError when the provided min_length is negative.
    """
    with assert_raises(
        expected_exception=ValueError,
        match='StringMother min_length must be greater than or equal to 0.',
    ):
        StringMother.create(min_length=-1)


@mark.unit_testing
def test_string_mother_create_method_invalid_min_length_random_negative_value() -> None:
    """
    Check that StringMother create method raises a ValueError when the provided min_length is negative.
    """
    with assert_raises(
        expected_exception=ValueError,
        match='StringMother min_length must be greater than or equal to 0.',
    ):
        StringMother.create(min_length=IntegerMother.negative())


@mark.unit_testing
def test_string_mother_create_method_max_length_value() -> None:
    """
    Check that StringMother create method max_length parameter is the minimum permitted value.
    """
    StringMother.create(min_length=0, max_length=0)


@mark.unit_testing
def test_string_mother_create_method_min_length_max_length_value() -> None:
    """
    Check that StringMother create method min_length and max_length parameters are the minimum permitted value.
    """
    StringMother.create(min_length=0, max_length=1)


@mark.unit_testing
def test_string_mother_create_method_max_length_random_value() -> None:
    """
    Check that StringMother create method max_length parameter is a random positive integer.
    """
    max_length = IntegerMother.positive()

    StringMother.create(max_length=max_length)


@mark.unit_testing
def test_string_mother_create_method_max_length_negative_value() -> None:
    """
    Check that StringMother create method raises a ValueError when the provided max_length is negative.
    """
    with assert_raises(
        expected_exception=ValueError,
        match='StringMother max_length must be greater than or equal to 0.',
    ):
        StringMother.create(max_length=-1)


@mark.unit_testing
def test_string_mother_create_method_max_random_length_value() -> None:
    """
    Check that StringMother create method raises a ValueError when the provided max_length is negative.
    """
    with assert_raises(
        expected_exception=ValueError,
        match='StringMother max_length must be greater than or equal to 0.',
    ):
        StringMother.create(max_length=IntegerMother.negative())


@mark.unit_testing
def test_string_mother_create_method_min_length_greater_than_max_length() -> None:
    """
    Check that StringMother create method raises a ValueError when the provided min_length is greater than max_length.
    """
    min_length = IntegerMother.create(min=0, max=15)
    max_length = IntegerMother.create(min=16, max=32)

    with assert_raises(
        expected_exception=ValueError,
        match='StringMother min_length must be less than or equal to max_length.',
    ):
        StringMother.create(min_length=max_length, max_length=min_length)


@mark.unit_testing
def test_string_mother_create_method_invalid_characters_type() -> None:
    """
    Check that StringMother create method raises a TypeError when the provided characters is not a string.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='StringMother characters must be a string.',
    ):
        StringMother.create(characters=StringMother.invalid_type())


@mark.unit_testing
def test_string_mother_create_method_invalid_characters_value() -> None:
    """
    Check that StringMother create method raises a ValueError when the provided characters is empty.
    """
    with assert_raises(
        expected_exception=ValueError,
        match='StringMother characters must not be empty.',
    ):
        StringMother.create(characters=StringMother.empty())


@mark.unit_testing
def test_string_mother_empty_method_happy_path() -> None:
    """
    Check that StringMother empty method returns an empty string.
    """
    value = StringMother.empty()

    assert type(value) is str
    assert value == ''


@mark.unit_testing
def test_string_mother_of_length_method_happy_path() -> None:
    """
    Check that StringMother of_length method returns a string value with a length equal to the provided length.
    """
    length = IntegerMother.positive()
    value = StringMother.of_length(length=length)

    assert type(value) is str
    assert len(value) == length


@mark.unit_testing
def test_string_mother_of_length_method_invalid_length_type() -> None:
    """
    Check that StringMother of_length method raises a TypeError when the provided length is not an integer.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='StringMother min_length must be an integer.',
    ):
        StringMother.of_length(length=IntegerMother.invalid_type())


@mark.unit_testing
def test_string_mother_of_length_method_minimum_length_value() -> None:
    """
    Check that StringMother of_length method length parameter is the minimum permitted value.
    """
    StringMother.of_length(length=0)


@mark.unit_testing
def test_string_mother_of_length_method_length_random_positive_value() -> None:
    """
    Check that StringMother of_length method length parameter is a random positive integer.
    """
    length = IntegerMother.positive()
    StringMother.of_length(length=length)


@mark.unit_testing
def test_string_mother_of_length_method_invalid_length_negative_value() -> None:
    """
    Check that StringMother of_length method raises a ValueError when the provided length is negative.
    """
    with assert_raises(
        expected_exception=ValueError,
        match='StringMother min_length must be greater than or equal to 0.',
    ):
        StringMother.of_length(length=-1)


@mark.unit_testing
def test_string_mother_of_length_method_invalid_length_random_negative_value() -> None:
    """
    Check that StringMother of_length method raises a ValueError when the provided length is negative.
    """
    with assert_raises(
        expected_exception=ValueError,
        match='StringMother min_length must be greater than or equal to 0.',
    ):
        StringMother.of_length(length=IntegerMother.negative())


@mark.unit_testing
def test_string_mother_lowercase_method_happy_path() -> None:
    """
    Check that StringMother lowercase method returns a lowercase string value.
    """
    value = StringMother.lowercase()

    assert type(value) is str
    assert value.islower()
    assert 1 <= len(value) <= 128


@mark.unit_testing
def test_string_mother_lowercase_method_min_length_value() -> None:
    """
    Check that StringMother lowercase method min_length parameter is the minimum permitted value.
    """
    StringMother.lowercase(min_length=0)


@mark.unit_testing
def test_string_mother_lowercase_method_min_length_random_value() -> None:
    """
    Check that StringMother lowercase method min_length parameter is a random positive integer.
    """
    min_length = IntegerMother.positive()

    StringMother.lowercase(min_length=min_length)


@mark.unit_testing
def test_string_mother_lowercase_method_invalid_min_length_type() -> None:
    """
    Check that StringMother lowercase method raises a TypeError when the provided min_length is not an integer.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='StringMother min_length must be an integer.',
    ):
        StringMother.lowercase(min_length=IntegerMother.invalid_type())


@mark.unit_testing
def test_string_mother_lowercase_method_invalid_max_length_type() -> None:
    """
    Check that StringMother lowercase method raises a TypeError when the provided max_length is not an integer.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='StringMother max_length must be an integer.',
    ):
        StringMother.lowercase(max_length=IntegerMother.invalid_type())


@mark.unit_testing
def test_string_mother_lowercase_method_min_length_negative_value() -> None:
    """
    Check that StringMother lowercase method raises a ValueError when the provided min_length is negative.
    """
    with assert_raises(
        expected_exception=ValueError,
        match='StringMother min_length must be greater than or equal to 0.',
    ):
        StringMother.lowercase(min_length=-1)


@mark.unit_testing
def test_string_mother_lowercase_method_invalid_min_length_value() -> None:
    """
    Check that StringMother lowercase method raises a ValueError when the provided min_length is negative.
    """
    with assert_raises(
        expected_exception=ValueError, match='StringMother min_length must be greater than or equal to 0.'
    ):
        StringMother.lowercase(min_length=IntegerMother.negative())


@mark.unit_testing
def test_string_mother_lowercase_method_max_length_value() -> None:
    """
    Check that StringMother lowercase method max_length parameter is the minimum permitted value.
    """
    StringMother.lowercase(min_length=0, max_length=0)


@mark.unit_testing
def test_string_mother_lowercase_method_min_length_max_length_value() -> None:
    """
    Check that StringMother lowercase method min_length and max_length parameters are the minimum permitted value.
    """
    StringMother.lowercase(min_length=0, max_length=1)


@mark.unit_testing
def test_string_mother_lowercase_method_max_length_random_value() -> None:
    """
    Check that StringMother lowercase method max_length parameter is a random positive integer.
    """
    max_length = IntegerMother.positive()

    StringMother.lowercase(max_length=max_length)


@mark.unit_testing
def test_string_mother_lowercase_method_max_length_negative_value() -> None:
    """
    Check that StringMother lowercase method raises a ValueError when the provided max_length is negative.
    """
    with assert_raises(
        expected_exception=ValueError,
        match='StringMother max_length must be greater than or equal to 0.',
    ):
        StringMother.lowercase(max_length=-1)


@mark.unit_testing
def test_string_mother_lowercase_method_invalid_max_length_value() -> None:
    """
    Check that StringMother lowercase method raises a ValueError when the provided max_length is negative.
    """
    with assert_raises(
        expected_exception=ValueError,
        match='StringMother max_length must be greater than or equal to 0.',
    ):
        StringMother.lowercase(max_length=IntegerMother.negative())


@mark.unit_testing
def test_string_mother_lowercase_method_min_length_greater_than_max_length() -> None:
    """
    Check that StringMother lowercase method raises a ValueError when the provided min_length is greater than
    max_length.
    """
    min_length = IntegerMother.create(min=0, max=15)
    max_length = IntegerMother.create(min=16, max=32)

    with assert_raises(
        expected_exception=ValueError,
        match='StringMother min_length must be less than or equal to max_length.',
    ):
        StringMother.lowercase(min_length=max_length, max_length=min_length)


@mark.unit_testing
def test_string_mother_uppercase_method_happy_path() -> None:
    """
    Check that StringMother uppercase method returns an uppercase string value.
    """
    value = StringMother.uppercase()

    assert type(value) is str
    assert value.isupper()
    assert 1 <= len(value) <= 128


@mark.unit_testing
def test_string_mother_uppercase_method_min_length_value() -> None:
    """
    Check that StringMother uppercase method min_length parameter is the minimum permitted value.
    """
    StringMother.uppercase(min_length=0)


@mark.unit_testing
def test_string_mother_uppercase_method_min_length_random_value() -> None:
    """
    Check that StringMother uppercase method min_length parameter is a random positive integer.
    """
    min_length = IntegerMother.positive()

    StringMother.uppercase(min_length=min_length)


@mark.unit_testing
def test_string_mother_uppercase_method_invalid_min_length_type() -> None:
    """
    Check that StringMother uppercase method raises a TypeError when the provided min_length is not an integer.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='StringMother min_length must be an integer.',
    ):
        StringMother.uppercase(min_length=IntegerMother.invalid_type())


@mark.unit_testing
def test_string_mother_uppercase_method_invalid_max_length_type() -> None:
    """
    Check that StringMother uppercase method raises a TypeError when the provided max_length is not an integer.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='StringMother max_length must be an integer.',
    ):
        StringMother.uppercase(max_length=IntegerMother.invalid_type())


@mark.unit_testing
def test_string_mother_uppercase_method_min_length_negative_value() -> None:
    """
    Check that StringMother uppercase method raises a ValueError when the provided min_length is negative.
    """
    with assert_raises(
        expected_exception=ValueError,
        match='StringMother min_length must be greater than or equal to 0.',
    ):
        StringMother.uppercase(min_length=-1)


@mark.unit_testing
def test_string_mother_uppercase_method_invalid_min_length_value() -> None:
    """
    Check that StringMother uppercase method raises a ValueError when the provided min_length is negative.
    """
    with assert_raises(
        expected_exception=ValueError, match='StringMother min_length must be greater than or equal to 0.'
    ):
        StringMother.uppercase(min_length=IntegerMother.negative())


@mark.unit_testing
def test_string_mother_uppercase_method_max_length_value() -> None:
    """
    Check that StringMother uppercase method max_length parameter is the minimum permitted value.
    """
    StringMother.uppercase(min_length=0, max_length=0)


@mark.unit_testing
def test_string_mother_uppercase_method_min_length_max_length_value() -> None:
    """
    Check that StringMother uppercase method min_length and max_length parameters are the minimum permitted value.
    """
    StringMother.uppercase(min_length=0, max_length=1)


@mark.unit_testing
def test_string_mother_uppercase_method_max_length_random_value() -> None:
    """
    Check that StringMother uppercase method max_length parameter is a random positive integer.
    """
    max_length = IntegerMother.positive()

    StringMother.uppercase(max_length=max_length)


@mark.unit_testing
def test_string_mother_uppercase_method_max_length_negative_value() -> None:
    """
    Check that StringMother uppercase method raises a ValueError when the provided max_length is negative.
    """
    with assert_raises(
        expected_exception=ValueError,
        match='StringMother max_length must be greater than or equal to 0.',
    ):
        StringMother.uppercase(max_length=-1)


@mark.unit_testing
def test_string_mother_uppercase_method_invalid_max_length_value() -> None:
    """
    Check that StringMother uppercase method raises a ValueError when the provided max_length is negative.
    """
    with assert_raises(
        expected_exception=ValueError,
        match='StringMother max_length must be greater than or equal to 0.',
    ):
        StringMother.uppercase(max_length=IntegerMother.negative())


@mark.unit_testing
def test_string_mother_uppercase_method_min_length_greater_than_max_length() -> None:
    """
    Check that StringMother uppercase method raises a ValueError when the provided min_length is greater than
    max_length.
    """
    min_length = IntegerMother.create(min=0, max=15)
    max_length = IntegerMother.create(min=16, max=32)

    with assert_raises(
        expected_exception=ValueError,
        match='StringMother min_length must be less than or equal to max_length.',
    ):
        StringMother.uppercase(min_length=max_length, max_length=min_length)


@mark.unit_testing
def test_string_mother_titlecase_method_happy_path() -> None:
    """
    Check that StringMother titlecase method returns a titlecase string value.
    """
    value = StringMother.titlecase()

    assert type(value) is str
    assert 1 <= len(value) <= 128
    assert value[0].isupper() and (value[1:].islower() or value[1:].isnumeric() or value[1:] == '')


@mark.unit_testing
def test_string_mother_titlecase_method_min_length_value() -> None:
    """
    Check that StringMother titlecase method min_length parameter is the minimum permitted value.
    """
    StringMother.titlecase(min_length=0)


@mark.unit_testing
def test_string_mother_titlecase_method_min_length_random_value() -> None:
    """
    Check that StringMother titlecase method min_length parameter is a random positive integer.
    """
    min_length = IntegerMother.positive()

    StringMother.titlecase(min_length=min_length)


@mark.unit_testing
def test_string_mother_titlecase_method_invalid_min_length_type() -> None:
    """
    Check that StringMother titlecase method raises a TypeError when the provided min_length is not an integer.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='StringMother min_length must be an integer.',
    ):
        StringMother.titlecase(min_length=IntegerMother.invalid_type())


@mark.unit_testing
def test_string_mother_titlecase_method_invalid_max_length_type() -> None:
    """
    Check that StringMother titlecase method raises a TypeError when the provided max_length is not an integer.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='StringMother max_length must be an integer.',
    ):
        StringMother.titlecase(max_length=IntegerMother.invalid_type())


@mark.unit_testing
def test_string_mother_titlecase_method_min_length_negative_value() -> None:
    """
    Check that StringMother titlecase method raises a ValueError when the provided min_length is negative.
    """
    with assert_raises(
        expected_exception=ValueError,
        match='StringMother min_length must be greater than or equal to 0.',
    ):
        StringMother.titlecase(min_length=-1)


@mark.unit_testing
def test_string_mother_titlecase_method_invalid_min_length_value() -> None:
    """
    Check that StringMother titlecase method raises a ValueError when the provided min_length is negative.
    """
    with assert_raises(
        expected_exception=ValueError, match='StringMother min_length must be greater than or equal to 0.'
    ):
        StringMother.titlecase(min_length=IntegerMother.negative())


@mark.unit_testing
def test_string_mother_titlecase_method_max_length_value() -> None:
    """
    Check that StringMother titlecase method max_length parameter is the minimum permitted value.
    """
    StringMother.titlecase(min_length=0, max_length=0)


@mark.unit_testing
def test_string_mother_titlecase_method_min_length_max_length_value() -> None:
    """
    Check that StringMother titlecase method min_length and max_length parameters are the minimum permitted value.
    """
    StringMother.titlecase(min_length=0, max_length=1)


@mark.unit_testing
def test_string_mother_titlecase_method_max_length_random_value() -> None:
    """
    Check that StringMother titlecase method max_length parameter is a random positive integer.
    """
    max_length = IntegerMother.positive()

    StringMother.titlecase(max_length=max_length)


@mark.unit_testing
def test_string_mother_titlecase_method_max_length_negative_value() -> None:
    """
    Check that StringMother titlecase method raises a ValueError when the provided max_length is negative.
    """
    with assert_raises(
        expected_exception=ValueError,
        match='StringMother max_length must be greater than or equal to 0.',
    ):
        StringMother.titlecase(max_length=-1)


@mark.unit_testing
def test_string_mother_titlecase_method_invalid_max_length_value() -> None:
    """
    Check that StringMother titlecase method raises a ValueError when the provided max_length is negative.
    """
    with assert_raises(
        expected_exception=ValueError,
        match='StringMother max_length must be greater than or equal to 0.',
    ):
        StringMother.titlecase(max_length=IntegerMother.negative())


@mark.unit_testing
def test_string_mother_titlecase_method_min_length_greater_than_max_length() -> None:
    """
    Check that StringMother titlecase method raises a ValueError when the provided min_length is greater than
    max_length.
    """
    min_length = IntegerMother.create(min=0, max=15)
    max_length = IntegerMother.create(min=16, max=32)

    with assert_raises(
        expected_exception=ValueError,
        match='StringMother min_length must be less than or equal to max_length.',
    ):
        StringMother.titlecase(min_length=max_length, max_length=min_length)


@mark.unit_testing
def test_string_mother_mixedcase_method_happy_path() -> None:
    """
    Check that StringMother mixedcase method returns a mixedcase string value.
    """
    value = StringMother.mixedcase()

    assert type(value) is str
    assert 1 <= len(value) <= 128
    assert any(char.islower() or char.isupper() for char in value)


@mark.unit_testing
def test_string_mother_mixedcase_method_min_length_value() -> None:
    """
    Check that StringMother mixedcase method min_length parameter is the minimum permitted value.
    """
    StringMother.mixedcase(min_length=0)


@mark.unit_testing
def test_string_mother_mixedcase_method_min_length_random_value() -> None:
    """
    Check that StringMother mixedcase method min_length parameter is a random positive integer.
    """
    min_length = IntegerMother.positive()

    StringMother.mixedcase(min_length=min_length)


@mark.unit_testing
def test_string_mother_mixedcase_method_invalid_min_length_type() -> None:
    """
    Check that StringMother mixedcase method raises a TypeError when the provided min_length is not an integer.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='StringMother min_length must be an integer.',
    ):
        StringMother.mixedcase(min_length=IntegerMother.invalid_type())


@mark.unit_testing
def test_string_mother_mixedcase_method_invalid_max_length_type() -> None:
    """
    Check that StringMother mixedcase method raises a TypeError when the provided max_length is not an integer.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='StringMother max_length must be an integer.',
    ):
        StringMother.mixedcase(max_length=IntegerMother.invalid_type())


@mark.unit_testing
def test_string_mother_mixedcase_method_min_length_negative_value() -> None:
    """
    Check that StringMother mixedcase method raises a ValueError when the provided min_length is negative.
    """
    with assert_raises(
        expected_exception=ValueError,
        match='StringMother min_length must be greater than or equal to 0.',
    ):
        StringMother.mixedcase(min_length=-1)


@mark.unit_testing
def test_string_mother_mixedcase_method_invalid_min_length_value() -> None:
    """
    Check that StringMother mixedcase method raises a ValueError when the provided min_length is negative.
    """
    with assert_raises(
        expected_exception=ValueError, match='StringMother min_length must be greater than or equal to 0.'
    ):
        StringMother.mixedcase(min_length=IntegerMother.negative())


@mark.unit_testing
def test_string_mother_mixedcase_method_max_length_value() -> None:
    """
    Check that StringMother mixedcase method max_length parameter is the minimum permitted value.
    """
    StringMother.mixedcase(min_length=0, max_length=0)


@mark.unit_testing
def test_string_mother_mixedcase_method_min_length_max_length_value() -> None:
    """
    Check that StringMother mixedcase method min_length and max_length parameters are the minimum permitted value.
    """
    StringMother.mixedcase(min_length=0, max_length=1)


@mark.unit_testing
def test_string_mother_mixedcase_method_max_length_random_value() -> None:
    """
    Check that StringMother mixedcase method max_length parameter is a random positive integer.
    """
    max_length = IntegerMother.positive()

    StringMother.mixedcase(max_length=max_length)


@mark.unit_testing
def test_string_mother_mixedcase_method_max_length_negative_value() -> None:
    """
    Check that StringMother mixedcase method raises a ValueError when the provided max_length is negative.
    """
    with assert_raises(
        expected_exception=ValueError,
        match='StringMother max_length must be greater than or equal to 0.',
    ):
        StringMother.mixedcase(max_length=-1)


@mark.unit_testing
def test_string_mother_mixedcase_method_invalid_max_length_value() -> None:
    """
    Check that StringMother mixedcase method raises a ValueError when the provided max_length is negative.
    """
    with assert_raises(
        expected_exception=ValueError,
        match='StringMother max_length must be greater than or equal to 0.',
    ):
        StringMother.mixedcase(max_length=IntegerMother.negative())


@mark.unit_testing
def test_string_mother_mixedcase_method_min_length_greater_than_max_length() -> None:
    """
    Check that StringMother mixedcase method raises a ValueError when the provided min_length is greater than
    max_length.
    """
    min_length = IntegerMother.create(min=0, max=15)
    max_length = IntegerMother.create(min=16, max=32)

    with assert_raises(
        expected_exception=ValueError,
        match='StringMother min_length must be less than or equal to max_length.',
    ):
        StringMother.mixedcase(min_length=max_length, max_length=min_length)


@mark.unit_testing
def test_string_mother_alpha_method_happy_path() -> None:
    """
    Check that StringMother alpha method returns an alpha string value.
    """
    value = StringMother.alpha()

    assert type(value) is str
    assert value.isalpha()
    assert 1 <= len(value) <= 128


@mark.unit_testing
def test_string_mother_alpha_method_min_length_value() -> None:
    """
    Check that StringMother alpha method min_length parameter is the minimum permitted value.
    """
    StringMother.alpha(min_length=0)


@mark.unit_testing
def test_string_mother_alpha_method_min_length_random_value() -> None:
    """
    Check that StringMother alpha method min_length parameter is a random positive integer.
    """
    min_length = IntegerMother.positive()

    StringMother.alpha(min_length=min_length)


@mark.unit_testing
def test_string_mother_alpha_method_invalid_min_length_type() -> None:
    """
    Check that StringMother alpha method raises a TypeError when the provided min_length is not an integer.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='StringMother min_length must be an integer.',
    ):
        StringMother.alpha(min_length=IntegerMother.invalid_type())


@mark.unit_testing
def test_string_mother_alpha_method_invalid_max_length_type() -> None:
    """
    Check that StringMother alpha method raises a TypeError when the provided max_length is not an integer.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='StringMother max_length must be an integer.',
    ):
        StringMother.alpha(max_length=IntegerMother.invalid_type())


@mark.unit_testing
def test_string_mother_alpha_method_min_length_negative_value() -> None:
    """
    Check that StringMother alpha method raises a ValueError when the provided min_length is negative.
    """
    with assert_raises(
        expected_exception=ValueError,
        match='StringMother min_length must be greater than or equal to 0.',
    ):
        StringMother.alpha(min_length=-1)


@mark.unit_testing
def test_string_mother_alpha_method_invalid_min_length_value() -> None:
    """
    Check that StringMother alpha method raises a ValueError when the provided min_length is negative.
    """
    with assert_raises(
        expected_exception=ValueError, match='StringMother min_length must be greater than or equal to 0.'
    ):
        StringMother.alpha(min_length=IntegerMother.negative())


@mark.unit_testing
def test_string_mother_alpha_method_max_length_value() -> None:
    """
    Check that StringMother alpha method max_length parameter is the minimum permitted value.
    """
    StringMother.alpha(min_length=0, max_length=0)


@mark.unit_testing
def test_string_mother_alpha_method_min_length_max_length_value() -> None:
    """
    Check that StringMother alpha method min_length and max_length parameters are the minimum permitted value.
    """
    StringMother.alpha(min_length=0, max_length=1)


@mark.unit_testing
def test_string_mother_alpha_method_max_length_random_value() -> None:
    """
    Check that StringMother alpha method max_length parameter is a random positive integer.
    """
    max_length = IntegerMother.positive()

    StringMother.alpha(max_length=max_length)


@mark.unit_testing
def test_string_mother_alpha_method_max_length_negative_value() -> None:
    """
    Check that StringMother alpha method raises a ValueError when the provided max_length is negative.
    """
    with assert_raises(
        expected_exception=ValueError,
        match='StringMother max_length must be greater than or equal to 0.',
    ):
        StringMother.alpha(max_length=-1)


@mark.unit_testing
def test_string_mother_alpha_method_invalid_max_length_value() -> None:
    """
    Check that StringMother alpha method raises a ValueError when the provided max_length is negative.
    """
    with assert_raises(
        expected_exception=ValueError,
        match='StringMother max_length must be greater than or equal to 0.',
    ):
        StringMother.alpha(max_length=IntegerMother.negative())


@mark.unit_testing
def test_string_mother_alpha_method_min_length_greater_than_max_length() -> None:
    """
    Check that StringMother alpha method raises a ValueError when the provided min_length is greater than max_length.
    """
    min_length = IntegerMother.create(min=0, max=15)
    max_length = IntegerMother.create(min=16, max=32)

    with assert_raises(
        expected_exception=ValueError,
        match='StringMother min_length must be less than or equal to max_length.',
    ):
        StringMother.alpha(min_length=max_length, max_length=min_length)


@mark.unit_testing
def test_string_mother_alphanumeric_method_happy_path() -> None:
    """
    Check that StringMother alphanumeric method returns an alphanumeric string value.
    """
    value = StringMother.alphanumeric()

    assert type(value) is str
    assert value.isalnum()
    assert 1 <= len(value) <= 128


@mark.unit_testing
def test_string_mother_alphanumeric_method_min_length_value() -> None:
    """
    Check that StringMother alphanumeric method min_length parameter is the minimum permitted value.
    """
    StringMother.alphanumeric(min_length=0)


@mark.unit_testing
def test_string_mother_alphanumeric_method_min_length_random_value() -> None:
    """
    Check that StringMother alphanumeric method min_length parameter is a random positive integer.
    """
    min_length = IntegerMother.positive()

    StringMother.alphanumeric(min_length=min_length)


@mark.unit_testing
def test_string_mother_alphanumeric_method_invalid_min_length_type() -> None:
    """
    Check that StringMother alphanumeric method raises a TypeError when the provided min_length is not an integer.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='StringMother min_length must be an integer.',
    ):
        StringMother.alphanumeric(min_length=IntegerMother.invalid_type())


@mark.unit_testing
def test_string_mother_alphanumeric_method_invalid_max_length_type() -> None:
    """
    Check that StringMother alphanumeric method raises a TypeError when the provided max_length is not an integer.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='StringMother max_length must be an integer.',
    ):
        StringMother.alphanumeric(max_length=IntegerMother.invalid_type())


@mark.unit_testing
def test_string_mother_alphanumeric_method_min_length_negative_value() -> None:
    """
    Check that StringMother alphanumeric method raises a ValueError when the provided min_length is negative.
    """
    with assert_raises(
        expected_exception=ValueError,
        match='StringMother min_length must be greater than or equal to 0.',
    ):
        StringMother.alphanumeric(min_length=-1)


@mark.unit_testing
def test_string_mother_alphanumeric_method_invalid_min_length_value() -> None:
    """
    Check that StringMother alphanumeric method raises a ValueError when the provided min_length is negative.
    """
    with assert_raises(
        expected_exception=ValueError, match='StringMother min_length must be greater than or equal to 0.'
    ):
        StringMother.alphanumeric(min_length=IntegerMother.negative())


@mark.unit_testing
def test_string_mother_alphanumeric_method_max_length_value() -> None:
    """
    Check that StringMother alphanumeric method max_length parameter is the minimum permitted value.
    """
    StringMother.alphanumeric(min_length=0, max_length=0)


@mark.unit_testing
def test_string_mother_alphanumeric_method_min_length_max_length_value() -> None:
    """
    Check that StringMother alphanumeric method min_length and max_length parameters are the minimum permitted value.
    """
    StringMother.alphanumeric(min_length=0, max_length=1)


@mark.unit_testing
def test_string_mother_alphanumeric_method_max_length_random_value() -> None:
    """
    Check that StringMother alphanumeric method max_length parameter is a random positive integer.
    """
    max_length = IntegerMother.positive()

    StringMother.alphanumeric(max_length=max_length)


@mark.unit_testing
def test_string_mother_alphanumeric_method_max_length_negative_value() -> None:
    """
    Check that StringMother alphanumeric method raises a ValueError when the provided max_length is negative.
    """
    with assert_raises(
        expected_exception=ValueError,
        match='StringMother max_length must be greater than or equal to 0.',
    ):
        StringMother.alphanumeric(max_length=-1)


@mark.unit_testing
def test_string_mother_alphanumeric_method_invalid_max_length_value() -> None:
    """
    Check that StringMother alphanumeric method raises a ValueError when the provided max_length is negative.
    """
    with assert_raises(
        expected_exception=ValueError,
        match='StringMother max_length must be greater than or equal to 0.',
    ):
        StringMother.alphanumeric(max_length=IntegerMother.negative())


@mark.unit_testing
def test_string_mother_alphanumeric_method_min_length_greater_than_max_length() -> None:
    """
    Check that StringMother alphanumeric method raises a ValueError when the provided min_length is greater than
    max_length.
    """
    min_length = IntegerMother.create(min=0, max=15)
    max_length = IntegerMother.create(min=16, max=32)

    with assert_raises(
        expected_exception=ValueError,
        match='StringMother min_length must be less than or equal to max_length.',
    ):
        StringMother.alphanumeric(min_length=max_length, max_length=min_length)


@mark.unit_testing
def test_string_mother_numeric_method_happy_path() -> None:
    """
    Check that StringMother numeric method returns a numeric string value.
    """
    value = StringMother.numeric()

    assert type(value) is str
    assert value.isdigit()
    assert 1 <= len(value) <= 128


@mark.unit_testing
def test_string_mother_numeric_method_min_length_value() -> None:
    """
    Check that StringMother numeric method min_length parameter is the minimum permitted value.
    """
    StringMother.numeric(min_length=0)


@mark.unit_testing
def test_string_mother_numeric_method_min_length_random_value() -> None:
    """
    Check that StringMother numeric method min_length parameter is a random positive integer.
    """
    min_length = IntegerMother.positive()

    StringMother.numeric(min_length=min_length)


@mark.unit_testing
def test_string_mother_numeric_method_invalid_min_length_type() -> None:
    """
    Check that StringMother numeric method raises a TypeError when the provided min_length is not an integer.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='StringMother min_length must be an integer.',
    ):
        StringMother.numeric(min_length=IntegerMother.invalid_type())


@mark.unit_testing
def test_string_mother_numeric_method_invalid_max_length_type() -> None:
    """
    Check that StringMother numeric method raises a TypeError when the provided max_length is not an integer.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='StringMother max_length must be an integer.',
    ):
        StringMother.numeric(max_length=IntegerMother.invalid_type())


@mark.unit_testing
def test_string_mother_numeric_method_min_length_negative_value() -> None:
    """
    Check that StringMother numeric method raises a ValueError when the provided min_length is negative.
    """
    with assert_raises(
        expected_exception=ValueError,
        match='StringMother min_length must be greater than or equal to 0.',
    ):
        StringMother.numeric(min_length=-1)


@mark.unit_testing
def test_string_mother_numeric_method_invalid_min_length_value() -> None:
    """
    Check that StringMother numeric method raises a ValueError when the provided min_length is negative.
    """
    with assert_raises(
        expected_exception=ValueError, match='StringMother min_length must be greater than or equal to 0.'
    ):
        StringMother.numeric(min_length=IntegerMother.negative())


@mark.unit_testing
def test_string_mother_numeric_method_max_length_value() -> None:
    """
    Check that StringMother numeric method max_length parameter is the minimum permitted value.
    """
    StringMother.numeric(min_length=0, max_length=0)


@mark.unit_testing
def test_string_mother_numeric_method_min_length_max_length_value() -> None:
    """
    Check that StringMother numeric method min_length and max_length parameters are the minimum permitted value.
    """
    StringMother.numeric(min_length=0, max_length=1)


@mark.unit_testing
def test_string_mother_numeric_method_max_length_random_value() -> None:
    """
    Check that StringMother numeric method max_length parameter is a random positive integer.
    """
    max_length = IntegerMother.positive()

    StringMother.numeric(max_length=max_length)


@mark.unit_testing
def test_string_mother_numeric_method_max_length_negative_value() -> None:
    """
    Check that StringMother numeric method raises a ValueError when the provided max_length is negative.
    """
    with assert_raises(
        expected_exception=ValueError,
        match='StringMother max_length must be greater than or equal to 0.',
    ):
        StringMother.numeric(max_length=-1)


@mark.unit_testing
def test_string_mother_numeric_method_invalid_max_length_value() -> None:
    """
    Check that StringMother numeric method raises a ValueError when the provided max_length is negative.
    """
    with assert_raises(
        expected_exception=ValueError,
        match='StringMother max_length must be greater than or equal to 0.',
    ):
        StringMother.numeric(max_length=IntegerMother.negative())


@mark.unit_testing
def test_string_mother_numeric_method_min_length_greater_than_max_length() -> None:
    """
    Check that StringMother numeric method raises a ValueError when the provided min_length is greater than max_length.
    """
    min_length = IntegerMother.create(min=0, max=15)
    max_length = IntegerMother.create(min=16, max=32)

    with assert_raises(
        expected_exception=ValueError,
        match='StringMother min_length must be less than or equal to max_length.',
    ):
        StringMother.numeric(min_length=max_length, max_length=min_length)


def test_string_mother_not_trimmed_method_happy_path() -> None:
    """
    Check that StringMother not_trimmed method returns a string value with random spaces.
    """
    value = StringMother.not_trimmed()

    assert type(value) is str
    assert len(value.strip()) != len(value)
    assert 2 <= len(value) <= 128


@mark.unit_testing
def test_string_mother_not_trimmed_method_min_length_value() -> None:
    """
    Check that StringMother not_trimmed method min_length parameter is the minimum permitted value.
    """
    StringMother.not_trimmed(min_length=2)


@mark.unit_testing
def test_string_mother_not_trimmed_method_min_length_random_value() -> None:
    """
    Check that StringMother not_trimmed method min_length parameter is a random positive integer.
    """
    min_length = IntegerMother.create(min=2, max=128)

    StringMother.not_trimmed(min_length=min_length)


@mark.unit_testing
def test_string_mother_not_trimmed_method_invalid_min_length_type() -> None:
    """
    Check that StringMother not_trimmed method raises a TypeError when the provided min_length is not an integer.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='StringMother min_length must be an integer.',
    ):
        StringMother.not_trimmed(min_length=IntegerMother.invalid_type())


@mark.unit_testing
def test_string_mother_not_trimmed_method_invalid_max_length_type() -> None:
    """
    Check that StringMother not_trimmed method raises a TypeError when the provided max_length is not an integer.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='StringMother max_length must be an integer.',
    ):
        StringMother.not_trimmed(max_length=IntegerMother.invalid_type())


@mark.unit_testing
def test_string_mother_not_trimmed_method_min_length_negative_value() -> None:
    """
    Check that StringMother not_trimmed method raises a ValueError when the provided min_length is negative.
    """
    with assert_raises(
        expected_exception=ValueError,
        match='StringMother min_length must be greater than or equal to 2.',
    ):
        StringMother.not_trimmed(min_length=1)


@mark.unit_testing
def test_string_mother_not_trimmed_method_invalid_min_length_value() -> None:
    """
    Check that StringMother not_trimmed method raises a ValueError when the provided min_length is negative.
    """
    with assert_raises(
        expected_exception=ValueError, match='StringMother min_length must be greater than or equal to 2.'
    ):
        StringMother.not_trimmed(min_length=IntegerMother.create(max=1))


@mark.unit_testing
def test_string_mother_not_trimmed_method_max_length_random_value() -> None:
    """
    Check that StringMother not_trimmed method max_length parameter is a random positive integer.
    """
    max_length = IntegerMother.create(min=2)

    StringMother.not_trimmed(max_length=max_length)


@mark.unit_testing
def test_string_mother_not_trimmed_method_max_length_negative_value() -> None:
    """
    Check that StringMother not_trimmed method raises a ValueError when the provided max_length is negative.
    """
    with assert_raises(
        expected_exception=ValueError,
        match='StringMother max_length must be greater than or equal to 2.',
    ):
        StringMother.not_trimmed(max_length=1)


@mark.unit_testing
def test_string_mother_not_trimmed_method_invalid_max_length_value() -> None:
    """
    Check that StringMother not_trimmed method raises a ValueError when the provided max_length is negative.
    """
    with assert_raises(
        expected_exception=ValueError,
        match='StringMother max_length must be greater than or equal to 2.',
    ):
        StringMother.not_trimmed(max_length=IntegerMother.create(max=1))


@mark.unit_testing
def test_string_mother_not_trimmed_method_min_length_greater_than_max_length() -> None:
    """
    Check that StringMother not_trimmed method raises a ValueError when the provided min_length is greater than
    max_length.
    """
    min_length = IntegerMother.create(min=2, max=15)
    max_length = IntegerMother.create(min=16, max=32)

    with assert_raises(
        expected_exception=ValueError,
        match='StringMother min_length must be less than or equal to max_length.',
    ):
        StringMother.not_trimmed(min_length=max_length, max_length=min_length)


@mark.unit_testing
def test_string_mother_invalid_type_method_happy_path() -> None:
    """
    Check that StringMother invalid_type method returns a non-string value.
    """
    assert type(StringMother.invalid_type()) is not str


@mark.unit_testing
def test_string_mother_invalid_value_method_happy_path() -> None:
    """
    Check that StringMother invalid_value method returns a non-printable string value.
    """
    value = StringMother.invalid_value()

    assert type(value) is str
    assert not value.isprintable()
