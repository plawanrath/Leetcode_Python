"""
Input 
    4
  /   \
  2    5
 / \
1   3

lowstCommonAncestor(1, 5) - 4

**Caveat: In the tree also store the parent of a node

There are 3 possible cases:

1. There could be an equal distance between p and q
2. p has a longer distance to travel than q to reach LCA
3. q has a longer distance to travel than p to reach LCA

So we could simply traverse from both p and q and store the visited node in a set. If we come across a node that we previously visited,
that essentially means that we fould the common ancestor. 

lowstCommonAncestor(1, 5)
seen = {}

while p:
    1. p = 1
    seen = {1}
    2. p = 2
    seen = {1, 2}
    3. p = 4 
    seen = {1, 2, 4}

while q:
    1. q = 5
    seen = {1, 2, 4, 5}
    2. q = 4
    q is in seen so return q

return 4 which is the LCA.
"""

class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None
        self.parent = None



def lowestCommonAncestorParent(p: 'Node', q: 'Node') -> 'Node':
    seen = set()

    while p:
        seen.add(p)
        p = p.parent
    
    while q:
        if q in seen:
            return q
        q = q.parent
    return None


"""
Find LCA when parent is not given in the Node. In this root will also be passed to the function.
If we cannot pass root to the function then we should convert this Tree into the above tree where the tree node also has the parent. Then use approach 1.

Since we know that p and q will definitely exist, traverse the tree in DFS. When we encounter either p or q, return a boolean
denoting that we found the nodes. THe LCA would then be the node from which both the subtree recursions returned True. 

This is a backtracking problem.

Input 
    4
  /   \
  2    5
 / \
1   3

lowstCommonAncestor(1, 5)
    dfs(4)
        - left, left_res = dfs(2)
            - left, left_res = dfs(1)
                - node = 1, p = 1, q = 1.
                    since node == 1, return 1, False
              left = 1, left_res = False
            - right, right_ree = dfs(3)
                - node = 3, p = 1, q = 5
                    elif left will be True
                        return 1, False
              right = 1, right_res = False
            node = 2, left = 1, left_res = False, right = 1, right_res = False
            - if left and right:  -> True:
                return 2, True
        - left = 2, left_res = True
        - right, right_res = dfs(5)
            - node = 5, p = 1, q = 5
                since node == q return 5, False
        - right = 5, right_res = False
        node = 4, left = 2, left_res = True, right = 5, right_res = False
        - if left and right: -> True
            return 4, True

That will give you 4 which is the LCA.

Complexity: O(n) time and O(N) space used by the recursion call stack.
"""
class Node2:
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None


def lowestCommonAncestor(root: 'Node2', p: 'Node2', q: 'Node2') -> 'Node2':
    def dfs(node): # DFS will return a tuple of a parent node and if its LCA or not
        if not node:
            return (None, False)
        left, left_res = dfs(node.left)
        right, right_res = dfs(node.right)

        if node == p or node == q: # node is either p or q and also maybe the parent of whichever != node
            return node, right or left
        if left and right: # The situation where p and q are both children of a node
            return node, True
        elif left: # Found something on the left side, propagating up
            return left, left_res
        else: # Found something on the right side, propagating up
            return right, right_res

    res_node, isLCA = dfs(root)
    if not isLCA: 
        return None
    return res_node