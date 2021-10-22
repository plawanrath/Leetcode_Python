"""
Given a root of an N-ary tree, you need to compute the length of the diameter of the tree.

The diameter of an N-ary tree is the length of the longest path between any two nodes in the tree. 
This path may or may not pass through the root.

Input:
        1
      / | \
     3  2  4
   /  \
  5   6
Output: 3  

Idea: Diameter will always be from one leaf at one end to another leaf at another end.
So if we get the maximum depth and the second highest depth a sum of those 2 should be the diameter.

We can find depth using DFS.

Time and Space: O(N)
"""
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []


def diameter(root: 'Node') -> int:
    def dfs(root: Node):
        nonlocal diameterRes
        first = second = 0
        for neighbor in root.children:
            depth = dfs(neighbor)
            if depth > first:
                first, second = depth, first
            elif depth > second:
                second = depth
        diameterRes = max(diameterRes, first + second)
        return first + 1
    
    diameterRes = 0
    dfs(root)
    return diameterRes
