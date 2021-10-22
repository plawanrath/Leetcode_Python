"""
Given an m x n binary grid grid where each 1 marks the home of one friend, return the minimal total travel distance.

The total travel distance is the sum of the distances between the houses of the friends and the meeting point.

The distance is calculated using Manhattan Distance, where distance(p1, p2) = |p2.x - p1.x| + |p2.y - p1.y|.

Input: grid = [
    [1,0,0,0,1],
    [0,0,0,0,0],
    [0,0,1,0,0]
]
Output: 6
Explanation: Given three friends living at (0,0), (0,4), and (2,2).
The point (0,2) is an ideal meeting point, as the total travel distance of 2 + 2 + 2 = 6 is minimal.
So return 6.

Brute Force: A brute force approach is to evaluate all possible meeting points in the grid. 
We could apply breadth-first search originating from each of the point.

Idea:
Median minimizes the absolute distance of points. 
We simply find the list of x and y co-ordinates where we have a building. Then we 
individually sort them to find the median element in each list. 
This is the point which is closest meeting point.

To find the total walking distance, simply add abs(x_median-x) and abs(y_median-y) to the final result. 
Note it doesnt matter that we sorted the co-ordinate lists since the order in which we add does not matter.

Time Complexity: O(MN)
Space: O(M+N) for coordinates
"""
from typing import List


def minTotalDistance(grid: List[List[int]]):
    def getBuildingPoints():
        coordinates = []
        for i in range(grid):
            for j in range(grid[0]):
                if grid[i][j] == 1:
                    coordinates.append((i,j))
        return coordinates
    
    def getMedianCoordinates(rows, cols):
        # rows, cols = list(zip(*coordinates))
        rows.sort()
        cols.sort()
        x_median, y_median = rows[len(rows)//2], cols[len(cols)//2]
        return x_median, y_median
    
    result = 0
    coordinates = getBuildingPoints()
    rows, cols = list(zip(*coordinates))
    row_median, col_median = getMedianCoordinates(rows, cols)

    for x in rows:
        result += abs(row_median - x)
    for y in cols:
        result += abs(col_median - y)
    return result
