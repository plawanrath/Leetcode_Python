"""
Given the root of a binary tree, return the average value of the 
nodes on each level in the form of an array. Answers within 10-5 of the actual answer will be accepted.

Approach: Run DFS, create a dictionary of (sum, count) for each level and at the end loop
through that dictionary and generate the average.
"""
from typing import List
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def averageOfLevels(root: Optional[TreeNode]) -> List[float]:
    if not root:
        return []
    level_sum_and_counts = {}
    def dfs(node, depth):
        nonlocal level_sum_and_counts
        if not node:
            return
        if depth not in level_sum_and_counts:
            level_sum_and_counts[depth] = (node.val, 1)
        else:
            curr_sum, curr_count = level_sum_and_counts[depth]
            level_sum_and_counts[depth] = (curr_sum+node.val, curr_count+1)
        dfs(node.left, depth + 1)
        dfs(node.right, depth + 1)
    
    dfs(root, 0)
    res = []
    for levels, cum_and_counts in level_sum_and_counts.items():
        res.append(cum_and_counts[0]/cum_and_counts[1])
    return res