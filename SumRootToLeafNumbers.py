"""
You are given the root of a binary tree containing digits from 0 to 9 only.

Each root-to-leaf path in the tree represents a number.

For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.
Return the total sum of all root-to-leaf numbers. 

    1
   / \
  2   3
nput: root = [1,2,3]
Output: 25
Explanation:
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.
Therefore, sum = 12 + 13 = 25.  

Approach:
DFS - Recursive Preorder Traversal
First create current_number
Use a root_to_leaf sum. if it's a leaf, update root-to-leaf sum
Do this in preorder traversal

Time Complexity: O(N), SPace: O(H) for call stack where H is the height of the tree
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def sumNumbers(root: Optional[TreeNode]) -> int:
    def preorder(node, curr_number):
        nonlocal root_to_leaf
        if node:
            curr_number = curr_number * 10 + node.val
            if not (node.left or node.right):
                root_to_leaf += curr_number
            preorder(node.left, curr_number)
            preorder(node.right, curr_number)
    
    root_to_leaf = 0
    preorder(root, 0)
    return root_to_leaf
