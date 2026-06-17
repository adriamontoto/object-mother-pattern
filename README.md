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

The **Object Mother Pattern** is a Python 🐍 package that simplifies and standardizes the creation of test 🧪 data.
Instead of hand-writing random values, invalid values, range boundaries, dates, identifiers, URLs, credit cards, and
other fixtures in every test module, you use reusable object mother classes with consistent validation behavior.
<br><br>

## Table of Contents

- [📥 Installation](#installation)
- [📚 Documentation](#documentation)
- [⚡ Quick Start](#quick-start)
- [🧩 Core Ideas](#core-ideas)
- [🤔 Why Object Mothers?](#why-object-mothers)
- [📃 Available Mothers](#available-mothers)
- [🧪 Testing Patterns](#testing-patterns)
- [🎄 Real-Life Case: Christmas Detector Service](#real-life-case-christmas-detector-service)
- [🧑‍🔧 Creating Your Own Object Mother](#creating-your-own-object-mother)
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

You can install the companion AI-agent skill from [skills.sh](https://www.skills.sh/) with Vercel's `skills` CLI:

```bash
npx skills add adriamontoto/object-mother-pattern
```

Review the skill source in [`skills/object-mother-pattern`](skills/object-mother-pattern) before installing it in
sensitive environments.

<p align="right">
    <a href="#readme-top">🔼 Back to top</a>
</p><br><br>

<a name="documentation"></a>

## 📚 Documentation

The root README is the entry point. Deeper guides live in this repository and are linked here:

- [`docs/README.md`](docs/README.md): Documentation hub.
- [`docs/usage/README.md`](docs/usage/README.md): Core usage, imports, validation, and custom mothers.
- [`docs/catalog/README.md`](docs/catalog/README.md): Feature map by mother category.
- Catalog details: [`primitives`](docs/catalog/primitives/README.md), [`dates`](docs/catalog/dates/README.md),
  [`identifiers`](docs/catalog/identifiers/README.md), [`internet`](docs/catalog/internet/README.md),
  [`money`](docs/catalog/money/README.md), and [`people/text`](docs/catalog/people/README.md).
- [`docs/testing/README.md`](docs/testing/README.md): Testing patterns for valid, invalid, boundary, and deterministic
  data.
- [`AI Skill`](skills/README.md): Installable skill package that teaches AI agents how to use Object Mother Pattern.

This [project's DeepWiki documentation](https://deepwiki.com/adriamontoto/object-mother-pattern) is also available for
generated repository navigation.

<p align="right">
    <a href="#readme-top">🔼 Back to top</a>
</p><br><br>

<a name="quick-start"></a>

## ⚡ Quick Start

Use mothers directly in tests when you need valid values:

```python
from object_mother_pattern import (
    BooleanMother,
    DateMother,
    FloatMother,
    IntegerMother,
    StringMother,
)
from object_mother_pattern.mothers.identifiers.uuid import UuidV4Mother

integer = IntegerMother.create(min=-4, max=15)
amount = FloatMother.create(min=0, max=100, decimals=2)
enabled = BooleanMother.create()
username = StringMother.lowercase(min_length=8, max_length=16)
date = DateMother.create()
uuid = UuidV4Mother.create()
```

Pass an explicit `value` when a test needs a known valid value and you still want the mother to validate it:

```python
from object_mother_pattern import IntegerMother

assert IntegerMother.create(value=7) == 7
```

Generate values outside an accepted range when testing validation failures:

```python
from datetime import date

from object_mother_pattern import DateMother

value = DateMother.out_of_range(
    start_date=date(year=2025, month=1, day=1),
    end_date=date(year=2025, month=1, day=31),
)
```

<p align="right">
    <a href="#readme-top">🔼 Back to top</a>
</p><br><br>

<a name="core-ideas"></a>

## 🧩 Core Ideas

Most mothers follow the same pattern:

- `create(value=...)` validates and returns an explicit value.
- `create(...)` without `value` generates a valid random value.
- Dedicated helpers such as `empty()`, `of_length()`, `positive()`, `odd()`, or `out_of_range()` express common test
  shapes.
- `invalid_type()` generates a value with the wrong type for negative-path tests.
- Collection mothers can compose other mothers with callables such as `item_mother`, `key_mother`, and `value_mother`.

```python
from object_mother_pattern.models import DictMother, ListMother
from object_mother_pattern import IntegerMother, StringMother

values = ListMother.of_length(length=3, item_mother=IntegerMother.positive)
payload = DictMother.of_length(
    length=2,
    key_mother=lambda: StringMother.lowercase(min_length=4, max_length=8),
    value_mother=IntegerMother.create,
)
```

<p align="right">
    <a href="#readme-top">🔼 Back to top</a>
</p><br><br>

<a name="why-object-mothers"></a>

## 🤔 Why Object Mothers?

Object mothers help tests say what kind of value they need instead of repeating how that value is built. A hardcoded
literal such as `'john@example.com'`, `'550e8400-e29b-41d4-a716-446655440000'`, or `42` can be perfectly valid, but when
every test invents its own literals the setup becomes duplicated, inconsistent, and harder to update when a validation
rule changes.

Use object mothers when the exact value does not matter and the test only needs a value that satisfies a shape:

```python
from object_mother_pattern import IntegerMother
from object_mother_pattern.mothers.internet import EmailAddressMother

email = EmailAddressMother.create()
quantity = IntegerMother.positive()

assert '@' in email
assert quantity > 0
```

This keeps the test focused on the behavior under test. The mother owns the details of valid email generation, positive
integer generation, invalid types, ranges, and special formats. If those rules evolve, tests that only need "a valid
email" or "a positive integer" do not need to be rewritten.

Hardcoded values are still the best choice when the value is the point of the test:

- Use fixed literals for exact serialization, snapshots, URLs, JSON, SQL, error messages, and UI copy.
- Use explicit boundary values for deliberate limits such as minimum length, maximum length, zero, one, empty strings,
  first date, last date, or a known invalid format.
- Use a known literal when reproducing a specific bug.
- Use `create(value=...)` when you want an explicit value but still want the mother to validate that it belongs to the
  expected shape.

```python
from object_mother_pattern import IntegerMother, StringMother

assert StringMother.create(value='invoice-paid') == 'invoice-paid'
assert IntegerMother.create(value=10) == 10
```

The practical rule is simple: generate values for invariant-based tests, hardcode values for exact examples and
intentional limits.

<p align="right">
    <a href="#readme-top">🔼 Back to top</a>
</p><br><br>

<a name="available-mothers"></a>

## 📃 Available Mothers

The package includes mothers for:

| Category | Examples |
| --- | --- |
| Models | `BaseMother`, `EnumerationMother`, `ListMother`, `DictMother` |
| Primitives | `BooleanMother`, `BytesMother`, `FloatMother`, `IntegerMother`, `StringMother` |
| Dates | `DateMother`, `DatetimeMother`, `StringDateMother`, `StringDatetimeMother`, timezone mothers |
| Identifiers | UUID mothers, Spanish identifiers, world/country code identifiers |
| Internet | URLs, domains, hosts, ports, IP addresses, networks, MAC addresses, email addresses, user agents |
| Money | IBANs, credit cards by brand, Bitcoin wallet values |
| People | Full names, usernames, passwords |
| Extra | Text snippets |

See [`docs/catalog/README.md`](docs/catalog/README.md) for a deeper feature map and import guidance.

<p align="right">
    <a href="#readme-top">🔼 Back to top</a>
</p><br><br>

<a name="testing-patterns"></a>

## 🧪 Testing Patterns

Use explicit values when an assertion depends on exact output:

```python
from object_mother_pattern import StringMother

assert StringMother.create(value='known-value') == 'known-value'
```

Use generated values when the test only cares about invariants:

```python
from object_mother_pattern import IntegerMother

value = IntegerMother.positive()

assert value > 0
```

Use invalid helpers for negative-path coverage:

```python
from pytest import raises

from object_mother_pattern import IntegerMother

with raises(TypeError):
    IntegerMother.create(value=IntegerMother.invalid_type())
```

More guidance is available in [`docs/testing/README.md`](docs/testing/README.md).

<p align="right">
    <a href="#readme-top">🔼 Back to top</a>
</p><br><br>

<a name="real-life-case-christmas-detector-service"></a>

## 🎄 Real-Life Case: Christmas Detector Service

This service checks whether a date falls within a Christmas holiday range. Tests use
[`DateMother`](https://github.com/adriamontoto/object-mother-pattern/blob/master/object_mother_pattern/mothers/dates/date/date_mother.py)
to create dates inside and outside the accepted range without duplicating date-generation logic.

```python
from datetime import date
from object_mother_pattern import DateMother


class ChristmasDetectorService:
    def __init__(self) -> None:
        self._christmas_start = date(year=2024, month=12, day=24)
        self._christmas_end = date(year=2025, month=1, day=6)

    def is_christmas(self, today: date) -> bool:
        return self._christmas_start <= today <= self._christmas_end


christmas_detector_service = ChristmasDetectorService()


def test_christmas_detector_is_christmas() -> None:
    today = DateMother.create(
        start_date=date(year=2024, month=12, day=25),
        end_date=date(year=2025, month=1, day=6),
    )

    assert christmas_detector_service.is_christmas(today=today)


def test_christmas_detector_is_not_christmas() -> None:
    today = DateMother.out_of_range(
        start_date=date(year=2024, month=12, day=24),
        end_date=date(year=2025, month=1, day=6),
    )

    assert christmas_detector_service.is_christmas(today=today) is False
```

<p align="right">
    <a href="#readme-top">🔼 Back to top</a>
</p><br><br>

<a name="creating-your-own-object-mother"></a>

## 🧑‍🔧 Creating Your Own Object Mother

You can extend the functionality of this library by subclassing the
[`BaseMother`](https://github.com/adriamontoto/object-mother-pattern/blob/master/object_mother_pattern/models/base_mother.py)
class. A custom mother should validate explicit values and generate valid values when no value is provided.

```python
from random import randint

from object_mother_pattern.models import BaseMother


class PositiveIntegerMother(BaseMother[int]):
    @classmethod
    def create(cls, *, value: int | None = None) -> int:
        if value is not None:
            if type(value) is not int:
                raise TypeError('PositiveIntegerMother value must be an integer.')

            if value <= 0:
                raise ValueError('PositiveIntegerMother value must be positive.')

            return value

        return randint(a=1, b=100)
```

More detail is available in [`docs/usage/README.md`](docs/usage/README.md).

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
