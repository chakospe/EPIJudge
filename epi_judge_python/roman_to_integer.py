from test_framework import generic_test


def roman_to_integer(s: str) -> int:
    T = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    i, running_sum = 0, 0
    while True:
        if i < len(s) - 1:
            if T[s[i]] >= T[s[i + 1]]:
                running_sum += T[s[i]]
                i += 1
            else:
                running_sum += T[s[i + 1]] - T[s[i]]
                i += 2
        else:
            running_sum += T[s[i]]
            i += 1
        if i >= len(s):
            break
    return running_sum

# avg/med: 3 us/3 us
# def roman_to_integer(s: str) -> int:
#     T = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
#     i, running_sum = 0, 0
#     while True:
#         if i < len(s) - 1:
#             if T[s[i]] >= T[s[i + 1]]:
#                 running_sum += T[s[i]]
#                 i += 1
#             else:
#                 running_sum += T[s[i + 1]] - T[s[i]]
#                 i += 2
#         else:
#             running_sum += T[s[i]]
#             i += 1
#         if i >= len(s):
#             break
#     return running_sum



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('roman_to_integer.py',
                                       'roman_to_integer.tsv',
                                       roman_to_integer))
