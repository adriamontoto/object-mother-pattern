"""
IntegerMother module.
"""

from sys import version_info

if version_info >= (3, 12):
    from typing import override  # pragma: no cover
else:
    from typing_extensions import override  # pragma: no cover

from object_mother_pattern.mothers.base_mother import BaseMother


class IntegerMother(BaseMother[int]):
    """
    IntegerMother class.

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
        Create a random integer within the provided range. If a value is provided, it will be returned.

        Args:
            value (int | None, optional): Integer value. Defaults to None.
            min (int, optional): Minimum integer value. Defaults to -100.
            max (int, optional): Maximum integer value. Defaults to 100.

        Raises:
            TypeError: If value is not an integer.
            TypeError: If min is not an integer.
            TypeError: If max is not an integer.
            ValueError: If min is greater than max.

        Returns:
            int: Random integer.

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

        return cls._random().pyint(min_value=min, max_value=max)

    @classmethod
    def positive(cls, *, max: int = 100) -> int:
        """
        Create a random positive integer, greater than 0.

        Args:
            max (int, optional): Maximum positive integer value. Defaults to 100.

        Raises:
            ValueError: If max is less than 1.

        Returns:
            int: Random positive integer.

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
        Create a random negative integer, less than 0.

        Args:
            min (int, optional): Minimum negative integer value. Defaults to -100.

        Raises:
            TypeError: If min is not an integer.
            ValueError: If min is greater than -1.

        Returns:
            int: Random negative integer.

        Example:
        ```python
        from object_mother_pattern.mothers import IntegerMother

        negative = IntegerMother.negative(min=-61)
        print(negative)
        # >>> -45
        ```
        """
        return cls.create(min=min, max=-1)
