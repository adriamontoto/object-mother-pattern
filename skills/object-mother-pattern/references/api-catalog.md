# API Catalog

This catalog reflects the current repository API. If working in another project, check the installed
`object-mother-pattern` version before using newer mothers.

Most concrete mothers inherit `BaseMother.invalid_type(*, remove_types: Iterable[type[Any]] | None = None) -> Any`.
The method tables below list category-specific public helpers and constructors.

## Top-Level Imports

```python
from object_mother_pattern import (
    AmexCreditCardMother,
    BooleanMother,
    BtcWalletMother,
    BytesMother,
    CreditCardBrand,
    CreditCardMother,
    DateMother,
    DatetimeMother,
    DiscoverCreditCardMother,
    FloatMother,
    IbanMother,
    IntegerMother,
    MastercardCreditCardMother,
    StringCase,
    StringDateMother,
    StringDatetimeMother,
    StringMother,
    VisaCreditCardMother,
)
```

`StringCase` values:

- `StringCase.LOWERCASE`
- `StringCase.UPPERCASE`
- `StringCase.MIXEDCASE`

## Models

Import:

```python
from object_mother_pattern.models import BaseMother, DictMother, EnumerationMother, ListMother
```

### BaseMother

- `create(*, value: Any | None = None) -> T`
- `invalid_type(*, remove_types: Iterable[type[Any]] | None = None) -> Any`

### ListMother

- `create(*, value: list[T] | None = None, min_length: int = 0, max_length: int = 10, item_mother: Callable[[], T] | None = None) -> list[T]`
- `empty() -> list[Any]`
- `of_length(*, length: int, item_mother: Callable[[], T] | None = None) -> list[T]`

### DictMother

- `create(*, value: dict[K, V] | None = None, min_length: int = 0, max_length: int = 10, key_mother: Callable[[], K] | None = None, value_mother: Callable[[], V] | None = None) -> dict[K, V]`
- `empty() -> dict[Any, Any]`
- `of_length(*, length: int, key_mother: Callable[[], K] | None = None, value_mother: Callable[[], V] | None = None) -> dict[K, V]`

### EnumerationMother

- `create(*, value: E | None = None, exclude: Iterable[E] | None = None) -> E`
- `invalid_type(remove_types: Iterable[type[Any]] | None = None) -> Any`

## Primitives

Import:

```python
from object_mother_pattern import BooleanMother, BytesMother, FloatMother, IntegerMother, StringMother
```

### BooleanMother

- `create(*, value: bool | None = None, probability_true: float = 0.5) -> bool`
- `true() -> bool`
- `false() -> bool`

### BytesMother

- `create(*, value: bytes | None = None, min_length: int = 1, max_length: int = 128) -> bytes`
- `empty() -> bytes`
- `of_length(*, length: int) -> bytes`

### FloatMother

- `create(*, value: int | float | None = None, min: int | float = -1.0, max: int | float = 1.0, decimals: int | None = None) -> float`
- `invalid_type(*, remove_types: Iterable[type[Any]] | None = None) -> Any`
- `positive(*, max: int | float = 1.0, decimals: int | None = None) -> float`
- `positive_or_zero(*, max: int | float = 1.0, decimals: int | None = None) -> float`
- `negative(*, min: int | float = -1.0, decimals: int | None = None) -> float`
- `negative_or_zero(*, min: int | float = -1.0, decimals: int | None = None) -> float`
- `out_of_range(*, min: int | float = -1.0, max: int | float = 1.0, range: int | float = 1.0, decimals: int | None = None) -> float`

### IntegerMother

- `create(*, value: int | None = None, min: int = -100, max: int = 100) -> int`
- `positive(*, max: int = 100) -> int`
- `positive_or_zero(*, max: int = 100) -> int`
- `negative(*, min: int = -100) -> int`
- `negative_or_zero(*, min: int = -100) -> int`
- `even(*, value: int | None = None) -> int`
- `odd(*, value: int | None = None) -> int`
- `out_of_range(*, min: int = -100, max: int = 100, range: int = 100) -> int`

### StringMother

