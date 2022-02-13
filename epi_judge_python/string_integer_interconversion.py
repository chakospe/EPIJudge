from test_framework import generic_test
from test_framework.test_failure import TestFailure


def int_to_string(x: int) -> str:
    if x == 0:
        return '0'
    is_negative = x < 0
    x = abs(x)
    s = []
    while x > 0:
        s.append(chr(ord('0') + x % 10))
        x //= 10
    return ('-' if is_negative else '') + ''.join(reversed(s))


def string_to_int(s: str) -> int:
    scalar = -1 if s[0] == '-' else 1
    s = s[(s[0] in '-+'):]
    running_sum, d = 0, 1
    for i in range(len(s)):
        running_sum += d * ('0123456789'.index(s[~i]))
        d *= 10
    return scalar * running_sum



def wrapper(x, s):
    if int(int_to_string(x)) != x:
        raise TestFailure('Int to string conversion failed')
    if string_to_int(s) != x:
        raise TestFailure('String to int conversion failed')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('string_integer_interconversion.py',
                                       'string_integer_interconversion.tsv',
                                       wrapper))
