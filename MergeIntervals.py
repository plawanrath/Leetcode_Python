"""
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, 
and return an array of the non-overlapping intervals that cover all the intervals in the input.

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

Approach: Sort by start time. Then add the first interval to a stack and when processing the next element
check if the interval at the top of the stack can be merged. If it cannot be merged then add that to stack. 
If it can be merged then pop from stack, calculate the new end time and add it back to stack.

At the end of this process your stack is the answer.

Time Complexity: O(n log n), space: O(n)
"""


from typing import List


def mergeIntervals(intervals: List[List[int]]) -> List[List[int]]:
    # sort by start time
    intervals.sort(key=lambda x: x[0])

    res = []
    for interval in intervals:
        if not res or interval[0] > res[-1][1]:
            res.append(interval)
        else:
            val = res.pop()
            maxEnd = max(val[1], interval[1])
            res.append([val[0], maxEnd])
    return res

