"""
Given a 2D matrix matrix, handle multiple queries of the following type:

Calculate the sum of the elements of matrix inside the rectangle defined by its upper 
left corner (row1, col1) and lower right corner (row2, col2).

Implement the NumMatrix class:

1. NumMatrix(int[][] matrix) Initializes the object with the integer matrix matrix.
2. int sumRegion(int row1, int col1, int row2, int col2) Returns the sum of the elements of 
matrix inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).

Idea:
This problem brings up one of the characteristics of a 2D matrix: the sum of the elements in any 
rectangular range of a matrix (M) can be defined mathematically by the overlap of four other 
rectangular ranges that originate at M[0][0].

The sum of the rectangle (0,0)->(i,j) is equal to the cell (i,j), plus the rectangle (0,0)->(i,j-1), 
plus the rectangle (0,0)->(i-1,j), minus the rectangle (0,0)->(i-1,j-1). We subtract the last 
rectangle because it represents the overlap of the previous two rectangles that were added.

Approach: Dynamic Programming

With this information, we can use a dynamic programming (DP) approach to build a prefix sum matrix (dp) 
from M iteratively, where dp[i][j] will represent the sum of the rectangle (0,0)->(i,j). 
We'll add an extra row and column in order to prevent out-of-bounds issues at i-1 and j-1 
(similar to a prefix sum array), and we'll fill dp with 0s.

At each cell, we'll add its value from M to the dp values of the cell on the left and the one above, 
which represent their respective rectangle sums, and then subtract from that the top-left diagonal value, 
which represents the overlapping rectangle of the previous two additions.

Then, we just reverse the process for sumRegion(): We start with the sum at dp[R2+1][C2+1] 
(due to the added row/column), then subtract the left and top rectangles before adding back 
in the doubly-subtracted top-left diagonal rectangle.

Time Complexity:
constructor: O(M * N) where M and N are the dimensions of the input matrix
sumRegion: O(1)

Space Complexity:
constructor: O(M * N) for the DP matrix
constructor: O(1) if you're able to modify the input and use an in-place DP approach
sumRegion: O(1)
"""
from typing import List


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        ylen, xlen = len(matrix) + 1, len(matrix[0]) + 1
        self.dp = [[0] * xlen for _ in range(ylen)]
        for i in range(1, ylen):
            for j in range(1, xlen):
                self.dp[i][j] = matrix[i-1][j-1] + self.dp[i-1][j] + self.dp[i][j-1] - self.dp[i-1][j-1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.dp[row2+1][col2+1] - self.dp[row2+1][col1] - self.dp[row1][col2+1] + self.dp[row1][col1]