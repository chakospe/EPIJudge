from test_framework import generic_test


def precompute_reverse(x: int) -> int:
    # ASSUMPTION: x is a 16-bit word
    size = 16
    for i in range(int(size / 2)):
        if (x >> i) & 1 != (x >> (size - 1 - i)) & 1:
            x ^= ((1 << i) | (1 << (size - 1 - i)))
    return x


PRECOMPUTED_REVERSE = [precompute_reverse(i) for i in range(1 + 0xFFFF)]


def reverse_bits(x: int) -> int:
    mask_size = 16
    mask = 0xFFFF
    return PRECOMPUTED_REVERSE[x & mask] << (3 * mask_size) | \
           PRECOMPUTED_REVERSE[x >> (1 * mask_size) & mask] << (2 * mask_size) | \
           PRECOMPUTED_REVERSE[x >> (2 * mask_size) & mask] << (1 * mask_size) | \
           PRECOMPUTED_REVERSE[x >> (3 * mask_size) & mask]


# avg/med: 2 us/1 us
# def precompute_reverse(x: int) -> int:
#     # ASSUMPTION: x is a 16-bit word
#     size = 16
#     for i in range(int(size / 2)):
#         if (x >> i) & 1 != (x >> (size - 1 - i)) & 1:
#             x ^= ((1 << i) | (1 << (size - 1 - i)))
#     return x
#
# PRECOMPUTED_REVERSE = [precompute_reverse(i) for i in range(1 + 0xFFFF)]
#
# def reverse_bits(x: int) -> int:
#     mask_size = 16
#     mask = 0xFFFF
#     return PRECOMPUTED_REVERSE[x & mask] << (3 * mask_size) | \
#            PRECOMPUTED_REVERSE[x >> (1 * mask_size) & mask] << (2 * mask_size) | \
#            PRECOMPUTED_REVERSE[x >> (2 * mask_size) & mask] << (1 * mask_size) | \
#            PRECOMPUTED_REVERSE[x >> (3 * mask_size) & mask]


# avg/med: 11 us/8 us
# def reverse_bits(x: int) -> int:
#     for i in range(32):
#         if (x >> i) & 1 != (x >> (63 - i)) & 1:
#             x ^= ((1 << i) | (1 << (63 - i)))
#     return x

# avg/med: 11 us/11 us
# def reverse_bits(x: int) -> int:
#     l = [0] * 64
#     i = 0
#     while x:
#         l[i] = x & 1
#         x >>= 1
#         i += 1
#     y = 0
#     for j in range(len(l)):
#         y |= (l[j] << (63 - j))
#     return y


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_bits.py', 'reverse_bits.tsv',
                                       reverse_bits))
