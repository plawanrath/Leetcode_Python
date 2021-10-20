"""
You are given two lists of closed intervals, firstList and secondList, where firstList[i] = [starti, endi] 
and secondList[j] = [startj, endj]. Each list of intervals is pairwise disjoint and in sorted order.

Return the intersection of these two interval lists.

A closed interval [a, b] (with a <= b) denotes the set of real numbers x with a <= x <= b.

The intersection of two closed intervals is a set of real numbers that are either empty or 
represented as a closed interval. For example, the intersection of [1, 3] and [2, 4] is [2, 3].

Input: firstList = [[0,2],[5,10],[13,23],[24,25]], secondList = [[1,5],[8,12],[15,24],[25,26]]
Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]

Idea:
In an interval [a, b], call b the "endpoint".

If A[0] has the smallest endpoint, it can only intersect B[0]. 
After, we can discard A[0] since it cannot intersect anything else.

Similarly, if B[0] has the smallest endpoint, it can only intersect A[0], 
and we can discard B[0] after since it cannot intersect anything else.

We use two pointers, i and j, to virtually manage "discarding" A[0] or B[0]

Time & Space Complexity: O(M + N)
"""
from typing import List


def intervalIntersection(firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
    res = []
    i = j = 0

    while i < len(firstList) and j < len(secondList):
        # Let's check if A[i] intersects B[j].
        # lo - the startpoint of the intersection
        # hi - the endpoint of the intersection
        lo = max(firstList[i][0], secondList[j][0])
        hi = min(firstList[i][1], secondList[j][1])
        if lo <= hi:
            res.append([lo, hi])

        # Remove the interval with the smallest endpoint
        if firstList[i][1] < secondList[j][1]:
            i += 1
        else:
            j += 1

    return res