"""
Given a characters array tasks, representing the tasks a CPU needs to do, where each letter 
represents a different task. Tasks could be done in any order. Each task is done in one unit of time. 
For each unit of time, the CPU could complete either one task or just be idle.

However, there is a non-negative integer n that represents the cooldown period between two 
same tasks (the same letter in the array), that is that there must be at least n units of time 
between any two same tasks.

Return the least number of units of times that the CPU will take to finish all the given tasks.

Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation: 
A -> B -> idle -> A -> B -> idle -> A -> B
There is at least 2 units of time between any two same tasks.

Idea:

The problem can be broken down as follows:

1. tasks = ["A","A","A","B","B","B"], n = 2
A B X
A B X
A B

answer = 8 (3 * 2 + 2)

2. tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"], n = 2
A B C
A D E
A F G
A X X
A X X
A

answer = 16 (5 * 3 + 1)

3. tasks = ["A","A","A","B","B","B", "C","C","C", "D", "D", "E"], n = 2
A B C D E
A B C D A
B C 

answer = 12 (no idle time so this is just len(tasks))

If you generalize this, you get this formula

(frequency of the max task - 1) * (n + 1) + last_row
or
len(tasks) 
whichever is higher

last_row = count of max frequency tasks

Time Complexity: O(n), Space: We will have a list of frequencies which is limited by a constant of the number
of tasks so O(1)
"""
from collections import Counter
from typing import List


def leastInterval(tasks: List[str], n: int) -> int:
    l = list(Counter(tasks).values())
    max_freq = max(l)
    last_row = len([x for x in l if x == max_freq])
    return max( (max_freq - 1) * (n + 1) + last_row, len(tasks))