"""
A conveyor belt has packages that must be shipped from one port to another within 'days' days.

The ith package on the conveyor belt has a weight of weights[i]. Each day, we load 
the ship with packages on the conveyor belt (in the order given by weights). We may not 
load more weight than the maximum weight capacity of the ship.

Return the least weight capacity of the ship that will result in all the packages on 
the conveyor belt being shipped within days days.

Input: weights = [1,2,3,4,5,6,7,8,9,10], days = 5
Output: 15
Explanation: A ship capacity of 15 is the minimum to ship all the packages in 5 days like this:
1st day: 1, 2, 3, 4, 5
2nd day: 6, 7
3rd day: 8
4th day: 9
5th day: 10

Note that the cargo must be shipped in the order given, so using a ship of capacity 14 and 
splitting the packages into parts like (2, 3, 4, 5), (1, 6, 7), (8), (9), (10) is not allowed.

# Method I : Binary Search
# TC : O(N*log(sum(N) - max(N)))
# Quite Challenging Problem
# Intitution Behind Binary Search ?

# We know that our boundary lies within max(weights) to sum(weights) because
# we might have D >= len(weights) that means we can ship one weight in each
# particular days so least weight capacity will be max(weights)

# Also if day == 1,then we have ship all weights in 1 day,in that case least weight 
# capacity will be sum of all weights.

# So after this we know that our ans lies between ans -> (max(weights) to (sum(weights)))

# So boundary space of binary search is left = max(weigts) ,right = sum(weigts)

# After that we check for mid which is actually capacity of ship.
# If capacity is greater obivously it will take less days to ship all weights.

# So if days  < D that means we have days left in our account then we can optimise our 
# solution by decreasing the capacity.

# How can we decrease our capacity ?

# By decreasing our ans space. So rigt will move to mid.

# If capacity become too less than it will take more number of days than required
# In that case we have to increase our capacity that is we have increase mid 
# So we increase our left to mid.
# Gradually our boundary decrease and it satisfy our d and give our result.
"""
from typing import List


def shipWithinDays(weights: List[int], Days: int) -> int:
    def feasibility(capacity: int) -> bool:
        days = 1
        total = 0
        for weight in weights:
            total += weight
            if total > capacity:
                total = weight
                days += 1
                if days > Days:
                    return False
        return True
    
    left, right = max(weights), sum(weights)
    while left < right:
        mid = left + (right - left) // 2
        if feasibility(mid):
            right = mid
        else:
            left = mid + 1
    return left