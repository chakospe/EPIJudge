from test_framework import generic_test


def add(a, b):
    return a if not b else add(a ^ b, (a & b) << 1)


def multiply(x: int, y: int) -> int:
    sum = 0
    while x:
        if x & 1:
            sum = add(sum, y)
        x >>= 1
        y <<= 1
    return sum

# avg/med: 9 us/8 us
# def add(a, b):
#     return a if not b else add(a ^ b, (a & b) << 1)
#
#
# def multiply(x: int, y: int) -> int:
#     sum = 0
#     while x:
#         if x & 1:
#             sum = add(sum, y)
#         x >>= 1
#         y <<= 1
#     return sum


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('primitive_multiply.py',
                                       'primitive_multiply.tsv', multiply))
