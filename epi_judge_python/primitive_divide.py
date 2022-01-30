from test_framework import generic_test


def divide(x: int, y: int) -> int:
    q = 0
    k = 0
    while x >= y:
        while x > (y << (k + 1)):
            k += 1
        q += 1 << k
        x -= y << k
        k = 0
    return q


# avg/med: 4 us/1 us
# def divide(x: int, y: int) -> int:
#     q = 0
#     k = 0
#     while x >= y:
#         while x > (y << (k + 1)):
#             k += 1
#         q += 1 << k
#         x -= y << k
#         k = 0
#     return q


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('primitive_divide.py',
                                       'primitive_divide.tsv', divide))
