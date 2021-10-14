"""
You are given an array points, an integer angle, and your location, 
where location = [posx, posy] and points[i] = [xi, yi] both denote integral coordinates on the X-Y plane.

Initially, you are facing directly east from your position. You cannot move 
from your position, but you can rotate. In other words, posx and posy cannot be changed. 
Your field of view in degrees is represented by angle, determining how wide you can see 
from any given view direction. Let d be the amount in degrees that you rotate counterclockwise. 
Then, your field of view is the inclusive range of angles [d - angle/2, d + angle/2].

You can see some set of points if, for each point, the angle formed by the point, 
your position, and the immediate east direction from your position is in your field of view.

There can be multiple points at one coordinate. There may be points at your location, 
and you can always see these points regardless of your rotation. Points do not obstruct your 
vision to other points.

Return the maximum number of points you can see.


Algorithm:
The basic algorithm I used was to compute the polar angles 
(while counting/removing any points which coincided with your 'location'), 
then sort the angles, and then count the number of points in each relevant sector 
using 2 pointers (slow/fast) remembering that the circle wraps around. 

1. Compute the Angles of Each Point Relative to Yourself : O(n)
2. Looping over all points:
    - Get the Next Point
    - Check if the Point is Not at Your Location
    - Compute the Angle of the Point in Radians
    - Record that the Point Exists
3. Sort the Remaining Angles : O(nlogn)
4. Convert the Angle to Radians
5. Use 2 pointers to count number of points in each sector
    - Take i and j where i is the slow pointer and j is the fast pointer
    - Increment j as Much as Possible to Find the Points in the Current Sector
    - Save the max result
"""
from typing import List
from math import atan2, pi, tau


def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
    #Compute the Angles of Each Point Relative to Yourself : O(n)
    angles = []
    Y, X = location.pop(), location.pop() #I'm just being extra about the memory thing here...
    m = 0
    for i in range(len(points)):
        #Get the Next Point
        x, y = points.pop()
        
        #Check if the Point is Not at Your Location
        if x != X or y != Y:
            #Compute the Angle of the Point in Radians
            angles.append(atan2(y - Y, x - X)) #'atan2' outputs an angle in radians
        else:
            #Record that the Point Exists
            m += 1
    
    #Sort the Remaining Angles : O(nlogn)
    angles.sort()
    
    #Convert the Angle to Radians
    angle *= pi/180
    
    #2-Pointer Solution : O(n)
    j = 1
    n = 0
    N = len(angles)
    for J, i in enumerate(range(N), start = N):
        #Increment j as Much as Possible to Find the Points in the Current Sector
        # Tau is precisely the number that connects a circumference to that quantity
        while j < J and (angles[j%N] - angles[i])%tau <= angle:
            j += 1
        
        #Check the Case
        if j == J:
            #The Result is Optimal
            return m + N
        else:
            #Save the Best Result so Far
            n = max(n, j - i)
    
    #Return the Maximum Number of Points
    return m + n