"""
Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.

Implement the MovingAverage class:

MovingAverage(int size) Initializes the object with the size of the window size.
double next(int val) Returns the moving average of the last size values of the stream.

Approach:
1. We could use a Deque which has a constant time for adding and removing numbers on both ends.
2. We could also keep the sum of previous window numbers. So to make moving average computation easier, when 
    a new element is added simply add the new number to the sum and subtract the number that is being evicted.

Time Complexity: O(1)
Space: O(n)
"""
from collections import deque


class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.count = 0
        self.window = deque()
        self.window_sum = 0
        

    def next(self, val: int) -> float:
        if self.count == self.size:
            pop = self.window.popleft()
            self.window_sum -= pop
            self.count -= 1
        self.window.append(val)
        self.window_sum += val
        self.count += 1

        return self.window_sum / min(self.count, self.size)