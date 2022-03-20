from binary_tree_node import BinaryTreeNode
from test_framework import generic_test

def height_balance(tree: BinaryTreeNode) -> (int, bool):
    if not tree:
        return -1, True
    left_height, left_balance = height_balance(tree.left)
    if not left_balance:
        return -1, False
    right_height, right_balance = height_balance(tree.right)
    if not right_balance:
        return -1, False
    balance = abs(left_height - right_height) <= 1
    height = 1 + max(left_height, right_height)
    return height, balance


def is_balanced_binary_tree(tree: BinaryTreeNode) -> bool:
    return height_balance(tree)[1]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_balanced.py',
                                       'is_tree_balanced.tsv',
                                       is_balanced_binary_tree))
