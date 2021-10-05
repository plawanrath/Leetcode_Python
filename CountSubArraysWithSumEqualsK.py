from typing import List
"""
Given an array of integers nums and an integer k, r
eturn the total number of continuous subarrays whose sum equals to k.

nums = [1,2,3,-3], k = 3
Return 3
subarrays are [1, 2] [3] and [1,2,3,-3]

Idea: Use a hashmap to store cumilitive sum upto all the indices and the number of 
time the cumulitive sum occurs. 

We traverse over the array and keep on finding the cumulative sum. Every 
time we encounter a new sum, we make a new entry in the hashmap corresponding to that sum. 
If the same sum occurs again, we increment the count corresponding to that sum in the hashmap. 
Further, for every sum encountered, we also determine the number of times the sum sum-ksum−k 
has occurred already, since it will determine the number of times a subarray with sum kk has 
occurred up to the current index. We increment the countcount by the same amount.

count, csum = 0
sumMap = {0: 1}
for num in nums:
    1. num = 1
    csum = 0 + 1 = 1
    csum - k = -2 in sumMap -> No
    sumMap = {0: 1, 1: 1}

    2. num = 2
    csum = 1 + 2 = 3
    csum - k = 3 - 3 = 0 in sumMap -> Yes
        count = 0 + sumMap[0] = 0 + 1 = 1
    sumMap = {0: 1, 1: 1, 3: 1}

    3. num = 3
    csum = 3 + 3 = 6
    csum - k = 6 - 3 in sumMap -> Yes
        count = 1 + sumMap[3] = 1+ 1 = 2
    sumMap[6] = sumMap.get(6, 0) + 1 = 1
    sumMap = {0: 1, 1: 1, 3: 1, 6: 1}

    4. num = -3
    csum = 6 - 3 = 3
    csum - k = 3 - 3 = 0 in sumMap -> Yes
        count = 2 + sumMap[0] = 2 + 1 = 3
    sumMap[3] = sumMap.get(3, 0) + 1 = 1 + 1 = 2
    sumMap = {0: 1, 1: 1, 3: 2, 6: 1} 
"""

def subarraySum(nums: List[int], k: int) -> int:
    count, csum = 0, 0
    sumMap = {}
    sumMap[0] = 1 # THis is a map of (cumulativeSum, occurances) so sum 0 had occured once.
    for num in nums:
        csum += num
        if csum - k in sumMap:
            count += sumMap[csum - k]
        sumMap[csum] = sumMap.get(csum, 0) + 1
    return count