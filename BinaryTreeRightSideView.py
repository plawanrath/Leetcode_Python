"""
Given the root of a binary tree, imagine yourself standing on the right side of it, 
return the values of the nodes you can see ordered from top to bottom.


Input Tree
    4
  /   \
  2    5
 / \
1   3
Output: [4, 5, 3]

Approach:
Run a BFS and keep track of levels. Use a map of levels to node and simply replace the nodes
on a level. Since BFS goes left to right on a level, you will eventually get the right side view
when you return the dictionary values.

rightSideView(4)
    queue = [(4, 0)], levelMap = {}
    while queue:
        1. node, level = 4, 0
           levelMap = {0: 4}
           queue = [(2, 1), (5, 1)]
        2. node, level = 2, 1
           levelMap = {0: 4, 1: 2}
           queue = [(5, 1), (1, 2), (3, 2)]
        3. node, level = 5, 1
           levelMap = {0: 4, 1: 5}
           queue = [(1, 2), (3, 2), (None, 2), (None, 2)]
        4. node, val = 1, 2
           levelMap = {0: 4, 1: 5, 2: 1}
           queue = [(3, 2), (None, 2), (none, 2), (None, 3), (None, 3)]
        5. node, val = 3, 2
           levelMap = {0: 4, 1: 5, 2: 3}
           queue = [(None, 2), (none, 2), (None, 3), (None, 3), (None, 3), (None, 3)]
        All the None values in the queue will just continue in "if not node" condition.
        return [4, 5, 3]

Time complexity: O(n)
Space Complecity: O(n)
"""
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def rightSideView(root):
    if not root:
        return None
    
    queue = deque([(root, 0)])
    levelMap = {}
    while queue:
        node, level = queue.popleft()
        if not node:
            continue
        levelMap[level] = node.val
        queue.append((node.left, level + 1))
        queue.append((node.right, level + 1))
    return levelMap.values()