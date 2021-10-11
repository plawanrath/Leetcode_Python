"""
Implement next permutation, which rearranges numbers into the 
lexicographically next greater permutation of numbers.

If such an arrangement is not possible, it must rearrange it as 
the lowest possible order (i.e., sorted in ascending order).

Input: nums = [1,2,3]
Output: [1,3,2]

Input: nums = [1,1,5]
Output: [1,5,1]

Input: nums = [3,2,1]
Output: [1,2,3]

Input: nums = [1]
Output: [1]

This needs to be done in-place. 

Time complexity: O(n)
"""

from typing import List


def nextPermutation(nums: List[int]) -> None:
    #if the length is 1, there will be only 1 permutation (itself)
    n = len(nums)
    if n == 1:
        return nums
    
    temp = nums.copy() #creating a copy of the given array
    
    #Case 1 : When the array is in descending order
    #we will simply return the ascending form of the given array
    temp.sort(reverse = True)
    if temp == nums:
        nums.sort()
        return nums
    
    #Case 2 : When the array is in ascending order
    #we will just have to swap the element at (n-1)th and (n-2)th index
    temp.sort()
    if temp == nums:
        nums[n-1], nums[n-2] = nums[n-2],nums[n-1]
        return nums
    
    #Case 3 : When array is neither in ascending nor descending form
    #Basic Idea is : 
    #First, we will start iterating from backwards and find the point where descending form breaks(let index be x)
    #Second, we will find the element just greater than the element at (x-1)th index and swap them
    #Third, we will revert (or sort) the suffix array - it starts from index x and continues till (n-1)th index
    
    x = n - 1
    while (x > 0 and nums[x] <= nums[x-1]):
        x -= 1
        
    if (x - 1) >= 0:
        for y in range(n-1, x - 1, -1):
            if nums[y] > nums[x-1]:
                nums[y], nums[x-1] = nums[x-1], nums[y]
                break
    
    j = n - 1
    while x < j:
        nums[x], nums[j] = nums[j], nums[x]
        x += 1
        j -= 1
    return nums
