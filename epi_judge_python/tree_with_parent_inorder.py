from typing import List

from binary_tree_with_parent_prototype import BinaryTreeNode
from test_framework import generic_test


def inorder_traversal(tree: BinaryTreeNode) -> List[int]:
    prev, result = None, []
    while tree:
        if prev is tree.parent:
            if tree.left:
                nxt = tree.left
            else:
                result.append(tree.data)
                nxt = tree.right or tree.parent
        elif prev is tree.left:
            result.append(tree.data)
            nxt = tree.right or tree.parent
        else:
            nxt = tree.parent
        prev, tree = tree, nxt
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_with_parent_inorder.py',
                                       'tree_with_parent_inorder.tsv',
                                       inorder_traversal))
