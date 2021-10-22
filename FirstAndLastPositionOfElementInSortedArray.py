"""
Given an array of integers nums sorted in non-decreasing order, 
find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Approach: Binary Search

1. We pass a variable isFirst to the binary search to denote if we are looking for the first or the last occurence of the target.
2. Perform normal binary search. When we find the target though there can be 2 cases:
    - sFirst is true = This implies that we are trying to find the first occurrence of the element. 
        If mid == begin or nums[mid - 1] != target, then we return mid as the first occurrence of the target. Otherwise, we update end = mid - 1
    - sFirst is false = his implies we are trying to find the last occurrence of the element. If mid == end or nums[mid + 1] != target, t
        hen we return mid as the last occurrence of the target. Otherwise, we update begin = mid + 1

Time Complexity: O(log n)
"""
from typing import List


def searchRange(nums: List[int], target: int) -> List[int]:
    def binSearch(isFirst: bool):
        begin, end = 0, len(nums) - 1
        while begin <= end:
            mid = (begin + end) // 2
            if nums[mid] == target:
                if isFirst:
                    if mid == begin or nums[mid-1] != target:
                        return mid
                    # Search on the left side for the bound.
                    end = mid - 1
                else:
                    if mid == end or nums[mid + 1] != target:
                        return mid
                    begin = mid + 1
            elif nums[mid] > target:
                end = mid - 1
            else:
                begin = mid + 1
        return -1

    firstPos = binSearch(isFirst=True)
    if firstPos == -1:
        return [-1, -1]
    lastPos = binSearch(isFirst=False)
    return [firstPos, lastPos]