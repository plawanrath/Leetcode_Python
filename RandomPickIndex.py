"""
Given an integer array nums with possible duplicates, randomly output the index of a given target number. 
You can assume that the given target number must exist in the array.

Picks a random index i from nums where nums[i] == target. 
If there are multiple valid i's, then each index should have an equal

nums = [1, 2, 3, 3, 3]
pick(3) should return either 2,3,4 with equal probability.
pick(1) would return 0 since 1 is present only once. 

Approach 1: If the array is not super large, then we can precompute and store the positions 
where a number occurs. 

Time complexity: O(N) for building the map and O(1) for pick. But space complexity will be O(N).
So not ideal for large amounts of data.
"""
from typing import List
import collections
import random


class PickRandom:
    def __init__(self, nums: List[int]):
        self.h = collections.defaultdict(list)
        for i, num in enumerate(nums):
            self.h[num].append(i)

    def pick(self, target: int) -> int:
        return self.h[target][random.randint(0, len(self.h[target]) - 1)]

"""
## RC ##
    ## APPROACH : RESERVOIR SAMPLING ##
    ## 1. If we already know size of the array, its simple, we can use random.choice() for all the indicies of that target and return. ( as random.choice has equal probability on all the indices )
    ## 2. What if the array size is not know, its infinite data set ?
    ## 3. THe idea is that we will use a count to keep track of how many times the target occured and use random.randint(0, count-1) to ensure equal probablity of a number that is repeated.
    ## 4. Just like reservoir sampling, we maintain previous occurance count, say for [1,2,3,3,3] and target = 3, for i=2: we random int in the range 0 to 0, (prob = 1) when count = 2, random can in[0,1], prob =1/2, count = 3, random range = [0,2], prob = 1/3.
    
	## TIME COMPLEXITY : O(N) ##
	## SPACE COMPLEXITY : O(N) ##

    Example:
    nums = [1, 2, 3]
        line 56: for x = 3 and i = 2: count = 1
        chance = random.randint(0, 0) which will return 0
        function returns i = 2 (the only position for 3)
    
    nums = [1, 2, 3, 3]
        for i = 2:
            count = 1
            chance = random.randint(0,0)
            so res = i = 2
        for i = 3:
            count = 2
            chance = random.randint(0, 1)
            if chance is 0:
                res = i = 3
            if chance is not 0:
                res remains 2
        Therefore giving 1/count equal probability of both happening. 
"""
class PickRandomRS:
    def __init__(self, nums: List[int]):
        self.nums = nums

    def pick(self, target: int) -> int:
        res = None
        count = 0
        for i, x in enumerate(self.nums):
            if x == target:
                count += 1
                chance = random.randint(0, count - 1)
                # chance of getting 0 is 1/count, then we pick that number. So when we have 3 nums, chance of picking it is 1/3, (if chance is not 0, i value may be previous value or even previous before that. so prob remains 1/count)
                if chance == 0:
                    res = i
        return res