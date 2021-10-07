"""
You are given a 0-indexed array of positive integers w where w[i] describes the weight of the ith index.

You need to implement the function pickIndex(), which randomly picks an index in the range [0, w.length - 1] (inclusive) 
and returns it. The probability of picking an index i is w[i] / sum(w).

Example:
nums = [1, 3]
Probablity of picking the index 0 is 1 / (1 + 3) = 25%
Probability of picking the index 1 is 3 / (1 + 3) = 75%

Given a list of positive values, we are asked to randomly pick up a value based on the weight of each value. 
To put it simple, the task is to do sampling with weight.

Approach:
We get a random number (float) from 0 to 1.
Then, we add the weights cumulatively and divide by the sum of weights and maintain them in an array.
Example:
w: [1,2,3,4]
Sum of elements in w: 10
Normalised weights: [0.1, 0.2, 0.3, 0.4]
Cumulative weights: [0.1, 0.3, 0.6, 1.0]

Now, we get a random number between 0 and 1.
We do a binary search and find the index where it has to be inserted. That index will be the return value.

Time Complexity: Constructor: O(n), pickIndex = O(log n)
Space complexity: Constructor: O(n), pickIndex = O(1)
"""
from typing import List
from random import random


class Solution:

    def __init__(self, w: List[int]):
        self.w = w
        self.c = [0] * len(w)
        s = sum(w)
        self.c[0] = w[0]/s
        for i in range(1, len(w)):
            self.c[i] = self.c[i-1] + w[i]/s

    def pickIndex(self) -> int: # Binary search to get the index where a random number between 0 and 1 should be inserted.
        n = random() # This generates a random float between 0 and 1
        # Lower and upper bounds
        start = 0
        end = len(self.c) - 1
    
        # Traverse the search space
        while start<= end:
    
            mid =(start + end)//2
    
            if self.c[mid] == n:
                return mid
    
            elif self.c[mid] < n:
                start = mid + 1
            else:
                end = mid-1
    
        # Return the insert position
        return end + 1