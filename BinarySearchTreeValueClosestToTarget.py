"""
Given the root of a binary search tree and a target value, return the value in the 
BST that is closest to the target.

Input:
        4
      /   \
     2     5
   /  \
  1    3
target = 3.714286

Output: 4

Idea:
Binary Search

go left if target is smaller than current root value, and go right otherwise. 
Choose the closest to target value at each step.

Time Complexity: O(H) where H is the height of the BST
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


def closestValue(self, root: Optional[TreeNode], target: float) -> int:
    closest = root.val
    while root:
        closest = min(root.val, closest, key=lambda x: abs(target - x))
        if target < root.val:
            root = root.left
        else:
            root = root.right
    return closest