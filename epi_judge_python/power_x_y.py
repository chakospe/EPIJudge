from test_framework import generic_test


def power(x: float, y: int) -> float:
    result, power = 1., y
    if y < 0:
        power, x = -power, 1. / x
    while power:
        if power & 1:
            result *= x
        x, power = x * x, power >> 1
    return result

# avg/med: 2 us/2 us
# def power(x: float, y: int) -> float:
#     result, power = 1., y
#     if y < 0:
#         power, x = -power, 1. / x
#     while power:
#         if power & 1:
#             result *= x
#         x, power = x * x, power >> 1
#     return result


# avg/med: 438 us/320 us
# def power(x: float, y: int) -> float:
#     result = 1
#     if y < 0:
#         x = 1 / x
#         y *= -1
#     while y > 0:
#         result *= x
#         y -= 1
#     return result


if __name__ == '__main__':
    exit(generic_test.generic_test_main('power_x_y.py', 'power_x_y.tsv',
                                        power))