- `create(*, value: str | None = None, min_length: int = 1, max_length: int = 128, characters: str = ALPHABET_BASIC) -> str`
- `empty() -> str`
- `lowercase(*, min_length: int = 1, max_length: int = 128) -> str`
- `uppercase(*, min_length: int = 1, max_length: int = 128) -> str`
- `titlecase(*, min_length: int = 1, max_length: int = 128) -> str`
- `mixedcase(*, min_length: int = 1, max_length: int = 128) -> str`
- `of_length(*, length: int) -> str`
- `alpha(*, min_length: int = 1, max_length: int = 128) -> str`
- `alphanumeric(*, min_length: int = 1, max_length: int = 128) -> str`
- `numeric(*, min_length: int = 1, max_length: int = 128) -> str`
- `kebab_case(*, min_length: int = 1, max_length: int = 128) -> str`
- `camel_case(*, min_length: int = 1, max_length: int = 128) -> str`
- `pascal_case(*, min_length: int = 1, max_length: int = 128) -> str`
- `snake_case(*, min_length: int = 1, max_length: int = 128) -> str`
- `screaming_snake_case(*, min_length: int = 1, max_length: int = 128) -> str`
- `not_trimmed(*, min_length: int = 2, max_length: int = 128) -> str`
- `invalid_value(*, length: int = 8) -> str`

## Dates And Timezones

Imports:

```python
from object_mother_pattern import DateMother, DatetimeMother, StringDateMother, StringDatetimeMother
from object_mother_pattern.mothers.dates import StringTimezoneMother, TimezoneMother
```

### DateMother

- `create(*, value: date | None = None, start_date: date | None = None, end_date: date | None = None) -> date`
- `out_of_range(*, start_date: date | None = None, end_date: date | None = None, range: int = 100) -> date`

### StringDateMother

- `create(*, value: str | None = None, start_date: date | None = None, end_date: date | None = None) -> str`
- `out_of_range(*, start_date: date | None = None, end_date: date | None = None, range: int = 100) -> str`
- `invalid_value() -> str`

### DatetimeMother

- `create(*, value: datetime | None = None, start_datetime: datetime | None = None, end_datetime: datetime | None = None) -> datetime`
- `out_of_range(*, start_datetime: datetime | None = None, end_datetime: datetime | None = None, range: int = 100) -> datetime`

### StringDatetimeMother

- `create(*, value: str | None = None, start_datetime: datetime | None = None, end_datetime: datetime | None = None) -> str`
- `out_of_range(*, start_datetime: datetime | None = None, end_datetime: datetime | None = None, range: int = 100) -> str`
- `invalid_value() -> str`

### TimezoneMother

- `create(*, value: tzinfo | None = None) -> tzinfo`

### StringTimezoneMother

- `create(*, value: str | None = None) -> str`

## UUID Identifiers

Import:

```python
from object_mother_pattern.mothers.identifiers.uuid import (
    StringUuidMother,
    StringUuidV1Mother,
    StringUuidV3Mother,
    StringUuidV4Mother,
    StringUuidV5Mother,
    StringUuidV6Mother,
    StringUuidV7Mother,
    StringUuidV8Mother,
    UuidMother,
    UuidV1Mother,
    UuidV3Mother,
    UuidV4Mother,
    UuidV5Mother,
    UuidV6Mother,
    UuidV7Mother,
    UuidV8Mother,
)
```

### UUID Objects

- `UuidMother.create(*, value: UUID | None = None, exclude_versions: set[int] | None = None) -> UUID`
- `UuidV1Mother.create(*, value: UUID | None = None) -> UUID`
- `UuidV3Mother.create(*, value: UUID | None = None, namespace: UUID | None = None, name: str | None = None) -> UUID`
- `UuidV4Mother.create(*, value: UUID | None = None) -> UUID`
- `UuidV5Mother.create(*, value: UUID | None = None, namespace: UUID | None = None, name: str | None = None) -> UUID`
- `UuidV6Mother.create(*, value: UUID | None = None) -> UUID`
- `UuidV7Mother.create(*, value: UUID | None = None) -> UUID`
- `UuidV8Mother.create(*, value: UUID | None = None) -> UUID`

