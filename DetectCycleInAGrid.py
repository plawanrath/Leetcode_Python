"""
Given a 2D array of characters grid of size m x n, you need to find if there exists any cycle 
consisting of the same value in grid.

Return true if any cycle of the same value exists in grid, otherwise, return false.

Approach:
At each point (i, j) in grid, do following:

Start DFS from (i, j).
The trick was to keep track of the previous element so that you don't go back there wihle doing dfs
Only visit a point if it has same character as starting position
If you still reach a visited point again, there is a cycle.
"""
from typing import List


def containsCycle(A: List[List[str]]) -> bool:
    R, C = len(A), len(A[0])
    visited = set()
    
    def neighbors(r, c):
        return [(i, j) for i, j in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)] if 0 <= i < R and 0 <= j < C and A[i][j] == A[r][c]]
    
    def dfs(r, c, x, prev, seen):
        if (r, c) in seen:
            return True
        seen.add((r, c))
        visited.add((r, c))

        for i, j in neighbors(r, c):
            if not prev or prev != (i, j):
                if dfs(i, j, x, (r, c), seen):
                    return True
        return False
        
    
    for r in range(R):
        for c in range(C):
            if (r, c) not in visited:
                seen = set()
                if dfs(r, c, A[r][c], None, seen):
                    return True
    return False