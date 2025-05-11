"""
Test module for the PortMother class.
"""

from pytest import mark, raises as assert_raises

from object_mother_pattern.mothers.internet import PortMother
from object_mother_pattern.mothers.primitives import IntegerMother


@mark.unit_testing
def test_port_mother_happy_path() -> None:
    """
    Test PortMother happy path.
    """
    value = PortMother.create()

    assert type(value) is int
    assert 0 <= value <= 65535


def test_port_mother_value() -> None:
    """
    Test PortMother create method with value.
    """
    value = IntegerMother.create(min=0, max=65535)

    assert PortMother.create(value=value) == value


def test_port_mother_invalid_type() -> None:
    """
    Test PortMother create method with invalid type.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='PortMother value must be a integer.',
    ):
        PortMother.create(value=IntegerMother.invalid_type())


def test_port_mother_standard_ports() -> None:
    """
    Test PortMother standard port methods.
    """
    assert PortMother.ftp_data() == 20
    assert PortMother.ftp_control() == 21
    assert PortMother.ssh() == 22
    assert PortMother.telnet() == 23
    assert PortMother.smtp() == 25
    assert PortMother.dns() == 53
    assert PortMother.dhcp_server() == 67
    assert PortMother.dhcp_client() == 68
    assert PortMother.http() == 80
    assert PortMother.pop3() == 110
    assert PortMother.ntp() == 123
    assert PortMother.imap() == 143
    assert PortMother.snmp_monitor() == 161
    assert PortMother.snmp_trap() == 162
    assert PortMother.ldap() == 389
    assert PortMother.https() == 443
    assert PortMother.doh() == 443
    assert PortMother.smtps() == 465
    assert PortMother.imaps() == 993
    assert PortMother.pop3s() == 995
    assert PortMother.openvpn() == 1194
    assert PortMother.microsoft_sql_server() == 1433
    assert PortMother.oracle() == 1521
    assert PortMother.mysql() == 3306
    assert PortMother.mariadb() == 3306
    assert PortMother.postgresql() == 5432
    assert PortMother.rdp() == 3389
    assert PortMother.redis() == 6379
    assert PortMother.minecraft() == 25565
    assert PortMother.mongodb() == 27017
    assert PortMother.wireguard() == 51820


def test_port_mother_invalid_value() -> None:
    """
    Test PortMother invalid_value method.
    """
    port = PortMother.invalid_value()

    assert type(port) is int
    assert port < 0 or port > 65535
