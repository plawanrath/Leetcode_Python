"""
Given a root of a BST and two integers low and high, return sum of values
of all nodes that fall within that range(range inclusive)

Input BST
    4
  /   \
  2    5
 / \
1   3

low = 3, high = 5
return 3 + 4 + 5 = 12

rangeSumBST(root=Node(4), low = 3, high=5)

sum = 0
dfs(4)
    - low <= 4 <= high (4 is between 3 and 5 inclusive)
        - sum = 0 + 4 = 4
    - low < node.val ? -> 3 < 4 -> True
        - dfs(2)
            - low <= 2 <= high ? -> No (2 is not in between 3 and 5)
            - low < 2 ? -> No
            - high > 2 -> Yes (5 is > 2)
                - dfs(3)
                    - low <= 3 <= high -> Yes (3 is between 3 and 5 inclusive)
                        - sum = 4 + 3 = 7
                    return
            return
    - high > node.val ?  -> 5 > 4 ? -. Yes
        - dfs(5)
            - low <= 5 <= high -> Yes (5 is between 3 and 5 inclusive)
                - sum = 7 + 5 = 12
        return 12

return 12

Complexity O(n) time and space because of space taken by call stack.
"""

class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None


def rangeSumBST(root: Node, low: int, high: int) -> int:
    def dfs(node: Node):
        nonlocal sum
        if node:
            if low <= node.val <= high:
                sum += node.val
            if low < node.val:
                dfs(node.left)
            if high > node.val:
                dfs(node.right)
    
    sum = 0
    dfs(root)
    return sum
