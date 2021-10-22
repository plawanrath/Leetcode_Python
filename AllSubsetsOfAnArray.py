"""
Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Approach: DFS and backtracking
"""
from typing import List

def subsets(self, nums):
    ret = []
    self.dfs(nums, [], ret)
    return ret

def dfs(self, nums, path, ret):
    ret.append(path)
    for i in range(len(nums)):
        self.dfs(nums[i+1:], path+[nums[i]], ret)