"""
IntegerMother module.
"""

from sys import version_info

if version_info >= (3, 12):
    from typing import override  # pragma: no cover
else:
    from typing_extensions import override  # pragma: no cover

from random import choice, randint

from object_mother_pattern.models import BaseMother


class IntegerMother(BaseMother[int]):
    """
    IntegerMother class is responsible for creating random integer values.

    Example:
    ```python
    from object_mother_pattern import IntegerMother

    number = IntegerMother.create(min=-4, max=15)
    print(number)
    # >>> 8
    ```
    """

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
        from object_mother_pattern import IntegerMother

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
        Create a random positive integer with an upper bound of `max`, from 1 to `max` (both included).

        Args:
            max (int, optional): Upper bound for the positive integer. Must be > 0. Defaults to 100.

        Raises:
            TypeError: If `max` is not an integer.
            ValueError: If `max` is not greater than 0.

        Returns:
            int: A randomly positive integer value.

        Example:
        ```python
        from object_mother_pattern import IntegerMother

        positive = IntegerMother.positive(max=15)
        print(positive)
        # >>> 2
        ```
        """
        return cls.create(min=1, max=max)

    @classmethod
    def positive_or_zero(cls, *, max: int = 100) -> int:
        """
        Create a random positive integer (including 0) with an upper bound of `max`, from 0 to `max` (both included).

        Args:
            max (int, optional): Upper bound for the positive integer. Must be >= 0. Defaults to 100.

        Raises:
            TypeError: If `max` is not an integer.
            ValueError: If `max` is not greater than or equal to 0.

        Returns:
            int: A randomly positive integer value.

        Example:
        ```python
        from object_mother_pattern import IntegerMother

        positive = IntegerMother.positive_or_zero(max=15)
        print(positive)
        # >>> 2
        ```
        """
        return cls.create(min=0, max=max)

    @classmethod
    def negative(cls, *, min: int = -100) -> int:
        """
        Create a random negative integer with a lower bound of `min`, from `min` to -1 (both included).

        Args:
            min (int, optional): Lower bound for the negative integer. Must be < 0. Defaults to -100.

        Raises:
            TypeError: If `min` is not an integer.
            ValueError: If `min` is not less than 0.

        Returns:
            int: A randomly negative integer value.

        Example:
        ```python
        from object_mother_pattern import IntegerMother

        negative = IntegerMother.negative(min=-61)
        print(negative)
        # >>> -45
        ```
        """
        return cls.create(min=min, max=-1)

    @classmethod
    def negative_or_zero(cls, *, min: int = -100) -> int:
        """
        Create a random negative integer (including 0) with a lower bound of `min`, from `min` to 0 (both included).

        Args:
            min (int, optional): Lower bound for the negative integer. Must be < 0. Defaults to -100.

        Raises:
            TypeError: If `min` is not an integer.
            ValueError: If `min` is not less than 0.

        Returns:
            int: A randomly negative integer value.

        Example:
        ```python
        from object_mother_pattern import IntegerMother

        negative = IntegerMother.negative_or_zero(min=-61)
        print(negative)
        # >>> -45
        ```
        """
        return cls.create(min=min, max=0)

    @classmethod
    def out_of_range(cls, *, min: int = -100, max: int = 100, range: int = 100) -> int:
        """
        Create a random integer value that is either less than `min` or greater than `max` (both excluded) by a range
        specified by the `range` parameter.

        Args:
            min (int, optional): The lower bound of the range. Defaults to -100.
            max (int, optional): The upper bound of the range. Defaults to 100.
            range (int, optional): The range offset. Must be > 0. Defaults to 100.

        Raises:
            TypeError: If `min` is not an integer.
            TypeError: If `max` is not an integer.
            ValueError: If `min` is greater than `max`.
            TypeError: If `range` is not an integer.
            ValueError: If `range` is a non-positive integer.

        Returns:
            int: A randomly generated integer value out of the provided range.

        Example:
        ```python
        from object_mother_pattern import IntegerMother

        number = IntegerMother.out_of_range(min=-10, max=10, range=20)
        print(number)
        # >>> -163
        ```
        """
        if type(min) is not int:
            raise TypeError('IntegerMother min value must be an integer.')

        if type(max) is not int:
            raise TypeError('IntegerMother max value must be an integer.')

        if min > max:
            raise ValueError('IntegerMother min value must be less than or equal to max value.')

        if type(range) is not int:
            raise TypeError('IntegerMother range must be an integer.')

        if range <= 0:
            raise ValueError('IntegerMother range must be greater than 0.')

        return choice(  # noqa: S311
            seq=[
                randint(a=min - range, b=min - 1),  # noqa: S311
                randint(a=max + 1, b=max + range),  # noqa: S311
            ]
        )
