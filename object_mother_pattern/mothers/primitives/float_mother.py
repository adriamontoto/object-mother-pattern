"""
FloatMother module.
"""

from sys import version_info

if version_info >= (3, 12):
    from typing import override  # pragma: no cover
else:
    from typing_extensions import override  # pragma: no cover

from random import randint, uniform
from typing import Any, Iterable

from object_mother_pattern.models import BaseMother


class FloatMother(BaseMother[float]):
    """
    FloatMother class is responsible for creating random float values.

    Example:
    ```python
    from object_mother_pattern import FloatMother

    number = FloatMother.create(min=-4, max=15, decimals=5)
    print(number)
    # >>> 0.83396
    ```
    """

    @classmethod
    @override
    def create(  # noqa: C901
        cls,
        *,
        value: int | float | None = None,
        min: int | float = -1.0,
        max: int | float = 1.0,
        decimals: int | None = None,
    ) -> float:
        """
        Create a random float value. If a specific float value is provided via `value`, it is returned after validation.
        Otherwise, a random float value is generated within the provided range of `min` and `max` (both included) and if
        provided, rounded to the `decimals` number of decimal places, otherwise a random number of decimal places
        between 0 and 10.

        Args:
            value (int | float | None, optional): Specific value to return. Defaults to None.
            min (int | float, optional): Minimum value of the range. Defaults to -1.0.
            max (int | float, optional): Maximum value of the range. Must be >= `min`. Defaults to 1.0.
            decimals (int | None, optional): Number of decimal places for the float. Must be >= 0 and <= 10. Defaults
            to None.

        Raises:
            TypeError: If the provided `value` is not an integer or a float.
            TypeError: If `min` is not an integer or a float.
            TypeError: If `max` is not an integer or a float.
            ValueError: If `min` is greater than `max`.
            TypeError: If `decimals` is not an integer.
            ValueError: If `decimals` is less than 0.
            ValueError: If `decimals` is greater than 10.

        Returns:
            float: A randomly float rounded value to the specified number of decimal places.

        Example:
        ```python
        from object_mother_pattern import FloatMother

        number = FloatMother.create(min=-4, max=15, decimals=5)
        print(number)
        # >>> 0.83396
        ```
        """
        if value is not None:
            if type(value) is not int and type(value) is not float:
                raise TypeError('FloatMother value must be an integer or a float.')

            return value

        if type(min) is not int and type(min) is not float:
            raise TypeError('FloatMother min value must be an integer or a float.')

        if type(max) is not int and type(max) is not float:
            raise TypeError('FloatMother max value must be an integer or a float.')

        if min > max:
            raise ValueError('FloatMother min value must be less than or equal to max value.')

        if decimals is None:
            decimals = randint(a=0, b=10)  # noqa: S311

        if type(decimals) is not int:
            raise TypeError('FloatMother decimals value must be an integer.')

        if decimals < 0:
            raise ValueError('FloatMother decimals value must be greater than or equal to 0.')

        if decimals > 10:
            raise ValueError('FloatMother decimals value must be less than or equal to 10.')

        if min == max:
            return round(number=min, ndigits=decimals)

        return round(number=uniform(a=min, b=max), ndigits=decimals)  # noqa: S311

    @override
    @classmethod
    def invalid_type(cls, *, remove_types: Iterable[type[Any]] | None = None) -> Any:  # noqa: C901
        """
        Create an invalid type.

        Args:
            remove_types (Iterable[type[Any]] | None, optional): Iterable of types to remove. Defaults to None.

        Returns:
            Any: Invalid type.
        """
        remove_types = set() if remove_types is None else set(remove_types)
        remove_types.add(int)

        return super().invalid_type(remove_types=remove_types)
