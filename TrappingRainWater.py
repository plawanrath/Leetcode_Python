"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6


Brute Force:

1. Iterate over the array from left to right:
    Initialize left_max = 0, right_max = 0
    Iterate from the current element to the beginning of array updating left_max
    Iterate from the current element to the end of array updating the right_max
    Add min(left_max, right_max) - height[i] to get the answer

This will be O(n^2) complexity. But can be made faster using DP.

Dynamic Programming:
In brute force, we iterate over the left and right parts again and again just to find the highest bar size upto that index. But, this could be stored.

Algorithm:
Find maximum height of bar from the left end upto an index i in the array call it left_max.
Find maximum height of bar from the right end upto an index i in the array call it right_max
Iterate over the height array and update the answer:
    Add min(left_max[i], right_max[i]) - height[i] to answer.


Time Complexity: O(n), Space: O(n)

Example:
height = [0,1,0,2,1,0,1,3,2,1,2,1]

left_max = [0,1,1,2,2,2,2,3,3,3,3,3]
right_max = [3,3,3,3,3,3,3,3,2,2,2,1]
height = [0,1,0,2,1,0,1,3,2,1,2,1]

for i in range(height):
    1. result = 0 + 0 = 0
    2. result = 1 -1 = 0
    3. result = 1 - 0 = 1
    4. result = 1 + (2-2) = 1
    5. result = 1 + (2-1) = 2
    6. result = 2 + (2-0) = 4
    7. result = 4 + (2-1) = 5
    8. result = 5 + (3-3) = 5
    9. result = 5 + (2-2) = 5
    10. result = 5 + (2-1) = 6
    11. result = 6 + (2-2) = 6
    12. result = 6 + (1-1) = 6

Answer = 6
"""

from typing import List


def trap(height: List[int]) -> int:
    if not height:
        return 0
    result = 0
    left_max, right_max = [0] * len(height), [0] * len(height)
    
    left_max[0] = height[0]
    for i in range(1, len(height)):
        left_max[i] = max(height[i], left_max[i - 1])
    
    right_max[len(height) - 1] = height[len(height) - 1]
    for j in reversed(range(len(height) - 1)):
        right_max[j] = max(height[j], right_max[j + 1])
    
    for i in range(len(height)):
        result += min(left_max[i], right_max[i]) - height[i]
    
    return result


"""
Approach 2: We can also simply use 2 pointers to keep track of max_left and max_right and then just directly keep
computing the answer as we iterate instead of storing them in a list. 

Time Complexity: O(n), Space: O(1)
"""

def trap2(height: List[int]) -> int:
    if not height:
        return 0
    result = 0
    left_max, right_max = 0, 0
    left, right = 0, len(height) - 1

    while left < right:
        if height[left] < height[right]:
            if height[left] > left_max:
                left_max = height[left]
            else:
                result += left_max - height[left]
            left += 1
        else:
            if height[right] > right_max:
                right_max = height[right]
            else:
                result += right_max - height[right]
            right -= 1
    
    return result
