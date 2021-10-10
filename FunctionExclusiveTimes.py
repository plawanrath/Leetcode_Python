"""
Return the exclusive time of each function in an array, where the value at the ith index 
represents the exclusive time for the function with ID i.

A function's exclusive time is the sum of execution times for all function calls in the program. 

Example: n = 2, logs = ["0:start:0","1:start:2","1:end:5","0:end:6"]

Functions: 0 0 1 1 1 1 0 
Timestamp: 0 1 2 3 4 5 6

Output: [3, 4]

Idea:
1. Use a stack to keep track of function calls and timestamps
2. We can use another result array which will store the final function times. 
    This function just keep track of the current timeSpent for each function whenever we process
    a new function.
3. Functions when started will be added to the stack and will be popped and processed when they end.

Example:
n = 2, logs = ["0:start:0","1:start:2","1:end:5","0:end:6"]
stack = [], res = [0, 0]

for funcTime in logs:
    1. funcId, eventType, timestamp = 0, start, 0
       eventType ==  start:
            stack = [[0, 0]]
    2. funcId, eventType, timestamp = 1, start, 2
       eventType == start:
            stack = [[0, 0], [1, 2]]
    3. funcId, eventType, timestamp = 1, end, 5
       eventType == end:
            funcId, startTime = 1, 2 and stack = [[0, 0]]
            timeSpent = timestamp - startTime + 1= 5 - 2 + 1 = 4
            res[1] = 0 + 4 i.e. res = [0, 4]

            We will update the timeSpent for the upper level function
            nextFunc, _ = 0, 0
            res[0] = 0-4 = -4 i.e res = [-4, 4]
    4. funcId, eventType, timestamp = 0, end, 6
       eventType == end:
            funcId, startTime = 0, 0 and stack is empty
            timeSpent = timestamp - startTime + 1 = 6 - 0 + 1 = 7
            res[0] = res[0] + timeSpent = -4 + 7 = 3
    
    res = [3, 4]

Returns [3, 4]

Complexity: O(n) time and space
"""
from typing import List


def exclusiveTimes(n: int, logs: List[str]) -> List[int]:
    stack = []
    res = [0] * n

    for funcTime in logs:
        # Here sometimes you maybe asked what what happens if you're dealing with unicode/ASCII strings
        # in that scenario you can convert it to ansii before doing the split.
        # For example: processTime.encode('ascii','ignore').split(':')
        funcId, eventType, timestamp = funcTime.split(":")
        if eventType == "start":
            stack.append([funcId, timestamp])
        elif eventType == "end":
            funcId, startTime = stack.pop()
            timeSpent = int(timestamp) - int(startTime) + 1 # We add one because the timestamps are inclusive
            res[int(funcId)] += timeSpent

            # Decrement time for next function in the stack
            if stack:
                nextFunc, _ = stack[-1]
                res[int(nextFunc)] -= timeSpent
    return res