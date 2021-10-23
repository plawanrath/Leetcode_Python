"""
In a given 2D binary array grid, there are two islands.  (An island is a 4-directionally connected group 
of 1s not connected to any other 1s.)

Now, we may change 0s to 1s so as to connect the two islands together to form 1 island.

Return the smallest number of 0s that must be flipped.  (It is guaranteed that the answer is at least 1.)

Input: grid = [
    [0,1,0],
    [0,0,0],
    [0,0,1]
]
Output: 2

Idea: DFS

1. Paint the first encountered island with the color '2'
2.. Start expanding this island by painting connected 'empty' cells
3. For every successive round, increase value of 'color' by 1 (This helps us keep track of the number of steps required)
4. End when we bump into an island i.e. when we encounter a cell with value '1' (original island which wasn't colored '2')
5. The answer is the difference of the current color value and '2' (the starting color)
"""
from typing import List


def shortestBridge(A: List[List[int]]) -> int:
    if not A:
        return 0
    m, n, flag = len(A), len(A[0]), False

    # Assigining '2' to one of the islands
    def paint(i, j):
        if i >= len(A) or i < 0 or j < 0 or j >= len(A[0]) or A[i][j] == 0 or A[i][j] == 2:
            return
        A[i][j] = 2
        for nb in [(0,1),(0,-1),(1,0),(-1,0)]:
            paint(i + nb[0], j + nb[1])

    # expanding from the perimeter of the island & incrementing color with every next outward move
    def expand(i, j, color):
        if i >= len(A) or i < 0 or j < 0 or j >= len(A[0]):
            return False
        if A[i][j] == 0:
            A[i][j] = color + 1
        return A[i][j] == 1

    
    # Finding and coloring the first encountered island
    for i in range(m):
        if flag:
            break
        for j in range(n):
            if A[i][j] == 1:
                paint(i, j)
                flag = True
                break
    
    # Growing outward and tracking number of steps taken to bump into other island
    for color in range(2, 2+m+n+1):
        for i in range(m):
            for j in range(n):
                if A[i][j] == color and (expand(i-1, j, color) or expand(i, j+1, color) or
                                            expand(i+1, j, color) or expand(i, j-1, color)):
                    return color-2