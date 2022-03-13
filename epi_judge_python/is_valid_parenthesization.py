from test_framework import generic_test


def is_well_formed(s: str) -> bool:
    left, lookup = [], {'(': ')', '[': ']', '{': '}'}
    for c in s:
        if c in lookup:
            left.append(c)
        else:
            if not left or lookup[left.pop()] != c:
                return False
    return not left


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_valid_parenthesization.py',
                                       'is_valid_parenthesization.tsv',
                                       is_well_formed))
