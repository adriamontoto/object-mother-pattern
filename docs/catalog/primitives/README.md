# Primitive Mothers

Primitive mothers generate small scalar values for tests. They are best used when a test needs a value with a shape or
boundary condition, not a specific domain fixture.

## Imports

```python
from object_mother_pattern import BooleanMother, BytesMother, FloatMother, IntegerMother, StringMother
```

## Catalog

| Mother | Typical Uses |
| --- | --- |
| `BooleanMother` | Random boolean values and explicit boolean validation. |
| `BytesMother` | Byte strings with optional length controls. |
| `FloatMother` | Floats with ranges, decimals, sign helpers, and out-of-range values. |
| `IntegerMother` | Integers with ranges, sign helpers, parity helpers, and out-of-range values. |
| `StringMother` | Strings with length, alphabet, casing, numeric, whitespace, and invalid helpers. |

## Examples

```python
from object_mother_pattern import IntegerMother, StringMother

identifier = IntegerMother.positive()
code = StringMother.uppercase(min_length=3, max_length=8)
invalid_name = StringMother.invalid_type()
```

## Guidance

- Use explicit `value=` when the assertion depends on exact output.
- Use random generated values when the test only cares about type or invariant.
- Use `invalid_type()` for type-error branches and range helpers for value-error branches.
- Keep generated random strings out of snapshots and exact serialization assertions.
