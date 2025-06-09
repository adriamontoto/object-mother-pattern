"""
Test module for the DomainMother class.
"""

from pytest import mark, raises as assert_raises

from object_mother_pattern.mothers import BooleanMother, IntegerMother, StringMother
from object_mother_pattern.mothers.internet import DomainMother
from object_mother_pattern.mothers.internet.domain_mother import DomainCase
from object_mother_pattern.mothers.internet.utils import get_label_dict, get_tld_dict


@mark.unit_testing
def test_domain_mother_create_method_happy_path() -> None:
    """
    Check that DomainMother create method returns a string value that is a valid domain.
    """
    value = DomainMother.create()

    domain_tld = value.lower().split('.')[-1]
    domain_labels = value.lower().split('.')[:-1]
    tlds = {tld for tlds in get_tld_dict().values() for tld in tlds}
    all_labels = {label for labels in get_label_dict().values() for label in labels}

    assert type(value) is str
    assert len(value) >= 4
    assert len(value) <= 253
    assert value == value.strip()
    assert not value.startswith('.') and not value.endswith('.')
    assert '..' not in value
    assert domain_tld in tlds
    assert len(domain_labels) >= 1
    assert len(domain_labels) <= 127
    for domain_label in domain_labels:
        assert domain_label == domain_label.strip()
        assert len(domain_label) >= 1
        assert len(domain_label) <= 63
        assert domain_label in all_labels or '-' in domain_label or domain_label.isalnum()


@mark.unit_testing
def test_domain_mother_create_method_happy_path_without_hyphens() -> None:
    """
    Check that DomainMother create method returns a string value that is a valid domain without hyphens.
    """
    value = DomainMother.create(include_hyphens=False)

    domain_tld = value.lower().split('.')[-1]
    domain_labels = value.lower().split('.')[:-1]
    tlds = {tld for tlds in get_tld_dict().values() for tld in tlds}
    all_labels = {label for labels in get_label_dict().values() for label in labels}

    assert type(value) is str
    assert len(value) >= 4
    assert len(value) <= 253
    assert value == value.strip()
    assert not value.startswith('.') and not value.endswith('.')
    assert '..' not in value
    assert domain_tld in tlds
    assert len(domain_labels) >= 1
    assert len(domain_labels) <= 127
    for domain_label in domain_labels:
        assert domain_label in all_labels or domain_label.isalnum()
        assert domain_label == domain_label.strip()
        assert len(domain_label) >= 1
        assert len(domain_label) <= 63
        assert '-' not in domain_label


@mark.unit_testing
def test_domain_mother_create_method_happy_path_without_numbers() -> None:
    """
    Check that DomainMother create method returns a string value that is a valid domain without numbers.
    """
    value = DomainMother.create(include_numbers=False)

    domain_tld = value.lower().split('.')[-1]
    domain_labels = value.lower().split('.')[:-1]
    tlds = {tld for tlds in get_tld_dict().values() for tld in tlds}
    all_labels = {label for labels in get_label_dict().values() for label in labels}

    assert type(value) is str
    assert len(value) >= 4
    assert len(value) <= 253
    assert value == value.strip()
    assert not value.startswith('.') and not value.endswith('.')
    assert '..' not in value
    assert domain_tld in tlds
    assert len(domain_labels) >= 1
    assert len(domain_labels) <= 127
    for domain_label in domain_labels:
        assert domain_label in all_labels or '-' in domain_label
        assert domain_label == domain_label.strip()
        assert len(domain_label) >= 1
        assert len(domain_label) <= 63
        for char in domain_label:
            assert char.isalpha() or char == '-'


