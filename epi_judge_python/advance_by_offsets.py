from typing import List

from test_framework import generic_test


def can_reach_end(A: List[int]) -> bool:
    far, last = 0, len(A) - 1
    i = 0
    while i <= far and far < last:
        far = max(far, i + A[i])
        i += 1
    return far >= last

# avg/med: 35 us/4 us
# def can_reach_end(A: List[int]) -> bool:
#     far, last = 0, len(A) - 1
#     i = 0
#     while i <= far and far < last:
#         far = max(far, i + A[i])
#         i += 1
#     return far >= last


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('advance_by_offsets.py',
                                       'advance_by_offsets.tsv',
                                       can_reach_end))
