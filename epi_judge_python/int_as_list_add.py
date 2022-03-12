from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def add_two_numbers(L1: ListNode, L2: ListNode) -> Optional[ListNode]:
    if L1 is None:
        return L2
    if L2 is None:
        return L1
    res_head = res_iter = ListNode()
    carry = 0
    while L1 or L2:
        if L1 is None:
            val = L2.data + carry
            L2 = L2.next
        elif L2 is None:
            val = L1.data + carry
            L1 = L1.next
        else:
            val = L1.data + L2.data + carry
            L1, L2 = L1.next, L2.next
        carry = val // 10
        val = val % 10
        res_iter.next = ListNode(val)
        res_iter = res_iter.next
    if carry == 1:
        res_iter.next = ListNode(1)
    return res_head.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_as_list_add.py',
                                       'int_as_list_add.tsv', add_two_numbers))
