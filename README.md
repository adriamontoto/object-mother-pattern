<a name="readme-top"></a>

# ⚒️ Object Mother Pattern

<p align="center">
    <a href="https://github.com/adriamontoto/object-mother-pattern/actions/workflows/ci.yaml?event=push&branch=master" target="_blank">
        <img src="https://github.com/adriamontoto/object-mother-pattern/actions/workflows/ci.yaml/badge.svg?event=push&branch=master" alt="CI Pipeline">
    </a>
    <a href="https://coverage-badge.samuelcolvin.workers.dev/redirect/adriamontoto/object-mother-pattern" target="_blank">
        <img src="https://coverage-badge.samuelcolvin.workers.dev/adriamontoto/object-mother-pattern.svg" alt="Coverage Pipeline">
    </a>
    <a href="https://pypi.org/project/object-mother-pattern" target="_blank">
        <img src="https://img.shields.io/pypi/v/object-mother-pattern?color=%2334D058&label=pypi%20package" alt="Package Version">
    </a>
    <a href="https://pypi.org/project/object-mother-pattern/" target="_blank">
        <img src="https://img.shields.io/pypi/pyversions/object-mother-pattern.svg?color=%2334D058" alt="Supported Python Versions">
    </a>
    <a href="https://pepy.tech/projects/object-mother-pattern" target="_blank">
        <img src="https://static.pepy.tech/badge/object-mother-pattern/month" alt="Package Downloads">
    </a>
    <a href="https://deepwiki.com/adriamontoto/object-mother-pattern" target="_blank">
        <img src="https://img.shields.io/badge/DeepWiki-adriamontoto%2Fobject--mother--pattern-blue.svg?logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACwAAAAyCAYAAAAnWDnqAAAAAXNSR0IArs4c6QAAA05JREFUaEPtmUtyEzEQhtWTQyQLHNak2AB7ZnyXZMEjXMGeK/AIi+QuHrMnbChYY7MIh8g01fJoopFb0uhhEqqcbWTp06/uv1saEDv4O3n3dV60RfP947Mm9/SQc0ICFQgzfc4CYZoTPAswgSJCCUJUnAAoRHOAUOcATwbmVLWdGoH//PB8mnKqScAhsD0kYP3j/Yt5LPQe2KvcXmGvRHcDnpxfL2zOYJ1mFwrryWTz0advv1Ut4CJgf5uhDuDj5eUcAUoahrdY/56ebRWeraTjMt/00Sh3UDtjgHtQNHwcRGOC98BJEAEymycmYcWwOprTgcB6VZ5JK5TAJ+fXGLBm3FDAmn6oPPjR4rKCAoJCal2eAiQp2x0vxTPB3ALO2CRkwmDy5WohzBDwSEFKRwPbknEggCPB/imwrycgxX2NzoMCHhPkDwqYMr9tRcP5qNrMZHkVnOjRMWwLCcr8ohBVb1OMjxLwGCvjTikrsBOiA6fNyCrm8V1rP93iVPpwaE+gO0SsWmPiXB+jikdf6SizrT5qKasx5j8ABbHpFTx+vFXp9EnYQmLx02h1QTTrl6eDqxLnGjporxl3NL3agEvXdT0WmEost648sQOYAeJS9Q7bfUVoMGnjo4AZdUMQku50McDcMWcBPvr0SzbTAFDfvJqwLzgxwATnCgnp4wDl6Aa+Ax283gghmj+vj7feE2KBBRMW3FzOpLOADl0Isb5587h/U4gGvkt5v60Z1VLG8BhYjbzRwyQZemwAd6cCR5/XFWLYZRIMpX39AR0tjaGGiGzLVyhse5C9RKC6ai42ppWPKiBagOvaYk8lO7DajerabOZP46Lby5wKjw1HCRx7p9sVMOWGzb/vA1hwiWc6jm3MvQDTogQkiqIhJV0nBQBTU+3okKCFDy9WwferkHjtxib7t3xIUQtHxnIwtx4mpg26/HfwVNVDb4oI9RHmx5WGelRVlrtiw43zboCLaxv46AZeB3IlTkwouebTr1y2NjSpHz68WNFjHvupy3q8TFn3Hos2IAk4Ju5dCo8B3wP7VPr/FGaKiG+T+v+TQqIrOqMTL1VdWV1DdmcbO8KXBz6esmYWYKPwDL5b5FA1a0hwapHiom0r/cKaoqr+27/XcrS5UwSMbQAAAABJRU5ErkJggg==" alt="Project Documentation">
    </a>
