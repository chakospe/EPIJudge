import functools
from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def create_list_of_leaves(tree: BinaryTreeNode) -> List[BinaryTreeNode]:

    def helper(node: BinaryTreeNode, partial: List[BinaryTreeNode]) -> List[BinaryTreeNode]:
        if node is None:
            return partial
        if not node.left and not node.right:
            partial.append(node)
            return partial
        if node.left:
            partial = helper(node.left, partial)
        if node.right:
            partial = helper(node.right, partial)
        return partial

    return helper(tree, [])


@enable_executor_hook
def create_list_of_leaves_wrapper(executor, tree):
    result = executor.run(functools.partial(create_list_of_leaves, tree))

    if any(x is None for x in result):
        raise TestFailure('Result list can\'t contain None')
    return [x.data for x in result]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_connect_leaves.py',
                                       'tree_connect_leaves.tsv',
                                       create_list_of_leaves_wrapper))
