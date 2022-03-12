from list_node import ListNode
from test_framework import generic_test


def reverse_list(L: ListNode) -> ListNode:
    if L is None or L.next is None:
        return L
    dummy_head, dummy_tail = L, L
    while dummy_tail.next:
        dummy_tail = dummy_tail.next
    node = dummy_head
    while node is not dummy_tail:
        dummy_head = node.next
        node.next = dummy_tail.next
        dummy_tail.next = node
        node = dummy_head
    return dummy_tail



def is_linked_list_a_palindrome(L: ListNode) -> bool:
    slow = fast = L
    while fast and fast.next:
        slow, fast = slow.next, fast.next.next
    first, second = L, reverse_list(slow)
    while second and first:
        if first.data != second.data:
            return False
        first, second = first.next, second.next
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_list_palindromic.py',
                                       'is_list_palindromic.tsv',
                                       is_linked_list_a_palindrome))