</p>

The **Object Mother Pattern** is a Python 🐍 package that simplifies and standardizes the creation of test 🧪 objects. This pattern is especially helpful in testing scenarios where you need to generate multiple instances of complex objects quickly and consistently. By providing a set of prebuilt 🛠️ object mothers, you can drop these into your existing test suite and skip the boilerplate setup yourself.
<br><br>

## Table of Contents

- [📥 Installation](#installation)
- [📚 Documentation](#-documentation)
- [💻 Utilization](#utilization)
  - [📃 Available Mothers](#available-mothers)
  - [🎄 Real-Life Case: Christmas Detector Service](#real-life-case-christmas-detector-service)
  - [🧑‍🔧 Creating your own Object Mother](#creating-your-own-object-mother)
- [🤝 Contributing](#contributing)
- [🔑 License](#license)

<p align="right">
    <a href="#readme-top">🔼 Back to top</a>
</p><br><br>

<a name="installation"></a>

## 📥 Installation

You can install **Object Mother Pattern** using `pip`:

```bash
pip install object-mother-pattern
```

<p align="right">
    <a href="#readme-top">🔼 Back to top</a>
</p><br><br>

<a name="documentation"></a>

## 📚 Documentation

This [project's documentation](https://deepwiki.com/adriamontoto/object-mother-pattern) is powered by DeepWiki, which provides a comprehensive overview of the **Object Mother Pattern** and its usage.

<p align="right">
    <a href="#readme-top">🔼 Back to top</a>
</p><br><br>

<a name="utilization"></a>

## 💻 Utilization

Here is how you can utilize the **Object Mother** library to generate various types of test data:

```python
from object_mother_pattern import (
    BooleanMother,
    FloatMother,
    IntegerMother,
    StringDateMother,
    StringMother,
    UuidMother,
)

# Generate a random integer between -4 and 15
number = IntegerMother.create(min=-4, max=15)
print(number)
# >>> 8

# Generate a random float between -4 and 15 with 5 Decimal Places
number = FloatMother.create(min=-4, max=15, decimals=5)
print(number)
# >>> 0.83396

# Generate a random boolean
boolean = BooleanMother.create()
print(boolean)
# >>> True

# Generate a random string
string = StringMother.create()
print(string)
# >>> zFUmlsODZqzwyGjrOOqBtYzNwlJdOETalkXbuSegoQpgEnYQTCDeoifWrTQXMm

# Generate a random string of specific length
string = StringMother.of_length(length=10)
print(string)
# >>> TfkrYRxUFT

# Generate a random UUID
uuid = UuidMother.create()
print(uuid)
# >>> 3e9e0f3a-64a3-474f-9127-368e723f389f

# Generate a random date
date = StringDateMother.create()
print(date)
# >>> 2015-09-15
```

<p align="right">
    <a href="#readme-top">🔼 Back to top</a>
</p><br><br>

<a name="available-mothers"></a>

## 📃 Available Mothers

The package offers a wide collection of object mothers grouped by domain:

### Primitives

- [`object_mother_pattern.BooleanMother`](https://github.com/adriamontoto/object-mother-pattern/blob/master/object_mother_pattern/mothers/primitives/boolean_mother.py) - Responsible for generating random boolean values.
- [`object_mother_pattern.BytesMother`](https://github.com/adriamontoto/object-mother-pattern/blob/master/object_mother_pattern/mothers/primitives/bytes_mother.py) - Responsible for generating random bytes objects.
- [`object_mother_pattern.FloatMother`](https://github.com/adriamontoto/object-mother-pattern/blob/master/object_mother_pattern/mothers/primitives/float_mother.py) - Responsible for generating random float values within a range.
- [`object_mother_pattern.IntegerMother`](https://github.com/adriamontoto/object-mother-pattern/blob/master/object_mother_pattern/mothers/primitives/integer_mother.py) - Responsible for generating random integer numbers within a range.
- [`object_mother_pattern.StringMother`](https://github.com/adriamontoto/object-mother-pattern/blob/master/object_mother_pattern/mothers/primitives/string_mother.py) - Responsible for generating random strings with configurable length and characters.

### Dates

- [`object_mother_pattern.DateMother`](https://github.com/adriamontoto/object-mother-pattern/blob/master/object_mother_pattern/mothers/dates/date/date_mother.py) - Responsible for generating random date instances.
- [`object_mother_pattern.DatetimeMother`](https://github.com/adriamontoto/object-mother-pattern/blob/master/object_mother_pattern/mothers/dates/datetime/datetime_mother.py) - Responsible for generating random datetime instances.
- [`object_mother_pattern.StringDateMother`](https://github.com/adriamontoto/object-mother-pattern/blob/master/object_mother_pattern/mothers/dates/date/string_date_mother.py) - Responsible for generating ISO formatted date strings.
- [`object_mother_pattern.StringDatetimeMother`](https://github.com/adriamontoto/object-mother-pattern/blob/master/object_mother_pattern/mothers/dates/datetime/string_datetime_mother.py) - Responsible for generating ISO 8601 formatted datetime strings.
- [`object_mother_pattern.mothers.dates.TimezoneMother`](https://github.com/adriamontoto/object-mother-pattern/blob/master/object_mother_pattern/mothers/dates/timezone/timezone_mother.py) - Responsible for generating random timezone objects.
- [`object_mother_pattern.mothers.dates.StringTimezoneMother`](https://github.com/adriamontoto/object-mother-pattern/blob/master/object_mother_pattern/mothers/dates/timezone/string_timezone_mother.py) - Responsible for generating timezone names as strings.

### Identifiers

- [`object_mother_pattern.UuidMother`](https://github.com/adriamontoto/object-mother-pattern/blob/master/object_mother_pattern/mothers/identifiers/uuid_mother.py) - Responsible for generating random UUIDv4 values.
- [`object_mother_pattern.StringUuidMother`](https://github.com/adriamontoto/object-mother-pattern/blob/master/object_mother_pattern/mothers/identifiers/string_uuid_mother.py) - Responsible for generating UUIDv4 as strings.
- [`object_mother_pattern.mothers.identifiers.countries.spain.DniMother`](https://github.com/adriamontoto/object-mother-pattern/blob/master/object_mother_pattern/mothers/identifiers/countries/spain/dni_mother.py) - Responsible for generating valid Spanish DNI numbers.
- [`object_mother_pattern.mothers.identifiers.countries.spain.NieMother`](https://github.com/adriamontoto/object-mother-pattern/blob/master/object_mother_pattern/mothers/identifiers/countries/spain/nie_mother.py) - Responsible for generating valid Spanish NIE numbers.

### Internet

- [`object_mother_pattern.mothers.internet.AwsCloudRegionMother`](https://github.com/adriamontoto/object-mother-pattern/blob/master/object_mother_pattern/mothers/internet/aws_cloud_region_mother.py) - Responsible for generating AWS region codes.
- [`object_mother_pattern.mothers.internet.DomainMother`](https://github.com/adriamontoto/object-mother-pattern/blob/master/object_mother_pattern/mothers/internet/domain_mother.py) - Responsible for generating domain names with valid TLDs.
- [`object_mother_pattern.mothers.internet.Ipv4AddressMother`](https://github.com/adriamontoto/object-mother-pattern/blob/master/object_mother_pattern/mothers/internet/ipv4_address_mother.py) - Responsible for generating IPv4 addresses.
- [`object_mother_pattern.mothers.internet.Ipv4NetworkMother`](https://github.com/adriamontoto/object-mother-pattern/blob/master/object_mother_pattern/mothers/internet/ipv4_network_mother.py) - Responsible for generating IPv4 network ranges.
- [`object_mother_pattern.mothers.internet.Ipv6AddressMother`](https://github.com/adriamontoto/object-mother-pattern/blob/master/object_mother_pattern/mothers/internet/ipv6_address_mother.py) - Responsible for generating IPv6 addresses.
- [`object_mother_pattern.mothers.internet.Ipv6NetworkMother`](https://github.com/adriamontoto/object-mother-pattern/blob/master/object_mother_pattern/mothers/internet/ipv6_network_mother.py) - Responsible for generating IPv6 network ranges.
- [`object_mother_pattern.mothers.internet.MacAddressMother`](https://github.com/adriamontoto/object-mother-pattern/blob/master/object_mother_pattern/mothers/internet/mac_address_mother.py) - Responsible for generating MAC addresses in various formats.
- [`object_mother_pattern.mothers.internet.PortMother`](https://github.com/adriamontoto/object-mother-pattern/blob/master/object_mother_pattern/mothers/internet/port_mother.py) - Responsible for generating network port numbers.

### Money

- [`object_mother_pattern.mothers.money.cryptocurrencies.BtcWalletMother`](https://github.com/adriamontoto/object-mother-pattern/blob/master/object_mother_pattern/mothers/money/cryptocurrencies/btc_wallet_mother.py) - Responsible for generating Bitcoin wallet addresses using BIP39 words list.

### People

- [`object_mother_pattern.mothers.people.FullNameMother`](https://github.com/adriamontoto/object-mother-pattern/blob/master/object_mother_pattern/mothers/people/full_name_mother.py) - Responsible for generating realistic full names.
- [`object_mother_pattern.mothers.people.PasswordMother`](https://github.com/adriamontoto/object-mother-pattern/blob/master/object_mother_pattern/mothers/people/password_mother.py) - Responsible for generating password strings with strength options.
- [`object_mother_pattern.mothers.people.UsernameMother`](https://github.com/adriamontoto/object-mother-pattern/blob/master/object_mother_pattern/mothers/people/username_mother.py) - Responsible for generating username strings.

### Extra

- [`object_mother_pattern.mothers.extra.TextMother`](https://github.com/adriamontoto/object-mother-pattern/blob/master/object_mother_pattern/mothers/extra/text_mother.py) - Responsible for generating random text snippets.

<p align="right">
    <a href="#readme-top">🔼 Back to top</a>
</p><br><br>

<a name="real-life-case-christmas-detector-service"></a>

### 🎄 Real-Life Case: Christmas Detector Service

Below is an example of a real-life scenario where **Object Mother Pattern** can help simplify test date creation. We have a `ChristmasDetectorService` that checks if a given date falls within a specific Christmas holiday range. Using the [`DateMother`](https://github.com/adriamontoto/object-mother-pattern/blob/master/object_mother_pattern/mothers/dates/date/date_mother.py) class, we can easily generate dates both within and outside of this range for our tests, this ensuring that every possible scenario is covered.

```python
from datetime import date
from object_mother_pattern import DateMother


class ChristmasDetectorService:
    def __init__(self) -> None:
        self.christmas_start = date(year=2024, month=12, day=24)
        self.christmas_end = date(year=2025, month=1, day=6)

    def is_christmas(self, today: date) -> bool:
        return self.christmas_start <= today <= self.christmas_end


christmas_detector_service = ChristmasDetectorService()


def test_christmas_detector_is_christmas() -> None:
    date_mother = DateMother.create(
        start_date=date(year=2024, month=12, day=25),
        end_date=date(year=2025, month=1, day=6),
    )

    assert christmas_detector_service.is_christmas(today=date_mother)


def test_christmas_detector_is_not_christmas() -> None:
    date_mother = DateMother.out_of_range(
        start_date=date(year=2024, month=12, day=24),
        end_date=date(year=2025, month=1, day=6),
    )

    assert not christmas_detector_service.is_christmas(today=date_mother)
```

<p align="right">
    <a href="#readme-top">🔼 Back to top</a>
</p><br><br>

<a name="creating-your-own-object-mother"></a>

### 🧑‍🔧 Creating your own Object Mother

You can extend the functionality of this library by subclassing the
[`BaseMother`](https://github.com/adriamontoto/object-mother-pattern/blob/master/object_mother_pattern/models/base_mother.py)
class. Your custom mother must implement the `create` method to generate the
desired type.

```python
from random import randint

from object_mother_pattern.models import BaseMother


class IntegerMother(BaseMother[int]):
    @classmethod
    def create(cls, *, value: int | None = None, min: int = -100, max: int = 100) -> int:
        if value is not None:
            if not isinstance(value, int):
                raise TypeError('IntegerMother value must be an integer.')

            return value

        return randint(a=min, b=max)
```

<p align="right">
    <a href="#readme-top">🔼 Back to top</a>
</p><br><br>

<a name="contributing"></a>

## 🤝 Contributing

We love community help! Before you open an issue or pull request, please read:

- [`🤝 How to Contribute`](https://github.com/adriamontoto/object-mother-pattern/blob/master/.github/CONTRIBUTING.md)
- [`🧭 Code of Conduct`](https://github.com/adriamontoto/object-mother-pattern/blob/master/.github/CODE_OF_CONDUCT.md)
- [`🔐 Security Policy`](https://github.com/adriamontoto/object-mother-pattern/blob/master/.github/SECURITY.md)

_Thank you for helping make **⚒️ Object Mother Pattern** package awesome! 🌟_

<p align="right">
    <a href="#readme-top">🔼 Back to top</a>
</p><br><br>

<a name="license"></a>

## 🔑 License

This project is licensed under the terms of the [`MIT license`](https://github.com/adriamontoto/object-mother-pattern/blob/master/LICENSE.md).

<p align="right">
    <a href="#readme-top">🔼 Back to top</a>
</p>
