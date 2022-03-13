import collections
from typing import Iterator, List

from test_framework import generic_test


def examine_buildings_with_sunset(sequence: Iterator[int]) -> List[int]:
    BuildingWithHeight = collections.namedtuple('BuildingWithHeight', ('id', 'height'))

    l: List[BuildingWithHeight] = []
    for idx, height in enumerate(sequence):
        while l and l[-1].height <= height:
            l.pop()
        l.append(BuildingWithHeight(idx, height))
    return [i.id for i in reversed(l)]


def examine_buildings_with_sunset_wrapper(sequence):
    return examine_buildings_with_sunset(iter(sequence))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sunset_view.py', 'sunset_view.tsv',
                                       examine_buildings_with_sunset))
