from test_framework import generic_test


def precompute_parity(x: int) -> int:
    result = 0
    while x:
        result ^= 1
        x &= x - 1
    return result

PRECOMPUTED_PARITY = [precompute_parity(i) for i in range(1+0xFFFF)]

def parity(x: int) -> int:
    bit_mask = 0xFFFF
    x ^= x >> 32
    x ^= x >> 16
    return PRECOMPUTED_PARITY[x & bit_mask]


# avg/med: 1 us/1 us
# def precompute_parity(x: int) -> int:
#     result = 0
#     while x:
#         result ^= 1
#         x &= x - 1
#     return result
#
# PRECOMPUTED_PARITY = [precompute_parity(i) for i in range(1+0xFFFF)]
#
# def parity(x: int) -> int:
#     bit_mask = 0xFFFF
#     x ^= x >> 32
#     x ^= x >> 16
#     return PRECOMPUTED_PARITY[x & bit_mask]


# avg/med: 2 us/2 us
# def precompute_parity(x: int) -> int:
#     result = 0
#     while x:
#         result ^= 1
#         x &= x - 1
#     return result
#
# PRECOMPUTED_PARITY = [precompute_parity(i) for i in range(0xFFFF)]
#
# def parity(x: int) -> int:
#     mask_size = 16
#     bit_mask = 0xFFFF
#     return (PRECOMPUTED_PARITY[x >> (3 * mask_size)] ^
#             PRECOMPUTED_PARITY[x >> (2 * mask_size) & bit_mask] ^
#             PRECOMPUTED_PARITY[x >> (1 * mask_size) & bit_mask] ^
#             PRECOMPUTED_PARITY[x >> (0 * mask_size) & bit_mask])


# avg/med: 2 us/1 us
# def parity(x: int) -> int:
#     x ^= x >> 32
#     x ^= x >> 16
#     x ^= x >> 8
#     x ^= x >> 4
#     x ^= x >> 2
#     x ^= x >> 1
#     return x & 1

# avg/med: 7 us/6 us
# def parity(x: int) -> int:
#     result = 0
#     while x:
#         result ^= x & 1
#         x >>= 1
#     return result

# avg/med: 3 us/3 us
# def parity(x: int) -> int:
#     result = 0
#     while x:
#         result ^= 1
#         x &= x - 1
#     return result


if __name__ == '__main__':
    exit(generic_test.generic_test_main('parity.py', 'parity.tsv', parity))
