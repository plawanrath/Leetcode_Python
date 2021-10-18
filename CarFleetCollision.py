"""
There are n cars traveling at different speeds in the same direction along a one-lane road. 
You are given an array cars of length n, where cars[i] = [positioni, speedi] represents:

positioni is the distance between the ith car and the beginning of the road in meters. 
It is guaranteed that positioni < positioni+1.
speedi is the initial speed of the ith car in meters per second.
For simplicity, cars can be considered as points moving along the number line. 
Two cars collide when they occupy the same position. Once a car collides with another car, 
they unite and form a single car fleet. The cars in the formed fleet will have the same 
position and the same speed, which is the initial speed of the slowest car in the fleet.

Return an array answer, where answer[i] is the time, in seconds, at which the ith car 
collides with the next car, or -1 if the car does not collide with the next car.
Answers within 10-5 of the actual answers are accepted.

Input: cars = [[1,2],[2,1],[4,3],[7,2]]
Output: [1.00000,-1.00000,3.00000,-1.00000]
Explanation: After exactly one second, the first car will collide with the second car, 
and form a car fleet with speed 1 m/s. After exactly 3 seconds, the third car will collide 
with the fourth car, and form a car fleet with speed 2 m/s.


Idea:
For each car, you can split the time into intervals sperated by the collision events of 
the ahead cars We do that by having a stack of the ahead cars that can have 
potential collision with the following car. If the following car don't 
collide with the ahead car, then you remove that car from the stack.
"""
from typing import List


def getCollisionTimes(cars: List[List[int]]) -> List[float]:
    def expected_collision_time(p1, s1, p2, s2):
        """Expected collision time for car2 in front of car1 (p1 < p2)
            but car2 slower than car1 (s1 > s2)
        """
        if s2 >= s1:
            return -1.  # no collision
        return (p2 - p1) / (s1 - s2)
    
    collision_times = []  # our answer
    collision_stack = []  # (init position, init speed, collision time) of ahead collisions
    
    for p, s in reversed(cars):
        t = -1.
        while len(collision_stack) > 0:
            p2, s2, t2 = collision_stack[-1]
            t = expected_collision_time(p, s, p2, s2)
            if s > s2 and (t <= t2 or t2 < 0):
                break  # collision
            else:
                t = -1.  # no collision
                collision_stack.pop()
        collision_stack.append((p, s, t))
        collision_times.append(t)
    return collision_times[::-1]