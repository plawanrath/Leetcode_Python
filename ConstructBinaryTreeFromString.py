"""
You need to construct a binary tree from a string consisting of parenthesis and integers.

The whole input represents a binary tree. 
It contains an integer followed by zero, one or two pairs of parenthesis. 
The integer represents the root's value and a pair of parenthesis contains a 
child binary tree with the same structure.

You always start to construct the left child node of the parent first if it exists.

Input: s = "4(2(3)(1))(6(5))"
Output
        4
      /   \
     2     6
    / \   /
   3   1 5

Idea: We will use recursion to go down the string and evict brackets
When evicting brackets for opening brackets we will recursively make 
children.

Time and Space Complexity: O(n)
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def str2tree(s: str) -> Optional[TreeNode]:
    if not s:
        return None
    
    def buildTree(remainder):
        if not remainder:
            return None
        
        # Remove '(' during recursion. We will always enter this function with paranthesis
        remainder.pop(0)

        # Get the digits
        val = ''
        while remainder and remainder[0] not in ['(', ')']:
            val += remainder.pop(0)      
        node = TreeNode(int(val))

        # If we meet '(' after extracting the digits, we explore the remain as the children nodes
        if remainder[0] == '(':
            # First explore the left child
            node.left = buildTree(remainder)
            # If still has '(', explore as the right child 
            if remainder[0] == '(':
                node.right = buildTree(remainder)
        
        # remove )
        remainder.pop(0)
        return node

    # pad the string with paranthesis and pass it to the buildTree function
    return buildTree(['('] + list(s) + [')'])