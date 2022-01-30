import collections

from test_framework import generic_test
from test_framework.test_failure import PropertyName

Rect = collections.namedtuple('Rect', ('x', 'y', 'width', 'height'))


def intersect_rectangle(r1: Rect, r2: Rect) -> Rect:
    x = max(r1[0], r2[0])
    y = max(r1[1], r2[1])
    width = min(r1[0] + r1[2], r2[0] + r2[2]) - x
    height = min(r1[1] + r1[3], r2[1] + r2[3]) - y
    if width < 0 or height < 0:
        return Rect(0, 0, -1, -1)
    else:
        return Rect(x, y, width, height)

# avg/med: 4 us/3 us
# def intersect_rectangle(r1: Rect, r2: Rect) -> Rect:
#     x = max(r1[0], r2[0])
#     y = max(r1[1], r2[1])
#     width = min(r1[0] + r1[2], r2[0] + r2[2]) - x
#     height = min(r1[1] + r1[3], r2[1] + r2[3]) - y
#     if width < 0 or height < 0:
#         return Rect(0, 0, -1, -1)
#     else:
#         return Rect(x, y, width, height)


def intersect_rectangle_wrapper(r1, r2):
    return intersect_rectangle(Rect(*r1), Rect(*r2))


def res_printer(prop, value):
    def fmt(x):
        return [x[0], x[1], x[2], x[3]] if x else None

    if prop in (PropertyName.EXPECTED, PropertyName.RESULT):
        return fmt(value)
    else:
        return value


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('rectangle_intersection.py',
                                       'rectangle_intersection.tsv',
                                       intersect_rectangle_wrapper,
                                       res_printer=res_printer))