@mark.unit_testing
def test_domain_mother_create_method_happy_path_without_hyphens_and_numbers() -> None:
    """
    Check that DomainMother create method returns a string value that is a valid domain without hyphens and numbers.
    """
    value = DomainMother.create(include_hyphens=False, include_numbers=False)

    domain_tld = value.lower().split('.')[-1]
    domain_labels = value.lower().split('.')[:-1]
    tlds = {tld for tlds in get_tld_dict().values() for tld in tlds}
    all_labels = {label for labels in get_label_dict().values() for label in labels}

    assert type(value) is str
    assert len(value) >= 4
    assert len(value) <= 253
    assert value == value.strip()
    assert not value.startswith('.') and not value.endswith('.')
    assert '..' not in value
    assert domain_tld in tlds
    assert len(domain_labels) >= 1
    assert len(domain_labels) <= 127
    assert all(domain_label in all_labels for domain_label in domain_labels)
    for domain_label in domain_labels:
        assert domain_label == domain_label.strip()
        assert len(domain_label) >= 1
        assert len(domain_label) <= 63


@mark.unit_testing
def test_domain_mother_create_method_value() -> None:
    """
    Check that DomainMother create method returns the provided value.
    """
    value = DomainMother.create()

    assert DomainMother.create(value=value) == value


@mark.unit_testing
def test_domain_mother_create_method_invalid_value_type() -> None:
    """
    Check that DomainMother create method raises a TypeError when the provided value is not a string.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='DomainMother value must be a string.',
    ):
        DomainMother.create(value=DomainMother.invalid_type())


@mark.unit_testing
def test_domain_mother_create_method_min_length_and_max_length_min_permitted_value() -> None:
    """
    Check that DomainMother create method min_length and max_length parameters are equal to the minimum permitted value.
    """
    DomainMother.create(min_length=4, max_length=4)


@mark.unit_testing
def test_domain_mother_create_method_min_labels_and_max_labels_min_permitted_value() -> None:
    """
    Check that DomainMother create method min_labels and max_labels parameters are equal to the minimum permitted value.
    """
    DomainMother.create(min_labels=2, max_labels=2)


@mark.unit_testing
def test_domain_mother_create_method_min_permitted_min_length_value() -> None:
    """
    Check that DomainMother create method min_length parameter is the minimum permitted value.
    """
    DomainMother.create(min_length=4)


@mark.unit_testing
def test_domain_mother_create_method_min_length_random_value() -> None:
    """
    Check that DomainMother create method min_length parameter is a random positive integer.
    """
    min_length = IntegerMother.create(min=4, max=253)

    DomainMother.create(min_length=min_length, max_length=253, min_labels=2, max_labels=127)


@mark.unit_testing
def test_domain_mother_create_method_invalid_min_length_type() -> None:
    """
    Check that DomainMother create method raises a TypeError when the provided min_length is not an integer.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='DomainMother min_length must be an integer.',
    ):
        DomainMother.create(min_length=IntegerMother.invalid_type())


@mark.unit_testing
def test_domain_mother_create_method_min_length_too_small_value() -> None:
    """
    Check that DomainMother create method raises a ValueError when the provided min_length is too small.
    """
    with assert_raises(
        expected_exception=ValueError,
        match='DomainMother min_length must be at least 4.',
    ):
        DomainMother.create(min_length=3)


@mark.unit_testing
def test_domain_mother_create_method_invalid_min_length_random_too_small_value() -> None:
    """
    Check that DomainMother create method raises a ValueError when the provided min_length is too small.
    """
    with assert_raises(
        expected_exception=ValueError,
        match='DomainMother min_length must be at least 4.',
    ):
        DomainMother.create(min_length=IntegerMother.create(max=3))


@mark.unit_testing
def test_domain_mother_create_method_max_permitted_max_length_value() -> None:
    """
    Check that DomainMother create method max_length parameter is the minimum permitted value.
    """
    DomainMother.create(max_length=253)


@mark.unit_testing
def test_domain_mother_create_method_max_length_random_value() -> None:
    """
    Check that DomainMother create method max_length parameter is a random positive integer.
    """
    max_length = IntegerMother.create(min=4, max=253)

    DomainMother.create(min_length=4, max_length=max_length, min_labels=2, max_labels=127)


