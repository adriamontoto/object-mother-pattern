"""
This module describes several alphabets.
"""

SPECIAL_CHARS = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'  # some chars can break csv files (, ; |)
SUPER_SPECIAL_CHARS = ' £çÇñÑ¡¿'  # some chars are not accepted by some websites (contains space)

ALPHABET_LOWERCASE_BASIC = 'abcdefghijklmnopqrstuvwxyz'
ALPHABET_UPPERCASE_BASIC = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
DIGITS_BASIC = '0123456789'
ALPHABET_BASIC = ALPHABET_LOWERCASE_BASIC + ALPHABET_UPPERCASE_BASIC + DIGITS_BASIC
