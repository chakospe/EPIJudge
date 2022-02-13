from typing import List

from test_framework import generic_test


# Check if a partially filled matrix has any conflicts.
def is_valid_sudoku(partial_assignment: List[List[int]]) -> bool:
    row_sets = [set() for i in range(9)]
    col_sets = [set() for i in range(9)]
    sub_sets = [[set() for i in range(3)] for j in range(3)]
    for row in range(9):
        for col in range(9):
            val = partial_assignment[row][col]
            if val != 0:
                if val in row_sets[row] or val in col_sets[col] or val in sub_sets[row // 3][col // 3]:
                    return False
                else:
                    row_sets[row].add(val)
                    col_sets[col].add(val)
                    sub_sets[row // 3][col // 3].add(val)
    return True

# avg/med: 20 us/24 us
# def is_valid_sudoku(partial_assignment: List[List[int]]) -> bool:
#     row_sets = [set() for i in range(9)]
#     col_sets = [set() for i in range(9)]
#     sub_sets = [[set() for i in range(3)] for j in range(3)]
#     for row in range(9):
#         for col in range(9):
#             val = partial_assignment[row][col]
#             if val != 0:
#                 if val in row_sets[row] or val in col_sets[col] or val in sub_sets[row // 3][col // 3]:
#                     return False
#                 else:
#                     row_sets[row].add(val)
#                     col_sets[col].add(val)
#                     sub_sets[row // 3][col // 3].add(val)
#     return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_valid_sudoku.py',
                                       'is_valid_sudoku.tsv', is_valid_sudoku))
