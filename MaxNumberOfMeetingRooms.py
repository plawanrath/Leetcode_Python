"""
Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], 
return the minimum number of conference rooms required.

O(N log N) Time and O(N) Space
"""
from queue import PriorityQueue


def minMeetingRooms(intervals):
    if not intervals:
        return 0
    intervals.sort(key=lambda x: x[0]) # sort by start time
    pq = PriorityQueue()
    pq.put(intervals[0][1])
    for i in range(1, len(intervals)):
        curr = pq.get()
        if intervals[i][0] < curr:
            pq.put(curr)
        pq.put(intervals[i][1])
    return pq.qsize()