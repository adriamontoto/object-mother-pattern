"""
Test module for the BaseMother class.
"""

from importlib import util as importlib_util
from pathlib import Path
from re import escape
from types import ModuleType
from typing import Final

from pytest import mark, raises as assert_raises

from object_mother_pattern.models import BaseMother

PROJECT_ROOT: Final[Path] = Path(__file__).resolve().parents[2]
BASE_MOTHER_PATH: Final[Path] = PROJECT_ROOT / 'object_mother_pattern' / 'models' / 'base_mother.py'


def _load_base_mother(module_name: str, *, block_value_object: bool = False) -> ModuleType:
    """
    Load ``base_mother.py`` under an isolated module name.

    Args:
        module_name (str): Name to register the module under ``sys.modules``.
        block_value_object (bool): When True, simulate ``ImportError`` for ``value_object_pattern``.

    Returns:
        ModuleType: Loaded ``base_mother`` module instance.
    """
    import builtins
    import sys

    sys.modules.pop(module_name, None)

    original_import = builtins.__import__

    def fake_import(name: str, *args: object, **kwargs: object):
        if block_value_object and name == 'value_object_pattern':
            raise ImportError
        return original_import(name, *args, **kwargs)

    builtins.__import__ = fake_import
    try:
        spec = importlib_util.spec_from_file_location(module_name, BASE_MOTHER_PATH)
        assert spec is not None and spec.loader is not None

        module = importlib_util.module_from_spec(spec)
        sys.modules[module_name] = module
        spec.loader.exec_module(module)

        return module
    finally:
        builtins.__import__ = original_import


@mark.unit_testing
def test_base_mother_cannot_be_instantiated() -> None:
    """
    Test BaseMother cannot be instantiated.
    """
    with assert_raises(
        expected_exception=TypeError,
        match=r"Can't instantiate abstract class BaseMother with.*",
    ):
        BaseMother()  # type: ignore[abstract]


@mark.unit_testing
def test_base_mother_init_with_invalid_type() -> None:
    """
    Test BaseMother initialization with invalid type.
    """
    value = BaseMother.invalid_type(remove_types=(list, set, tuple, dict))

    with assert_raises(
        expected_exception=TypeError,
        match=r'BaseMother\[.*\] <<<.*>>> must be a type. Got <<<.*>>> type.',
    ):

        class BooleanMother(BaseMother[value]):  # type: ignore[valid-type]
            pass


@mark.unit_testing
def test_base_mother_init_without_parameterization() -> None:
    """
    Test BaseMother initialization without parameterization.
    """
    with assert_raises(
        expected_exception=TypeError,
        match=escape(pattern='BaseMother must be parameterized, e.g. "class BooleanMother(BaseMother[bool])".'),
    ):

        class BooleanMother(BaseMother):  # type: ignore[type-arg]
            pass


@mark.unit_testing
def test_base_mother_without_value_object_dependency() -> None:
    """
    Simulate missing value_object_pattern to cover the ImportError branch.
    """
    module = _load_base_mother('base_mother_no_vo', block_value_object=True)

    assert module.HAS_VALUE_OBJECTS is False

    value = module.BaseMother.invalid_type(remove_types=(list, set, tuple, dict))

    with assert_raises(TypeError, match=r'BaseMother\[.*\] <<<.*>>> must be a type. Got <<<.*>>> type.'):

        class BooleanMother(module.BaseMother[value]):  # type: ignore[valid-type]
            pass


@mark.unit_testing
def test_base_mother_with_value_object() -> None:
    """
    Test BaseMother handles ValueObject subclasses by using the inner type.
    """
    module = _load_base_mother('base_mother_with_vo')

    from value_object_pattern import ValueObject  # imported after helper to use real package

    class IntegerValueObject(ValueObject[int]):  # noqa: D401 - simple wrapper
        pass

    class IntegerMother(module.BaseMother[IntegerValueObject]):
        @classmethod
        def create(cls, *, value: int | None = None) -> IntegerValueObject:
            return IntegerValueObject(value=value if value is not None else 7)

    assert module.HAS_VALUE_OBJECTS is True
    assert IntegerMother._type is int
    result = IntegerMother.create()
    assert isinstance(result, IntegerValueObject)
    assert result.value == 7
