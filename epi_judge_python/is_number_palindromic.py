import math

from test_framework import generic_test


def is_palindrome_number(x: int) -> bool:
    if x <= 0:
        return x == 0
    num_digits = 1 + math.floor(math.log10(x))
    for i in range(num_digits // 2):
        lsd = x % 10
        msd = x // (10 ** (num_digits - 1))
        if lsd != msd:
            return False
        x %= (10 ** (num_digits - 1))
        x //= 10
        num_digits -= 2
    return True

# avg/med: 3 us/2 us
# def is_palindrome_number(x: int) -> bool:
#     if x <= 0:
#         return x == 0
#     num_digits = 1 + math.floor(math.log10(x))
#     for i in range(num_digits // 2):
#         lsd = x % 10
#         msd = x // (10 ** (num_digits - 1))
#         if lsd != msd:
#             return False
#         x %= (10 ** (num_digits - 1))
#         x //= 10
#         num_digits -= 2
#     return True

# avg/med: 2 us/2 us
# def is_palindrome_number(x: int) -> bool:
#     if x <= 0:
#         return x == 0
#     num_digits = 1 + math.floor(math.log10(x))
#     msd_mask = 10 ** (num_digits - 1)
#     for i in range(num_digits // 2):
#         if x // msd_mask != x % 10:
#             return False
#         x %= msd_mask
#         x //= 10
#         msd_mask //= 100
#     return True

# avg/med: 2 us/1 us
# def is_palindrome_number(x: int) -> bool:
#     if x < 0:
#         return False
#     s = str(x)
#     l = len(s)
#     for i in range(l // 2):
#         if s[i] != s[l - 1 - i]:
#             return False
#     return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_number_palindromic.py',
                                       'is_number_palindromic.tsv',
                                       is_palindrome_number))
