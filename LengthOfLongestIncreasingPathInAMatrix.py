"""
Given an m x n integers matrix, return the length of the longest increasing path in matrix.

Input: matrix = [
    [9,9,4],
    [6,6,8],
    [2,1,1]
]
Output: 4
Explanation: The longest increasing path is [1, 2, 6, 9].

Idea: DFS + memorization
Keep track of the longest path for each coordinates that we've already visited in a cache. 
If we encounter them again in the future we can just do a O(1) lookup in the cache.

Time and Space: O(N*M)
"""
from typing import List


def longestIncreasingPath(matrix: List[List[int]]) -> int:
    if not matrix:
        return 0
    
    longest_path = 0
    rows = len(matrix)
    cols = len(matrix[0])
    cache = [[None] * cols for _ in range(rows)]
    
    def dfs(x: int, y: int) -> int:
        if cache[x][y]:
            return cache[x][y]
        longest_path = 0
        for i, j in [(0,1),(0,-1),(1,0),(-1,0)]:
            newX, newY = x+i, y+j
            if newX >= 0 and newX < rows and newY >= 0 and newY < cols and matrix[newX][newY] > matrix[x][y]:
                longest_path = max(longest_path, dfs(newX, newY))
        cache[x][y] = longest_path + 1
        return cache[x][y]
    
    for x in range(rows):
        for y in range(cols):
            longest_path = max(longest_path, dfs(x, y))
    
    return longest_path