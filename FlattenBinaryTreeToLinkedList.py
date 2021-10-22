"""
Given the root of a binary tree, flatten the tree into a "linked list":

The "linked list" should use the same TreeNode class where the right child pointer points to the next 
node in the list and the left child pointer is always null.
The "linked list" should be in the same order as a pre-order traversal of the binary tree.

Algorithm:
1. We use a pointer for traversing the nodes of our tree starting from the root. We have a loop that 
    keeps going until the node pointer becomes null which is when we would be done processing the entire tree.
2. For every node we check if it has a left child or not. If it doesn't we simply move on to the right hand side 
3. If the node does have a left child, we find the first node on the rightmost branch of the left subtree 
    which doesn't have a right child
4. Once we find this rightmost node, we rewire the connections to flatten them as follows.
        rightmost.right = node.right
        node.right = node.left
        node.left = null
5. And we move on to the right node to continue processing of our tree.

Time: O(N), Space: O(1)
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def flatten(root: Optional[TreeNode]) -> None:
    if not root:
        return
    
    node = root
    while node:
        # If the node has a left child
        if node.left:
            # Find the rightmost node
            rightmost = node.left
            while rightmost.right:
                rightmost = rightmost.right
            
            #update connections
            rightmost.right = node.right
            node.right = node.left
            node.left = None
        
        # move on to the right side of the tree
        node = node.right
    
