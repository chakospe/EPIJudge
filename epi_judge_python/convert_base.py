from test_framework import generic_test
import string
import functools

def to_base10(s: str, b: int) -> int:
    is_negative = s[0] == '-'
    scalar = -1 if is_negative else 1
    s = s[is_negative:]
    f = lambda x, c: x * b + string.hexdigits.index(c.lower())
    return scalar * functools.reduce(f, s, 0)

def convert_base(num_as_string: str, b1: int, b2: int) -> str:
    x = to_base10(num_as_string, b1)
    if x == 0:
        return '0'
    is_negative = x < 0
    prefix = '-' if is_negative else ''
    x = abs(x)
    s = []
    while x > 0:
        s.append(string.hexdigits[x % b2])
        x //= b2
    return prefix + ''.join(reversed(s)).upper()


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('convert_base.py', 'convert_base.tsv',
                                       convert_base))
