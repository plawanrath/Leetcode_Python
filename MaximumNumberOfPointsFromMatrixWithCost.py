"""
You are given an m x n integer matrix points (0-indexed). Starting with 0 points, 
you want to maximize the number of points you can get from the matrix.

To gain points, you must pick one cell in each row. Picking the cell at coordinates 
(r, c) will add points[r][c] to your score.

However, you will lose points if you pick a cell too far from the cell that you picked 
in the previous row. For every two adjacent rows r and r + 1 (where 0 <= r < m - 1), 
picking cells at coordinates (r, c1) and (r + 1, c2) will subtract abs(c1 - c2) from your score.

Return the maximum number of points you can achieve.

Input: points = 
[
    [1,2,3],
    [1,5,1],
    [3,1,1],
]
Output: 9
Explanation:
The blue cells denote the optimal cells to pick, which have coordinates (0, 2), (1, 1), and (2, 0).
You add 3 + 5 + 3 = 11 to your score.
However, you must subtract abs(2 - 1) + abs(1 - 0) = 2 from your score.
Your final score is 11 - 2 = 9.

Idea:
Find prefix and suffix for each row
then at each iteration find the max from both array and adding in current row values.
For index j in current row :
curr[j] = max(left[j],right[j])+points[i][j]
then
pre = curr[:]

For a certain index j, the maximum value could from its left, or right(including itself). 
Thus we build two arrays, left, right, and focus on the maximum value only coming from its left or right.
"""
from typing import List


def maxPoints(points: List[List[int]]) -> int:
    m = len(points)
    n = len(points[0])
    
    if m==1:
        return max(points[0])
    
    if n==1:
        s=0
        for j in range(m):
            s+=points[j][0]
        return s
    
    def lt(row):
        left = [ele for ele in row]
        for i in range(1,len(left)):
            left[i] = max(left[i], left[i-1]-1)
        return left
    
    def rt(row):
        right = [ele for ele in row]
        for i in range(len(row)-2,-1,-1):
            right[i] = max(right[i],right[i+1]-1)
        return right
    
    pre  = points[0]
    for i in range(1,m):
        left = lt(pre)
        right= rt(pre)
        curr = [0 for _ in range(n)]
        for j in range(n):
            curr[j] = points[i][j]+max(left[j],right[j])    
        pre = curr[:]
                    
    return max(pre)