"""
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

Approach:
Divide and Conquer. Basically Pair up k lists and merge k pairs
then merge those k/2 pairs of lists to form k/4 pair of lists and so on.
This is similar to how merge sort works. 

Time Complexity: O(N log k), Space: O(1)
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def mergeKLists(lists):
    amount = len(lists)
    if not amount:
        return None
    interval = 1
    while interval < amount:
        for i in range(0, amount-interval, interval*2):
            lists[i] = merge2Lists(lists[i], lists[i + interval])
        interval *= 2
    return lists[0] if amount > 0 else lists

def merge2Lists(l1, l2):
    head = point = ListNode(0)
    while l1 and l2:
        if l1.val <= l2.val:
            point.next = l1
            l1 = l1.next
        else:
            point.next = l2
            l2 = l2.next
        point = point.next
    if not l1:
        point.next = l2
    else:
        point.next = l1
    return head.next