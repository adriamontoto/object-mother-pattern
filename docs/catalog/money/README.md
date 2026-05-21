# Money Mothers

Money mothers generate payment-shaped and cryptocurrency-shaped values for tests.

## Imports

```python
from object_mother_pattern import CreditCardMother, IbanMother
from object_mother_pattern.mothers.money.cryptocurrencies import BtcWalletMother
```

## Catalog

| Mother | Typical Uses |
| --- | --- |
| `IbanMother` | IBAN values with supported country lengths and computed check digits. |
| `CreditCardMother` | Any supported credit-card brand. |
| `VisaCreditCardMother` | Visa-like card numbers with Luhn checksum. |
| `MastercardCreditCardMother` | Mastercard-like card numbers with Luhn checksum. |
| `AmexCreditCardMother` | American Express-like card numbers with Luhn checksum. |
| `DiscoverCreditCardMother` | Discover-like card numbers with Luhn checksum. |
| `CreditCardBrand` | Enum of supported credit-card brands. |
| `BtcWalletMother` | Bitcoin wallet-like values from the bundled generator. |

## Example

```python
from object_mother_pattern import CreditCardMother, IbanMother

card = CreditCardMother.create()
spanish_iban = IbanMother.create(country_code='ES')
```
