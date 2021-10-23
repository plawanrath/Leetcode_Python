"""
Given a list of lists of integers, nums, return all elements of nums in diagonal order

Input: nums = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
Output: [1,4,2,7,5,3,8,6,9]

Idea:
Concept: Along diagonal, the sum of the indices are always SAME. For ex- take index- 
[0,2], [1,1], [2,0] (all have a total sum of 2).
So we will try to make a empty List of list, and sum of index will act a new index for List of list.

Time : O(n^2)
"""
from typing import List


def findDiagonalOrder(nums: List[List[int]]) -> List[int]:
    res = []
    for i, r in enumerate(nums):
        for j, val in enumerate(r):
            if len(res) <= i + j: # adding a empty list at index i  + j
                res.append([])
            res[i+j].append(val)
    l = []
    for r in res:
        l+=reversed(r)
    return l
