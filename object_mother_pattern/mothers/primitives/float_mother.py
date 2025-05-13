"""
FloatMother module.
"""

from random import choice, randint, uniform
from sys import version_info

if version_info >= (3, 12):
    from typing import override  # pragma: no cover
else:
    from typing_extensions import override  # pragma: no cover

from object_mother_pattern.mothers.base_mother import BaseMother


class FloatMother(BaseMother[float]):
    """
    FloatMother class is responsible for creating random float values.

    Example:
    ```python
    from object_mother_pattern.mothers import FloatMother

    number = FloatMother.create(min=-4, max=15, decimals=5)
    print(number)
    # >>> 0.83396
    ```
    """

    _type: type = float

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
            decimals (int | None, optional): Number of decimal places for the float. Must be >= 1 and <= 10. Defaults
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
        from object_mother_pattern.mothers import FloatMother

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

        if min == 0:
            min = 0.0000000001  # pragma: no cover

        if max == 0:
            max = 0.0000000001  # pragma: no cover

        return round(number=uniform(a=min, b=max), ndigits=decimals)  # noqa: S311

    @classmethod
    def positive(cls, *, max: int | float = 1.0, decimals: int | None = None) -> float:
        """
        Create a random positive float with an upper bound of `max` and if provided, rounded to the `decimals` number of
        decimal places, otherwise a random number of decimal places between 0 and 10.

        Args:
            max (int | float, optional): Upper bound for the positive float. Must be >= 0. Defaults to 1.0.
            decimals (int | None, optional): Number of decimal places. Must be >= 0 and <= 10. Defaults to None.

        Raises:
            TypeError: If `max` is not an integer or a float.
            ValueError: If `max` is not greater than 0.
            TypeError: If `decimals` is provided but is not an integer.
            ValueError: If `decimals` is not between 0 and 10 (inclusive).

        Returns:
            float: A randomly positive float value rounded to the specified number of decimal places.

        Example:
        ```python
        from object_mother_pattern.mothers import FloatMother

        positive = FloatMother.positive(max=15)
        print(positive)
        # >>> 8.71
        ```
        """
        return cls.create(min=0.0000000001, max=max, decimals=decimals)

    @classmethod
    def negative(cls, *, min: int | float = -1.0, decimals: int | None = None) -> float:
        """
        Create a random negative float with a lower bound of `min` and if provided, rounded to the `decimals` number of
        decimal places, otherwise a random number of decimal places between 0 and 10.

        Args:
            min (int | float, optional): Lower bound for the negative float. Must be < 0. Defaults to -1.0.
            decimals (int | None, optional): Number of decimal places. Must be >= 0 and <= 10. Defaults to None.

        Raises:
            TypeError: If `min` is not an integer or a float.
            ValueError: If `min` is greater than -1.
            TypeError: If `decimals` is provided but is not an integer.
            ValueError: If `decimals` is not between 0 and 10 (inclusive).

        Returns:
            float: A randomly negative float value rounded to the specified number of decimal places.

        Example:
        ```python
        from object_mother_pattern.mothers import FloatMother

        negative = FloatMother.negative(min=-61)
        print(negative)
        # >>> -13.93
        ```
        """
        return cls.create(min=min, max=-0.0000000001, decimals=decimals)

    @classmethod
    def out_of_range(cls, *, min: int | float = -1.0, max: int | float = 1.0, range: int | float = 1) -> float:
        """
        Create a random float value that is either less than `min` or greater than `max` by an offset
        specified by the `range` parameter.

        Args:
            min (int | float, optional): The lower bound of the range. Defaults to -1.0.
            max (int | float, optional): The upper bound of the range. Defaults to 1.0.
            range (int | float, optional): The range offset. Must be >= 0. Defaults to 1.

        Raises:
            TypeError: If `min` is not an integer or a float.
            TypeError: If `max` is not an integer or a float.
            ValueError: If `min` is greater than `max`.
            TypeError: If `range` is not an integer or a float.
            ValueError: If `range` is a negative value.

        Returns:
            float: A randomly generated float value out of the provided range.

        Example:
        ```python
        from object_mother_pattern.mothers import FloatMother

        number = FloatMother.out_of_range()
        print(number)
        # >>> -1.2073998516955866
        ```
        """
        if type(min) is not int and type(min) is not float:
            raise TypeError('FloatMother min value must be an integer or a float.')

        if type(max) is not int and type(max) is not float:
            raise TypeError('FloatMother max value must be an integer or a float.')

        if min > max:
            raise ValueError('FloatMother min value must be less than or equal to max value.')

        if type(range) is not int and type(range) is not float:
            raise TypeError('FloatMother range must be an integer or a float.')

        if range < 0:
            raise ValueError('FloatMother range must be a positive value.')

        epsilon = 1e-12
        return choice(  # noqa: S311
            seq=[
                uniform(a=min - range, b=min - epsilon),  # noqa: S311
                uniform(a=max + epsilon, b=max + range),  # noqa: S311
            ]
        )