### UUID Strings

- `StringUuidMother.create(*, value: str | None = None, exclude_versions: set[int] | None = None) -> str`
- `StringUuidMother.invalid_value() -> str`
- `StringUuidV1Mother.create(*, value: str | None = None) -> str`
- `StringUuidV1Mother.invalid_value() -> str`
- `StringUuidV3Mother.create(*, value: str | None = None, namespace: UUID | None = None, name: str | None = None) -> str`
- `StringUuidV3Mother.invalid_value() -> str`
- `StringUuidV4Mother.create(*, value: str | None = None) -> str`
- `StringUuidV4Mother.invalid_value() -> str`
- `StringUuidV5Mother.create(*, value: str | None = None, namespace: UUID | None = None, name: str | None = None) -> str`
- `StringUuidV5Mother.invalid_value() -> str`
- `StringUuidV6Mother.create(*, value: str | None = None) -> str`
- `StringUuidV6Mother.invalid_value() -> str`
- `StringUuidV7Mother.create(*, value: str | None = None) -> str`
- `StringUuidV7Mother.invalid_value() -> str`
- `StringUuidV8Mother.create(*, value: str | None = None) -> str`
- `StringUuidV8Mother.invalid_value() -> str`

## World Identifiers

Import:

```python
from object_mother_pattern.mothers.identifiers.world import (
    CountryTldMother,
    Iso3166Alpha2CodeMother,
    Iso3166Alpha3CodeMother,
    Iso3166NumericCodeMother,
    PhoneCodeMother,
    VinMother,
)
```

- `CountryTldMother.create(*, value: str | None = None) -> str`
- `CountryTldMother.invalid_value() -> str`
- `Iso3166Alpha2CodeMother.create(*, value: str | None = None) -> str`
- `Iso3166Alpha2CodeMother.invalid_value() -> str`
- `Iso3166Alpha3CodeMother.create(*, value: str | None = None) -> str`
- `Iso3166Alpha3CodeMother.invalid_value() -> str`
- `Iso3166NumericCodeMother.create(*, value: int | None = None) -> int`
- `Iso3166NumericCodeMother.invalid_value() -> int`
- `PhoneCodeMother.create(*, value: str | None = None) -> str`
- `PhoneCodeMother.invalid_value() -> str`
- `VinMother.create(*, value: str | None = None) -> str`
- `VinMother.invalid_value() -> str`

## Spanish Identifiers

Import:

```python
from object_mother_pattern.mothers.identifiers.countries.spain import (
    DniMother,
    NieMother,
    NifMother,
    NussMother,
    PassportMother,
    PhoneNumberMother,
    VehiclePlateMother,
)
```

### Documents And Phone Numbers

- `DniMother.create(*, value: str | None = None, string_case: StringCase | None = None) -> str`
- `DniMother.invalid_value() -> str`
- `NieMother.create(*, value: str | None = None, string_case: StringCase | None = None) -> str`
- `NieMother.invalid_value() -> str`
- `NifMother.create(*, value: str | None = None, string_case: StringCase | None = None, first_letter: str | None = None) -> str`
- `NifMother.invalid_value() -> str`
- `NussMother.create(*, value: str | None = None) -> str`
- `NussMother.invalid_value() -> str`
- `PassportMother.create(*, value: str | None = None, string_case: StringCase | None = None) -> str`
- `PassportMother.invalid_value() -> str`
- `PhoneNumberMother.create(*, value: str | None = None) -> str`
- `PhoneNumberMother.mobile() -> str`
- `PhoneNumberMother.landline() -> str`
- `PhoneNumberMother.with_plus_34_prefix() -> str`
- `PhoneNumberMother.with_34_prefix() -> str`
- `PhoneNumberMother.with_0034_prefix() -> str`
- `PhoneNumberMother.without_country_code() -> str`
- `PhoneNumberMother.invalid_value() -> str`

### Vehicle Plates

All specific Spanish vehicle-plate mothers support:

- `create(*, value: str | None = None) -> str`
- `invalid_value() -> str`

