"""
We are given an array asteroids of integers representing asteroids in a row.

For each asteroid, the absolute value represents its size, and the sign represents 
its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller 
one will explode. If both are the same size, both will explode. Two asteroids moving in 
the same direction will never meet.

Input: asteroids = [5,10,-5]
Output: [5,10]
Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.

What happens if an astroid is 0 ?
Can we ignore those ?

Approach:
This can be solved using a Stack.
For each astroid:
    1. If the astroid is positive, add it to stack.
    2. while there are asteroids moving right (in stack) smaller than the current astroid, pop them
    3. If the last element is same as the current element then we can also pop
    4. If the top of stack is also negative then that means astroids are moving in same direction so add current to stack

"""
from typing import List


def asteroidCollision(asteroids: List[int]) -> List[int]:
    res = []
    for a in asteroids:
        if not res or a > 0:
            res.append(a)
        elif a < 0:
            while res and res[-1] > 0 and res[-1] < abs(a):
                res.pop()
            
            if res and res[-1] == abs(a):
                res.pop()
            elif not res or res[-1] < 0:
                res.append(a)
    return res