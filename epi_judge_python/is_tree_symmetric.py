from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def check_symmetric(subtree0: BinaryTreeNode, subtree1: BinaryTreeNode) -> bool:
    if not subtree0 and not subtree1:
        return True
    elif subtree0 and subtree1:
        return (subtree0.data == subtree1.data
                and check_symmetric(subtree0.left, subtree1.right)
                and check_symmetric(subtree0.right, subtree1. left))
    else:
        return False


def is_symmetric(tree: BinaryTreeNode) -> bool:
    return not tree or check_symmetric(tree.left, tree.right)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_symmetric.py',
                                       'is_tree_symmetric.tsv', is_symmetric))
