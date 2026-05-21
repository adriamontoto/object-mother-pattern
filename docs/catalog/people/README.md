# People And Text Mothers

People and text mothers generate human-readable strings for tests that need identity-like or prose-like values.

## Imports

```python
from object_mother_pattern.mothers.extra import TextMother
from object_mother_pattern.mothers.people import FullNameMother, PasswordMother, UsernameMother
```

## Catalog

| Mother | Typical Uses |
| --- | --- |
| `FullNameMother` | Full-name strings. |
| `UsernameMother` | Username strings. |
| `PasswordMother` | Password-shaped strings for validation tests. |
| `TextMother` | Longer text snippets. |

## Guidance

- Generated names and usernames are fixtures, not identities.
- Generated passwords are not credentials and should not be used for accounts.
- Prefer explicit text for exact UI copy, snapshot, or serialization assertions.
- Use generated text when the test only needs non-empty or length-constrained content.
