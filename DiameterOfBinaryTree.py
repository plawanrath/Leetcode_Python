"""
Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any 
two nodes in a tree. This path may or may not pass through the root.

Input Tree
    4
  /   \
  2    5
 / \
1   3
Output: 3 which is the length of 1->2->4->5 or 3->2->4->5

Idea: THe longest path will always be between 2 leaves. 
The problem seems to be solvable using DFS

Algorithm:
1. Initalize an integer variable diameter to keep track of the longest path we find from the DFS.
2. Recursively run DFS that can return the longestPath from a given node out of its left and right branches.
        If node is None, we have reached the end of the tree, hence we should return 0
        we want to recursively explore node's children and store them in leftPath and rightPath
        If leftPath plus rightPath is longer than the current longest diameter found, then we need to update diameter
        finally, we return the longer one of leftPath and rightPath and add 1 for the parent. 

Input Tree
    4
  /   \
  2    5
 / \
1   3

diameter = 0
longestPath(4):
    leftPath = longestPath(2):
        leftPath = longestPath(1):
            leftPath, rightPath = 0, 0
            diameter = 0
            return 1
        leftPath = 1
        rightPath = longestPath(3):
            leftPath, rightPath = 0, 0
            diameter = 0
            return 1
        rightPath = 1
        diameter = max(0, 1 + 1) = 2
        return max(1, 1) + 1 = 2
    leftPath = 2
    rightPath = longestPath(5)
        leftPath, rightPath = 0, 0
        diameter = 2
        return max(0, 0) + 1 = 1
    rightPath = 1
    diameter = max(2, 2 + 1) = max(2, 3) = 3
    return max(2, 1) + 1 = 3

return diameter = 3

Time and space complexity: O(n)
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def diameterOfBinaryTree(root: Optional[TreeNode]) -> int:
    diameter = 0

    def longestPath(node: TreeNode):
        nonlocal diameter
        if not node:
            return 0
        # recursively find the longest path for left and right branches
        leftPath = longestPath(node.left)
        rightPath = longestPath(node.right)
        # update the diameter if left_path plus right_path is larger
        diameter = max(diameter, leftPath + rightPath)

        return max(leftPath, rightPath) + 1
    
    longestPath(root)
    return diameter