Aggregate mother:

- `VehiclePlateMother.create(*, value: str | None = None) -> str`
- `VehiclePlateMother.invalid_value() -> str`

Specific plate-family mothers:

- `AdministrativeTechnicianVehiclePlateMother`
- `AirForceVehiclePlateMother`
- `ArmyVehiclePlateMother`
- `CanariasPoliceVehiclePlateMother`
- `CatalanPoliceVehiclePlateMother`
- `CivilGuardVehiclePlateMother`
- `ConsularCorpsVehiclePlateMother`
- `DiplomaticCorpsVehiclePlateMother`
- `EspecialVehiclePlateMother`
- `HistoricalVehiclePlateMother`
- `InternationalOrganizationVehiclePlateMother`
- `MinistryDevelopmentVehiclePlateMother`
- `MinistryEnvironmentVehiclePlateMother`
- `NationalPoliceVehiclePlateMother`
- `NavyVehiclePlateMother`
- `OrdinaryTruckVehiclePlateMother`
- `OrdinaryVehiclePlateMother`
- `ProvincialSystemVehiclePlateMother`
- `StateMotorPoolVehiclePlateMother`
- `TemporalCompanyNotRegisteredVehiclePlateMother`
- `TemporalCompanyRegisteredVehiclePlateMother`
- `TemporalPrivateIndividualVehiclePlateMother`
- `TwoWheelsVehiclePlateMother`

## Internet

Import:

```python
from object_mother_pattern.mothers.internet import (
    AwsCloudRegionMother,
    DomainMother,
    EmailAddressMother,
    HostMother,
    HttpHttpsUrlMother,
    HttpUrlMother,
    HttpsUrlMother,
    ImeiMother,
    IpAddressMother,
    IpNetworkMother,
    Ipv4AddressMother,
    Ipv4NetworkMother,
    Ipv6AddressMother,
    Ipv6NetworkMother,
    KebabCaseKeyMother,
    KeyMother,
    MacAddressMother,
    PortMother,
    SlugMother,
    SnakeCaseKeyMother,
    UrlMother,
    UserAgentMother,
)
```

### URLs, Hosts, Domains, And Email

- `UrlMother.create(*, value: str | None = None, host_type: str | None = None) -> str`
- `UrlMother.with_scheme(*, scheme: str, host_type: str | None = None) -> str`
- `UrlMother.with_domain() -> str`
- `UrlMother.with_ipv4_address() -> str`
- `UrlMother.with_ipv6_address() -> str`
- `UrlMother.with_query() -> str`
- `UrlMother.with_fragment() -> str`
- `UrlMother.with_query_and_fragment() -> str`
- `UrlMother.invalid_value() -> str`
- `HttpUrlMother.create(*, value: str | None = None, host_type: str | None = None) -> str`
- `HttpUrlMother.invalid_value() -> str`
- `HttpsUrlMother.create(*, value: str | None = None, host_type: str | None = None) -> str`
- `HttpsUrlMother.invalid_value() -> str`
- `HttpHttpsUrlMother.create(*, value: str | None = None, host_type: str | None = None) -> str`
- `HttpHttpsUrlMother.invalid_value() -> str`
- `HostMother.create(*, value: str | None = None) -> str`
- `HostMother.domain() -> str`
- `HostMother.ipv4_address() -> str`
- `HostMother.ipv6_address() -> str`
- `HostMother.invalid_value() -> str`
- `DomainMother.create(*, value: str | None = None, min_length: int = 10, max_length: int = 30, min_labels: int = 2, max_labels: int = 4, string_case: StringCase | None = None, include_hyphens: bool = True, include_numbers: bool = True) -> str`
- `DomainMother.of_length(*, length: int) -> str`
- `DomainMother.rfc_create() -> str`
- `DomainMother.invalid_value() -> str`
- `EmailAddressMother.create(*, value: str | None = None, min_length: int = 8, max_length: int = 64, domain: str | None = None, string_case: StringCase | None = None) -> str`
- `EmailAddressMother.of_length(*, length: int) -> str`
- `EmailAddressMother.rfc_create() -> str`
- `EmailAddressMother.invalid_value() -> str`

