"""
Test module for the EmailAddressMother class.
"""

from typing import Any

from pytest import MonkeyPatch, mark, raises as assert_raises

from object_mother_pattern.mothers import IntegerMother, StringCase, StringMother
from object_mother_pattern.mothers.internet import DomainMother, EmailAddressMother
from object_mother_pattern.mothers.people import UsernameMother


def _domain_factory_that_fails_after_first_call() -> Any:
    """
    Create a domain factory that only supports explicit string-case calls.
    """

    def factory(cls: type[DomainMother], /, **kwargs: object) -> str:
        """
        Create a test domain or fail like an exhausted random domain generator.
        """
        if 'string_case' in kwargs:
            return 'example.com'

        raise ValueError

    return classmethod(factory)


def _domain_factory_that_returns_one_oversized_domain() -> Any:
    """
    Create a domain factory that first returns an oversized domain.
    """
    calls = 0

    def factory(cls: type[DomainMother], /, **kwargs: object) -> str:
        """
        Create one oversized domain and then valid test domains.
        """
        nonlocal calls
        if 'string_case' in kwargs:
            return 'example.com'

        calls += 1
        if calls == 1:
            return 'x' * 254

        return 'example.com'

    return classmethod(factory)


def _long_username_factory(cls: type[UsernameMother], /, **kwargs: object) -> str:
    """
    Create an oversized username for local-part validation tests.
    """
    return 'x' * 65


def _oversized_rfc_domain_factory(cls: type[DomainMother]) -> str:
    """
    Create an oversized RFC domain for fallback tests.
    """
    return 'x' * 254


def _assert_valid_email(value: str, *, min_length: int = 6, max_length: int = 254) -> None:
    """
    Assert that a generated email has the expected basic shape and length.
    """
    local_part, domain_part = value.split('@')

    assert type(value) is str
    assert min_length <= len(value) <= max_length
    assert value.count('@') == 1
    assert 1 <= len(local_part) <= 64
    assert '.' in domain_part


@mark.unit_testing
def test_email_address_mother_create_method_happy_path() -> None:
    """
    Check that EmailAddressMother create method returns a valid email address.
    """
    _assert_valid_email(EmailAddressMother.create(), min_length=8, max_length=64)


@mark.unit_testing
def test_email_address_mother_create_method_with_value() -> None:
    """
    Check that EmailAddressMother create method returns the provided value.
    """
    value = 'ada@example.com'

    assert EmailAddressMother.create(value=value) == value


@mark.unit_testing
def test_email_address_mother_create_method_invalid_value_type() -> None:
    """
    Check that EmailAddressMother create method raises a TypeError when value is not a string.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='EmailAddressMother value must be a string.',
    ):
        EmailAddressMother.create(value=EmailAddressMother.invalid_type())


@mark.unit_testing
def test_email_address_mother_create_method_invalid_length_types() -> None:
    """
    Check that EmailAddressMother create method validates length parameter types.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='EmailAddressMother min_length must be an integer.',
    ):
        EmailAddressMother.create(min_length=IntegerMother.invalid_type())

    with assert_raises(
        expected_exception=TypeError,
        match='EmailAddressMother max_length must be an integer.',
    ):
        EmailAddressMother.create(max_length=IntegerMother.invalid_type())


@mark.unit_testing
def test_email_address_mother_create_method_invalid_length_bounds() -> None:
    """
    Check that EmailAddressMother create method validates length bounds.
    """
    with assert_raises(
        expected_exception=ValueError,
        match='EmailAddressMother min_length must be at least 6.',
    ):
        EmailAddressMother.create(min_length=5)

    with assert_raises(
        expected_exception=ValueError,
        match='EmailAddressMother max_length must be at most 254.',
    ):
        EmailAddressMother.create(max_length=255)

    with assert_raises(
        expected_exception=ValueError,
        match='EmailAddressMother min_length must be less than or equal to max_length.',
    ):
        EmailAddressMother.create(min_length=20, max_length=10)


@mark.unit_testing
def test_email_address_mother_create_method_with_domain() -> None:
    """
    Check that EmailAddressMother create method uses the provided domain.
    """
    value = EmailAddressMother.create(domain='example.com', string_case=StringCase.LOWERCASE)

    assert value.endswith('@example.com')
    assert value.split('@')[0].islower()


@mark.unit_testing
def test_email_address_mother_create_method_invalid_domain_type() -> None:
    """
    Check that EmailAddressMother create method raises a TypeError when domain is not a string.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='EmailAddressMother domain must be a string.',
    ):
        EmailAddressMother.create(domain=EmailAddressMother.invalid_type())


@mark.unit_testing
def test_email_address_mother_create_method_domain_too_long() -> None:
    """
    Check that EmailAddressMother create method rejects an oversized provided domain.
    """
    with assert_raises(
        expected_exception=ValueError,
        match='Domain "example.com" is too long',
    ):
        EmailAddressMother.create(min_length=8, max_length=8, domain='example.com')


@mark.unit_testing
def test_email_address_mother_create_method_string_case_uppercase() -> None:
    """
    Check that EmailAddressMother can force uppercase local parts.
    """
    value = EmailAddressMother.create(domain='example.com', string_case=StringCase.UPPERCASE)

    assert value.split('@')[0].isupper()


@mark.unit_testing
def test_email_address_mother_create_method_string_case_mixedcase() -> None:
    """
    Check that EmailAddressMother accepts mixed-case generation.
    """
    _assert_valid_email(EmailAddressMother.create(domain='example.com', string_case=StringCase.MIXEDCASE))


@mark.unit_testing
def test_email_address_mother_create_method_invalid_string_case_type() -> None:
    """
    Check that EmailAddressMother validates string_case type.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='EmailAddressMother string_case must be a StringCase.',
    ):
        EmailAddressMother.create(string_case=StringMother.invalid_type())


