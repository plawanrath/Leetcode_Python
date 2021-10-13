"""
Given an m x n matrix, return true if the matrix is Toeplitz. Otherwise, return false.

A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same elements.

Input: matrix = [
    [1,2,3,4],
    [5,1,2,3],
    [9,5,1,2]
    ]
Output: true
Explanation:
The diagonals are:
"[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]".
In each diagonal all elements are the same, so the answer is True.
"""
from typing import List


def isToeplitzMatrix(matrix: List[List[int]]) -> bool:
    row=len(matrix)
    col=len(matrix[0])
    
    if row==1 or col==1:
        return True
    
    c=0
    while c<col:
        check=matrix[0][c]
        x,y=1,c+1
        while x <row and y<col:
            if matrix[x][y]!=check:
                return False
            x+=1
            y+=1
        c+=1
    
    r=1
    while r<row:
        check=matrix[r][0]
        x=r+1
        y=1
        while x<row and y<col:
            if matrix[x][y]!=check:
                return False
            x+=1
            y+=1
        r+=1
    
    return True