from typing import List
from sorted_arrays_merge import merge_sorted_arrays
from test_framework import generic_test

# Average running time:    1 ms
# Median running time:     1 ms
def sort_k_increasing_decreasing_array(A: List[int]) -> List[int]:
    if len(A) < 2:
        return A

    switch_indices, subarrays = [], []
    for idx in range(1, len(A)):
        prev, curr = A[idx-1], A[idx]
        if (len(switch_indices) % 2 == 0 and curr < prev) or (len(switch_indices) % 2 == 1 and curr > prev):
            switch_indices.append(idx)
            continue

    if len(switch_indices) == 0:
        return A

    subarrays.append(A[:switch_indices[0]])
    for idx in range(1, len(switch_indices)):
        prev, curr = switch_indices[idx-1], switch_indices[idx]
        temp = A[prev:curr]
        if idx % 2 == 1:
            temp = list(reversed(temp))
        subarrays.append(temp)
    temp = A[switch_indices[len(switch_indices)-1]:]
    if len(switch_indices) % 2 == 1:
        temp = list(reversed(temp))
    subarrays.append(temp)
    return merge_sorted_arrays(subarrays)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sort_increasing_decreasing_array.py',
                                       'sort_increasing_decreasing_array.tsv',
                                       sort_k_increasing_decreasing_array))
