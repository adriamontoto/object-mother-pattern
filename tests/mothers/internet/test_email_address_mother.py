# """
# Test module for the EmailAddressMother class.
# """

# from pytest import mark, raises as assert_raises

# from object_mother_pattern.mothers import IntegerMother, StringCase, StringMother
# from object_mother_pattern.mothers.internet import DomainMother, EmailAddressMother
# from object_mother_pattern.mothers.internet.utils import get_tld_dict


# @mark.unit_testing
# def test_email_address_mother_create_method_happy_path() -> None:
#     """
#     Check that EmailAddressMother create method returns a string value that is a valid email address.
#     """
#     value = EmailAddressMother.create()
#     local_part, domain_part = value.split('@')

#     assert type(value) is str
#     assert len(value) >= 8
#     assert len(value) <= 64
#     assert value == value.strip()
#     assert '@' in value
#     assert value.count('@') == 1
#     assert len(local_part) >= 1
#     assert len(local_part) <= 64
#     assert len(domain_part) >= 4
#     assert '.' in domain_part
#     assert not domain_part.startswith('.') and not domain_part.endswith('.')


# @mark.unit_testing
# def test_email_address_mother_create_method_with_value() -> None:
#     """
#     Check that EmailAddressMother create method returns the provided value.
#     """
#     test_email = EmailAddressMother.create()
#     value = EmailAddressMother.create(value=test_email)

#     assert value == test_email


# @mark.unit_testing
# def test_email_address_mother_create_method_invalid_value_type() -> None:
#     """
#     Check that EmailAddressMother create method raises a TypeError when the provided value is not a string.
#     """
#     with assert_raises(
#         expected_exception=TypeError,
#         match='EmailAddressMother value must be a string.',
#     ):
#         EmailAddressMother.create(value=EmailAddressMother.invalid_type())


# @mark.unit_testing
# def test_email_address_mother_create_method_min_length_and_max_length_constraints() -> None:
#     """
#     Check that EmailAddressMother create method respects min_length and max_length constraints.
#     """
#     value = EmailAddressMother.create(min_length=10, max_length=20)

#     assert 10 <= len(value) <= 20


# @mark.unit_testing
# def test_email_address_mother_create_method_invalid_min_length_type() -> None:
#     """
#     Check that EmailAddressMother create method raises a TypeError when min_length is not an integer.
#     """
#     with assert_raises(
#         expected_exception=TypeError,
#         match='EmailAddressMother min_length must be an integer.',
#     ):
#         EmailAddressMother.create(min_length=IntegerMother.invalid_type())


# @mark.unit_testing
# def test_email_address_mother_create_method_invalid_max_length_type() -> None:
#     """
#     Check that EmailAddressMother create method raises a TypeError when max_length is not an integer.
#     """
#     with assert_raises(
#         expected_exception=TypeError,
#         match='EmailAddressMother max_length must be an integer.',
#     ):
#         EmailAddressMother.create(max_length=IntegerMother.invalid_type())


# @mark.unit_testing
# def test_email_address_mother_create_method_min_length_too_small() -> None:
#     """
#     Check that EmailAddressMother create method raises a ValueError when min_length is less than 6.
#     """
#     with assert_raises(
#         expected_exception=ValueError,
#         match='EmailAddressMother min_length must be at least 6.',
#     ):
#         EmailAddressMother.create(min_length=5)


# @mark.unit_testing
# def test_email_address_mother_create_method_max_length_too_large() -> None:
#     """
#     Check that EmailAddressMother create method raises a ValueError when max_length exceeds 254.
#     """
#     with assert_raises(
#         expected_exception=ValueError,
#         match='EmailAddressMother max_length must be at most 254.',
#     ):
#         EmailAddressMother.create(max_length=255)


# @mark.unit_testing
# def test_email_address_mother_create_method_min_length_greater_than_max_length() -> None:
#     """
#     Check that EmailAddressMother create method raises a ValueError when min_length > max_length.
#     """
#     with assert_raises(
#         expected_exception=ValueError,
#         match='EmailAddressMother min_length must be less than or equal to max_length.',
#     ):
#         EmailAddressMother.create(min_length=20, max_length=10)


# @mark.unit_testing
# def test_email_address_mother_create_method_with_domain() -> None:
#     """
#     Check that EmailAddressMother create method uses the provided domain.
#     """
#     test_domain = DomainMother.create()
#     value = EmailAddressMother.create(domain=test_domain)

#     domain_part = value.split('@')[1]
#     assert domain_part == test_domain


# @mark.unit_testing
# def test_email_address_mother_create_method_invalid_domain_type() -> None:
#     """
#     Check that EmailAddressMother create method raises a TypeError when domain is not a string.
#     """
#     with assert_raises(
#         expected_exception=TypeError,
#         match='EmailAddressMother domain must be a string.',
#     ):
#         EmailAddressMother.create(domain=IntegerMother.create())


