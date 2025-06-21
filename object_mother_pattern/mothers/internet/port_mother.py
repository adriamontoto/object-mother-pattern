"""
PortMother module.
"""

from sys import version_info

if version_info >= (3, 12):
    from typing import override  # pragma: no cover
else:
    from typing_extensions import override  # pragma: no cover

from object_mother_pattern.models import BaseMother
from object_mother_pattern.mothers.primitives.integer_mother import IntegerMother


class PortMother(BaseMother[int]):
    """
    PortMother class is responsible for creating random port values.

    Example:
    ```python
    from object_mother_pattern.mothers.internet import PortMother

    port = PortMother.create()
    print(port)
    # >>> 443
    ```
    """

    @classmethod
    @override
    def create(cls, *, value: int | None = None) -> int:
        """
        Create a random port value. If a specific port value is provided via `value`, it is returned
        after validation. Otherwise, a random port value is generated.

        Args:
            value (int | None, optional): Specific value to return. Defaults to None.

        Raises:
            TypeError: If the provided `value` is not an integer.

        Returns:
            int: A randomly generated port value.

        Example:
        ```python
        from object_mother_pattern.mothers.internet import PortMother

        port = PortMother.create()
        print(port)
        # >>> 443
        ```
        """
        if value is not None:
            if type(value) is not int:
                raise TypeError('PortMother value must be a integer.')

            return value

        return IntegerMother.create(min=0, max=65535)

    @classmethod
    def ftp_data(cls) -> int:
        """
        Create a random integer FTP data port value.

        Returns:
            int: A randomly integer FTP data port value.

        Example:
        ```python
        from object_mother_pattern.mothers.internet import PortMother

        port = PortMother.ftp_data()
        print(port)
        # >>> 20
        ```
        """
        return 20

    @classmethod
    def ftp_control(cls) -> int:
        """
        Create a random integer FTP control port value.

        Returns:
            int: A randomly integer FTP control port value.

        Example:
        ```python
        from object_mother_pattern.mothers.internet import PortMother

        port = PortMother.ftp_control()
        print(port)
        # >>> 21
        ```
        """
        return 21

    @classmethod
    def ssh(cls) -> int:
        """
        Create a random integer SSH port value.

        Returns:
            int: A randomly integer SSH port value.

        Example:
        ```python
        from object_mother_pattern.mothers.internet import PortMother

        port = PortMother.ssh()
        print(port)
        # >>> 22
        ```
        """
        return 22

    @classmethod
    def telnet(cls) -> int:
        """
        Create a random integer Telnet port value.

        Returns:
            int: A randomly integer Telnet port value.

        Example:
        ```python
        from object_mother_pattern.mothers.internet import PortMother

        port = PortMother.telnet()
        print(port)
        # >>> 23
        ```
        """
        return 23

    @classmethod
    def smtp(cls) -> int:
        """
        Create a random integer SMTP port value.

        Returns:
            int: A randomly integer SMTP port value.

        Example:
        ```python
        from object_mother_pattern.mothers.internet import PortMother

        port = PortMother.smtp()
        print(port)
        # >>> 25
        ```
        """
        return 25

    @classmethod
    def dns(cls) -> int:
        """
        Create a random integer DNS port value.

        Returns:
            int: A randomly integer DNS port value.

        Example:
        ```python
        from object_mother_pattern.mothers.internet import PortMother

        port = PortMother.dns()
        print(port)
        # >>> 53
        ```
        """
        return 53

    @classmethod
    def dhcp_server(cls) -> int:
        """
        Create a random integer DHCP server port value.

        Returns:
            int: A randomly integer DHCP server port value.

        Example:
        ```python
        from object_mother_pattern.mothers.internet import PortMother

        port = PortMother.dhcp_server()
        print(port)
        # >>> 67
        ```
        """
        return 67

    @classmethod
    def dhcp_client(cls) -> int:
        """
        Create a random integer DHCP client port value.

        Returns:
            int: A randomly integer DHCP client port value.

        Example:
        ```python
        from object_mother_pattern.mothers.internet import PortMother

        port = PortMother.dhcp_client()
        print(port)
        # >>> 68
        ```
        """
        return 68

    @classmethod
    def http(cls) -> int:
        """
        Create a random integer HTTP port value.

        Returns:
            int: A randomly integer HTTP port value.

        Example:
        ```python
        from object_mother_pattern.mothers.internet import PortMother

        port = PortMother.http()
        print(port)
        # >>> 80
        ```
        """
        return 80

    @classmethod
    def pop3(cls) -> int:
        """
        Create a random integer POP3 port value.

        Returns:
            int: A randomly integer POP3 port value.

        Example:
        ```python
        from object_mother_pattern.mothers.internet import PortMother

        port = PortMother.pop3()
        print(port)
        # >>> 110
        ```
        """
        return 110

    @classmethod
    def ntp(cls) -> int:
        """
        Create a random integer NTP port value.

        Returns:
            int: A randomly integer NTP port value.

        Example:
        ```python
        from object_mother_pattern.mothers.internet import PortMother

        port = PortMother.ntp()
        print(port)
        # >>> 123
        ```
        """
        return 123

    @classmethod
    def imap(cls) -> int:
        """
        Create a random integer IMAP port value.

        Returns:
            int: A randomly integer IMAP port value.

        Example:
        ```python
        from object_mother_pattern.mothers.internet import PortMother

        port = PortMother.imap()
        print(port)
        # >>> 143
        ```
        """
        return 143

    @classmethod
    def snmp_monitor(cls) -> int:
        """
        Create a random integer SNMP monitor port value.

        Returns:
            int: A randomly integer SNMP monitor port value.

        Example:
        ```python
        from object_mother_pattern.mothers.internet import PortMother

        port = PortMother.snmp_monitor()
        print(port)
        # >>> 161
        ```
        """
        return 161

    @classmethod
    def snmp_trap(cls) -> int:
        """
        Create a random integer SNMP trap port value.

        Returns:
            int: A randomly integer SNMP trap port value.

        Example:
        ```python
        from object_mother_pattern.mothers.internet import PortMother

        port = PortMother.snmp_trap()
        print(port)
        # >>> 162
        ```
        """
        return 162

    @classmethod
    def ldap(cls) -> int:
        """
        Create a random integer LDAP port value.

        Returns:
            int: A randomly integer LDAP port value.

        Example:
        ```python
        from object_mother_pattern.mothers.internet import PortMother

        port = PortMother.ldap()
        print(port)
        # >>> 389
        ```
        """
        return 389

    @classmethod
    def https(cls) -> int:
        """
        Create a random integer HTTPS port value.

        Returns:
            int: A randomly integer HTTPS port value.

        Example:
        ```python
        from object_mother_pattern.mothers.internet import PortMother

        port = PortMother.https()
        print(port)
        # >>> 443
        ```
        """
        return 443

    @classmethod
    def doh(cls) -> int:
        """
        Create a random integer DNS over HTTPS port value.

        Returns:
            int: A randomly integer DNS over HTTPS port value.

        Example:
        ```python
        from object_mother_pattern.mothers.internet import PortMother

        port = PortMother.doh()
        print(port)
        # >>> 443
        ```
        """
        return 443

    @classmethod
    def smtps(cls) -> int:
        """
        Create a random integer SMTPS port value.

        Returns:
            int: A randomly integer SMTPS port value.

        Example:
        ```python
        from object_mother_pattern.mothers.internet import PortMother

        port = PortMother.smtps()
        print(port)
        # >>> 465
        ```
        """
        return 465

    @classmethod
    def imaps(cls) -> int:
        """
        Create a random integer IMAPS port value.

        Returns:
            int: A randomly integer IMAPS port value.

        Example:
        ```python
        from object_mother_pattern.mothers.internet import PortMother

        port = PortMother.imaps()
        print(port)
        # >>> 993
        ```
        """
        return 993

    @classmethod
    def pop3s(cls) -> int:
        """
        Create a random integer POP3S port value.

        Returns:
            int: A randomly integer POP3S port value.

        Example:
        ```python
        from object_mother_pattern.mothers.internet import PortMother

        port = PortMother.pop3s()
        print(port)
        # >>> 995
        ```
        """
        return 995

    @classmethod
    def openvpn(cls) -> int:
        """
        Create a random integer OpenVPN port value.

        Returns:
            int: A randomly integer OpenVPN port value.

        Example:
        ```python
        from object_mother_pattern.mothers.internet import PortMother

        port = PortMother.openvpn()
        print(port)
        # >>> 1194
        ```
        """
        return 1194

    @classmethod
    def microsoft_sql_server(cls) -> int:
        """
        Create a random integer Microsoft SQL Server port value.

        Returns:
            int: A randomly integer Microsoft SQL Server port value.

        Example:
        ```python
        from object_mother_pattern.mothers.internet import PortMother

        port = PortMother.microsoft_sql_server()
        print(port)
        # >>> 1433
        ```
        """
        return 1433

    @classmethod
    def oracle(cls) -> int:
        """
        Create a random integer Oracle port value.

        Returns:
            int: A randomly integer Oracle port value.

        Example:
        ```python
        from object_mother_pattern.mothers.internet import PortMother

        port = PortMother.oracle()
        print(port)
        # >>> 1521
        ```
        """
        return 1521

    @classmethod
    def mysql(cls) -> int:
        """
        Create a random integer MySQL port value.

        Returns:
            int: A randomly integer MySQL port value.

        Example:
        ```python
        from object_mother_pattern.mothers.internet import PortMother

        port = PortMother.mysql()
        print(port)
        # >>> 3306
        ```
        """
        return 3306

    @classmethod
    def mariadb(cls) -> int:
        """
        Create a random integer MariaDB port value.

        Returns:
            int: A randomly integer MariaDB port value.

        Example:
        ```python
        from object_mother_pattern.mothers.internet import PortMother

        port = PortMother.mariadb()
        print(port)
        # >>> 3306
        ```
        """
        return 3306

    @classmethod
    def rdp(cls) -> int:
        """
        Create a random integer RDP port value.

        Returns:
            int: A randomly integer RDP port value.

        Example:
        ```python
        from object_mother_pattern.mothers.internet import PortMother

        port = PortMother.rdp()
        print(port)
        # >>> 3389
        ```
        """
        return 3389

    @classmethod
    def postgresql(cls) -> int:
        """
        Create a random integer PostgreSQL port value.

        Returns:
            int: A randomly integer PostgreSQL port value.

        Example:
        ```python
        from object_mother_pattern.mothers.internet import PortMother

        port = PortMother.postgresql()
        print(port)
        # >>> 5432
        ```
        """
        return 5432

    @classmethod
    def redis(cls) -> int:
        """
        Create a random integer Redis port value.

        Returns:
            int: A randomly integer Redis port value.

        Example:
        ```python
        from object_mother_pattern.mothers.internet import PortMother

        port = PortMother.redis()
        print(port)
        # >>> 6379
        ```
        """
        return 6379

    @classmethod
    def minecraft(cls) -> int:
        """
        Create a random integer Minecraft port value.

        Returns:
            int: A randomly integer Minecraft port value.

        Example:
        ```python
        from object_mother_pattern.mothers.internet import PortMother

        port = PortMother.minecraft()
        print(port)
        # >>> 25565
        ```
        """
        return 25565

    @classmethod
    def mongodb(cls) -> int:
        """
        Create a random integer MongoDB port value.

        Returns:
            int: A randomly integer MongoDB port value.

        Example:
        ```python
        from object_mother_pattern.mothers.internet import PortMother

        port = PortMother.mongodb()
        print(port)
        # >>> 27017
        ```
        """
        return 27017

    @classmethod
    def wireguard(cls) -> int:
        """
        Create a random integer WireGuard port value.

        Returns:
            int: A randomly integer WireGuard port value.

        Example:
        ```python
        from object_mother_pattern.mothers.internet import PortMother

        port = PortMother.wireguard()
        print(port)
        # >>> 51820
        ```
        """
        return 51820

    @classmethod
    def invalid_value(cls) -> int:
        """
        Create an invalid integer port value.

        Returns:
            int: A randomly invalid integer port value.

        Example:
        ```python
        from object_mother_pattern.mothers.internet import PortMother

        port = PortMother.invalid_value()
        print(port)
        # >>> -4237
        ```
        """
        return IntegerMother.out_of_range(min=0, max=65535)
