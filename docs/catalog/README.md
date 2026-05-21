# Mother Catalog

This catalog summarizes the package surface by category. Import paths vary by group: common mothers are re-exported from
`object_mother_pattern`, while specialized mothers live under their category packages.

For deeper category references, use:

- [Primitive Mothers](primitives/README.md)
- [Date And Time Mothers](dates/README.md)
- [Identifier Mothers](identifiers/README.md)
- [Internet Mothers](internet/README.md)
- [Money Mothers](money/README.md)
- [People And Text Mothers](people/README.md)

## Models

| Mother | Purpose |
| --- | --- |
| `BaseMother[T]` | Abstract contract for typed mothers. |
| `EnumerationMother[E]` | Base class for enum value mothers. |
| `ListMother` | Lists with optional length bounds and item factories. |
| `DictMother` | Dictionaries with optional length bounds, key factories, and value factories. |

Import:

```python
from object_mother_pattern.models import BaseMother, DictMother, EnumerationMother, ListMother
```

## Primitives

| Mother | Purpose |
| --- | --- |
| `BooleanMother` | Boolean values. |
| `BytesMother` | Byte strings. |
| `FloatMother` | Floats with ranges, precision, sign helpers, and out-of-range values. |
| `IntegerMother` | Integers with ranges, sign helpers, parity helpers, and out-of-range values. |
| `StringMother` | Strings with length, character-set, casing, and empty-value helpers. |

Import:

```python
from object_mother_pattern import BooleanMother, FloatMother, IntegerMother, StringMother
```

See [Primitive Mothers](primitives/README.md) for method-level guidance and examples.

## Dates And Time

| Mother | Purpose |
| --- | --- |
| `DateMother` | `date` values inside or outside ranges. |
| `DatetimeMother` | `datetime` values inside or outside ranges. |
| `StringDateMother` | ISO-like date strings. |
| `StringDatetimeMother` | ISO-like datetime strings. |
| `TimezoneMother` | `tzinfo` timezone objects. |
| `StringTimezoneMother` | Timezone names as strings. |

Import:

```python
from object_mother_pattern import DateMother, DatetimeMother, StringDateMother, StringDatetimeMother
from object_mother_pattern.mothers.dates import StringTimezoneMother, TimezoneMother
```

See [Date And Time Mothers](dates/README.md) for boundary and deterministic-test guidance.

## Identifiers

Identifier mothers cover UUIDs, country/world identifiers, and country-specific identifiers.

UUID examples:

```python
from object_mother_pattern.mothers.identifiers.uuid import StringUuidMother, UuidMother, UuidV4Mother
```

Country-specific examples:

```python
from object_mother_pattern.mothers.identifiers.countries.spain import DniMother, NieMother, NifMother
```

World identifier examples:

```python
from object_mother_pattern.mothers.identifiers.world import Iso3166Alpha2CodeMother, VinMother
```

Use exact-version UUID mothers when a test needs a specific UUID version. Use `UuidMother.create(exclude_versions=...)`
when the test only needs any supported UUID except some versions.

See [Identifier Mothers](identifiers/README.md) for UUID, world, Spanish, and vehicle-plate families.

## Internet

Internet mothers cover network and web-shaped values:

| Area | Examples |
| --- | --- |
| URLs and hosts | `UrlMother`, `HttpUrlMother`, `HttpsUrlMother`, `HttpHttpsUrlMother`, `HostMother`, `DomainMother` |
| Addresses and networks | `IpAddressMother`, `Ipv4AddressMother`, `Ipv6AddressMother`, `IpNetworkMother` |
| Network metadata | `MacAddressMother`, `PortMother`, `AwsCloudRegionMother`, `UserAgentMother` |
| Keys and slugs | `KeyMother`, `SlugMother` |
| Contact-like values | `EmailAddressMother`, `ImeiMother` |

Import:

```python
from object_mother_pattern.mothers.internet import DomainMother, EmailAddressMother, UrlMother
```

See [Internet Mothers](internet/README.md) for URL, address, network, slug, key, and metadata families.

## Money

| Mother | Purpose |
| --- | --- |
| `IbanMother` | IBAN-like values. |
| `CreditCardMother` | Credit card values across supported brands. |
| Brand-specific credit card mothers | Visa, Mastercard, American Express, and Discover values. |
| `BtcWalletMother` | Bitcoin wallet-like values using the bundled BIP39 word list. |

Import:

```python
from object_mother_pattern import CreditCardMother, IbanMother
from object_mother_pattern.mothers.money.cryptocurrencies import BtcWalletMother
```

See [Money Mothers](money/README.md) for payment-shaped and cryptocurrency test data notes.

## People And Extra Text

| Mother | Purpose |
| --- | --- |
| `FullNameMother` | Full names. |
| `UsernameMother` | Username strings. |
| `PasswordMother` | Password-shaped strings for tests. |
| `TextMother` | Text snippets. |

Import:

```python
from object_mother_pattern.mothers.people import FullNameMother, PasswordMother, UsernameMother
from object_mother_pattern.mothers.extra import TextMother
```

See [People And Text Mothers](people/README.md) for identity-like and free-text helpers.

## Catalog Checklist

- Use top-level imports for common primitives, dates, and money mothers.
- Use category imports for specialized identifiers, internet values, people values, and extra text.
- Prefer exact-version or exact-category mothers when the test depends on a specific format.
- Prefer aggregate mothers when any valid value in a family is acceptable.
