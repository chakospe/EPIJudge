import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


# Returns the number of valid entries after deletion.
def delete_duplicates(A: List[int]) -> int:
    num_valid, prev, prev_idx = 0, float('inf'), -1
    for i in range(len(A)):
        if A[i] != prev:
            num_valid += 1
            prev = A[i]
            A[prev_idx + 1] = A[i]
            prev_idx += 1
    A = A[:(1 + num_valid)]
    return num_valid

# avg/med: 14 us/5 us
# def delete_duplicates(A: List[int]) -> int:
#     num_valid, prev, prev_idx = 0, float('inf'), -1
#     for i in range(len(A)):
#         if A[i] != prev:
#             num_valid += 1
#             prev = A[i]
#             A[prev_idx + 1] = A[i]
#             prev_idx += 1
#     A = A[:(1 + num_valid)]
#     return num_valid


@enable_executor_hook
def delete_duplicates_wrapper(executor, A):
    idx = executor.run(functools.partial(delete_duplicates, A))
    return A[:idx]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sorted_array_remove_dups.py',
                                       'sorted_array_remove_dups.tsv',
                                       delete_duplicates_wrapper))
