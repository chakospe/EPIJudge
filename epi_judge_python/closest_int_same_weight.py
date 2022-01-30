from test_framework import generic_test


def closest_int_same_bit_count(x: int) -> int:
    if x & 1:
        x = ~x
        return ~(x & (x - 1) | ((x & ~(x - 1))) >> 1)
    return x & (x - 1) | ((x & ~(x - 1)) >> 1)



# avg/med: 1 us/1 us
# def closest_int_same_bit_count(x: int) -> int:
#     lsb = x & 1
#     i = 1
#     while x >> i & 1 == lsb:
#         i += 1
#     return x ^ (3 << (i - 1))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('closest_int_same_weight.py',
                                       'closest_int_same_weight.tsv',
                                       closest_int_same_bit_count))
