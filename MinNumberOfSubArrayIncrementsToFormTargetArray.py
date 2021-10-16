"""
Given an array of positive integers target and an array initial of same size with all zeros.

Return the minimum number of operations to form a target array from initial if you are allowed to 
do the following operation:
Choose any subarray from initial and increment each value by one.

Input: target = [1,2,3,2,1]
Output: 3
Explanation: We need at least 3 operations to form the target array from the initial array.
[0,0,0,0,0] increment 1 from index 0 to 4 (inclusive).
[1,1,1,1,1] increment 1 from index 1 to 3 (inclusive).
[1,2,2,2,1] increment 1 at index 2.
[1,2,3,2,1] target array is formed.

Approach:

target = [1,2,3,2,1]
dp = [1, 0, 0, 0, 0]

for i in range(1, 5):
    1. i = 1
    target[1] = 2 > target[0] = 1 ---> Go to else
        dp[1] = dp[0] + (2 - 1) = 1 + 1 = 2
        dp =[1,2,0,0,0]
    2. i = 2
    target[2] = 3 > target[1] = 2 ---> Go to else
        dp[2] = dp[1] + (3 - 2) = 2 + 1 = 3
        dp = [1,2,3,0,0]
    3. i = 3
    target[3] = 2 <= target[2] = 3 ---> enter if
        dp[3] = dp[2] = 3
        dp = [1, 2, 3, 3, 0]
    4. i = 4
    target[4] = 1 <= target[3] = 2 --> enter if
        dp[4] = dp[3] = 3
        dp = [1,2,3,3,3]

Return 3
"""
from typing import List


def minNumberOperations(target: List[int]) -> int:
    n = len(target)
    dp = [0] * n
    dp[0] = target[0]
    for i in range(1, n):
        if target[i] <= target[i-1]:
            dp[i] = dp[i-1]
        else:
            dp[i] = dp[i-1] + (target[i] - target[i-1])
    
    return dp[n-1]