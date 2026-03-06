"""
Internal helpers for credit card generation.
"""

from random import choice, randint


def _generate_luhn_number(*, prefix: str, length: int) -> str:
    """
    Generate a Luhn-valid numeric string of the requested length with the given prefix.
    """
    body_length = length - len(prefix) - 1
    body = ''.join(str(randint(0, 9)) for _ in range(body_length))  # noqa: S311
    partial = f'{prefix}{body}'
    check_digit = _luhn_check_digit(partial)

    return f'{partial}{check_digit}'


def _luhn_check_digit(number_without_check: str) -> int:
    """
    Compute the Luhn check digit for a numeric string that is missing the final digit.
    """
    digits = [int(char) for char in number_without_check]
    # Starting from the right, double every second digit
    for idx in range(len(digits) - 1, -1, -2):
        doubled = digits[idx] * 2
        digits[idx] = doubled - 9 if doubled > 9 else doubled

    total = sum(digits)
    return (10 - (total % 10)) % 10


def _pick_prefix(prefixes: tuple[str, ...]) -> str:
    """
    Select a random prefix from the provided tuple.
    """
    return choice(seq=prefixes)  # noqa: S311
