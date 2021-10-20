"""
Given an m x n matrix mat, return an array of all the elements of the array in a diagonal order.

Input: mat = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
Output: [1,2,4,7,5,3,6,8,9]


Idea:
The key here is to realize that the sum of indices on all diagonals are equal.
For example, in

[1,2,3]
[4,5,6]
[7,8,9]
2, 4 are on the same diagonal, and they share the index sum of 1. (2 is matrix[0][1] and 4 is in matrix[1][0]). 3,5,7 are on the same diagonal, 
and they share the sum of 2. (3 is matrix[0][2], 5 is matrix[1][1], and 7 is matrix [2][0]).

SO, if you can loop through the matrix, store each element by the sum of its indices in a dictionary, 
you have a collection of all elements on shared diagonals.

The last part is easy, build your answer (a list) by elements on diagonals. To capture the 'zig zag' or 'snake' phenomena of this problem, 
simply reverse every other diagonal level. So check if the level is divisible by 2.

Time Complexity: O(N*M)
Space: O(N)
"""

from typing import List
from collections import defaultdict


def findDiagonalOrder(matrix: List[List[int]]) -> List[int]:
    d=defaultdict(int)
    #loop through matrix
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            #Append to dictionary for sum of indices aka the diagonal,
            d[i+j].append(matrix[i][j])
    # we're done with the pass, let's build our answer array
    ans= []
    #look at the diagonal and each diagonal's elements
    for entry in d.items():
        #each entry looks like (diagonal level (sum of indices), [elem1, elem2, elem3, ...])
        #snake time, look at the diagonal level
        if entry[0] % 2 == 0:
            #Here we append in reverse order because its an even numbered level/diagonal. 
            [ans.append(x) for x in entry[1][::-1]]
        else:
            [ans.append(x) for x in entry[1]]
    return ans




"""
Using Simulation
You basically walk the matrix and keep adding to result and you will need to flip direction when you reach
the end of one diagonal before moving on th the next diagonal. Figuring out the next diagonal will be the trick.

Time Complexity: O(N*M), Space: O(1)
"""

def findDiagonalOrder(matrix: List[List[int]]) -> List[int]:
    
    # Check for an empty matrix
    if not matrix or not matrix[0]:
        return []
    
    # The dimensions of the matrix
    N, M = len(matrix), len(matrix[0])
    
    # Incides that will help us progress through 
    # the matrix, one element at a time.
    row, column = 0, 0
    
    # As explained in the article, this is the variable
    # that helps us keep track of what direction we are
    # processing the current diaonal
    direction = 1
    
    # Final result array that will contain all the elements
    # of the matrix
    result = []
    
    # The uber while loop which will help us iterate over all
    # the elements in the array.
    while row < N and column < M:
        
        # First and foremost, add the current element to 
        # the result matrix. 
        result.append(matrix[row][column])
        
        # Move along in the current diagonal depending upon
        # the current direction.[i, j] -> [i - 1, j + 1] if 
        # going up and [i, j] -> [i + 1][j - 1] if going down.
        new_row = row + (-1 if direction == 1 else 1)
        new_column = column + (1 if direction == 1 else -1)
        
        # Checking if the next element in the diagonal is within the
        # bounds of the matrix or not. If it's not within the bounds,
        # we have to find the next head. 
        if new_row < 0 or new_row == N or new_column < 0 or new_column == M:
            
            # If the current diagonal was going in the upwards
            # direction.
            if direction:
                
                # For an upwards going diagonal having [i, j] as its tail
                # If [i, j + 1] is within bounds, then it becomes
                # the next head. Otherwise, the element directly below
                # i.e. the element [i + 1, j] becomes the next head
                row += (column == M - 1)
                column += (column < M - 1)
            else:
                
                # For a downwards going diagonal having [i, j] as its tail
                # if [i + 1, j] is within bounds, then it becomes
                # the next head. Otherwise, the element directly below
                # i.e. the element [i, j + 1] becomes the next head
                column += (row == N - 1)
                row += (row < N - 1)
                
            # Flip the direction
            direction = 1 - direction        
        else:
            row = new_row
            column = new_column
                    
    return result                 