"""
Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. 
If there is no clear path, return -1.

A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell 
(i.e., (n - 1, n - 1)) such that:

All the visited cells of the path are 0.
All the adjacent cells of the path are 8-directionally connected (i.e., 
    they are different and they share an edge or a corner).
The length of a clear path is the number of visited cells of this path.

Input: grid = [
    [0,0,0],
    [1,1,0],
    [1,1,0]
]
Output: 4

Idea:
We can use BFS to find the shortest path. I think A* search will be more accurate here. But
will try BFS because its quicker to write. 

Time and Space: O(N)
"""
from typing import List
from collections import deque


def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
    N = len(grid)

    def is_clear(cell):
        return grid[cell[0]][cell[1]] == 0

    def get_neighbours(cell):
        (i, j) = cell
        directions = [(-1, -1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
        neighbors = []
        for direction in directions:
            if 0 <= i + direction[0] < N and 0 <= j + direction[1] < N and is_clear((i+direction[0], j+direction[1])):
                neighbors.append((i+direction[0], j+direction[1]))
        return neighbors

    start = (0, 0)
    goal = (N - 1, N - 1)

    queue = deque()
    if is_clear(start):
        queue.append(start)
    visited = set()
    path_len = {start: 1}

    while queue:
        cell = queue.popleft()
        if cell in visited:
            continue
        if cell == goal:
            return path_len[cell]
        visited.add(cell)
        for neighbour in get_neighbours(cell):
            if neighbour not in path_len:
                path_len[neighbour] = path_len[cell] + 1
            queue.append(neighbour)

    return -1