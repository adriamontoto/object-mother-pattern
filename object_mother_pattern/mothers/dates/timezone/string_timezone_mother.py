"""
StringTimezoneMother module.
"""

from sys import version_info

if version_info >= (3, 12):
    from typing import override  # pragma: no cover
else:
    from typing_extensions import override  # pragma: no cover

from object_mother_pattern.models import BaseMother

from .timezone_mother import TimezoneMother


class StringTimezoneMother(BaseMother[str]):
    """
    StringTimezoneMother class is responsible for creating random string timezone names.

    Example:
    ```python
    from object_mother_pattern.mothers.dates import StringTimezoneMother

    timezone = StringTimezoneMother.create()
    print(timezone)
    # >>> UTC
    ```
    """

    @classmethod
    @override
    def create(cls, *, value: str | None = None) -> str:
        """Creates a timezone name as a string.

        Args:
            value: A specific timezone name to use. If None, a random one is generated.

        Returns:
            A timezone name as a string.

        Example:
        ```python
        from object_mother_pattern.mothers.dates import StringTimezoneMother

        timezone = StringTimezoneMother.create()
        print(timezone)
        # >>> UTC
        ```
        """
        if value is not None:
            if type(value) is not str:
                raise TypeError('StringTimezoneMother value must be a string.')

            return value

        return str(TimezoneMother.create())