@mark.unit_testing
def test_domain_mother_create_method_invalid_max_length_type() -> None:
    """
    Check that DomainMother create method raises a TypeError when the provided max_length is not an integer.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='DomainMother max_length must be an integer.',
    ):
        DomainMother.create(max_length=IntegerMother.invalid_type())


@mark.unit_testing
def test_domain_mother_create_method_max_length_too_large_value() -> None:
    """
    Check that DomainMother create method raises a ValueError when the provided max_length is too large.
    """
    with assert_raises(
        expected_exception=ValueError,
        match='DomainMother max_length must be at most 253.',
    ):
        DomainMother.create(max_length=254)


@mark.unit_testing
def test_domain_mother_create_method_invalid_max_length_random_too_large_value() -> None:
    """
    Check that DomainMother create method raises a ValueError when the provided max_length is too large.
    """
    with assert_raises(
        expected_exception=ValueError,
        match='IntegerMother min value must be less than or equal to max value.',
    ):
        DomainMother.create(max_length=IntegerMother.create(min=254))


@mark.unit_testing
def test_domain_mother_create_method_min_length_greater_than_max_length() -> None:
    """
    Check that DomainMother create method raises a ValueError when the provided min_length is greater than max_length.
    """
    min_length = IntegerMother.create(min=4, max=15)
    max_length = IntegerMother.create(min=16, max=32)

    with assert_raises(
        expected_exception=ValueError,
        match='DomainMother min_length must be less than or equal to max_length.',
    ):
        DomainMother.create(min_length=max_length, max_length=min_length)


@mark.unit_testing
def test_domain_mother_create_method_min_permitted_min_labels_value() -> None:
    """
    Check that DomainMother create method min_labels parameter is the minimum permitted value.
    """
    DomainMother.create(min_labels=2)


@mark.unit_testing
def test_domain_mother_create_method_min_labels_random_value() -> None:
    """
    Check that DomainMother create method min_labels parameter is a random positive integer.
    """
    min_labels = IntegerMother.create(min=2, max=127)

    DomainMother.create(min_length=4, max_length=253, min_labels=min_labels, max_labels=127)


@mark.unit_testing
def test_domain_mother_create_method_invalid_min_labels_type() -> None:
    """
    Check that DomainMother create method raises a TypeError when the provided min_labels is not an integer.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='DomainMother min_labels must be an integer.',
    ):
        DomainMother.create(min_labels=IntegerMother.invalid_type())


@mark.unit_testing
def test_domain_mother_create_method_min_labels_too_small_value() -> None:
    """
    Check that DomainMother create method raises a ValueError when the provided min_labels is too small.
    """
    with assert_raises(
        expected_exception=ValueError,
        match='DomainMother min_labels must be at least 2.',
    ):
        DomainMother.create(min_labels=1)


@mark.unit_testing
def test_domain_mother_create_method_invalid_min_labels_random_negative_value() -> None:
    """
    Check that DomainMother create method raises a ValueError when the provided min_labels is negative.
    """
    with assert_raises(
        expected_exception=ValueError,
        match='DomainMother min_labels must be at least 2.',
    ):
        DomainMother.create(min_labels=IntegerMother.create(max=1))


