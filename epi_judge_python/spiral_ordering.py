from typing import List

from test_framework import generic_test


def matrix_in_spiral_order(square_matrix: List[List[int]]) -> List[int]:
    return matrix_in_spiral_order_helper(square_matrix, False) if square_matrix else square_matrix


def matrix_in_spiral_order_helper(square_matrix: List[List[int]], start: bool) -> List[int]:
    n = len(square_matrix)
    if n == 1:
        return [square_matrix[0][0]]
    else:
        if start is False:
            return square_matrix[0] + \
                    [square_matrix[i][-1] for i in range(1, n)] + \
                    matrix_in_spiral_order_helper([row[:-1] for row in square_matrix[1:]], True)
        else:
            return list(reversed(square_matrix[-1])) + \
                    list(reversed([square_matrix[i][0] for i in range(0, n - 1)])) + \
                    matrix_in_spiral_order_helper([row[1:] for row in square_matrix[:-1]], False)

# avg/med: 174 us/113 us
# def matrix_in_spiral_order(square_matrix: List[List[int]]) -> List[int]:
#     return matrix_in_spiral_order_helper(square_matrix, False) if square_matrix else square_matrix
#
#
# def matrix_in_spiral_order_helper(square_matrix: List[List[int]], start: bool) -> List[int]:
#     n = len(square_matrix)
#     if n == 1:
#         return [square_matrix[0][0]]
#     else:
#         if start is False:
#             return square_matrix[0] + \
#                     [square_matrix[i][-1] for i in range(1, n)] + \
#                     matrix_in_spiral_order_helper([row[:-1] for row in square_matrix[1:]], True)
#         else:
#             return list(reversed(square_matrix[-1])) + \
#                     list(reversed([square_matrix[i][0] for i in range(0, n - 1)])) + \
#                     matrix_in_spiral_order_helper([row[1:] for row in square_matrix[:-1]], False)



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('spiral_ordering.py',
                                       'spiral_ordering.tsv',
                                       matrix_in_spiral_order))
