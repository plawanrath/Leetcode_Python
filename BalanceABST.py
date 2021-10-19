"""
Given the root of a binary search tree, return a balanced binary search tree with the same node values. 
If there is more than one answer, return any of them.

A binary search tree is balanced if the depth of the two subtrees of every node never differs by more than 1.

Idea:
If we do an inorder traversal on a BST that gives a sorted array.
So we would do an inorder traversal which would return sorted list of nodes.
FInally convert sorted list into a Balanced BST as follows:

1) Get the Middle of the array and make it root.
2) Recursively do same for left half and right half.
      a) Get the middle of left half and make it left child of the root
          created in step 1.
      b) Get the middle of right half and make it right child of the
          root created in step 1.

TIme COmplexity: O(n) for inorder and O(n) for traversal and conversion
"""

from os import _OnError


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def balanceBST(root: TreeNode) -> TreeNode:
    def inorder(node):
        nonlocal arr
        if node:
            inorder(node.left)
            arr.append(node)
            inorder(node.right)
    
    def array_to_bst(l, r):
        nonlocal arr
        if l > r or len(arr) == 0:
            return None
        else:
            mid = (l+r)//2
            new_root = arr[mid]
            new_root.left = array_to_bst(l,mid-1)
            new_root.right = array_to_bst(mid+1,r)

            return new_root
    
    arr = []
    inorder(root)
    return array_to_bst(0, len(arr)-1)