# @mark.unit_testing
# def test_email_address_mother_create_method_string_case_lowercase() -> None:
#     """
#     Test EmailAddressMother create method with lowercase string case.
#     """
#     value = EmailAddressMother.create(string_case=StringCase.LOWERCASE)

#     local_part = value.split('@')[0]
#     assert local_part.islower()


# @mark.unit_testing
# def test_email_address_mother_create_method_string_case_uppercase() -> None:
#     """
#     Test EmailAddressMother create method with uppercase string case.
#     """
#     value = EmailAddressMother.create(string_case=StringCase.UPPERCASE)

#     local_part = value.split('@')[0]
#     assert local_part.isupper()


# @mark.unit_testing
# def test_email_address_mother_create_method_string_case_mixedcase() -> None:
#     """
#     Test EmailAddressMother create method with mixed case.
#     """
#     value = EmailAddressMother.create(string_case=StringCase.MIXEDCASE)

#     assert isinstance(value, str)


# @mark.unit_testing
# def test_email_address_mother_create_method_invalid_string_case_type() -> None:
#     """
#     Check that EmailAddressMother create method raises a TypeError when string_case is invalid.
#     """
#     with assert_raises(
#         expected_exception=TypeError,
#         match='EmailAddressMother string_case must be a StringCase.',
#     ):
#         EmailAddressMother.create(string_case=StringMother.invalid_type())


# @mark.unit_testing
# def test_email_address_mother_rfc_create_method_happy_path() -> None:
#     """
#     Check that EmailAddressMother rfc_create method returns an RFC-compliant email address.
#     """
#     value = EmailAddressMother.rfc_create()

#     local_part, domain_part = value.split('@')
#     tlds = {tld for tlds in get_tld_dict().values() for tld in tlds}
#     domain_tld = domain_part.split('.')[-1].lower()

#     assert type(value) is str
#     assert len(value) >= 6
#     assert len(value) <= 254
#     assert len(local_part) <= 64
#     assert len(local_part) >= 1
#     assert value.islower()
#     assert '@' in value
#     assert value.count('@') == 1
#     assert domain_tld in tlds

#     for char in local_part:
#         assert char.isalnum() or char in '.+'


# @mark.unit_testing
# def test_email_address_mother_rfc_create_multiple_generations() -> None:
#     """
#     Test that EmailAddressMother rfc_create generates different RFC-compliant emails.
#     """
#     emails = {EmailAddressMother.rfc_create() for _ in range(20)}

#     assert len(emails) > 1
#     for email in emails:
#         assert len(email) <= 254
#         assert len(email.split('@')[0]) <= 64
#         assert email.islower()


# @mark.unit_testing
# def test_email_address_mother_rfc_create_handles_long_domains() -> None:
#     """
#     Test that EmailAddressMother rfc_create handles cases with very long domains gracefully.
#     """
#     for _ in range(10):
#         email = EmailAddressMother.rfc_create()
#         local_part, domain_part = email.split('@')

#         assert len(email) <= 254
#         assert len(local_part) <= 64
#         assert len(local_part) >= 1
#         assert len(domain_part) >= 4


# @mark.unit_testing
# def test_email_address_mother_generate_local_part_happy_path() -> None:
#     """
#     Test EmailAddressMother _generate_local_part method with valid parameters.
#     """
#     local_part = EmailAddressMother._generate_local_part(min_length=5, max_length=20)

#     assert isinstance(local_part, str)
#     assert 5 <= len(local_part) <= 20
#     assert len(local_part) <= 64


# @mark.unit_testing
# def test_email_address_mother_generate_local_part_max_length_exceeded() -> None:
#     """
#     Test EmailAddressMother _generate_local_part method raises error if local part exceeds 64 chars.
#     """
#     with assert_raises(
#         expected_exception=ValueError,
#         match='Local part length must be less than or equal to 64',
#     ):
#         EmailAddressMother._generate_local_part(min_length=65, max_length=70)


# @mark.unit_testing
# def test_email_address_mother_consistency_across_calls() -> None:
#     """
#     Test that EmailAddressMother produces consistent types and formats across multiple calls.
#     """
#     emails = [EmailAddressMother.create() for _ in range(10)]

#     assert all(isinstance(email, str) for email in emails)
#     for email in emails:
#         assert '@' in email
#         assert email.count('@') == 1
#         local_part, domain_part = email.split('@')
#         assert len(local_part) >= 1
#         assert len(domain_part) >= 4
#         assert '.' in domain_part


# @mark.unit_testing
# def test_email_address_mother_edge_case_minimum_length() -> None:
#     """
#     Test EmailAddressMother with minimum possible length constraints.
#     """
#     email = EmailAddressMother.create(min_length=8, max_length=15)

#     assert 8 <= len(email) <= 15
#     assert '@' in email
#     local_part, domain_part = email.split('@')
#     assert len(local_part) >= 1
#     assert len(domain_part) >= 4


