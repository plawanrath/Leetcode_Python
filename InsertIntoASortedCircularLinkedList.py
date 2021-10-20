"""
Given a Circular Linked List node, which is sorted in ascending order, write a 
function to insert a value insertVal into the list such that it remains a sorted circular list. 
The given node can be a reference to any single node in the list and may not necessarily be the 
smallest value in the circular list.

If there are multiple suitable places for insertion, you may choose any place to insert the 
new value. After the insertion, the circular list should remain sorted.

Idea:
There are only 3 cases:

1. When crossing from max-->min:
    If insertVal larger than max or smaller than min, insert here,
2. Normal case where cur.Val <= insertVal <= cur.next.Val
    Insert here,
3. If we completed a full cycle (cur.next = head) and haven't found a spot:
    This means a corner case has happened, where all value(s) in the cycle are the same, 
    because if there's any gradient in the original cycle the while loop would've caught it.

Time: O(N), Space: O(1)
"""
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


def insert(head: 'Node', insertVal: int) -> 'Node':
    p = Node(insertVal,None)
    if not head: 
        head = p.next = p
    cur = head
    while True:
        a,b = cur.next.val,cur.val
        # 1. a is min and b is max; insertVal is smaller than a
        # or larger than b
        # 2. Regular b <= insertVal <= a
        # 3. no suitable position and a full cycle has passed
        # this can happen when all elements are the same
        # or if there's only 1 element
        if (a < b and (insertVal<=a or insertVal>=b)) or (b <= insertVal <=a) or cur.next == head:
            p.next,cur.next = cur.next,p
            return head
        cur = cur.next
    return head