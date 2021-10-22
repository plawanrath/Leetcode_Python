"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Approach: 2 Pointer Walk

we could use two pointers. The first pointer advances the list by n+1 steps from the beginning, 
while the second pointer starts from the beginning of the list. Now, both pointers are exactly 
separated by n nodes apart. We maintain this constant gap by advancing both pointers together 
until the first pointer arrives past the last node. The second pointer will be pointing at the 
nnth node counting from the last. We relink the next pointer of the node referenced by the second 
pointer to point to the node's next next node.

Time: O(N), Space: O(1)
"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeNthFromEnd(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    dummy = ListNode(0)
    dummy.next = head
    first, second = dummy, dummy
    # Advances first pointer so that the gap between first and second is n nodes apart
    for i in range(n+1):
        first = first.next
    
    # Move first to the end, maintaining the gap
    while first:
        first = first.next
        second = second.next
    
    second.next = second.next.next
    return dummy.next