"""
You are given an m x n grid grid of values 0, 1, or 2, where:

each 0 marks an empty land that you can pass by freely,
each 1 marks a building that you cannot pass through, and
each 2 marks an obstacle that you cannot pass through.
You want to build a house on an empty land that reaches all buildings in the shortest total 
travel distance. You can only move up, down, left, and right.

Return the shortest travel distance for such a house. If it is not possible to build such a 
house according to the above rules, return -1.

The total travel distance is the sum of the distances between the houses of the friends and the meeting point.

The distance is calculated using Manhattan Distance, where distance(p1, p2) = |p2.x - p1.x| + |p2.y - p1.y|.

Input: grid = [
    [1,0,2,0,1],
    [0,0,0,0,0],
    [0,0,1,0,0]
]
Output: 7
Explanation: Given three buildings at (0,0), (0,4), (2,2), and an obstacle at (0,2).
The point (1,2) is an ideal empty land to build a house, as the total travel distance of 3+3+1=7 is minimal.
So return 7.


Idea:
The idea is to BFS from every house to every empty cell and sum up the distances of each 
house at each empty cell. Not all houses can visit every empty cell, meaning such an 
empty cell can't visit every house. Use a counter to see how many houses visited each 
empty cell and only use empty cells which all houses visited. Also, all houses need to 
be connected to each other for a solution. If during a BFS for a source house, we don't 
each every other house, the graph is disconnected. Return the valid empty cell with the 
min distance after all of this.

Time Complexity:
For each house, we will traverse across all reachable land. 
This will require O(O(number of zeros * number of ones)) time and 
the number of zeros and ones in the matrix is of order N * M. 
Consider that when half of the values in grid are 0 and half of the values are 1, 
total elements in grid would be (M . N) so their counts are (M . N)/2 and (M⋅N)/2 respectively, 
thus giving time complexity (M⋅N)/2⋅(M⋅N)/2, that results in O(N2 ⋅ M2).

Space Complexity: O(N⋅M)
"""
from typing import List
from math import isinf, inf
from collections import deque


def shortestDistance(grid: List[List[int]]) -> int:
    totalDist = [[[0, 0] for _ in range(len(grid[0]))] for _ in range(len(grid))] # sum, buildingCount
    numBuildings = sum(1 for row in grid for col in row if col == 1)
    
    def bfs(y, x):
        queue = deque()
        queue.append((y,x,0))
        visited = set()
        buildingsVisited = 0
        
        while queue:
            y, x, dist = queue.popleft()
            if not (0 <= y < len(grid)) or not (0 <= x < len(grid[0])):
                continue
            if grid[y][x] == 2:
                continue
            if (y,x) in visited:
                continue
            
            visited.add((y,x))
                
            if grid[y][x] == 1:
                buildingsVisited += 1
                if dist != 0:
                    continue
            
            if grid[y][x] == 0:
                totalDist[y][x][0] += dist
                totalDist[y][x][1] += 1
            
            for dy, dx in ((-1,0),(1,0),(0,-1),(0,1)):
                queue.append((y+dy,x+dx, dist+1))
        
        return buildingsVisited == numBuildings
    
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == 1:
                if not bfs(y,x):
                    return -1
            
    minDist = float(inf)
    for row in totalDist:
        for dist, buildingCount in row:
            if buildingCount != numBuildings:
                continue
            minDist = min(minDist, dist)
    
    return -1 if isinf(minDist) else minDist