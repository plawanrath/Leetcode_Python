"""
Implement the BSTIterator class that represents an iterator over the in-order traversal of a binary search tree (BST):

BSTIterator(TreeNode root) Initializes an object of the BSTIterator class. The root of the BST is given as part of the constructor. The pointer should be initialized to a non-existent number smaller than any element in the BST.
boolean hasNext() Returns true if there exists a number in the traversal to the right of the pointer, otherwise returns false.
int next() Moves the pointer to the right, then returns the number at the pointer.



Approach:

To get the in order array of the BST, we can do an in order DFS traversal and appended it all to an output array. For the next() method, 
we can initialize a starting index of -1, and every time that function is hit we increment the index and return the traversed array at that index. 
Creating both the index and array in the constructor helps us state-wise.

For the hasNext() function, we will always have something coming next in a traversal unless it has hit the end of the traversal. 
So if the index is less than or equal to the length of the traversal array, we return True. Otherwise it must mean we hit the end of the traversal array and we return False.
"""

from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:
    def __init__(self, root: TreeNode) -> None:
        self.inorder_list = self._inorder(root, [])
        self.index = -1

    def next(self) -> int:
        self.index+= 1
        return self.inorder_list[self.index]
    
    def hasNext(self) -> int:
        if self.index >= len(self.inorder_list) - 1:
            return False
        return True
    
    def _inorder(self, root: TreeNode, result: List[int]):
        if not root:
            return
        self._inorder(root.left, result)
        result.append(root.val)
        self._inorder(root.right, result)
        return result