"""
TimezoneMother module.
"""

from sys import version_info

if version_info >= (3, 12):
    from typing import override  # pragma: no cover
else:
    from typing_extensions import override  # pragma: no cover

from datetime import tzinfo
from random import choice
from zoneinfo import ZoneInfo, available_timezones

from object_mother_pattern.models import BaseMother


class TimezoneMother(BaseMother[tzinfo]):
    """
    TimezoneMother class is responsible for creating random timezone objects.

    Example:
    ```python
    from object_mother_pattern.mothers.dates import TimezoneMother

    timezone = TimezoneMother.create()
    print(timezone)
    # >>> UTC
    ```
    """

    @classmethod
    @override
    def create(cls, *, value: tzinfo | None = None) -> tzinfo:
        """
        Creates a timezone object.

        Args:
            value: A specific timezone object to use. If None, a random one is generated.

        Raises:
            TypeError: If the provided `value` is not a tzinfo.

        Returns:
            A timezone object.

        Example:
        ```python
        from object_mother_pattern.mothers.dates import TimezoneMother

        timezone = TimezoneMother.create()
        print(timezone)
        # >>> 'UTC'
        ```
        """
        if value is not None:
            if not isinstance(value, tzinfo):
                raise TypeError('TimezoneMother value must be a tzinfo.')

            return value

        return ZoneInfo(choice(seq=list(available_timezones())))  # noqa: S311
