"""
Given the head of a singly linked list, return true if it is a palindrome.

Algorithm:
the steps we need to do are:

1. Find the end of the first half.
2. Reverse the second half.
3. Determine whether or not there is a palindrome.
4. Restore the list.
5. Return the result.

Time Complexity: O(N), Space: O(1)
"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def isPalindrome(head: Optional[ListNode]) -> bool:
    if head is None:
        return True

    def end_of_first_half(head):
        fast = head
        slow = head
        while fast.next is not None and fast.next.next is not None:
            fast = fast.next.next
            slow = slow.next
        return slow

    def reverse_list(head):
        previous = None
        current = head
        while current is not None:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        return previous

    # Find the end of first half and reverse second half.
    first_half_end = end_of_first_half(head)
    second_half_start = reverse_list(first_half_end.next)

    # Check whether or not there's a palindrome.
    result = True
    first_position = head
    second_position = second_half_start
    while result and second_position is not None:
        if first_position.val != second_position.val:
            result = False
        first_position = first_position.next
        second_position = second_position.next

    # Restore the list and return the result.
    first_half_end.next = reverse_list(second_half_start)
    return result    
