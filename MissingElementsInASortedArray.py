"""
Given an integer array nums which is sorted in ascending order
 and all of its elements are unique and given also an integer k, 
 return the kth missing number starting from the leftmost number of the array.

Input: nums = [4,7,9,10], k = 1
Output: 5
Explanation: The first missing number is 5.

Input: nums = [4,7,9,10], k = 3
Output: 8
Explanation: The missing numbers are [5,6,8,...], hence the third missing number is 8.

Approach:
Binary Search - O(log n)
"""
from typing import List


def missingElement(nums: List[int], k: int) -> int:
    if not nums or k == 0:
        return 0
    
    diff = nums[-1] - nums[0] + 1 # complete length of the series
    missing = diff - len(nums) # complete length - real length
    if k > missing: # if k is larger than the number of mssing words in sequence
        return nums[-1] + k - missing # Case: [1, 2, 5, 6], k=3, missing = 2. 3rd missing would be 6+3-2 = 7
    
    left, right = 0, len(nums) - 1
    while left + 1 < right:
        mid = (left + right) // 2
        missing = nums[mid] - nums[left] - (mid - left)
        if missing < k:
            left = mid
            k -= missing # KEY: move left forward, we need to minus the missing words of this range
        else:
            right = mid
            
    return nums[left] + k # k should be between left and right index in the end
