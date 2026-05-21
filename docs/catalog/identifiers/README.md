# Identifier Mothers

Identifier mothers generate UUIDs, country/world identifiers, Spanish document identifiers, phone numbers, and vehicle
plates for tests.

## UUIDs

```python
from object_mother_pattern.mothers.identifiers.uuid import StringUuidV4Mother, UuidV4Mother
```

| Family | Mothers |
| --- | --- |
| Any supported UUID | `UuidMother`, `StringUuidMother` |
| Versioned UUID objects | `UuidV1Mother`, `UuidV3Mother`, `UuidV4Mother`, `UuidV5Mother`, `UuidV6Mother`, `UuidV7Mother`, `UuidV8Mother` |
| Versioned UUID strings | `StringUuidV1Mother`, `StringUuidV3Mother`, `StringUuidV4Mother`, `StringUuidV5Mother`, `StringUuidV6Mother`, `StringUuidV7Mother`, `StringUuidV8Mother` |

Use versioned mothers when code branches on a UUID version. Use aggregate mothers when any supported UUID is acceptable.

## World Identifiers

```python
from object_mother_pattern.mothers.identifiers.world import Iso3166Alpha2CodeMother, VinMother
```

| Mother | Typical Uses |
| --- | --- |
| `CountryTldMother` | Country top-level-domain test values. |
| `Iso3166Alpha2CodeMother` | ISO 3166 alpha-2 code test values. |
| `Iso3166Alpha3CodeMother` | ISO 3166 alpha-3 code test values. |
| `Iso3166NumericCodeMother` | ISO 3166 numeric code test values. |
| `PhoneCodeMother` | International phone code test values. |
| `VinMother` | Vehicle identification number test values. |

## Spanish Identifiers

```python
from object_mother_pattern.mothers.identifiers.countries.spain import DniMother, VehiclePlateMother
```

| Mother | Typical Uses |
| --- | --- |
| `DniMother` | Spanish DNI values. |
| `NieMother` | Spanish NIE values. |
| `NifMother` | Spanish NIF values. |
| `NussMother` | Spanish social security identifier values. |
| `PassportMother` | Spanish passport-like values. |
| `PhoneNumberMother` | Spanish phone number values. |
| `VehiclePlateMother` | Any supported Spanish vehicle plate format. |

## Spanish Vehicle Plates

Specific vehicle-plate mothers are available from
`object_mother_pattern.mothers.identifiers.countries.spain`.

| Family | Examples |
| --- | --- |
| Ordinary plates | `OrdinaryVehiclePlateMother`, `OrdinaryTruckVehiclePlateMother`, `TwoWheelsVehiclePlateMother` |
| Temporary plates | `TemporalCompanyNotRegisteredVehiclePlateMother`, `TemporalCompanyRegisteredVehiclePlateMother`, `TemporalPrivateIndividualVehiclePlateMother` |
| Official and service plates | `CivilGuardVehiclePlateMother`, `NationalPoliceVehiclePlateMother`, `StateMotorPoolVehiclePlateMother`, `NavyVehiclePlateMother`, `ArmyVehiclePlateMother`, `AirForceVehiclePlateMother` |
| Diplomatic and international plates | `DiplomaticCorpsVehiclePlateMother`, `ConsularCorpsVehiclePlateMother`, `InternationalOrganizationVehiclePlateMother` |
| Other supported formats | `AdministrativeTechnicianVehiclePlateMother`, `CanariasPoliceVehiclePlateMother`, `CatalanPoliceVehiclePlateMother`, `EspecialVehiclePlateMother`, `HistoricalVehiclePlateMother`, `MinistryDevelopmentVehiclePlateMother`, `MinistryEnvironmentVehiclePlateMother`, `ProvincialSystemVehiclePlateMother` |

## Guidance

- Generated identifiers are test fixtures, not proof of ownership or legal status.
- Use exact mothers when a test depends on a specific format.
- Use `invalid_value()` helpers when testing value validation in downstream value objects.
