import heapq
from typing import List, Tuple

from test_framework import generic_test


def merge_sorted_arrays(sorted_arrays: List[List[int]]) -> List[int]:
    min_heap: List[Tuple[int, int]]=[]
    sorted_arrays_iter = [iter(x) for x in sorted_arrays]

    for i, it in enumerate(sorted_arrays_iter):
        first_element = next(it, None)
        if first_element is not None:
            heapq.heappush(min_heap, (first_element, i))

    result = []
    while min_heap:
        smallest_entry, smallest_array_i = heapq.heappop(min_heap)
        result.append(smallest_entry)
        smallest_array_iter = sorted_arrays_iter[smallest_array_i]
        next_element = next(smallest_array_iter, None)
        if next_element is not None:
            heapq.heappush(min_heap, (next_element, smallest_array_i))

    return result


# Average running time:  726 us
# Median running time:   229 us
# def merge_sorted_arrays(sorted_arrays: List[List[int]]) -> List[int]:
#     min_heap: List[Tuple[int, int]]=[]
#     sorted_arrays_iter = [iter(x) for x in sorted_arrays]
#
#     for i, it in enumerate(sorted_arrays_iter):
#         first_element = next(it, None)
#         if first_element is not None:
#             heapq.heappush(min_heap, (first_element, i))
#
#     result = []
#     while min_heap:
#         smallest_entry, smallest_array_i = heapq.heappop(min_heap)
#         result.append(smallest_entry)
#         smallest_array_iter = sorted_arrays_iter[smallest_array_i]
#         next_element = next(smallest_array_iter, None)
#         if next_element is not None:
#             heapq.heappush(min_heap, (next_element, smallest_array_i))
#
#     return result

# Average running time:  692 us
# Median running time:   174 us
# def merge_sorted_arrays(sorted_arrays: List[List[int]]) -> List[int]:
#     return list(heapq.merge(*sorted_arrays))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sorted_arrays_merge.py',
                                       'sorted_arrays_merge.tsv',
                                       merge_sorted_arrays))
