"""
Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. 
The result should also be sorted in ascending order.

An integer a is closer to x than an integer b if:

|a - x| < |b - x|, or
|a - x| == |b - x| and a < b

Input: arr = [1,2,3,4,5], k = 4, x = 3
Output: [1,2,3,4]

Approach:
Binary Search - But what will be the upper bound ?
If there needs to be k elements, then the left bound's upper limit is arr.length - k, 
because if it were any further to the right, you would run out of elements to include in the final answer.

Perform a binary search. At each operation, calculate mid = (left + right) / 2 and 
compare the two elements located at arr[mid] and arr[mid + k]. 
If the element at arr[mid] is closer to x, then move the right pointer. If the element at 
arr[mid + k] is closer to x, then move the left pointer. Remember, the smaller element 
always wins when there is a tie.

At the end of the binary search, we have located the leftmost index for the final answer. 
Return the subarray starting at this index that contains k elements.

Time: O(log n), Space: O(1)
"""
from typing import List


def findClosestElements(arr: List[int], k: int, x: int) -> List[int]:
    left, right = 0, len(arr) - k
    while left < right:
        mid = (left + right) // 2
        if x - arr[mid] > arr[mid + k] - x:
            left = mid + 1
        else:
            right = mid

    return arr[left:left+k]

