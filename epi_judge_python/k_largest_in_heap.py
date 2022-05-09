from typing import List
import heapq

from test_framework import generic_test, test_utils

# Average running time:   55 us
# Median running time:    12 us
def k_largest_in_binary_heap(A: List[int], k: int) -> List[int]:
    if k <= 0:
        return []
    max_heap, result = [], []
    max_heap.append((-A[0], 0))
    for _ in range(k):
        val, idx = heapq.heappop(max_heap)
        result.append(-val)
        left_child_idx = 2 * idx + 1
        right_child_idx = 2 * idx + 2
        if left_child_idx < len(A):
            heapq.heappush(max_heap, (-A[left_child_idx], left_child_idx))
        if right_child_idx < len(A):
            heapq.heappush(max_heap, (-A[right_child_idx], right_child_idx))
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'k_largest_in_heap.py',
            'k_largest_in_heap.tsv',
            k_largest_in_binary_heap,
            comparator=test_utils.unordered_compare))
