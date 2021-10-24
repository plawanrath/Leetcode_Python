"""
An array nums of length n is beautiful if:

nums is a permutation of the integers in the range [1, n].
For every 0 <= i < j < n, there is no index k with i < k < j where 2 * nums[k] == nums[i] + nums[j].
Given the integer n, return any beautiful array nums of length n. There will be at least one valid 
answer for the given n.

Approach:
Reformulating the problem, nums[i]+nums[j] = 2*nums[k] is not allowed.

In terms of bits, we can start with thinking what would happen if nums[i] or nums[j] is odd or even.

Finding Recursion
We know splitting the array into odds and evens is beneficial. The trivial case is 
[odd numbers here] [even numbers here], or the opposite [even numbers here] [odd numbers here]. 
Both will work. For convenience, I'll take the first one.

example: n = 7
1 2 3 4 5 6 7 -> 1 3 5 7 | 2 4 6

This clearly won't work since 1 3 5 7 and 2 4 6 are troublesome in themselves, 
but if i is pointing to 1 3 5 7 and j to 2 4 6, we can stay safe.

Now, what if ... we break the 1 3 5 7 into two again? How? Just do a right-shift operation. 
(this is one of those problems whose solutions make sense once you know them lmao)

This makes the problem: 0 1 2 3. Doesn't this look eerily similar to the orignial problem? 
We can break this down as 1 3 | 0 2. This will work for evens as well (think why). We have found a recursion!
"""
from typing import List


def recurse(nums):
    if len(nums) <= 2: return nums
    return recurse(nums[::2]) + recurse(nums[1::2])

def beautifulArray(n: int) -> List[int]:
    return recurse([i for i in range(1, n+1)])