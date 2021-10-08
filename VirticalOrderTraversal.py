"""
Given the root of a binary tree, return the vertical order traversal of its nodes' values.

Input Tree
    4
  /   \
  2    5
 / \
1   3

Output: [[1], [2], [4,3], [5]]

Approach: 
1. Use BFS to traverse. WHen traversing with BFS, in the queue store node value and column index value. 
2. We can also keep track of the range of column indices using let's say min_index and max_index.
3. At the end of the BFS traversal bacisally we will walk through the column range [min_index, max_index] and add to
result accordingly.

Tree:
    4
  /   \
  2    5
 / \
1   3

verticalTraversal(4)
    vertical_order = {}, queue = [(4, 0)], min_column = 0, max_column = 0
    while queue:
        1. node, column = 4, 0
           min_column, max_column = 0, 0
           virtical_order = {0: [4]}
           queue = [(2, -1), (5, 1)]
        2. node, column = 2, -1
           min_column, max_column = -1, 0
           vertical_order = {0: [4], -1: [2]}
           queue = [(5, 1), (1, -2), (3, 0)]
        3. node, column = 5, 1
           virtical_order = {0: [4], -1: [2], 1: [5]}
           queue = [(1, -2), (3, 0), (None, 0), (None, 2)]
        4. node, column = 1, -2
           virtical_order = {0: [4], -1: [2], 1: [5], -2: [1]}
           queue = [(3, 0), (None, 0), (None, 2), (None, -3), (None, -1)]
        5. node, column = 3, 0
           virtical_order = {0: [4, 3], -1: [2], 1: [5], -2: [1]}
           queue = [(None, 0), (None, 2), (None, -3), (None, -1), (None, -1), (None, 1)]
        Since all the next values in queue are None, the loop will just continue in the "if not node" condition
        until queue is empty.
        Return: [[1], [2], [4, 3], [5]]

TIme complexity: O(n), space complexity: O(n)
""" 
from collections import defaultdict
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def verticalTraversal(root: TreeNode):
    if root is None:
        return []
    vertical_order = defaultdict(list) # Dict that will store list of node values by column
    queue = deque([(root, 0)])
    min_column = max_column = 0
    while queue:
        node, column = queue.popleft()
        if not node: 
            continue
        min_column, max_column = min(min_column, column), max(max_column, column)
        vertical_order[column].append(node.val)
        queue.append((node.left, column-1)) 
        queue.append((node.right, column+1))
    return [vertical_order[column] for column in range(min_column, max_column+1)]