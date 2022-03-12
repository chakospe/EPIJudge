import functools
import itertools

from test_framework import generic_test
from test_framework.test_failure import TestFailure


def decoding(s: str) -> str:
    count, result = 0, []
    for i in s:
        if i.isdigit():
            count = 10 * count + int(i)
        else:
            result.append(count * i)
            count = 0
    return ''.join(result)


def encoding(s: str) -> str:
    return ''.join(
        [
            str(len(list(group))) + key
            for key, group in itertools.groupby(s)
        ]
    )


# avg/med: 88 us/32 us
# def decoding(s: str) -> str:
#     count, result = 0, []
#     for i in s:
#         if i.isdigit():
#             count = 10 * count + int(i)
#         else:
#             result.append(count * i)
#             count = 0
#     return ''.join(result)
#
#
# def encoding(s: str) -> str:
#     return ''.join(
#         [
#             str(len(list(group))) + key
#             for key, group in itertools.groupby(s)
#         ]
#     )


def rle_tester(encoded, decoded):
    if decoding(encoded) != decoded:
        raise TestFailure('Decoding failed')
    if encoding(decoded) != encoded:
        raise TestFailure('Encoding failed')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('run_length_compression.py',
                                       'run_length_compression.tsv',
                                       rle_tester))
