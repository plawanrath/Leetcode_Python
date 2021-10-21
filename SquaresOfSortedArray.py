"""
Given an integer array nums sorted in non-decreasing order, 
return an array of the squares of each number sorted in non-decreasing order.

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].

Idea:
Since the array A is sorted, loosely speaking it has some negative elements with 
squares in decreasing order, then some non-negative elements with squares in increasing order.

or example, with [-3, -2, -1, 4, 5, 6], we have the negative part [-3, -2, -1] with squares 
[9, 4, 1], and the positive part [4, 5, 6] with squares [16, 25, 36]. 
The strategy is to iterate over the negative part in reverse, and the positive part in the forward direction.

Time Complexity: O(N)
Space: O(1)
"""
from typing import List


def sortedSquares(nums: List[int]) -> List[int]:
    n = len(nums)
    res = [0] * n
    left, right = 0, n - 1
    for i in range(n-1, -1, -1):
        if abs(nums[left]) < abs(nums[right]):
            sq = nums[right]
            right -= 1
        else:
            sq = nums[left]
            left += 1
        res[i] = sq * sq
    return res