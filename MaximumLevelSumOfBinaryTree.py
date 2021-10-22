"""
Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.

Return the smallest level x such that the sum of all the values of nodes at level x is maximal.

Input:
        1
       / \
      7   0
     / \
    7  -8
Output: 2
Explanation: 
Level 1 sum = 1.
Level 2 sum = 7 + 0 = 7.
Level 3 sum = 7 + -8 = -1.
So we return the level with the maximum sum which is level 2.     

Approach:
Do a DFS, keep track of sums at each level and then return maxsum.
We can use a dicrionary to keep track of sum by level.
"""
from typing import Optional
from collections import defaultdict


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxLevelSum(root: Optional[TreeNode]) -> int:
    levels = defaultdict(int)
    def sum_vals(root, depth):
        if root:
            levels[depth] += root.val
            sum_vals(root.left,  depth+1)
            sum_vals(root.right, depth+1)
        
    sum_vals(root, 1)
    return max(levels, key=levels.get)