"""
Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.

Find the kth positive integer that is missing from this array.

Input: arr = [2,3,4,7,11], k = 5
Output: 9
Explanation: The missing positive integers are [1,5,6,8,9,10,12,13,...]. The 5th missing positive integer is 9.

Approach:
Binary Search

Time Complexity: O(log n)
"""
from typing import List


def findKthPositive(self, arr: List[int], k: int) -> int:
    left, right = 0, len(arr) - 1
    while left <= right:
        pivot = (left + right) // 2
        # If number of positive integers
        # which are missing before arr[pivot]
        # is less than k -->
        # continue to search on the right.
        if arr[pivot] - pivot - 1 < k:
            left = pivot + 1
        # Otherwise, go left.
        else:
            right = pivot - 1

    # At the end of the loop, left = right + 1,
    # and the kth missing is in-between arr[right] and arr[left].
    # The number of integers missing before arr[right] is
    # arr[right] - right - 1 -->
    # the number to return is
    # arr[right] + k - (arr[right] - right - 1) = k + left
    return left + k