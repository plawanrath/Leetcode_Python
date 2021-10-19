"""
A peak element is an element that is strictly greater than its neighbors.

Given an integer array nums, find a peak element, and return its index. 
If the array contains multiple peaks, return the index to any of the peaks.

Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.

Approach:
We can use binary search and return the left pointer when we reach the peak

Time and Space Complexity: O(log n)
"""
from typing import List


def findPeakElement(nums: List[int]) -> int:
    def search(l, r):
        if l == r:
            return l
        mid = (l + r) // 2
        if nums[mid] > nums[mid+1]:
            return search(l, mid)
        else:
            return search(mid+1, r)
    
    return search(0, len(nums)-1)