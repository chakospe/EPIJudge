from typing import List

from test_framework import generic_test


def plus_one(A: List[int]) -> List[int]:
    r = A[::-1]
    r[0] += 1
    if r[0] >= 10:
        r[0] = 0
        for i in range(1, len(r)):
            r[i] += 1
            if r[i] < 10:
                break
            else:
                r[i] = 0
        if r[-1] == 0:
            r.insert(len(r), 1)
    return r[::-1]

# avg/med: 1 us/1 us
# def plus_one(A: List[int]) -> List[int]:
#     r = A[::-1]
#     r[0] += 1
#     if r[0] >= 10:
#         r[0] = 0
#         for i in range(1, len(r)):
#             r[i] += 1
#             if r[i] < 10:
#                 break
#             else:
#                 r[i] = 0
#         if r[-1] == 0:
#             r.insert(len(r), 1)
#     return r[::-1]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_as_array_increment.py',
                                       'int_as_array_increment.tsv', plus_one))
