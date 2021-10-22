"""
Given an integer array nums of length n, return true if there is a triplet (i, j, k) 
which satisfies the following conditions:

0 < i, i + 1 < j, j + 1 < k < n - 1
The sum of subarrays (0, i - 1), (i + 1, j - 1), (j + 1, k - 1) and (k + 1, n - 1) is equal.
A subarray (l, r) represents a slice of the original array starting from the element indexed l to 
the element indexed r.

Input: nums = [1,2,1,2,1,2,1]
Output: true
Explanation:
i = 1, j = 3, k = 5. 
sum(0, i - 1) = sum(0, 0) = 1
sum(i + 1, j - 1) = sum(2, 2) = 1
sum(j + 1, k - 1) = sum(4, 4) = 1
sum(k + 1, n - 1) = sum(6, 6) = 1

Approach:
Store a map of {prefixSum: index}
Then we can iterate over the dictionary and check if there are 3 prefix sums that
match the condition required. 

Time: O(n^2), Space: O(N)
"""
from typing import List
from collections import defaultdict

def splitArray(self, nums: List[int]) -> bool:
    presum = [0]
    
    for num in nums:
        presum.append(presum[-1] + num)
    n = len(nums)
    dic = defaultdict(list)
    
    # Store prefix a dictionary of {prefixSum: index}
    for i, u in enumerate(presum):
        dic[u].append(i)
    
    # iterate over that dictionary and check the conditions
    for j in range(1, n - 1):
        for k in range(j + 2, n - 1):
            for i in dic[presum[-1] - presum[k + 1]]:
                if i + 1 >= j:
                    break
                if i != 0 and presum[i] == presum[j] - presum[i + 1] == presum[k] - presum[j + 1]:
                    return True
    return False