@mark.unit_testing
def test_email_address_mother_create_method_fallback_exact_short_length(monkeypatch: MonkeyPatch) -> None:
    """
    Check deterministic fallback generation for exact short lengths.
    """
    monkeypatch.setattr(DomainMother, 'create', _domain_factory_that_fails_after_first_call())

    assert EmailAddressMother.create(min_length=6, max_length=6, string_case=StringCase.LOWERCASE) == 'xx@a.b'
    assert len(EmailAddressMother.create(min_length=10, max_length=10, string_case=StringCase.LOWERCASE)) == 10
    assert len(EmailAddressMother.create(min_length=12, max_length=12, string_case=StringCase.LOWERCASE)) == 12


@mark.unit_testing
def test_email_address_mother_create_method_retries_oversized_generated_domain(monkeypatch: MonkeyPatch) -> None:
    """
    Check that create retries when a generated domain cannot satisfy length bounds.
    """
    monkeypatch.setattr(DomainMother, 'create', _domain_factory_that_returns_one_oversized_domain())

    _assert_valid_email(
        EmailAddressMother.create(min_length=8, max_length=20, string_case=StringCase.LOWERCASE),
        min_length=8,
        max_length=20,
    )


@mark.unit_testing
def test_email_address_mother_create_method_fallback_exact_long_length(monkeypatch: MonkeyPatch) -> None:
    """
    Check deterministic fallback generation when a max-length local part needs a custom domain.
    """
    monkeypatch.setattr(DomainMother, 'create', _domain_factory_that_fails_after_first_call())

    assert len(EmailAddressMother.create(min_length=75, max_length=75, string_case=StringCase.LOWERCASE)) == 75
    assert len(EmailAddressMother.create(min_length=100, max_length=100, string_case=StringCase.LOWERCASE)) == 100


@mark.unit_testing
def test_email_address_mother_create_method_fallback_range(monkeypatch: MonkeyPatch) -> None:
    """
    Check fallback generation for range constraints.
    """
    monkeypatch.setattr(DomainMother, 'create', _domain_factory_that_fails_after_first_call())

    _assert_valid_email(
        EmailAddressMother.create(min_length=6, max_length=7, string_case=StringCase.LOWERCASE),
        min_length=6,
        max_length=7,
    )


@mark.unit_testing
def test_email_address_mother_generate_local_part_rejects_long_values(monkeypatch: MonkeyPatch) -> None:
    """
    Check local-part generation rejects values longer than RFC permits.
    """
    monkeypatch.setattr(UsernameMother, 'create', classmethod(_long_username_factory))

    with assert_raises(
        expected_exception=ValueError,
        match='Local part length must be less than or equal to 64.',
    ):
        EmailAddressMother._generate_local_part(min_length=1, max_length=64)


@mark.unit_testing
def test_email_address_mother_of_length_method_happy_path() -> None:
    """
    Check that EmailAddressMother of_length method returns an email of the requested length.
    """
    length = 16

    assert len(EmailAddressMother.of_length(length=length)) == length


@mark.unit_testing
def test_email_address_mother_rfc_create_method_happy_path() -> None:
    """
    Check that EmailAddressMother rfc_create method returns an RFC-shaped email address.
    """
    value = EmailAddressMother.rfc_create()

    _assert_valid_email(value)
    assert value == value.lower()


@mark.unit_testing
def test_email_address_mother_rfc_create_method_recovers_from_domain_error(monkeypatch: MonkeyPatch) -> None:
    """
    Check that RFC generation retries transient domain-generation failures.
    """
    calls = 0

    def domain_factory(cls: type[DomainMother]) -> str:
        """
        Fail once and then return a valid RFC domain.
        """
        nonlocal calls
        calls += 1
        if calls == 1:
            raise KeyError
        return 'example.com'

    monkeypatch.setattr(DomainMother, 'rfc_create', classmethod(domain_factory))

    assert EmailAddressMother.rfc_create().endswith('@example.com')


@mark.unit_testing
def test_email_address_mother_rfc_create_method_fallback(monkeypatch: MonkeyPatch) -> None:
    """
    Check that RFC generation falls back after exhausting invalid domains.
    """
    monkeypatch.setattr(DomainMother, 'rfc_create', classmethod(_oversized_rfc_domain_factory))

    _assert_valid_email(EmailAddressMother.rfc_create())


@mark.unit_testing
def test_email_address_mother_invalid_value_method() -> None:
    """
    Check that invalid_value returns a string.
    """
    assert type(EmailAddressMother.invalid_value()) is str