### IP Addresses, Networks, MAC, Ports

- `IpAddressMother.create(*, value: str | None = None) -> str`
- `IpAddressMother.invalid_value() -> str`
- `Ipv4AddressMother.create(*, value: str | None = None) -> str`
- `Ipv4AddressMother.public() -> str`
- `Ipv4AddressMother.private() -> str`
- `Ipv4AddressMother.unspecified() -> str`
- `Ipv4AddressMother.loopback() -> str`
- `Ipv4AddressMother.broadcast() -> str`
- `Ipv4AddressMother.invalid_value() -> str`
- `Ipv6AddressMother.create(*, value: str | None = None) -> str`
- `Ipv6AddressMother.unspecified() -> str`
- `Ipv6AddressMother.loopback() -> str`
- `Ipv6AddressMother.invalid_value() -> str`
- `IpNetworkMother.create(*, value: str | None = None) -> str`
- `IpNetworkMother.invalid_value() -> str`
- `Ipv4NetworkMother.create(*, value: str | None = None) -> str`
- `Ipv4NetworkMother.invalid_value() -> str`
- `Ipv6NetworkMother.create(*, value: str | None = None) -> str`
- `Ipv6NetworkMother.invalid_value() -> str`
- `MacAddressMother.create(*, value: str | None = None, mac_format: MacAddressFormat | None = None, string_case: StringCase | None = None) -> str`
- `MacAddressMother.lowercase() -> str`
- `MacAddressMother.uppercase() -> str`
- `MacAddressMother.mixed() -> str`
- `MacAddressMother.raw_format() -> str`
- `MacAddressMother.universal_format() -> str`
- `MacAddressMother.windows_format() -> str`
- `MacAddressMother.cisco_format() -> str`
- `MacAddressMother.space_format() -> str`
- `MacAddressMother.null() -> str`
- `MacAddressMother.broadcast() -> str`
- `MacAddressMother.invalid_value() -> str`
- `PortMother.create(*, value: int | None = None) -> int`
- `PortMother.invalid_value() -> int`

Known port helpers on `PortMother`:

- `ftp_data() -> int`
- `ftp_control() -> int`
- `ssh() -> int`
- `telnet() -> int`
- `smtp() -> int`
- `dns() -> int`
- `dhcp_server() -> int`
- `dhcp_client() -> int`
- `http() -> int`
- `pop3() -> int`
- `ntp() -> int`
- `imap() -> int`
- `snmp_monitor() -> int`
- `snmp_trap() -> int`
- `ldap() -> int`
- `https() -> int`
- `doh() -> int`
- `smtps() -> int`
- `imaps() -> int`
- `pop3s() -> int`
- `openvpn() -> int`
- `microsoft_sql_server() -> int`
- `oracle() -> int`
- `mysql() -> int`
- `mariadb() -> int`
- `rdp() -> int`
- `postgresql() -> int`
- `redis() -> int`
- `minecraft() -> int`
- `mongodb() -> int`
- `wireguard() -> int`

### Keys, Slugs, Metadata

- `KeyMother.create(*, value: str | None = None, min_length: int = 3, max_length: int = 64) -> str`
- `KeyMother.of_length(*, length: int) -> str`
- `KeyMother.snake_case(*, min_length: int = 1, max_length: int = 64) -> str`
- `KeyMother.kebab_case(*, min_length: int = 1, max_length: int = 64) -> str`
- `KeyMother.invalid_value() -> str`
- `SnakeCaseKeyMother.create(*, value: str | None = None, min_length: int = 1, max_length: int = 64) -> str`
- `SnakeCaseKeyMother.of_length(*, length: int) -> str`
- `SnakeCaseKeyMother.invalid_value() -> str`
- `KebabCaseKeyMother.create(*, value: str | None = None, min_length: int = 1, max_length: int = 64) -> str`
- `KebabCaseKeyMother.of_length(*, length: int) -> str`
- `KebabCaseKeyMother.invalid_value() -> str`
- `SlugMother.create(*, value: str | None = None, min_length: int = 3, max_length: int = 64) -> str`
- `SlugMother.of_length(*, length: int) -> str`
- `SlugMother.invalid_value() -> str`
- `AwsCloudRegionMother.create(*, value: str | None = None) -> str`
- `AwsCloudRegionMother.invalid_value() -> str`
- `ImeiMother.create(*, value: str | None = None) -> str`
- `ImeiMother.invalid_value() -> str`
- `UserAgentMother.create(*, value: str | None = None, min_length: int = 64, max_length: int = 256) -> str`
- `UserAgentMother.of_length(*, length: int) -> str`
- `UserAgentMother.invalid_value() -> str`

