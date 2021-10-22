"""
ou are given an m x n binary matrix grid. An island is a group of 1's (representing land) 
connected 4-directionally (horizontal or vertical.) You may assume all four edges of the 
grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.

Approach:
We want to know the area of each connected shape in the grid, then take the maximum of these.
We can find the area by doing a DFS from a 1 and going in all directions until we hit 0.

O(R * C) will be the time and space complexity
"""

def maxAreaOfIsland(grid):
    seen = set()
    def area(r, c):
        if not (0 <= r < len(grid) and 0 <= c < len(grid[0])
                and (r, c) not in seen and grid[r][c]):
            return 0
        seen.add((r, c))
        return (1 + area(r+1, c) + area(r-1, c) +
                area(r, c-1) + area(r, c+1))

    return max(area(r, c)
                for r in range(len(grid))
                for c in range(len(grid[0])))