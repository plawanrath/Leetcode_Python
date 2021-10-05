"""
Input 
    4
  /   \
  2    5
 / \
1   3

Output: 1 -> 2 -> 3 -> 4 -> 5 [Doubly Linked List]
This should happen in-place by manipulating the same tree into a Circular doubly linkedlist

We will store the first node and keep track of current node during traversal.
Use the first node to link to the last node at the end for circular linkedlist

first, lsat = None
inorder(4)
    - inorder(2)
        - inorder(1)
            - first = 1, last = 1 - returns
        - if last -> true
            - 1 -> 2 (current node is 2 last is 1)
          last = 2
          inorder(3)
            - if last -> true
                1 -> 2 -> 3 (current node is 3 and last node is 2 which is already linked with 1)
            last = 3
            return
    - if last -> true
        - 1 -> 2 -> 3 -> 4 (current node is 4 and last node is 3)
      last = 4
      return
      - inorder(5)
        - if last -> true
            - 1 -> 2 -> 3 -> 4 -> 5 (since current node is 5 and last node is 4)
        last = 5
        return

Link last with first for circular
- 1 -> 2 -> 3 -> 4 -> 5 (5 -> 1)

O(n) time and space
"""
from typing import Optional


class Node:
    def __init__(self, val: int, left: Optional['Node']=None, right: Optional['Node']=None) -> None:
        self.val = val
        self.left = left
        self.right = right


def treeToDoublyList(root: 'Node') -> 'Node':
    def inorder(node: 'Node'):
        nonlocal first, last
        if node:
            inorder(node.left)
            if last:
                # last keeps track of the previous node. So if there was a previous node, link it to tbe current node
                last.right = node
                node.left = last
            else:
                first = node
            last = node
            inorder(node.right)

    if not root:
        return None
    
    first, last = None, None
    inorder(root)
    # make the linked list circular
    last.right = first
    first.left = last

    return first

