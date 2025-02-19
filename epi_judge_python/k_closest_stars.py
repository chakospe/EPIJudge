import functools
import heapq
import math
from typing import Iterator, List
import itertools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


class Star:
    def __init__(self, x: float, y: float, z: float) -> None:
        self.x, self.y, self.z = x, y, z

    @property
    def distance(self) -> float:
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def __lt__(self, rhs: 'Star') -> bool:
        return self.distance < rhs.distance

    def __repr__(self):
        return str(self.distance)

    def __str__(self):
        return self.__repr__()

    def __eq__(self, rhs):
        return math.isclose(self.distance, rhs.distance)


# Average running time:  248 us
# Median running time:    48 us
def find_closest_k_stars(stars: Iterator[Star], k: int) -> List[Star]:
    max_heap, stars = [], iter(stars)
    for x in itertools.islice(stars, k):
        heapq.heappush(max_heap, (-x.distance, x))
    for x in stars:
        if -x.distance > max_heap[0][0]:
            heapq.heapreplace(max_heap, (-x.distance, x))
    return [s[1] for s in max_heap]


# Average running time:  404 us
# Median running time:    51 us
# def find_closest_k_stars(stars: Iterator[Star], k: int) -> List[Star]:
#     max_heap = []
#     for star in stars:
#         heapq.heappush(max_heap, (-star.distance, star))
#         while len(max_heap) >= k + 1:
#             heapq.heappop(max_heap)
#     return [s[1] for s in max_heap]



def comp(expected_output, output):
    if len(output) != len(expected_output):
        return False
    return all(
        math.isclose(s.distance, d)
        for s, d in zip(sorted(output), expected_output))


@enable_executor_hook
def find_closest_k_stars_wrapper(executor, stars, k):
    stars = [Star(*a) for a in stars]
    return executor.run(functools.partial(find_closest_k_stars, iter(stars),
                                          k))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('k_closest_stars.py',
                                       'k_closest_stars.tsv',
                                       find_closest_k_stars_wrapper, comp))
