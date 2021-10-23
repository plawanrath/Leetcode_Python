"""
You are given an n x n integer matrix grid where each value grid[i][j] 
represents the elevation at that point (i, j).

The rain starts to fall. At time t, the depth of the water everywhere is t. 
You can swim from a square to another 4-directionally adjacent square if and only 
if the elevation of both squares individually are at most t. You can swim infinite distances in zero time.
Of course, you must stay within the boundaries of the grid during your swim.

Return the least time until you can reach the bottom right square (n - 1, n - 1) 
if you start at the top left square (0, 0).

Input: grid = [
    [0,2],
    [1,3]
]
Output: 3
Explanation:
At time 0, you are in grid location (0, 0).
You cannot go anywhere else because 4-directionally adjacent neighbors have a higher elevation than t = 0.
You cannot reach point (1, 1) until time 3.
When the depth of water is 3, we can swim anywhere inside the grid.

Idea:
Whether the swim is possible is a monotone function with respect to time, 
so we can binary search this function for the correct time: the smallest T for which the swim is possible.

Say we guess that the correct time is T. To check whether it is possible, we perform a 
simple DFS where we can only walk in squares that are at most T.

Time: O(N^2 log N), Space: O(N^2)
"""
def swimInWater(grid):
    N = len(grid)

    def possible(T):
        stack = [(0, 0)]
        seen = {(0, 0)}
        while stack:
            r, c = stack.pop()
            if r == c == N-1: return True
            for cr, cc in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):
                if (0 <= cr < N and 0 <= cc < N
                        and (cr, cc) not in seen and grid[cr][cc] <= T):
                    stack.append((cr, cc))
                    seen.add((cr, cc))
        return False

    lo, hi = grid[0][0], N * N
    while lo < hi:
        mi = (lo + hi) // 2
        if not possible(mi):
            lo = mi + 1
        else:
            hi = mi
    return lo