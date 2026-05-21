from random import randint


def generate_luhn_number(*, prefix: str, length: int) -> str:
    """
    Generate a Luhn-valid numeric string of the requested length with the given prefix.

    Args:
        prefix (str): The starting digits of the number.
        length (int): The total length of the number to generate, including the prefix and check digit.

    Returns:
        str: A Luhn-valid numeric string of the specified length.
    """
    body_length = length - len(prefix) - 1
    body = ''.join(str(randint(0, 9)) for _ in range(body_length))  # noqa: S311
    partial = f'{prefix}{body}'
    check_digit = luhn_check_digit(number_without_check=partial)

    return f'{partial}{check_digit}'


def luhn_check_digit(*, number_without_check: str) -> int:
    """
    Compute the Luhn check digit for a numeric string that is missing the final digit.

    Args:
        number_without_check (str): The numeric string for which to compute the check digit, excluding the final check
        digit.

    Returns:
        int: The Luhn check digit that should be appended to the input string to make it Luhn-valid.
    """
    digits = [int(char) for char in number_without_check]
    for idx in range(len(digits) - 1, -1, -2):
        doubled = digits[idx] * 2
        digits[idx] = doubled - 9 if doubled > 9 else doubled

    total = sum(digits)
    return (10 - (total % 10)) % 10
