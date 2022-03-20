from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def sum_root_to_leaf(tree: BinaryTreeNode) -> int:
    if not tree:
        return 0
    else:
        return helper(tree, 0)


def helper(tree: BinaryTreeNode, mask: int) -> int:
    partial = (mask << 1) | tree.data
    if tree.left and tree.right:
        return (helper(tree.left, partial) +
                helper(tree.right, partial))
    elif tree.left:
        return helper(tree.left, partial)
    elif tree.right:
        return helper(tree.right, partial)
    else:
        return partial


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sum_root_to_leaf.py',
                                       'sum_root_to_leaf.tsv',
                                       sum_root_to_leaf))
