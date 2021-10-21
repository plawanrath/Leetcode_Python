"""
Given the root of a binary tree, return an array of the largest value in each row of the tree (0-indexed).

Example:
Input Tree
    4
  /   \
  2    5
 / \
1   3
Output = [4,5,3]

Idea: We can do DFS and each time just store the largest value at current depth.

O(N) time and Space
"""
from typing import Optional
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def largestValues(root: Optional[TreeNode]) -> List[int]:
    def dfs(node, depth):
        nonlocal res
        if not node:
            return
        if len(res) - 1 < depth: # we haven't come to this depth in the past
            res += [node.val]
        elif res[depth] < node.val: # if current node val is bigger
            res[depth] = node.val
        if node.right:
            dfs(node.right, depth + 1)
        if node.left:
            dfs(node.left, depth + 1)
    
    res = []
    dfs(root, 0)
    return res
