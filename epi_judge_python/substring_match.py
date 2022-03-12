import functools

from test_framework import generic_test


def rabin_karp(t: str, s: str) -> int:
    if len(t) < len(s):
        return -1
    base = 26
    power_s = base ** max(0, len(s) - 1)
    hash_s = functools.reduce(lambda h, c: h * base + ord(c), s, 0)
    hash_t = functools.reduce(lambda h, c: h * base + ord(c), t[:len(s)], 0)
    for i in range(len(s), len(t)):
        if hash_t == hash_s and t[i - len(s):i] == s:
            return i - len(s)
        hash_t -= power_s * ord(t[i - len(s)])
        hash_t = base * hash_t + ord(t[i])
    if t[-len(s):] == s:
        return len(t) - len(s)
    return -1


# avg/med: 37 us/9 us
# def rabin_karp(t: str, s: str) -> int:
#     if len(t) < len(s):
#         return -1
#     base = 26
#     power_s = base ** max(0, len(s) - 1)
#     hash_s = functools.reduce(lambda h, c: h * base + ord(c), s, 0)
#     hash_t = functools.reduce(lambda h, c: h * base + ord(c), t[:len(s)], 0)
#     for i in range(len(s), len(t)):
#         if hash_t == hash_s and t[i - len(s):i] == s:
#             return i - len(s)
#         hash_t -= power_s * ord(t[i - len(s)])
#         hash_t = base * hash_t + ord(t[i])
#     if t[-len(s):] == s:
#         return len(t) - len(s)
#     return -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('substring_match.py',
                                       'substring_match.tsv', rabin_karp))
