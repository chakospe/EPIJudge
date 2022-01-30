from test_framework import generic_test


def reverse(x: int) -> int:
    pos = 1 if x > 0 else -1
    x = pos * x
    result, power, temp= 0, 0, x
    while temp // 10:
        power += 1
        temp //= 10
    while power >= 0:
        result += (x % 10) * (10 ** power)
        x //= 10
        power -= 1
    return pos * result

# avg/med: 6 us/4 us
# def reverse(x: int) -> int:
#     pos = 1 if x > 0 else -1
#     x = pos * x
#     result, power, temp= 0, 0, x
#     while temp // 10:
#         power += 1
#         temp //= 10
#     while power >= 0:
#         result += (x % 10) * (10 ** power)
#         x //= 10
#         power -= 1
#     return pos * result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_digits.py',
                                       'reverse_digits.tsv', reverse))
