from typing import List
"""
You are given an n x n binary matrix grid. You are allowed to change at most one 0 to be 1

Return size of largest island after this operation 

Grid:
[
    [1, 0],
    [0, 1]
]
Result = 3

If we change one of the 0s to 1s we will get an island of size 3.

Naive DFS (very slow): FOr each 0 change that to 1 and then run DFS to find island size. Record the maxsize 
this way.

1. I will use a dictionary to remember the size of an island by a unique id - Dictionary will store {id, sizeOfIsland}
2. I will use dfs to get the size but I will also add the unique island id into the gtid itself. This will help us find the largest island later.
3. Then for each 0 use a seen dictionary to look at the neighboring group ids and add the area of those groups + 1 for the 0 we are toggling (the single operation of changing a 0 to 1)
4. Take the maximum of above

Grid:
[
    [1, 0],
    [0, 1]
]

area = {}
index = 2
for r and c in grid:
    1. grid[0][0] == 1 ? Yes:
        area[2] = dfs(0, 0, 2) --- inside dfs ---
            res = 1
            grid = [[2, 0], [0, 1]]
            for nr and nc in neighbors:
                First neighbor: nr = 0, nc = 1
                grid[0][1] == 1 ? -> No:
                Second neighbor: nr = 1, nc = 0
                grid[1][0] == 1 ? -> No:
            return 1 ------- end dfs ------
        area[2] = 1
        index = 3
    2. grid[0][1] == 1 ? No
    3. grid[1][0] == 1 ? No
    4. grid[1][1] == 1 ? Yes:
        area[3] = dfs(1, 1, 3) ----- inside dfs ------
        res = 1
        grid[1][1] = 3 i.e. grid = [[2, 0], [0, 3]]
        for nr and nc in neighbors:
            First neighbor: 
                grid[0][1] == 1 ? -> No
            Second neighbor:
                grid[1][0] == 1 ? -> No
        return 1 ---- end dfs ------
        area[3] = 1
        index = 4

        ans = max(area.values()) = 1
        grid = [[2, 0], [0, 3]]
        for r and c in grid:
            1. grid[0][0] == 0 ? - No
            2. grid[0][1] == 0 ? - Yes
                seen = {2, 3} i.e. grid[nr][nc] where neighbors have an island id
                answer = max(ans, 1 + sum(area[all seen]))
                answer = max(1, 1 + sum([1, 1]))
                answer = max(1, 1 + 2)
                answer = 3
            3. grid[1][0] == 0 ? - Yes
                Same as 2 will return 3 as answer
            4. grid[1][1] == 0 ? - No
return 3

Complexity: O(n^2) time and space O(n^2) which is because we use area and call stack of recursive DFS
"""

def largestIsland(grid: List[List[int]]) -> int:
    directions = [[0,1], [0,-1], [1,0], [-1,0]]
    
    def neighbors(r, c):
        for dr, dc in directions:
            if 0 <= r+dr < len(grid) and 0 <= c+dc < len(grid):
                yield r+dr, c+dc
    
    def dfs(r, c, index):
        res = 1 # size of island is 1 when we start
        # update the grid value with the unique undex for that group marking it as seen
        grid[r][c] = index
        for nr, nc in neighbors(r, c):
            if grid[nr][nc] == 1:
                res += dfs(nr, nc, index)
        return res
    
    area = {}
    # since 0 and 1 denote land and water, let's start the unique group id index from 2
    index = 2
    for r in range(len(grid)):
        for c in range(len(grid)):
            if grid[r][c] == 1:
                area[index] = dfs(r, c, index)
                index += 1
    
    ans = max(area.values()) if area else 0
    for r in range(len(grid)):
        for c in range(len(grid)):
            if grid[r][c] == 0:
                seen = {grid[nr][nc] for nr, nc in neighbors(r, c) if grid[nr][nc] > 1}
                ans = max(ans, 1 + sum(area[i] for i in seen))
    return ans

