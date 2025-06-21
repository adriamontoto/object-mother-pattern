"""
BooleanMother module.
"""

from sys import version_info

if version_info >= (3, 12):
    from typing import override  # pragma: no cover
else:
    from typing_extensions import override  # pragma: no cover

from random import uniform

from object_mother_pattern.models import BaseMother


class BooleanMother(BaseMother[bool]):
    """
    BooleanMother class is responsible for creating random boolean values.

    Example:
    ```python
    from object_mother_pattern import BooleanMother

    boolean = BooleanMother.create()
    print(boolean)
    # >>> True
    ```
    """

    @classmethod
    @override
    def create(cls, *, value: bool | None = None, probability_true: float = 0.5) -> bool:
        """
        Create a boolean value. If a specific boolean value is provided via `value`, it is returned after validation.
        Otherwise, a random boolean is generated with a probability of returning True defined by `probability_true`.

        Args:
            value (bool | None, optional): A specific boolean value to return. Defaults to None.
            probability_true (float, optional): Probability of returning True. Must be >= 0.0 and <= 1.0. Defaults to
            0.5.

        Raises:
            TypeError: If the provided `value` is not a boolean.
            TypeError: If `probability_true` is not a float.
            ValueError: If `probability_true` is less than 0.0.
            ValueError: If `probability_true` is more than 1.0.

        Returns:
            bool: A randomly generated boolean value.

        Example:
        ```python
        from object_mother_pattern import BooleanMother

        boolean = BooleanMother.create()
        print(boolean)
        # >>> True
        ```
        """
        if value is not None:
            if type(value) is not bool:
                raise TypeError('BooleanMother value must be a boolean.')

            return value

        if type(probability_true) is not float:
            raise TypeError('BooleanMother probability_true must be a float.')

        if probability_true < 0.0:
            raise ValueError('BooleanMother probability_true must be greater than or equal to 0.0.')

        if probability_true > 1.0:
            raise ValueError('BooleanMother probability_true must be less than or equal to 1.0.')

        return uniform(a=0.0, b=1.0) < probability_true  # noqa: S311

    @classmethod
    def true(cls) -> bool:
        """
        Return a true boolean value.

        Returns:
            bool: True boolean value.

        Example:
        ```python
        from object_mother_pattern import BooleanMother

        boolean = BooleanMother.true()
        print(boolean)
        # >>> True
        ```
        """
        return True

    @classmethod
    def false(cls) -> bool:
        """
        Return a false boolean value.

        Returns:
            bool: False boolean value.

        Example:
        ```python
        from object_mother_pattern import BooleanMother

        boolean = BooleanMother.false()
        print(boolean)
        # >>> False
        ```
        """
        return False
