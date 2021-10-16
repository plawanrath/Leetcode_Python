"""
Given a m * n matrix of ones and zeros, return how many square submatrices have all ones.

Take an example of this matrix:
0 1 1 1
1 1 1 1
0 1 1 1

Maintain a running counter of length of each 2x2 square, and store the length of the square on the bottom right corner of each of those squares.

Starting at cell (1, 1), get length of the square -> min(value at (0,1), value at (1,0), value at (0,0)) + 1 = 1
As you navigate through the rest of the matrix, the matrix becomes:
0 1 1 1
1 1 2 2
0 1 2 3
Sum up all the values = 15
"""
from typing import List


def countSquares(matrix: List[List[int]]) -> int:
    m = len(matrix)
    n = len(matrix[0])
    count = 0
    # First row and first column can have only 1 possible option for sqare which is of length 1
    for i in range(m):
        if matrix[i][0]:
            count += 1
    for j in range(1, n): # We need to start j from 1 becuase if we start j from 0 and 
        # let's say (0,0) has a 1 then that square could end up being counted twice
        if matrix[0][j]:
            count += 1

    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][j]:
                # the min checks if there are any 0s surrounding the 1 then it cannot be a bigger square 
                length = min(matrix[i-1][j], matrix[i-1][j-1], matrix[i][j-1]) + 1 
                matrix[i][j] = length # update this length because we will use this length to make bigger squares
                count += length
    return count
