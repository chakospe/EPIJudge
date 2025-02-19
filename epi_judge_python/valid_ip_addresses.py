from typing import List

from test_framework import generic_test


def get_valid_ip_address(s: str) -> List[str]:
    def is_valid_part(s):
        return len(s) == 1 or (s[0] != '0' and int(s) < 256)

    result, parts = [], [''] * 4
    for i in range(1, min(4, len(s))):
        parts[0] = s[:i]
        if is_valid_part(parts[0]):
            for j in range(1, min(4, len(s) - i)):
                parts[1] = s[i:i + j]
                if is_valid_part(parts[1]):
                    for k in range(1, min(4, len(s) - i - j)):
                        parts[2], parts[3] = s[i + j:i + j + k], s[i + j + k:]
                        if is_valid_part(parts[2]) and is_valid_part(parts[3]):
                            result.append('.'.join(parts))
    return result

# avg/med: 23 us/23 us
# def get_valid_ip_address(s: str) -> List[str]:
#     def is_valid_part(s):
#         return len(s) == 1 or (s[0] != '0' and int(s) < 256)
#
#     result, parts = [], [''] * 4
#     for i in range(1, min(4, len(s))):
#         parts[0] = s[:i]
#         if is_valid_part(parts[0]):
#             for j in range(1, min(4, len(s) - i)):
#                 parts[1] = s[i:i + j]
#                 if is_valid_part(parts[1]):
#                     for k in range(1, min(4, len(s) - i - j)):
#                         parts[2], parts[3] = s[i + j:i + j + k], s[i + j + k:]
#                         if is_valid_part(parts[2]) and is_valid_part(parts[3]):
#                             result.append('.'.join(parts))
#     return result


def comp(a, b):
    return sorted(a) == sorted(b)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('valid_ip_addresses.py',
                                       'valid_ip_addresses.tsv',
                                       get_valid_ip_address,
                                       comparator=comp))
