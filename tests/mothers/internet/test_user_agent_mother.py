"""
Test module for the UserAgentMother class.
"""

from pytest import mark, raises as assert_raises

from object_mother_pattern.mothers import IntegerMother
from object_mother_pattern.mothers.internet import UserAgentMother


@mark.unit_testing
def test_user_agent_mother_create_happy_path() -> None:
    """
    Ensure create returns a trimmed user agent within the default length range.
    """
    value = UserAgentMother.create()

    assert type(value) is str
    assert 64 <= len(value) <= 256
    assert value == value.strip()


@mark.unit_testing
def test_user_agent_mother_create_returns_given_value() -> None:
    """
    Ensure create echoes the provided value.
    """
    custom = UserAgentMother.create()

    assert UserAgentMother.create(value=custom) == custom


@mark.unit_testing
def test_user_agent_mother_create_invalid_value_type() -> None:
    """
    Ensure create raises TypeError when value is not a string.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='UserAgentMother value must be a string.',
    ):
        UserAgentMother.create(value=UserAgentMother.invalid_type())


@mark.unit_testing
def test_user_agent_mother_create_invalid_min_length_type() -> None:
    """
    Ensure create raises TypeError when min_length is not an integer.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='UserAgentMother min_length must be an integer.',
    ):
        UserAgentMother.create(min_length=IntegerMother.invalid_type())


@mark.unit_testing
def test_user_agent_mother_create_invalid_max_length_type() -> None:
    """
    Ensure create raises TypeError when max_length is not an integer.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='UserAgentMother max_length must be an integer.',
    ):
        UserAgentMother.create(max_length=IntegerMother.invalid_type())


@mark.unit_testing
def test_user_agent_mother_create_min_length_too_small() -> None:
    """
    Ensure create raises ValueError when min_length is below 1.
    """
    with assert_raises(
        expected_exception=ValueError,
        match='UserAgentMother min_length must be greater than or equal to 1.',
    ):
        UserAgentMother.create(min_length=0)


@mark.unit_testing
def test_user_agent_mother_create_min_length_too_small_random() -> None:
    """
    Ensure create raises ValueError when min_length is randomly below 1.
    """
    with assert_raises(
        expected_exception=ValueError,
        match='UserAgentMother min_length must be greater than or equal to 1.',
    ):
        UserAgentMother.create(min_length=IntegerMother.negative())


@mark.unit_testing
def test_user_agent_mother_create_max_length_too_small() -> None:
    """
    Ensure create raises ValueError when max_length is below 1.
    """
    with assert_raises(
        expected_exception=ValueError,
        match='UserAgentMother max_length must be greater than or equal to 1.',
    ):
        UserAgentMother.create(max_length=0)


@mark.unit_testing
def test_user_agent_mother_create_max_length_too_small_random() -> None:
    """
    Ensure create raises ValueError when max_length is randomly below 1.
    """
    with assert_raises(
        expected_exception=ValueError,
        match='UserAgentMother max_length must be greater than or equal to 1.',
    ):
        UserAgentMother.create(max_length=IntegerMother.negative())


@mark.unit_testing
def test_user_agent_mother_create_min_length_greater_than_max_length() -> None:
    """
    Ensure create raises ValueError when min_length exceeds max_length.
    """
    min_length = IntegerMother.create(min=2)
    max_length = min_length - 1

    with assert_raises(
        expected_exception=ValueError,
        match='UserAgentMother min_length must be less than or equal to max_length.',
    ):
        UserAgentMother.create(min_length=min_length, max_length=max_length)


@mark.unit_testing
def test_user_agent_mother_of_length_returns_exact_length() -> None:
    """
    Ensure of_length returns a user agent string of the requested length.
    """
    length = IntegerMother.positive()
    value = UserAgentMother.of_length(length=length)

    assert type(value) is str
    assert len(value) == length


@mark.unit_testing
def test_user_agent_mother_invalid_value_method() -> None:
    """
    Ensure invalid_value returns a non-printable string value.
    """
    value = UserAgentMother.invalid_value()

    assert type(value) is str
    assert not value.isprintable()
