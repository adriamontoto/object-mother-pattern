"""
IntegerMother module.
"""

from sys import version_info

if version_info >= (3, 12):
    from typing import override  # pragma: no cover
else:
    from typing_extensions import override  # pragma: no cover

from random import randint

from object_mother_pattern.mothers.base_mother import BaseMother


class IntegerMother(BaseMother[int]):
    """
    IntegerMother class is responsible for creating random integer values.

    Example:
    ```python
    from object_mother_pattern.mothers import IntegerMother

    number = IntegerMother.create(min=-4, max=15)
    print(number)
    # >>> 8
    ```
    """

    _type: type = int

    @classmethod
    @override
    def create(cls, *, value: int | None = None, min: int = -100, max: int = 100) -> int:
        """
        Create a random integer value. If a specific integer value is provided via `value`, it is returned after
        validation. Otherwise, a random integer value is generated within the provided range of `min` and `max` (both
        included).

        Args:
            value (int | None, optional): Specific value to return. Defaults to None.
            min (int, optional): Minimum value of the range. Defaults to -100.
            max (int, optional): Maximum value of the range. Must be >= `min`. Defaults to 100.

        Raises:
            TypeError: If the provided `value` is not an integer.
            TypeError: If `min` is not an integer.
            TypeError: If `max` is not an integer.
            ValueError: If `min` is greater than `max`.

        Returns:
            int: A randomly generated integer value.

        Example:
        ```python
        from object_mother_pattern.mothers import IntegerMother

        number = IntegerMother.create(min=-4, max=15)
        print(number)
        # >>> 8
        ```
        """
        if value is not None:
            if type(value) is not int:
                raise TypeError('IntegerMother value must be an integer.')

            return value

        if type(min) is not int:
            raise TypeError('IntegerMother min value must be an integer.')

        if type(max) is not int:
            raise TypeError('IntegerMother max value must be an integer.')

        if min > max:
            raise ValueError('IntegerMother min value must be less than or equal to max value.')

        return randint(a=min, b=max)  # noqa: S311

    @classmethod
    def positive(cls, *, max: int = 100) -> int:
        """
        Create a random positive integer with an upper bound of `max`.

        Args:
            max (int, optional): Upper bound for the positive integer. Must be >= 0. Defaults to 100.

        Raises:
            TypeError: If `max` is not an integer.
            ValueError: If `max` is not greater than 0.

        Returns:
            int: A randomly positive integer value.

        Example:
        ```python
        from object_mother_pattern.mothers import IntegerMother

        positive = IntegerMother.positive(max=15)
        print(positive)
        # >>> 2
        ```
        """
        return cls.create(min=1, max=max)

    @classmethod
    def negative(cls, *, min: int = -100) -> int:
        """
        Create a random negative integer with a lower bound of `min`.

        Args:
            min (int, optional): Lower bound for the negative integer. Must be < 0. Defaults to -100.

        Raises:
            TypeError: If `min` is not an integer.
            ValueError: If `min` is not less than 0.

        Returns:
            int: A randomly negative integer value.

        Example:
        ```python
        from object_mother_pattern.mothers import IntegerMother

        negative = IntegerMother.negative(min=-61)
        print(negative)
        # >>> -45
        ```
        """
        return cls.create(min=min, max=-1)
