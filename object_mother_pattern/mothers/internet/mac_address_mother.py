"""
MacAddressMother module.
"""

from sys import version_info

if version_info >= (3, 12):
    from typing import override  # pragma: no cover
else:
    from typing_extensions import override  # pragma: no cover

from enum import StrEnum, unique
from random import choice
from typing import assert_never

from object_mother_pattern.mothers import StringMother
from object_mother_pattern.mothers.base_mother import BaseMother


@unique
class MacAddressFormat(StrEnum):
    """
    Type of MAC address formats.
    """

    RAW = 'raw'
    UNIVERSAL = 'universal'
    WINDOWS = 'windows'
    CISCO = 'cisco'
    SPACE = 'space'
    NULL = 'null'
    BROADCAST = 'broadcast'


@unique
class MacAddressCase(StrEnum):
    """
    Type of MAC address cases.
    """

    LOWERCASE = 'lowercase'
    UPPERCASE = 'uppercase'
    MIXED = 'mixed'


class MacAddressMother(BaseMother[str]):
    """
    MacAddressMother class is responsible for creating random MAC address values.

    Formats:
        - Raw: `D5B9EB4DC2CC`
        - Universal: `D5:B9:EB:4D:C2:CC`
        - Windows: `D5-B9-EB-4D-C2-CC`
        - Cisco: `D5B9.EB4D.C2CC`
        - Space: `D5 B9 EB 4D C2 CC`

    Example:
    ```python
    from object_mother_pattern.mothers.internet import MacAddressMother

    mac = MacAddressMother.create()
    print(mac)
    # >>> D5:B9:EB:4D:C2:CC
    ```
    """

    _type: type = str

    @classmethod
    @override
    def create(cls, *, value: str | None = None) -> str:  # noqa: C901
        """
        Create a random MAC address value with a random format and random case (lowercase, uppercase, mixed). If a
        specific MAC address value is provided via `value`, it is returned after validation.

        Args:
            value (str | None, optional): A specific MAC address value to return. Defaults to None.

        Raises:
            TypeError: If the provided `value` is not a string.

        Returns:
            str: A randomly generated MAC address value.

        Example:
        ```python
        from object_mother_pattern.mothers.internet import MacAddressMother

        mac = MacAddressMother.create()
        print(mac)
        # >>> D5:B9:EB:4D:C2:CC
        ```
        """
        if value is not None:
            if type(value) is not str:
                raise TypeError('MacAddressMother value must be a string.')

            return value

        mac_format = MacAddressFormat(value=choice(seq=tuple(MacAddressFormat)))  # noqa: S311
        match mac_format:
            case MacAddressFormat.RAW:
                mac_address = cls.raw_format()

            case MacAddressFormat.UNIVERSAL:
                mac_address = cls.universal_format()

            case MacAddressFormat.WINDOWS:
                mac_address = cls.windows_format()

            case MacAddressFormat.CISCO:
                mac_address = cls.cisco_format()

            case MacAddressFormat.SPACE:
                mac_address = cls.space_format()

            case MacAddressFormat.NULL:
                mac_address = cls.null()

            case MacAddressFormat.BROADCAST:
                mac_address = cls.broadcast()

            case _:
                assert_never(mac_format)

        mac_case = MacAddressCase(value=choice(seq=tuple(MacAddressCase)))  # noqa: S311
        match mac_case:
            case MacAddressCase.LOWERCASE:
                mac_address = mac_address.lower()

            case MacAddressCase.UPPERCASE:
                mac_address = mac_address.upper()

            case MacAddressCase.MIXED:
                mac_address = ''.join(choice(seq=(char.upper(), char.lower())) for char in mac_address)  # noqa: S311

            case _:
                assert_never(mac_case)

        return mac_address

    @classmethod
    def _create(cls) -> str:
        """
        Create a random MAC address value.

        Returns:
            str: Random MAC address string.
        """
        return cls._random().mac_address()

    @classmethod
    def lowercase(cls) -> str:
        """
        Create a random lowercase MAC address value.

        Returns:
            str: A randomly lowercase MAC address string.

        Example:
        ```python
        from object_mother_pattern.mothers.internet import MacAddressMother

        mac = MacAddressMother.lowercase()
        print(mac)
        # >>> d5:b9:eb:4d:c2:cc
        ```
        """
        return cls._create().lower()

    @classmethod
    def uppercase(cls) -> str:
        """
        Create a random uppercase MAC address value.

        Returns:
            str: A randomly uppercase MAC address string.

        Example:
        ```python
        from object_mother_pattern.mothers.internet import MacAddressMother

        mac = MacAddressMother.uppercase()
        print(mac)
        # >>> D5:B9:EB:4D:C2:CC
        ```
        """
        return cls._create()

    @classmethod
    def mixed(cls) -> str:
        """
        Create a random mixed-case MAC address value.

        Returns:
            str: A randomly mixed-case MAC address string.

        Example:
        ```python
        from object_mother_pattern.mothers.internet import MacAddressMother

        mac = MacAddressMother.mixed()
        print(mac)
        # >>> 82:66:2b:FA:80:6E
        ```
        """
        return ''.join(choice(seq=(char.upper(), char.lower())) for char in cls._create())  # noqa: S311

    @classmethod
    def raw_format(cls) -> str:
        """
        Create a random raw MAC address value `d5b9eb4dc2cc`.

        Returns:
            str: A randomly raw MAC address string.

        Example:
        ```python
        from object_mother_pattern.mothers.internet import MacAddressMother

        mac = MacAddressMother.raw_format()
        print(mac)
        # >>> d5b9eb4dc2cc
        ```
        """
        return cls._create().replace(':', '')

    @classmethod
    def universal_format(cls) -> str:
        """
        Create a random universal MAC address value `D5:B9:EB:4D:C2:CC`.

        Returns:
            str: A randomly universal MAC address string.

        Example:
        ```python
        from object_mother_pattern.mothers.internet import MacAddressMother

        mac = MacAddressMother.universal_format()
        print(mac)
        # >>> D5:B9:EB:4D:C2:CC
        ```
        """
        return cls._create()

    @classmethod
    def windows_format(cls) -> str:
        """
        Create a random Windows MAC address value `D5-B9-EB-4D-C2-CC`.

        Returns:
            str: A randomly Windows MAC address string.

        Example:
        ```python
        from object_mother_pattern.mothers.internet import MacAddressMother

        mac = MacAddressMother.windows_format()
        print(mac)
        # >>> D5-B9-EB-4D-C2-CC
        ```
        """
        return cls._create().replace(':', '-')

    @classmethod
    def cisco_format(cls) -> str:
        """
        Create a random Cisco MAC address value `D5B9.EB4D.C2CC`.

        Returns:
            str: A randomly Cisco MAC address string.

        Example:
        ```python
        from object_mother_pattern.mothers.internet import MacAddressMother

        mac = MacAddressMother.cisco_format()
        print(mac)
        # >>> D5B9.EB4D.C2CC
        ```
        """
        mac = cls.raw_format()
        return f'{mac[:4]}.{mac[4:8]}.{mac[8:]}'

    @classmethod
    def space_format(cls) -> str:
        """
        Create a random MAC address value with spaces `D5 B9 EB 4D C2 CC`.

        Returns:
            str: A randomly MAC address string with spaces.

        Example:
        ```python
        from object_mother_pattern.mothers.internet import MacAddressMother

        mac = MacAddressMother.space_format()
        print(mac)
        # >>> D5 B9 EB 4D C2 CC
        ```
        """
        return cls._create().replace(':', ' ')

    @classmethod
    def null(cls) -> str:
        """
        Create a null MAC address value `00:00:00:00:00:00`.

        Returns:
            str: A null MAC address string.

        Example:
        ```python
        from object_mother_pattern.mothers.internet import MacAddressMother

        mac = MacAddressMother.null()
        print(mac)
        # >>> 00:00:00:00:00:00
        ```
        """
        return '00:00:00:00:00:00'

    @classmethod
    def broadcast(cls) -> str:
        """
        Create a broadcast MAC address value `FF:FF:FF:FF:FF:FF`.

        Returns:
            str: A broadcast MAC address string.

        Example:
        ```python
        from object_mother_pattern.mothers.internet import MacAddressMother

        mac = MacAddressMother.broadcast()
        print(mac)
        # >>> FF:FF:FF:FF:FF:FF
        ```
        """
        return 'FF:FF:FF:FF:FF:FF'

    @classmethod
    def invalid_value(cls) -> str:
        """
        Create an invalid MAC address value.

        Returns:
            str: Invalid MAC address string.
        """
        return StringMother.invalid_value()
