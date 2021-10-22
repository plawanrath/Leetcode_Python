"""
Given the root of a binary tree, return the length of the longest consecutive sequence path.

Approach:

Use DFS
We use a variable length to store the current consecutive path length and pass it down the tree. 
As we traverse, we compare the current node with its parent node to determine if it is consecutive. 
If not, we reset the length.
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def longestConsecutive(root: Optional[TreeNode]) -> int:
    def dfs(node, parent, length):
        nonlocal maxlength
        if not node:
            return
        if parent and node.val == parent.val + 1:
            length += 1
        else:
            length = 1
        maxlength = max(maxlength, length)
        dfs(node.left, node, length)
        dfs(node.right, node, length)
    
    maxlength = 0
    dfs(root, None, 0)
    return maxlength