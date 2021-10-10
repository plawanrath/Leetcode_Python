"""
Given an integer array nums and an integer k, return true if nums has a continuous 
subarray of size at least two whose elements sum up to a multiple of k, or false otherwise.

An integer x is a multiple of k if there exists an integer n such that 
x = n * k. 0 is always a multiple of k.

Input: nums = [23,2,4,6,7], k = 6
Output: true
[2, 4] is a continuous subarray of size 2 whose elements sum up to 6.

Input: nums = [23,2,6,4,7], k = 6
Output: true
[23, 2, 6, 4, 7] is an continuous subarray of size 5 whose elements sum up to 42.

Idea:
A simple mod theory
If mod of two different numbers with same divisor is same, then difference of those 
numbers will be divisible by the divisor

example:
23 % 10 = 3 and 53 % 10 = 3 then 53 - 23 = 30 and 30 % 10 = 0 or
25 % 4 = 1 and 37 % 4 = 1 then 37 - 25 = 12 and 12 % 4 = 0

Idea:
prefixSum will always record prefixSum % k  values. So let's say we already found
a prefixSum that was already in map since they both were divided by the same k we can 
its safe to assume that the current sum would also be divisible by k.

To extend that, this means that if we to ensure that there are subarrays with 2 or more
numbers that add up to k then we should have atleast 2 indices stored in the prefixSumMap.

Example: nums = [23,2,4,6,7], k = 6
prefixSumMap = {0: -1}
prefixSum = 0

for i, num in nums:
    1. i, num, prefixSum = 0, 23, 0
       prefixSum = 23
       prefixSum = 23 % 6 = 5
       if prefixSum in prefixSumMap ? ---> No
       prefixSum = {0: -1, 5: 0}
    2. i, num, prefixSum = 1, 2, 5
       prefixSum = 5 + 2 = 7
       prefixSum = 7 % 6 = 1
       if prefixSum in prefixSumMap ---> No
       prefixSum = {0: -1, 5: 0, 1: 1}
    3. i, num, prefixSum = 2, 4, 1
       prefixSum = 1 + 4 = 5
       prefixSum = 5 % 6 = 1
       if prefixSum in prefixSumMap ---> Yes
            i = 2, prefixSumMap[1] = 1
            i - prefixSumMap[prefixSum] = 2 - 1 > 1 ? ----> No
    4. i, num, prefixSum = 3, 6, 1
        prefixSum = 1 + 6 = 7
        prefixSum = 7 % 6 = 1
        if prefixSum in prefixSumMap ---> Yes
            i = 3, prefixSumMap[1] = 1
            i - prefixSumMap[prefixSum] = 3 - 1 = 2 > 1 ? ----> Yes
                return True

answer = True

Edge Case where i - prefixSumMap[prefixSum] > 1 becomes important:
Example: [0], k = 1

prefixSumMap = {0: -1}
prefixSum = 0

for i, num in nums:
    i, num, prefixSum = 0, 0, 0
    prefixSum = 0
    prefixSum = 0 % 1 = 0
    if prefixSum in prefixSumMap -----> Yes
        i = 0, prefixSumMap[prefixSum] = -1
        i - prefixSumMap[prefixSum] = 0 - (-1) = 1 > 1 ---> No
    return False

Answer = False

Time and Space Complefity: O(n)
"""
from typing import List


def checkSubArraySumExists(nums: List[int], k: int) -> bool:
    prefixSumMap = {0: -1} # map stores prefixSum as key and index as value
    prefixSum = 0

    if not k:
        return False
    for i, num in enumerate(nums):
        prefixSum += num
        prefixSum = prefixSum % k
        if prefixSum in prefixSumMap:
            # if we to ensure that there are subarrays with 2 or more 
            # numbers that add up to k then we should have atleast 2 
            # indices stored in the prefixSumMap.
            if i - prefixSumMap[prefixSum] > 1:
                return True
        else:
            prefixSumMap[prefixSum] = i
    return False
