"""
Abstract base class for typed object mothers.
"""

from sys import version_info

if version_info >= (3, 12):
    from typing import override  # pragma: no cover
else:
    from typing_extensions import override  # pragma: no cover


from abc import ABC, abstractmethod
from datetime import date, datetime
from inspect import isclass
from random import choice
from typing import Any, Generic, Iterable, TypeVar, get_args, get_origin
from uuid import UUID, uuid4

from faker import Faker
from faker.providers import user_agent

try:
    from value_object_pattern import ValueObject

    HAS_VALUE_OBJECTS = True

except ImportError:
    HAS_VALUE_OBJECTS = False


T = TypeVar('T')


class BaseMother(ABC, Generic[T]):  # noqa: UP046
    """
    Define the common contract for object mother classes.

    Concrete mothers subclass `BaseMother[T]`, implement `create()`, and usually support two paths: return an explicit
    `value` after validation, or generate a random value that satisfies the mother invariants. The base class records
    the declared target type so test suites can ask a mother for a value of a different type through `invalid_type()`.

    ***This class is abstract and should not be instantiated directly***.

    Example:
    ```python
    from random import randint

    from object_mother_pattern.models import BaseMother


    class PositiveIntegerMother(BaseMother[int]):
        @classmethod
        def create(cls, *, value: int | None = None) -> int:
            if value is not None:
                if type(value) is not int:
                    raise TypeError('PositiveIntegerMother value must be an integer.')

                if value <= 0:
                    raise ValueError('PositiveIntegerMother value must be positive.')

                return value

            return randint(a=1, b=100)
    ```
    """

    _type: type

    @override
    def __init_subclass__(cls, **kwargs: Any) -> None:
        """
        Capture and validate the target type declared by a concrete mother.

        Subclasses must be parameterized as `BaseMother[T]`. If `T` is a `value_object_pattern.ValueObject` subclass,
        the inner value-object type is recorded so invalid-type generation excludes the value type rather than the
        wrapper class.

        Args:
            **kwargs: Keyword arguments forwarded to the parent class hook.

        Raises:
            TypeError: If the class parameter is not a type-like value.
            TypeError: If the subclass is not parameterized with `BaseMother[T]`.
        """
        super().__init_subclass__(**kwargs)

        for base in getattr(cls, '__orig_bases__', ()):
            if get_origin(tp=base) is BaseMother:
                mother_type, *_ = get_args(tp=base)

                if not isclass(object=mother_type) and get_origin(tp=mother_type) is None:
                    raise TypeError(f'BaseMother[...] <<<{mother_type}>>> must be a type. Got <<<{type(mother_type).__name__}>>> type.')  # noqa: E501  # fmt: skip

                if HAS_VALUE_OBJECTS and isclass(object=mother_type) and issubclass(mother_type, ValueObject):
                    mother_type = mother_type.type()

                cls._type = mother_type
                return

        raise TypeError('BaseMother must be parameterized, e.g. "class BooleanMother(BaseMother[bool])".')

    @classmethod
    def _random(cls) -> Faker:
        """
        Build a Faker instance configured for this package.

        Returns:
            Faker: Faker instance with the package's additional providers.
        """
        faker = Faker(use_weighting=False)
        faker.add_provider(user_agent)

        return faker

    @classmethod
    @abstractmethod
    def create(cls, *, value: Any | None = None) -> T:
        """
        Create a value of the mother's target type.

        Concrete mothers should validate and return a provided `value` when supplied. Without `value`, they should
        generate a random value that satisfies the same invariants.

        Args:
            value: Optional explicit value to validate and return.

        Returns:
            T: Valid value for the concrete mother.
        """

    @classmethod
    def invalid_type(cls, *, remove_types: Iterable[type[Any]] | None = None) -> Any:  # noqa: C901
        """
        Generate a value with a type that should be invalid for this mother.

        This helper is intended for negative-path tests. It automatically removes the concrete mother's target type when
        available, then randomly selects from common primitive, collection, date, and UUID types.

        Args:
            remove_types: Additional candidate types to exclude from the generated invalid values.

        Returns:
            Any: Value whose type differs from the excluded types.
        """
        faker = Faker()

        remove_types = set() if remove_types is None else set(remove_types)
        if hasattr(cls, '_type'):
            remove_types.add(cls._type)

        types: list[Any] = []
        if int not in remove_types:
            types.append(faker.pyint())

        if float not in remove_types:
            types.append(faker.pyfloat())

        if bool not in remove_types:
            types.append(faker.pybool())

        if str not in remove_types:
            types.append(faker.pystr())

        if bytes not in remove_types:
            types.append(faker.pystr().encode())

        if list not in remove_types:
            types.append(faker.pylist())  #  pragma: no cover

        if set not in remove_types:
            types.append(faker.pyset())  #  pragma: no cover

        if tuple not in remove_types:
            types.append(faker.pytuple())  #  pragma: no cover

        if dict not in remove_types:
            types.append(faker.pydict())  #  pragma: no cover

        if datetime not in remove_types:
            types.append(faker.date_time())

        if date not in remove_types:
            types.append(faker.date_object())

        if UUID not in remove_types:
            types.append(uuid4())

        return choice(seq=types)  # noqa: S311