@mark.unit_testing
def test_domain_mother_create_method_invalid_max_labels_type() -> None:
    """
    Check that DomainMother create method raises a TypeError when the provided max_labels is not an integer.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='DomainMother max_labels must be an integer.',
    ):
        DomainMother.create(max_labels=IntegerMother.invalid_type())


@mark.unit_testing
def test_domain_mother_create_method_max_permitted_max_labels_value() -> None:
    """
    Check that DomainMother create method max_labels parameter is the maximum permitted value.
    """
    DomainMother.create(max_labels=127)


@mark.unit_testing
def test_domain_mother_create_method_max_labels_too_large_value() -> None:
    """
    Check that DomainMother create method raises a ValueError when the provided max_labels is too large.
    """
    with assert_raises(
        expected_exception=ValueError,
        match='DomainMother max_labels must be at most 127.',
    ):
        DomainMother.create(max_labels=128)


@mark.unit_testing
def test_domain_mother_create_method_invalid_max_labels_random_too_large_value() -> None:
    """
    Check that DomainMother create method raises a ValueError when the provided max_labels is too large.
    """
    with assert_raises(
        expected_exception=ValueError,
        match='DomainMother max_labels must be at most 127.',
    ):
        DomainMother.create(max_labels=IntegerMother.create(min=128, max=253))


@mark.unit_testing
def test_domain_mother_create_method_min_labels_greater_than_max_labels() -> None:
    """
    Check that DomainMother create method raises a ValueError when the provided min_labels is greater than max_labels.
    """
    min_labels = IntegerMother.create(min=2, max=15)
    max_labels = IntegerMother.create(min=16, max=32)

    with assert_raises(
        expected_exception=ValueError,
        match='DomainMother min_labels must be less than or equal to max_labels.',
    ):
        DomainMother.create(min_labels=max_labels, max_labels=min_labels)


@mark.unit_testing
def test_domain_mother_lowercase_case() -> None:
    """
    Test DomainMother create method with lowercase case.
    """
    value = DomainMother.create(domain_case=DomainCase.LOWERCASE)

    assert value.islower()


@mark.unit_testing
def test_domain_mother_uppercase_case() -> None:
    """
    Test DomainMother create method with uppercase case.
    """
    value = DomainMother.create(domain_case=DomainCase.UPPERCASE)

    assert value.isupper()


@mark.unit_testing
def test_domain_mother_mixed_case() -> None:
    """
    Test DomainMother create method with mixed case.
    """
    value = DomainMother.create(domain_case=DomainCase.MIXEDCASE)

    assert any(char.islower() or char.isupper() for char in value)


@mark.unit_testing
def test_domain_mother_invalid_case() -> None:
    """
    Test DomainMother create method with invalid case.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='DomainMother domain_case must be a DomainCase.',
    ):
        DomainMother.create(domain_case=StringMother.invalid_type())


@mark.unit_testing
def test_domain_mother_invalid_include_hyphens() -> None:
    """
    Test DomainMother create method with invalid include_hyphens.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='DomainMother include_hyphens must be a boolean.',
    ):
        DomainMother.create(include_hyphens=BooleanMother.invalid_type())


@mark.unit_testing
def test_domain_mother_invalid_include_numbers() -> None:
    """
    Test DomainMother create method with invalid include_numbers.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='DomainMother include_numbers must be a boolean.',
    ):
        DomainMother.create(include_numbers=BooleanMother.invalid_type())


@mark.unit_testing
def test_domain_mother_of_length_method_happy_path() -> None:
    """
    Test DomainMother of_length method happy path.
    """
    length = IntegerMother.create(min=4, max=253)
    value = DomainMother.of_length(length=length)

    domain_tld = value.lower().split('.')[-1]
    domain_labels = value.lower().split('.')[:-1]
    tlds = {tld for tlds in get_tld_dict().values() for tld in tlds}
    all_labels = {label for labels in get_label_dict().values() for label in labels}

    assert type(value) is str
    assert len(value) == length
    assert value == value.strip()
    assert not value.startswith('.') and not value.endswith('.')
    assert '..' not in value
    assert domain_tld in tlds
    assert len(domain_labels) >= 1
    assert len(domain_labels) <= 127
    for domain_label in domain_labels:
        assert domain_label == domain_label.strip()
        assert len(domain_label) >= 1
        assert len(domain_label) <= 63
        assert domain_label in all_labels or '-' in domain_label or domain_label.isalnum()


@mark.unit_testing
def test_domain_mother_of_length_method_invalid_length_type() -> None:
    """
    Test DomainMother of_length method with invalid length type.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='DomainMother min_length must be an integer.',
    ):
        DomainMother.of_length(length=IntegerMother.invalid_type())


@mark.unit_testing
def test_domain_mother_invalid_type_method_happy_path() -> None:
    """
    Check that DomainMother invalid_type method returns a non-string value.
    """
    assert type(DomainMother.invalid_type()) is not str


@mark.unit_testing
def test_domain_mother_invalid_value_method_happy_path() -> None:
    """
    Check that DomainMother invalid_value method returns a non-printable string value.
    """
    value = DomainMother.invalid_value()

    assert type(value) is str
    assert not value.isprintable()
