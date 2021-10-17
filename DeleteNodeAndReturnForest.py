"""
Given the root of a binary tree, each node in the tree has a distinct value.

After deleting all nodes with a value in to_delete, we are left with a forest (a disjoint union of trees).

Return the roots of the trees in the remaining forest. You may return the result in any order.

Input Tree
    1
  /   \
  2    3
 / \   / \
4   5  6  7

Input: root = [1,2,3,4,5,6,7], to_delete = [3,5]
Output: [[1,2,null,4],[6],[7]]

Approach: DFS

Example:
Input: root = [1,2,3,4,5,6,7], to_delete = [3,5]
Input Tree
    1
  /   \
  2    3
 / \   / \
4   5  6  7

delNodes(1, [3, 5])
    forest = {TreeNode(1)}
    check_node(1)------- Inside checkNode 1 -----
        node.val = 1 is not in to_delete ---> Go to else
            node.left = check_node(2)------------- Inside checkNode(2) ------------
                node.val = 2 not in to_delete --> Go to else
                    node.left = check_node(4)---------------- Inside checkNode(4) ----------
                        node.val = 4 is not in to_delete --> go to else
                            node = 4 does not have left or right child so return 4
                        ---------------- Return checkNode(4) = 4 ----------
                    node.left = 4
                    node.right = check_node(5)---------------- Inside checkNode(5) ----------
                        node.val = 5 is in to_delete ----> enter if
                            forest -= {5} i.e. forest = {TreeNode(1)} -- no-op
                            if node.left -----> No
                            if node.right -----> No
                            return None
                        ---------------- Return checkNode(5) = None ----------
                    node.right = None
                ---------------- Return checkNode(2) = 2 ----------
            node.left = 2
            node.right = check_node(3)------------- Inside checkNode(3) ------------
                node.val = 3 is in to_delete ----> enter if
                    forest -= {3} i.e. forest = {TreeNode(1)} --- no-op
                    if ndoe.left ---> Yes
                        forest = {TreeNode(1), TreeNode(6)}
                        node.left = check_node(6)------------- Inside checkNode(6) ------------
                            node.val = 6 is not in to_delete
                            does not have left or right child so return 6
                        ---------------- Return checkNode(6) = 6 ----------
                    node.left = 6
                    if node.right ---> Yes
                        forest = {TreeNode(1), TreeNode(6), TreeNode(7)}
                        node.right = check_node(7)------------- Inside checkNode(7) ------------
                            node.val = 7 is not in to_delete
                            does not have left or right child so return 7
                            ---------------- Return checkNode(7) = 7 ----------
                    node.right = 7
                return None
            ---------------- Return checkNode(3) = None ----------
    ---------------- Return checkNode(1) = 1 ----------
Forest = {TreeNode(1), TreeNode(6), TreeNode(7)}


"""
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def delNodes(root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
    to_delete = set(to_delete)
    forest = {root} # Set of nodes in forest

    def check_node(node: TreeNode):
        nonlocal forest
        if node:
            if node.val in to_delete:
                forest -= {node} # this operation will delete from forest if a node is present otherwise no-op
                if node.left:
                    forest.add(node.left)
                    node.left = check_node(node.left)
                if node.right:
                    forest.add(node.right)
                    node.right = check_node(node.right)
                return None
            else:
                if node.left:
                    node.left = check_node(node.left)
                if node.right:
                    node.right = check_node(node.right)
                return node
    
    check_node(root)
    return list(forest)
