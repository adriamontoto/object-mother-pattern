"""
DomainMother module.
"""

from enum import StrEnum, unique
from random import choice, randint
from sys import version_info
from typing import assert_never

if version_info >= (3, 12):
    from typing import override  # pragma: no cover
else:
    from typing_extensions import override  # pragma: no cover

from object_mother_pattern.mothers import StringMother
from object_mother_pattern.mothers.base_mother import BaseMother

from .utils import get_label_dict, get_tld_dict


@unique
class DomainCase(StrEnum):
    """
    Type of Domain cases.
    """

    LOWERCASE = 'lowercase'
    UPPERCASE = 'uppercase'
    MIXEDCASE = 'mixedcase'


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

    _type: type = str

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
        domain_case: DomainCase | None = None,
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
            domain_case (DomainCase | None, optional): The case of the domain. Defaults to None.

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
            TypeError: If `domain_case` is not a DomainCase.
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

        if domain_case is None:
            domain_case = DomainCase(value=choice(seq=tuple(DomainCase)))  # noqa: S311

        if type(domain_case) is not DomainCase:
            raise TypeError('DomainMother domain_case must be a DomainCase.')

        tld_domains = get_tld_dict()
        labels = get_label_dict()

        for _ in range(10):
            try:
                domain_format = cls._generate_domain_format(
                    min_length=min_length,
                    max_length=max_length,
                    min_labels=min_labels,
                    max_labels=max_labels,
                )

                domain = cls._generate_domain(tld_domains=tld_domains, labels=labels, domain_format=domain_format)
                break

            except KeyError:
                continue

        match domain_case:
            case DomainCase.LOWERCASE:
                domain = domain.lower()

            case DomainCase.UPPERCASE:
                domain = domain.upper()

            case DomainCase.MIXEDCASE:
                domain = ''.join(choice(seq=(char.upper(), char.lower())) for char in domain)  # noqa: S311

            case _:  # pragma: no cover
                assert_never(domain_case)

        return domain

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
    def invalid_value(cls) -> str:
        """
        Create an invalid domain value.

        Returns:
            str: Invalid domain string.
        """
        return StringMother.invalid_value()
