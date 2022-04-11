from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def binary_tree_from_preorder_inorder(preorder: List[int],
                                      inorder: List[int]) -> BinaryTreeNode:
    node_to_inorder_idx = {data: i for i, data in enumerate(inorder)}

    def helper(preorder_start: int, preorder_end: int, inorder_start: int, inorder_end: int):
        if preorder_start >= preorder_end or inorder_start >= inorder_end:
            return None

        root_inorder_idx = node_to_inorder_idx[preorder[preorder_start]]
        left_subtree_size = root_inorder_idx - inorder_start

        left = helper(preorder_start + 1, preorder_start + 1 + left_subtree_size,
                      inorder_start, root_inorder_idx)
        right = helper(preorder_start + 1 + left_subtree_size, preorder_end,
                       root_inorder_idx + 1, inorder_end)

        return BinaryTreeNode(preorder[preorder_start], left, right)

    return helper(0, len(preorder), 0, len(inorder))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_from_preorder_inorder.py',
                                       'tree_from_preorder_inorder.tsv',
                                       binary_tree_from_preorder_inorder))
