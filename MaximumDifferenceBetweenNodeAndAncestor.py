"""
Given the root of a binary tree, find the maximum value v for which there exist different 
nodes a and b where v = |a.val - b.val| and a is an ancestor of b.

A node a is an ancestor of b if either: any child of a is equal to b or any 
child of a is an ancestor of b.

Approach: DFS

Algorithm

Step 1: Initialize a variable result to record the required maximum difference.

Step 2: Define a function helper, which takes three arguments as input.

The first argument is the current node, and the second and third arguments are the 
maximum and minimum values along the root to the current node, respectively.

In the function helper, update result and call helper on the left and right subtrees.

Step 3: Run helper on the root. It will automatically do recursion on every node.

Step 4: Finally, return result.

Space and Time: O(N)
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxAncestorDiff(root: Optional[TreeNode]) -> int:
    if not root:
        return
    # record the required maximum difference
    result = 0

    def dfs(node, curr_max, curr_min):
        nonlocal result
        if not node:
            return
        result = max(result, abs(curr_max-node.val), abs(curr_min-node.val))
        curr_max = max(curr_max, node.val)
        curr_min = min(curr_min, node.val)
        dfs(node.left, curr_max, curr_min)
        dfs(node.right, curr_max, curr_min)
    
    dfs(root, root.val, root.val)
    return result