"""
Given a binary array nums and an integer k, 
return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]

Idea: Sliding Window
We have to choose longest consecutive sequence of 1s with atmost k zeros 
(k zeros can be flipped to 1). We can use a sliding window approach for this 
since the problem is nothing but finding the longest window with atmost k zeros.

We can maintain two pointers l (left-most window index) and r (right-most window index). 
We have following possible scenarios -
1. nums[r] == 0 : We will try to include this in our window. Here we have two subcases:
    - k != 0: We can just include nums[r] in current window and extend it. 
        We will also decrement k denoting a zero has been picked in the current window
    - k == 0: Our window already contains maximum zeros (k) allowed. So, we need to shrink 
        our window size from the left till a zero is removed from the other end.
2. nums[r] == 1: We can simply pick this element and extend our window.
3. We will keep updating ans to hold the maximum of window size at any point in time and finally return it.
"""
from typing import List


def longestOnes(nums: List[int], k: int) -> int:
	n, ans, l = len(nums), 0, 0
	for r in range(n):
		if nums[r] == 0:                       # try to pick current 0
			if k == 0:                         # if window already picked k zeros, pop 1 from left and pick this
				while nums[l] != 0 : l += 1
				l += 1
			else : k-= 1                       # otherwise pick it and decrement k
		ans = max(ans, r - l + 1)              # update ans as max window size till now
	return ans