"""
Given the root of a binary tree, return the vertical order traversal of its nodes' values.

For each node at position (row, col), its left and right children will be at positions (row + 1, col - 1) and (row + 1, col + 1) respectively. The root of the tree is at (0, 0).

The vertical order traversal of a binary tree is a list of top-to-bottom orderings for each column index starting from the leftmost column and ending on the rightmost column. T
here may be multiple nodes in the same row and same column. In such a case, sort these nodes by their values.

Input Tree
    3
  /   \
  9    20
        / \
        15  7
Output: [[9],[3,15],[20],[7]]

Approach:
1. Use BFS to traverse the tree and record (col, row, val) into a list so that we can later sort.
2. Globally sort the list after BFS is done .
3. Then we can group them correctly partitioned by column index. We can use an ordered dict since that maintains a dictionary sorted by key


Example:

At the end of BFS, node_list:
[(0, 0, 3), (-1, 1, 9), (1, 1, 20), (0, 2, 15), (2, 2, 7)]

After Sorting, node_list:
[(-1, 1, 9), (0, 0, 3), (0, 2, 15), (1, 1, 20), (2, 2, 7)]

At step 3, ordered Dict will have:
OrderedDict([(-1, [9]), (0, [3, 15]), (1, [20]), (2, [7])])

Then we can simply return the values of ordered Dict:
[[9],[3,15],[20],[7]]

Why is this sorting and orderedDict required ?

Example:
    1
  /   \
  2    3
 / \   / \
4   6  5  7

This tree, without sorting will return:
[[4],[2],[1,6,5],[3],[7]]

With sorting and orderedDict usage will return:
[[4],[2],[1,5,6],[3],[7]]

When 2 nodes are in the same position, its required that they be sorted. This order is inherently maintained in a BST but may not be for a random Binary Tree.

Time Complexity: O(n log n), Space: O(n)
"""
from typing import List
from collections import deque, OrderedDict


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def verticalOrderSorted(root: TreeNode) -> List[List[int]]:
    if not root:
        return []

    q = deque([(root, 0, 0)])
    node_list = []
    while q:
        node, row, col = q.popleft()
        if not node:
            continue
        node_list.append((col, row, node.val))
        q.append((node.left, row + 1, col - 1))
        q.append((node.right, row+1, col+1))
    
    node_list.sort()

    ans = OrderedDict()
    for col, row, val in node_list:
        if col in ans:
            ans[col].append(val)
        else:
            ans[col] = [val]
    
    return ans.values()
