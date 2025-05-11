"""
Test module for the BtcWalletMother class.
"""

from pytest import mark, raises as assert_raises

from object_mother_pattern.mothers import IntegerMother, StringMother
from object_mother_pattern.mothers.money.cryptocurrencies import BtcWalletMother
from object_mother_pattern.mothers.money.cryptocurrencies.btc_wallet_mother import BtcWalletCase


@mark.unit_testing
def test_btc_wallet_mother_happy_path() -> None:
    """
    Test BtcWalletMother happy path.
    """
    value = BtcWalletMother.create()

    assert type(value) is str
    assert len(value.split()) == 12


@mark.unit_testing
def test_btc_wallet_mother_value() -> None:
    """
    Test BtcWalletMother create method with value.
    """
    value = BtcWalletMother.create()

    assert BtcWalletMother.create(value=value) == value


@mark.unit_testing
def test_btc_wallet_mother_random_word_number() -> None:
    """
    Test BtcWalletMother create method with random word number.
    """
    word_number = IntegerMother.positive()
    value = BtcWalletMother.create(word_number=word_number)

    assert type(value) is str
    assert len(value.split()) == word_number


@mark.unit_testing
def test_btc_wallet_mother_invalid_value_type() -> None:
    """
    Test BtcWalletMother create method with invalid value type.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='BtcWalletMother value must be a string.',
    ):
        BtcWalletMother.create(value=BtcWalletMother.invalid_type())


@mark.unit_testing
def test_btc_wallet_mother_invalid_word_number_type() -> None:
    """
    Test BtcWalletMother create method with invalid word_number type.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='BtcWalletMother word_number must be an integer.',
    ):
        BtcWalletMother.create(word_number=IntegerMother.invalid_type(remove_types=(float,)))


@mark.unit_testing
def test_btc_wallet_mother_invalid_word_number_value() -> None:
    """
    Test BtcWalletMother create method with invalid word_number value.
    """
    with assert_raises(
        expected_exception=ValueError,
        match='BtcWalletMother word_number must be greater than or equal to 1.',
    ):
        BtcWalletMother.create(word_number=IntegerMother.create(min=-100, max=0))


@mark.unit_testing
def test_btc_wallet_mother_invalid_type() -> None:
    """
    Test BtcWalletMother create method with invalid type.
    """
    assert type(BtcWalletMother.invalid_type()) is not str


@mark.unit_testing
def test_btc_wallet_mother_invalid_value() -> None:
    """
    Test BtcWalletMother invalid_value method.
    """
    value = BtcWalletMother.invalid_value()

    assert type(value) is str
    assert not value.isprintable()


@mark.unit_testing
def test_btc_wallet_mother_lowercase_case() -> None:
    """
    Test BtcWalletMother create method with lowercase case.
    """
    value = BtcWalletMother.create(wallet_case=BtcWalletCase.LOWERCASE)

    assert value.islower()


@mark.unit_testing
def test_btc_wallet_mother_uppercase_case() -> None:
    """
    Test BtcWalletMother create method with uppercase case.
    """
    value = BtcWalletMother.create(wallet_case=BtcWalletCase.UPPERCASE)

    assert value.isupper()


@mark.unit_testing
def test_btc_wallet_mother_mixed_case() -> None:
    """
    Test BtcWalletMother create method with mixed case.
    """
    value = BtcWalletMother.create(wallet_case=BtcWalletCase.MIXED)

    assert any(char.islower() or char.isupper() for char in value)


@mark.unit_testing
def test_btc_wallet_mother_invalid_case() -> None:
    """
    Test BtcWalletMother create method with invalid case.
    """
    with assert_raises(
        expected_exception=TypeError,
        match='BtcWalletMother wallet_case must be a BtcWalletCase.',
    ):
        BtcWalletMother.create(wallet_case=StringMother.invalid_type())
