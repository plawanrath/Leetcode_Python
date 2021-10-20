from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right
    
"""
   -10
  /   \
  9    20
      /  \ 
     15   7

max path = 15 -> 20 -> 7
max path sum = 15 + 20 + 7 = 42


Recursion: function that takes a node and computes the maximum sum including that node and zero or more modes of its subtrees.
But at each step we should also check if we should continue the current path or start a new path with current node as the highest node
in the new path. 

Caveats:
    For a single node the return value is the value of the node
    For a tree with all negative numbers, the best path will actually be the largest number in the whole tree. Adding 
    any other negative number to that number only makes it smaller. 

    This means that when we look at left and right branches of a node, if those don't lead to any gains then we can ignore them.
    For example:

        4
      /   \
     -3    -2

     Adding -3 or -2 to 4 will only reduce the value. This means that if the sum of all nodes on either of the branches of a particular node
     are less than 0 then that means that the branch is not worth exploring.

global maxSum = -inf
newMax = val + left + right --> Update maxSum at each step with max(maxSum, newMax)
recursion: val + max(left_subtree, right_subtree)

maxGain(-10)
 - newMax = val + left + right = -10 + maxGain(9) + maxGain(20)
 - maxGain(9)
    - newMax = 9 (since no left and right) 
    - maxSum = max(maxSum, newMax) = max(9, -inf) = 9
    - return val + max(left_subtree, right_subtree) = 9
 - maxGain(20)
   - newMax = val + left + right = 20 + maxGain(15) + maxGain(7)
   - maxGain(15)
     - newMax = 15
     - maxSum = max(maxSum, 15) = max(9,15) = 15
     - return val + max(left_subtree, right_subtree) = 15 
   - maxGain(7)
     - newMax = 7
     - maxSum = 15
     - return val + max(left_subtree, right_subtree) = 7 
   
   newMax = 20 + 15 + 7 = 42
   maxSum = max(15, 42) = 42
   return val + max(left_subtree, right_subtree) = 20 + max(15, 7) = 20 + 15 = 35

  
  newPath = -10 + 9 + 42 = 41
  maxSum = max(42, 41)
  return val + max(left_subtree, right_subtree) = -10 + max(maxGain(9), maxGain(20)) = -10 + max(9, 35) = 25
   

"""

def maxPathSum(root: Optional[TreeNode]) -> int:
    def maxGain(node: TreeNode) -> int:
        nonlocal maxSum
        if not node:
            return 0
        
        leftGain = max(maxGain(node.left), 0)
        rightGain = max(maxGain(node.right), 0)

        newMax = node.val + leftGain + rightGain
        maxSum = max(maxSum, newMax)

        return node.val + max(leftGain, rightGain)

    maxSum = float("-inf")
    maxGain(root)
    return maxSum
