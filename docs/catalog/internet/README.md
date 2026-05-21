# Internet Mothers

Internet mothers generate web, network, and protocol-shaped test data.

## Imports

```python
from object_mother_pattern.mothers.internet import DomainMother, EmailAddressMother, HttpsUrlMother, PortMother
```

## URLs, Hosts, And Domains

| Mother | Typical Uses |
| --- | --- |
| `UrlMother` | General URL values. |
| `HttpUrlMother` | HTTP-only URL values. |
| `HttpsUrlMother` | HTTPS-only URL values. |
| `HttpHttpsUrlMother` | HTTP or HTTPS URL values. |
| `HostMother` | Host values. |
| `DomainMother` | Domain values. |

## Addresses, Networks, And Ports

| Mother | Typical Uses |
| --- | --- |
| `IpAddressMother` | IPv4 or IPv6 address values. |
| `Ipv4AddressMother` | IPv4 address values. |
| `Ipv6AddressMother` | IPv6 address values. |
| `IpNetworkMother` | IPv4 or IPv6 network values. |
| `Ipv4NetworkMother` | IPv4 network values. |
| `Ipv6NetworkMother` | IPv6 network values. |
| `MacAddressMother` | MAC address values in supported formats. |
| `PortMother` | Valid port numbers. |

## Keys, Slugs, And Metadata

| Mother | Typical Uses |
| --- | --- |
| `KeyMother` | Generic key strings. |
| `SnakeCaseKeyMother` | snake_case key strings. |
| `KebabCaseKeyMother` | kebab-case key strings. |
| `SlugMother` | Slug strings. |
| `EmailAddressMother` | Email address strings. |
| `ImeiMother` | IMEI values. |
| `AwsCloudRegionMother` | AWS region identifiers. |
| `UserAgentMother` | User-agent strings. |
