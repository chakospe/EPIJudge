from test_framework import generic_test


def swap_bits(x, i, j):
    if (x >> i) & 1 != (x >> j) & 1:
        mask = (1 << i) | (1 << j)
        x ^= mask
    return x

# avg/med: 1 us/1 us
# def swap_bits(x, i, j):
#     if (x >> i) & 1 != (x >> j) & 1:
#         mask = (1 << i) | (1 << j)
#         x ^= mask
#     return x


# avg/med: 1 us/1 us
# def swap_bits(x, i, j):
#     bit_i = (x >> i) & 1
#     bit_j = (x >> j) & 1
#     if bit_i == bit_j:
#         return x
#     if bit_i == 1:
#         # flip bit i to 0 and bit j to 1
#         # & with i mask = 1 except bit i
#         # | with j mask = 0 except bit j
#         i_mask = (2 ** 64 - 1) ^ (1 << i)
#         j_mask = (1 << j)
#         return x & i_mask | j_mask
#     else:
#         # flip bit i to 1 and bit j to 0
#         # | with i mask = 0 except bit i
#         # & with j mask = 1 except bit j
#         i_mask = (1 << i)
#         j_mask = (2 ** 64 - 1) ^ (1 << j)
#         return x | i_mask & j_mask



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('swap_bits.py', 'swap_bits.tsv',
                                       swap_bits))
