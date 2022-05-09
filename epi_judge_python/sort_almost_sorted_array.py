import heapq
import itertools
from typing import Iterator, List

from test_framework import generic_test

# Average running time:  100 us
# Median running time:     7 us
def sort_approximately_sorted_array(sequence: Iterator[int],
                                    k: int) -> List[int]:
    sequence = iter(sequence)
    min_heap, result = [], []
    for x in itertools.islice(sequence, k):
        heapq.heappush(min_heap, x)
    for x in sequence:
        result.append(heapq.heappushpop(min_heap, x))
    while min_heap:
        result.append(heapq.heappop(min_heap))
    return result


def sort_approximately_sorted_array_wrapper(sequence, k):
    return sort_approximately_sorted_array(iter(sequence), k)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'sort_almost_sorted_array.py', 'sort_almost_sorted_array.tsv',
            sort_approximately_sorted_array_wrapper))