## Money

Imports:

```python
from object_mother_pattern import (
    AmexCreditCardMother,
    CreditCardBrand,
    CreditCardMother,
    DiscoverCreditCardMother,
    IbanMother,
    MastercardCreditCardMother,
    VisaCreditCardMother,
)
from object_mother_pattern.mothers.money.cryptocurrencies import BtcWalletMother
```

### IBAN

- `IbanMother.create(*, value: str | None = None, country_code: str | None = None) -> str`
- `IbanMother.invalid_value() -> str`

### Credit Cards

- `CreditCardMother.create(*, value: str | None = None, brand: CreditCardBrand | str | None = None, exclude: Iterable[CreditCardBrand | str] | None = None) -> str`
- `CreditCardMother.invalid_value() -> str`
- `VisaCreditCardMother.create(*, value: str | None = None) -> str`
- `VisaCreditCardMother.invalid_value() -> str`
- `MastercardCreditCardMother.create(*, value: str | None = None) -> str`
- `MastercardCreditCardMother.invalid_value() -> str`
- `AmexCreditCardMother.create(*, value: str | None = None) -> str`
- `AmexCreditCardMother.invalid_value() -> str`
- `DiscoverCreditCardMother.create(*, value: str | None = None) -> str`
- `DiscoverCreditCardMother.invalid_value() -> str`

`CreditCardBrand` is the supported-brand enum. Use brand-specific mothers when the brand matters; otherwise use
`CreditCardMother`.

### Cryptocurrency

- `BtcWalletMother.create(*, value: str | None = None, word_number: int = 12, string_case: StringCase | None = None) -> str`
- `BtcWalletMother.invalid_value() -> str`

## People And Extra Text

Imports:

```python
from object_mother_pattern.mothers.extra import TextMother
from object_mother_pattern.mothers.people import FullNameMother, PasswordMother, UsernameMother
```

### FullNameMother

- `create(*, value: str | None = None, min_length: int = 3, max_length: int = 128, string_case: StringCase | None = None) -> str`
- `of_length(*, length: int) -> str`
- `invalid_value() -> str`

### UsernameMother

- `create(*, value: str | None = None, min_length: int = 3, max_length: int = 32, separators: str = '_') -> str`
- `of_length(*, length: int) -> str`
- `invalid_value() -> str`

### PasswordMother

- `create(*, value: str | None = None, lowercase_count: int = 3, lowercase_alphabet: str = ALPHABET_LOWERCASE_BASIC, uppercase_count: int = 3, uppercase_alphabet: str = ALPHABET_UPPERCASE_BASIC, digits_count: int = 3, digits_alphabet: str = DIGITS_BASIC, special_characters_count: int = 3, special_characters_alphabet: str = SPECIAL_CHARS, super_special_characters_count: int = 0, super_special_characters_alphabet: str = SUPER_SPECIAL_CHARS, exclude_duplicates: bool = False) -> str`
- `random_length(*, min_length: int = 8, max_length: int = 16, exclude_super_special: bool = False, exclude_duplicates: bool = False) -> str`
- `of_length(*, length: int, exclude_super_special: bool = False, exclude_duplicates: bool = False) -> str`
- `invalid_value() -> str`

### TextMother

- `create(*, value: str | None = None, min_length: int = 1, max_length: int = 1024, string_case: StringCase | None = None) -> str`
- `empty() -> str`
- `of_length(*, length: int) -> str`
- `invalid_value() -> str`
