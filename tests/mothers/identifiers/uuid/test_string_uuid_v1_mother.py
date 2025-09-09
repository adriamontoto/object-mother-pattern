"""
Test module for the StringUuidMother class.
"""

from uuid import UUID

from pytest import mark, raises as assert_raises

from object_mother_pattern.mothers.identifiers import StringUuidV1Mother


@mark.unit_testing
def test_string_uuid1_mother_happy_path() -> None:
    """
    Test StringUuidMother happy path.
    """
    value = StringUuidV1Mother.create()

    assert type(value) is str
    assert UUID(value).version == 1


@mark.unit_testing
def test_string_uuid1_mother_value() -> None:
    """
    Test StringUuidMother create method with value.
    """
    value = StringUuidV1Mother.create()

    assert StringUuidV1Mother.create(value=value) == value


@mark.unit_testing
def test_string_uuid1_mother_invalid_type() -> None:
    """
    Test StringUuidMother create method with invalid type.
    """
    assert type(StringUuidV1Mother.invalid_type()) is not str


@mark.unit_testing
def test_string_uuid1_mother_invalid_value() -> None:
    """
    Test StringUuidMother invalid_value method.
    """
    value = StringUuidV1Mother.invalid_value()

    assert type(value) is str
    assert not value.isprintable()


@mark.unit_testing
def test_string_uuid1_mother_invalid_value_type() -> None:
    """
    Test StringUuidMother create method with invalid value type.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='StringUuidV1Mother value must be a string.',
    ):
        StringUuidV1Mother.create(value=StringUuidV1Mother.invalid_type())