# @mark.unit_testing
# def test_email_address_mother_edge_case_maximum_length() -> None:
#     """
#     Test EmailAddressMother with maximum RFC length constraints.
#     """
#     email = EmailAddressMother.create(min_length=50, max_length=254)

#     assert 50 <= len(email) <= 254
#     local_part, domain_part = email.split('@')
#     assert len(local_part) <= 64


# @mark.unit_testing
# def test_email_address_mother_domain_integration() -> None:
#     """
#     Test that EmailAddressMother properly integrates with domain generation.
#     """
#     tlds = {tld for tlds in get_tld_dict().values() for tld in tlds}

#     for _ in range(10):
#         email = EmailAddressMother.create()
#         domain_part = email.split('@')[1]
#         domain_tld = domain_part.split('.')[-1].lower()
#         assert domain_tld in tlds


# @mark.unit_testing
# def test_email_address_mother_invalid_type_method_happy_path() -> None:
#     """
#     Check that EmailAddressMother invalid_type method returns a non-string value.
#     """
#     assert type(EmailAddressMother.invalid_type()) is not str


# @mark.unit_testing
# def test_email_address_mother_invalid_value_method_happy_path() -> None:
#     """
#     Check that EmailAddressMother invalid_value method returns a non-printable string value.
#     """
#     value = EmailAddressMother.invalid_value()

#     assert type(value) is str
#     assert not value.isprintable()


# @mark.unit_testing
# def test_email_address_mother_create_method_domain_too_long_provided() -> None:
#     """
#     Test that EmailAddressMother raises ValueError when provided domain is too long for min_length.
#     """
#     long_domain = 'very-long-domain-name-that-exceeds-reasonable-length-for-testing-purposes.example.com'

#     with assert_raises(
#         expected_exception=ValueError,
#         match=f'Domain "{long_domain}" is too long to satisfy min_length 50.',
#     ):
#         EmailAddressMother.create(domain=long_domain, min_length=50)


# @mark.unit_testing
# def test_email_address_mother_of_length_method_happy_path() -> None:
#     """
#     Test that EmailAddressMother of_length method returns an email address of the specified length.
#     """
#     length = 15
#     email = EmailAddressMother.of_length(length=length)

#     assert isinstance(email, str)
#     assert len(email) == length
#     assert '@' in email
#     assert email.count('@') == 1

#     local_part, domain_part = email.split('@')
#     assert len(local_part) >= 1
#     assert len(domain_part) >= 4


# @mark.unit_testing
# def test_email_address_mother_of_length_method_various_lengths() -> None:
#     """
#     Test that EmailAddressMother of_length method works with various valid lengths.
#     """
#     test_lengths = [6, 10, 20, 30, 50, 100, 150, 254]

#     for length in test_lengths:
#         email = EmailAddressMother.of_length(length=length)
#         assert len(email) == length
#         assert '@' in email
#         local_part, domain_part = email.split('@')
#         assert len(local_part) <= 64  # RFC constraint


# @mark.unit_testing
# def test_email_address_mother_of_length_method_invalid_type() -> None:
#     """
#     Test that EmailAddressMother of_length method raises TypeError when length is not an integer.
#     """
#     with assert_raises(
#         expected_exception=TypeError,
#         match='EmailAddressMother min_length must be an integer.',
#     ):
#         EmailAddressMother.of_length(length=StringMother.create())


# @mark.unit_testing
# def test_email_address_mother_of_length_method_length_too_small() -> None:
#     """
#     Test that EmailAddressMother of_length method raises ValueError when length is less than 6.
#     """
#     with assert_raises(
#         expected_exception=ValueError,
#         match='EmailAddressMother min_length must be at least 6.',
#     ):
#         EmailAddressMother.of_length(length=5)


# @mark.unit_testing
# def test_email_address_mother_of_length_method_length_too_large() -> None:
#     """
#     Test that EmailAddressMother of_length method raises ValueError when length exceeds 254.
#     """
#     with assert_raises(
#         expected_exception=ValueError,
#         match='EmailAddressMother max_length must be at most 254.',
#     ):
#         EmailAddressMother.of_length(length=255)


# @mark.unit_testing
# def test_email_address_mother_of_length_method_minimum_length() -> None:
#     """
#     Test that EmailAddressMother of_length method works with minimum length (6).
#     """
#     email = EmailAddressMother.of_length(length=6)

#     assert len(email) == 6
#     assert '@' in email
#     local_part, domain_part = email.split('@')
#     assert len(local_part) >= 1
#     assert len(domain_part) >= 2  # At minimum needs a domain like "x.y"


# @mark.unit_testing
# def test_email_address_mother_of_length_method_maximum_length() -> None:
#     """
#     Test that EmailAddressMother of_length method works with maximum length (254).
#     """
#     email = EmailAddressMother.of_length(length=254)

#     assert len(email) == 254
#     assert '@' in email
#     local_part, domain_part = email.split('@')
#     assert len(local_part) <= 64  # RFC constraint
