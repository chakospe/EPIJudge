from typing import List

from test_framework import generic_test


def next_permutation(perm: List[int]) -> List[int]:
    inversion_point = len(perm) - 2
    while inversion_point >= 0 and perm[inversion_point] >= perm[inversion_point + 1]:
        inversion_point -= 1
    if inversion_point == -1:
        return []
    for i in reversed(range(inversion_point + 1, len(perm))):
        if perm[i] > perm[inversion_point]:
            perm[inversion_point], perm[i] = perm[i], perm[inversion_point]
            break
    perm[(inversion_point + 1):] = reversed(perm[(inversion_point + 1):])
    return perm

# avg/med: 3 us/2 us
# def next_permutation(perm: List[int]) -> List[int]:
#     inversion_point = len(perm) - 2
#     while inversion_point >= 0 and perm[inversion_point] >= perm[inversion_point + 1]:
#         inversion_point -= 1
#     if inversion_point == -1:
#         return []
#     for i in reversed(range(inversion_point + 1, len(perm))):
#         if perm[i] > perm[inversion_point]:
#             perm[inversion_point], perm[i] = perm[i], perm[inversion_point]
#             break
#     perm[(inversion_point + 1):] = reversed(perm[(inversion_point + 1):])
#     return perm



# avg/med: 4 us/4 us
# def next_permutation(perm: List[int]) -> List[int]:
#     if len(perm) == 1:
#         return []
#     l = 1
#     for i in range(len(perm) - 1, 0, -1):
#         if perm[i] > perm[i - 1]:
#             break
#         l += 1
#     if len(perm) == l:
#         return []
#     for i in range(l):
#         if perm[len(perm) - 1 - i] > perm[len(perm) - 1 - l]:
#             temp = perm[len(perm) - 1 - i]
#             perm[len(perm) - 1 - i] = perm[len(perm) - 1 - l]
#             perm[len(perm) - 1 - l] = temp
#             break
#     prefix = perm[:(len(perm) - l)]
#     suffix = perm[(len(perm) - l):]
#     return prefix + list(reversed(suffix))



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('next_permutation.py',
                                       'next_permutation.tsv',
                                       next_permutation))
