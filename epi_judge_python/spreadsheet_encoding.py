import string
import functools

from test_framework import generic_test


def ss_decode_col_id(col: str) -> int:
    f = lambda x, c: x * 26 + (1 + string.ascii_uppercase.index(c.upper()))
    return functools.reduce(f, col, 0)



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('spreadsheet_encoding.py',
                                       'spreadsheet_encoding.tsv',
                                       ss_decode_col_id))
