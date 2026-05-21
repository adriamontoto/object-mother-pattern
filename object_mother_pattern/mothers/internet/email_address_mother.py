"""
EmailAddressMother module.
"""

from sys import version_info

if version_info >= (3, 12):
    from typing import override  # pragma: no cover
else:
    from typing_extensions import override  # pragma: no cover


from random import choice
from typing import assert_never

from object_mother_pattern.models import BaseMother
from object_mother_pattern.mothers import StringCase, StringMother
from object_mother_pattern.mothers.people import UsernameMother

from .domain_mother import DomainMother


class EmailAddressMother(BaseMother[str]):
    """
    EmailAddressMother class is responsible for creating random email address values.

    Example:
    ```python
    from object_mother_pattern.mothers.internet import EmailAddressMother

    email_address = EmailAddressMother.create()
    print(email_address)
    # >>> fowler.archer.com
    ```
    """

    _type: type = str

    @classmethod
    @override
    def create(  # noqa: C901
        cls,
        *,
        value: str | None = None,
        min_length: int = 8,
        max_length: int = 64,
        domain: str | None = None,
        string_case: StringCase | None = None,
    ) -> str:
        """
        Create a random email address value. If a specific email address value is provided via `value`, it is returned
        after validation. Otherwise, a random email address value is generated within the provided range of `min_length`
        and `max_length` (both included) and with the provided `domain`. If `domain` is None, a random domain is
        generated. If `string_case` is None, a random case is chosen from the available StringCase options.

        Args:
            value (str | None, optional): Specific value to return. Defaults to None.
            min_length (int, optional): The minimum length of the email address. Must be >= 6. Defaults to 8.
            max_length (int, optional): The maximum length of the email address. Must be <= 254 and >= `min_length`.
            Defaults to 64.
            domain (str | None, optional): The domain of the email address. Defaults to None.
            string_case (StringCase | None, optional): The case of the email address. Defaults to None.

        Raises:
            TypeError: If `min_length` is not an integer.
            TypeError: If `max_length` is not an integer.
            ValueError: If `min_length` is less than 6.
            ValueError: If `max_length` is more than 254.
            ValueError: If `min_length` is greater than `max_length`.
            TypeError: If `string_case` is not a StringCase.

        Returns:
            str: A randomly generated email address value with the provided constraints.
        """
        if value is not None:
            if type(value) is not str:
                raise TypeError('EmailAddressMother value must be a string.')

            return value

        if type(min_length) is not int:
            raise TypeError('EmailAddressMother min_length must be an integer.')

        if type(max_length) is not int:
            raise TypeError('EmailAddressMother max_length must be an integer.')

        if min_length < 6:
            raise ValueError('EmailAddressMother min_length must be at least 6.')

        if max_length > 254:
            raise ValueError('EmailAddressMother max_length must be at most 254.')

        if min_length > max_length:
            raise ValueError('EmailAddressMother min_length must be less than or equal to max_length.')

        if string_case is None:
            string_case = StringCase(value=choice(seq=tuple(StringCase)))  # noqa: S311

        if type(string_case) is not StringCase:
            raise TypeError('EmailAddressMother string_case must be a StringCase.')

        domain_provided = domain is not None
        if domain is None:
            domain = DomainMother.create(string_case=string_case)

        if type(domain) is not str:
            raise TypeError('EmailAddressMother domain must be a string.')

        local_part = None
        final_domain = None

        for _ in range(1000):
            try:
                current_domain = domain if domain_provided else DomainMother.create()

                domain_len = len(current_domain)
                at_sign_len = 1
                max_local = min(max_length - domain_len - at_sign_len, 64)
                min_local = max(min_length - domain_len - at_sign_len, 1)

                if min_local > max_local:
                    if domain_provided:
                        raise ValueError(f'Domain "{current_domain}" is too long to satisfy min_length {min_length}.')

                    continue

                local_part = cls._generate_local_part(min_length=min_local, max_length=max_local)
                final_domain = current_domain
                break

            except ValueError as exception:
                if domain_provided:
                    raise exception

                continue

        if local_part is None or final_domain is None:
            at_sign_len = 1

            if min_length == max_length:
                if max_length <= 6:
                    final_domain = 'a.b'
                elif max_length <= 10:
                    final_domain = 'a.co'
                else:
                    final_domain = 'ex.co'

                local_len = max_length - len(final_domain) - at_sign_len

                if local_len <= 64:
                    local_part = 'x' * local_len
                else:
                    local_part = 'x' * 64
                    needed_domain_len = max_length - 64 - at_sign_len
                    if needed_domain_len <= 10:
                        final_domain = f'{"x" * (needed_domain_len - 3)}.co'
                    else:
                        parts = []
                        remaining = needed_domain_len - 3
                        while remaining > 0:
                            part_len = min(remaining, 10)
                            parts.append('x' * part_len)
                            remaining -= part_len
                            if remaining > 0:
                                remaining -= 1
                        parts.append('co')
                        final_domain = '.'.join(parts)
            else:
                final_domain = 'ex.co'
                local_len = min(max_length - len(final_domain) - at_sign_len, 64)
                local_len = max(min_length - len(final_domain) - at_sign_len, local_len)
                local_len = max(1, local_len)
                local_part = UsernameMother.create(min_length=local_len, max_length=local_len, separators='.')

        match string_case:
            case StringCase.LOWERCASE:
                local_part = local_part.lower()

            case StringCase.UPPERCASE:
                local_part = local_part.upper()

            case StringCase.MIXEDCASE:
                local_part = ''.join(choice(seq=(char.upper(), char.lower())) for char in local_part)  # noqa: S311

            case _:  # pragma: no cover
                assert_never(string_case)

        return f'{local_part}@{final_domain}'

    @classmethod
    def _generate_local_part(cls, *, min_length: int, max_length: int) -> str:
        """
        Generate a random local part for an email address.
        """
        local_part = UsernameMother.create(min_length=min_length, max_length=max_length, separators='.')
        if len(local_part) > 64:
            raise ValueError('Local part length must be less than or equal to 64.')

        return local_part

    @classmethod
    def of_length(cls, *, length: int) -> str:
        """
        Create a random email address value of a specific length.

        Args:
            length (int): Required total email-address length.

        Returns:
            str: Generated email address with exactly `length` characters.
        """
        return cls.create(min_length=length, max_length=length)

    @classmethod
    def rfc_create(cls) -> str:
        """
        Create a random syntactically valid email address value based on RFC length constraints.

        The generated value keeps the local part within 64 characters and the complete address within 254 characters.

        Returns:
            str: RFC-length-compatible email address value.
        """
        for _ in range(1000):
            try:
                domain = DomainMother.rfc_create()

                domain_len = len(domain)
                at_sign_len = 1
                max_local = min(254 - domain_len - at_sign_len, 64)
                min_local = max(6 - domain_len - at_sign_len, 1)

                if min_local > max_local:
                    continue

                local_part = cls._generate_local_part(min_length=min_local, max_length=max_local)

                return f'{local_part.lower()}@{domain}'

            except (ValueError, KeyError):
                continue

        return cls.create(min_length=6, max_length=254, string_case=StringCase.LOWERCASE)

    @classmethod
    def invalid_value(cls) -> str:
        """
        Create an invalid email address value for negative-path tests.

        Returns:
            str: Invalid email-address value.
        """
        return StringMother.invalid_value()
