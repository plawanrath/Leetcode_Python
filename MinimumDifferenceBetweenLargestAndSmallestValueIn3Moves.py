"""
Given an array nums, you are allowed to choose one element of nums and change it by any value in one move.

Return the minimum difference between the largest and smallest value of nums after perfoming at most 3 moves.

Input: nums = [5,3,2,4]
Output: 0
Explanation: Change the array [5,3,2,4] to [2,2,2,2]. In 3 moves I changed 3 values to 2
The difference between the maximum and minimum is 2-2 = 0.


Idea:
1. If the list has less than 3 elements then basically in 3 moves we could replace all number with any number so the min difference will be 0
2. Initiate minDifference
3. Sort the array
4. Get the window size = If we remove 3 elements in the array, how many elements are left.
5. Run through the entire array sliding the window and calculating min difference between the first and the last element of that window.
"""
from typing import List


def minDifference(nums: List[int]) -> int:
    if len(nums) <= 3:
        return 0
    min_diff = float("inf")
    nums.sort()

    window = len(nums) - 1 - 3

    for i in range(len(nums)):
        if i + window < len(nums):
            min_diff = min(min_diff, nums[i+window]-nums[i])
        else:
            break
    
    return min_diff