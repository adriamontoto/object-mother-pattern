"""
FloatMother module.
"""

from random import randint
from sys import version_info

if version_info >= (3, 12):
    from typing import override  # pragma: no cover
else:
    from typing_extensions import override  # pragma: no cover

from object_mother_pattern.mothers.base_mother import BaseMother


class FloatMother(BaseMother[float]):
    """
    FloatMother class.

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
        Create a random float within the provided range. If a value is provided, it will be returned.

        Args:
            value (int | float | None, optional): Float value. Defaults to None.
            min (int | float, optional): Minimum float value. Defaults to -1.0.
            max (int | float, optional): Maximum float value. Defaults to 1.0.
            decimals (int | None, optional): Number of decimal places, if None, a random number of decimal places will
            be used. Defaults to None.

        Raises:
            TypeError: If value is not an int or a float.
            TypeError: If min is not an int or a float.
            TypeError: If max is not an int or a float.
            ValueError: If min is greater than max.
            TypeError: If decimals is not an int.
            ValueError: If decimals is less than 0.
            ValueError: If decimals is greater than 10.

        Returns:
            float: Random float.

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
            decimals = randint(a=0, b=10)

        if type(decimals) is not int:
            raise TypeError('FloatMother decimals value must be an integer.')

        if decimals < 0:
            raise ValueError('FloatMother decimals value must be greater than or equal to 0.')

        if decimals > 10:
            raise ValueError('FloatMother decimals value must be less than or equal to 10.')

        if min == max:
            return min

        if min == 0:
            min = 0.0000000001  # pragma: no cover

        if max == 0:
            max = 0.0000000001  # pragma: no cover

        return cls._random().pyfloat(min_value=min, max_value=max, right_digits=decimals)

    @classmethod
    def positive(cls, *, max: int | float = 1.0, decimals: int | None = None) -> float:
        """
        Create a random positive float, greater than 0.

        Args:
            max (int | float, optional): Maximum positive float value. Defaults to 1.0.
            decimals (int | None, optional): Number of decimal places, if None, a random number of decimal places will
            be used. Defaults to None.

        Raises:
            TypeError: If max is not an int or a float.
            ValueError: If max is less than 1.
            TypeError: If decimals is not an int.
            ValueError: If decimals is less than 0.

        Returns:
            float: Random positive float.

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
        Create a random negative float, less than 0.

        Args:
            min (int | float, optional): Minimum negative float value. Defaults to -1.0.
            decimals (int | None, optional): Number of decimal places, if None, a random number of decimal places will
            be used. Defaults to None.

        Raises:
            TypeError: If min is not a float.
            ValueError: If min is greater than -1.
            TypeError: If decimals is not an int.
            ValueError: If decimals is less than 0.

        Returns:
            float: Random negative float.

        Example:
        ```python
        from object_mother_pattern.mothers import FloatMother

        negative = FloatMother.negative(min=-61)
        print(negative)
        # >>> -13.93
        ```
        """
        return cls.create(min=min, max=-0.0000000001, decimals=decimals)
