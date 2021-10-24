"""
An array is monotonic if it is either monotone increasing or monotone decreasing.

An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j]. An array nums is 
monotone decreasing if for all i <= j, nums[i] >= nums[j].

Given an integer array nums, return true if the given array is monotonic, or false otherwise.

Input: nums = [1,2,2,3]
Output: true

Input: nums = [6,5,4,4]
Output: true

Approach:

Define a cmp function as:
cmp(a,b) = -1 if a < b, 1 if a > b and 0 if a = b
We can have a variable that stores the first non-zero comparision that we see. Now if
we see another comparision in the other direction that means that the array is not monotomic. 
"""
from typing import List


def isMonotonic(nums: List[int]) -> bool:
    comp = 0
    for i in range(len(nums)-1):
        c = (nums[i] > nums[i+1]) - (nums[i] < nums[i+1])
        if c:
            if c != comp != 0:
                return False
            comp = c
    return True