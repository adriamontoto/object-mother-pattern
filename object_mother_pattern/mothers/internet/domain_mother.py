"""
DomainMother module.
"""

from sys import version_info

if version_info >= (3, 12):
    from typing import override  # pragma: no cover
else:
    from typing_extensions import override  # pragma: no cover

from random import choice, randint, sample
from typing import assert_never

from object_mother_pattern.models import BaseMother
from object_mother_pattern.mothers import StringCase
from object_mother_pattern.mothers.primitives.string_mother import StringMother

from .utils import get_label_dict, get_tld_dict


class DomainMother(BaseMother[str]):
    """
    DomainMother class is responsible for creating random domain values.

    Example:
    ```python
    from object_mother_pattern.mothers.internet import DomainMother

    domain = DomainMother.create()
    print(domain)
    # >>> fowler.archer.com
    ```
    """

    @classmethod
    @override
    def create(  # noqa: C901
        cls,
        *,
        value: str | None = None,
        min_length: int = 10,
        max_length: int = 30,
        min_labels: int = 2,
        max_labels: int = 4,
        string_case: StringCase | None = None,
        include_hyphens: bool = True,
        include_numbers: bool = True,
    ) -> str:
        """
        Create a random domain value. If a specific domain value is provided via `value`, it is returned after
        validation. Otherwise, a random domain value is generated within the provided range of `min_length` and
        `max_length` (both included) and with the provided range of `min_labels` and `max_labels` (both included). If
        `domain_case` is None, a random case is chosen from the available DomainCase options.

        Args:
            value (str | None, optional): Specific value to return. Defaults to None.
            min_length (int, optional): The minimum length of the domain. Must be >= 4. Defaults to 10.
            max_length (int, optional): The maximum length of the domain. Must be <= 253 and >= `min_length`. Defaults
            to 30.
            min_labels (int, optional): The minimum number of labels in the domain. Must be >= 2. Defaults to 2.
            max_labels (int, optional): The maximum number of labels in the domain. Must be <= 127 and >= `min_labels`.
            Defaults to 4.
            string_case (StringCase | None, optional): The case of the domain. Defaults to None.
            include_hyphens (bool, optional): Whether to include hyphens in the domain. Defaults to True.
            include_numbers (bool, optional): Whether to include numbers in the domain. Defaults to True.

        Raises:
            TypeError: If `min_length` is not an integer.
            TypeError: If `max_length` is not an integer.
            TypeError: If `min_labels` is not an integer.
            TypeError: If `max_labels` is not an integer.
            ValueError: If `min_length` is less than 4.
            ValueError: If `max_length` is more than 253.
            ValueError: If `min_length` is greater than `max_length`.
            ValueError: If `min_labels` is less than 2.
            ValueError: If `max_labels` is less than 2.
            ValueError: If `max_labels` is more than 127.
            ValueError: If `min_labels` is greater than `max_labels`.
            TypeError: If `string_case` is not a StringCase.
            TypeError: If `include_hyphens` is not a boolean.
            TypeError: If `include_numbers` is not a boolean.
            ValueError: If the total letters are not in the feasible range for given labels and constraints.

        Returns:
            str: A randomly generated domain value within the provided range of labels.

        Example:
        ```python
        from object_mother_pattern.mothers.internet import DomainMother

        domain = DomainMother.create()
        print(domain)
        # >>> fowler.archer.com
        ```
        """
        if value is not None:
            if type(value) is not str:
                raise TypeError('DomainMother value must be a string.')

            return value

        if type(min_length) is not int:
            raise TypeError('DomainMother min_length must be an integer.')

        if type(max_length) is not int:
            raise TypeError('DomainMother max_length must be an integer.')

        if type(min_labels) is not int:
            raise TypeError('DomainMother min_labels must be an integer.')

        if type(max_labels) is not int:
            raise TypeError('DomainMother max_labels must be an integer.')

        if min_length < 4:
            raise ValueError('DomainMother min_length must be at least 4.')

        if max_length > 253:
            raise ValueError('DomainMother max_length must be at most 253.')

        if min_length > max_length:
            raise ValueError('DomainMother min_length must be less than or equal to max_length.')

        if min_labels < 2:
            raise ValueError('DomainMother min_labels must be at least 2.')

        if max_labels > 127:
            raise ValueError('DomainMother max_labels must be at most 127.')

        if min_labels > max_labels:
            raise ValueError('DomainMother min_labels must be less than or equal to max_labels.')

        if string_case is None:
            string_case = StringCase(value=choice(seq=tuple(StringCase)))  # noqa: S311

        if type(string_case) is not StringCase:
            raise TypeError('DomainMother string_case must be a StringCase.')

        if type(include_hyphens) is not bool:
            raise TypeError('DomainMother include_hyphens must be a boolean.')

        if type(include_numbers) is not bool:
            raise TypeError('DomainMother include_numbers must be a boolean.')

        tld_domains = get_tld_dict()
        labels = get_label_dict()

        for _ in range(1000):  # pragma: no cover
            try:
                domain_format = cls._generate_domain_format(
                    min_length=min_length,
                    max_length=max_length,
                    min_labels=min_labels,
                    max_labels=max_labels,
                )

                domain = cls._generate_domain(tld_domains=tld_domains, labels=labels, domain_format=domain_format)
                break

            except (ValueError, KeyError):
                continue

        domain = cls._noisy_domain(domain=domain, include_hyphens=include_hyphens, include_numbers=include_numbers)

        match string_case:
            case StringCase.LOWERCASE:
                domain = domain.lower()

            case StringCase.UPPERCASE:
                domain = domain.upper()

            case StringCase.MIXEDCASE:
                domain = ''.join(choice(seq=(char.upper(), char.lower())) for char in domain)  # noqa: S311

            case _:  # pragma: no cover
                assert_never(string_case)

        return domain

    @classmethod
    def of_length(cls, *, length: int) -> str:
        """
        Create a random domain value of a specific length.

        Args:
            length (int): The length of the domain.

        Returns:
            str: A randomly generated domain value of the specified length.

        Example:
        ```python
        from object_mother_pattern.mothers.internet import DomainMother

        domain = DomainMother.of_length(length=16)
        print(domain)
        # >>> seen.dip.home.si
        ```
        """
        return cls.create(min_length=length, max_length=length, min_labels=2, max_labels=127)

    @classmethod
    def _generate_domain_format(  # noqa: C901
        cls,
        *,
        min_length: int = 10,
        max_length: int = 30,
        min_labels: int = 2,
        max_labels: int = 4,
    ) -> tuple[int, ...]:
        """
        Generate a random domain format based on the constraints. A domain format is a tuple of label lengths, so if the
        domain format is (4, 4, 3), the domain will be something like "data.iana.org".

        Args:
            min_length (int, optional): The minimum length of the domain. Must be >= 4. Defaults to 10.
            max_length (int, optional): The maximum length of the domain. Must be <= 253 and >= `min_length`. Defaults
            to 30.
            min_labels (int, optional): The minimum number of labels in the domain. Must be >= 2. Defaults to 2.
            max_labels (int, optional): The maximum number of labels in the domain. Must be <= 127 and >= `min_labels`.
            Defaults to 4.

        Raises:
            ValueError: If the total letters are not in the feasible range for given labels and constraints.

        Returns:
            tuple[int, ...]: The random domain format generated based on the constraints.
        """
        total_labels = randint(a=min_labels, b=max_labels)  # noqa: S311
        total_length = randint(a=min_length, b=max_length)  # noqa: S311
        total_letters = total_length - (total_labels - 1)

        lower_bounds = [1] * (total_labels - 1) + [2]  # minimum TLD length is 2
        upper_bounds = [64] * (total_labels - 1) + [18]  # maximum TLD length is 24, but there are not 19 and 21 TLDs

        min_required = sum(lower_bounds)
        max_possible = sum(upper_bounds)
        if total_letters < min_required or total_letters > max_possible:
            raise ValueError('Total letters not in the feasible range for given labels and constraints.')

        partition_extras = []
        extra_total = total_letters - min_required
        for i in range(total_labels):
            max_extra_for_label = upper_bounds[i] - lower_bounds[i]

            remaining_capacity = sum(upper_bounds[j] - lower_bounds[j] for j in range(i + 1, total_labels))
            min_extra_possible = max(0, extra_total - remaining_capacity)
            max_extra_possible = min(max_extra_for_label, extra_total)

            extra_for_label = randint(a=min_extra_possible, b=max_extra_possible)  # noqa: S311
            partition_extras.append(extra_for_label)
            extra_total -= extra_for_label

        return tuple(lower_bounds[i] + partition_extras[i] for i in range(total_labels))

    @classmethod
    def _generate_domain(
        cls,
        *,
        tld_domains: dict[int, tuple[str, ...]],
        labels: dict[int, tuple[str, ...]],
        domain_format: tuple[int, ...],
    ) -> str:
        """
        Generate a random domain based on given `tld_domains`, `labels` and `domain_format`.

        Args:
            tld_domains (dict[int, tuple[str, ...]]): The top level domains in lower case sorted by domain length.
            labels (dict[int, tuple[str, ...]]): The labels in lower case sorted by label length.
            domain_format (tuple[int]): A tuple of label lengths for the domain.

        Raises:
            KeyError: If a label length is not found in `labels`.

        Returns:
            str: The random domain generated based on the constraints.
        """
        domain = []
        domain.append(choice(seq=tld_domains[domain_format[-1]]))  # noqa: S311

        for length in list(reversed(domain_format))[1:]:
            domain.append(choice(seq=labels[length]))  # noqa: S311, PERF401

        return '.'.join(reversed(domain))

    @classmethod
    def _noisy_domain(cls, *, domain: str, include_hyphens: bool, include_numbers: bool) -> str:  # noqa: C901
        """
        Add noise to a domain by adding some random hyphens and numbers.

        Args:
            domain (str): The domain to add noise to.
            include_hyphens (bool): Whether to include hyphens in the domain.
            include_numbers (bool): Whether to include numbers in the domain.

        Returns:
            str: The domain with noise added.
        """
        *labels, tld = domain.split('.')
        domain_without_tld_length = len('.'.join(labels))

        max_noise = max(1, domain_without_tld_length // 4)

        number_of_hyphens = 0
        if include_hyphens:
            number_of_hyphens = randint(a=0, b=max_noise)  # noqa: S311

        number_of_numbers = 0
        if include_numbers:
            number_of_numbers = randint(a=0, b=max_noise)  # noqa: S311

        total_noise = number_of_hyphens + number_of_numbers
        if total_noise == 0:
            return domain

        legal_slots: list[tuple[int, int]] = []
        for idx, label in enumerate(labels):
            label_len = len(label)
            if label_len < 2:
                continue

            for position in range(1, label_len - 1):  # skip first/last char
                if label.startswith('xn--') and position in (2, 3):  # extra guard for Punycode A-labels
                    continue  # pragma: no cover

                legal_slots.append((idx, position))

        if not legal_slots:
            return domain

        total_noise = min(total_noise, len(legal_slots))
        number_of_hyphens = min(number_of_hyphens, total_noise)

        chosen_slots = sample(population=legal_slots, k=total_noise)  # noqa: S311
        hyphen_slots = set(sample(population=chosen_slots, k=number_of_hyphens)) if number_of_hyphens else set()
        digit_slots = set(chosen_slots) - hyphen_slots

        for idx, label in enumerate(labels):
            if all(idx != slot_idx for (slot_idx, _) in chosen_slots):
                continue

            chars = list(label)
            for position in range(len(chars)):
                if (idx, position) in hyphen_slots:
                    chars[position] = '-'

                elif (idx, position) in digit_slots:
                    chars[position] = str(randint(a=0, b=9))  # noqa: S311

            labels[idx] = ''.join(chars)

        return '.'.join([*labels, tld])

    @classmethod
    def rfc_create(cls) -> str:
        """
        Create a RFC 1035/1123 compliant domain name that strictly follows DNS specifications.

        This method generates domain names that comply with:
        - RFC 1035: Domain Names - Implementation and Specification
        - RFC 1123: Requirements for Internet Hosts - Application and Support
        - RFC 3696: Application Techniques for Checking and Transformation of Names

        RFC Requirements Enforced:
        - Total domain length ≤ 253 characters (presentation form)
        - Each label: 1-63 characters
        - Characters allowed: letters (a-z), digits (0-9), hyphens (-)
        - Hyphens cannot be at the beginning or end of labels
        - At least 2 labels (domain + TLD minimum)
        - Case insensitive (generated in lowercase)
        - Uses official IANA TLD list
        - Domain structure: 2-127 labels total

        Returns:
            str: A randomly generated RFC-compliant domain name.

        References:
            RFC 1035: https://www.rfc-editor.org/rfc/rfc1035
            RFC 1123: https://www.rfc-editor.org/rfc/rfc1123
            RFC 3696: https://www.rfc-editor.org/rfc/rfc3696
            IANA TLD List: https://data.iana.org/TLD/tlds-alpha-by-domain.txt

        Example:
            ```python
            from object_mother_pattern.mothers.internet import DomainMother

            domain = DomainMother.rfc_create()
            print(domain)
            # >>> q.e-------d.r------r.e.n.p.e.o.j.s.h.e.b.o.g.j.w.o.g.k.l.u.n.c.d.r.g.o.w.y.t.n.h.e.q.r.q.c.u.c.p.v.n.u.d.y.u.b.p.e.r.s.b.g.u.o.b.g.h.h.i.y.f.r.g.g.t.w.p.q.x.i.t.f.n.s.z.k.c.j.i.o.z.p.gh
            ```
        """  # noqa: E501
        return cls.create(
            min_length=4,
            max_length=253,
            min_labels=2,
            max_labels=127,
            string_case=StringCase.LOWERCASE,
            include_hyphens=True,
            include_numbers=True,
        )

    @classmethod
    def invalid_value(cls) -> str:
        """
        Create an invalid domain value.

        Returns:
            str: Invalid domain string.
        """
        return StringMother.invalid_value()
