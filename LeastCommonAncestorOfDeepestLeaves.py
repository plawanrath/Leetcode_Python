"""
Given the root of a binary tree, return the lowest common ancestor of its deepest leaves.
"""
from typing import Optional


class TreeNode:
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None


def lcaDeepestLeaves(root: Optional[TreeNode]) -> Optional[TreeNode]:
    def post_order(root):
        if not root:
            return 0, None
        d1, n1 = post_order(root.left)
        d2, n2 = post_order(root.right)
        if d1 == d2:
            return d1+1, root
        elif d1 > d2:
            return d1+1, n1
        else:
            return d2+1, n2
        
    d, n = post_order(root)
    return n