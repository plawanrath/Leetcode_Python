"""
The Hamming distance between two integers is the number of positions 
at which the corresponding bits are different.

Given an integer array nums, return the sum of Hamming distances between all the pairs of the integers in nums.

Input: nums = [4,14,2]
Output: 6
Explanation: In binary representation, the 4 is 0100, 14 is 1110, and 2 is 0010 (just
showing the four bits relevant in this case).
The answer will be:
HammingDistance(4, 14) + HammingDistance(4, 2) + HammingDistance(14, 2) = 2 + 2 + 2 = 6.

Approach:
For each bit, count how many numbers have 0 or 1 on that bit; the total difference on that bit is zero * one

zero: the amount of numbers which have 0 on bit i
one: the amount of numbers which have 1 on bit i

Sum up each bit, then we got the answer
Time Complexity: O(32*N) -> O(N)

"""
from typing import List


def totalHammingDistance(nums: List[int]) -> int:
    ans = 0
    for i in range(32):
        zero = one = 0
        mask = 1 << i
        for num in nums:
            if mask & num: one += 1
            else: zero += 1    
        ans += one * zero        
    return ans    