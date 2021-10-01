"""
heights = [4,2,3,1]

Return a sorted list of indices of buildings that have an ocean view. The ocean is to the right of a builing in the list of building heights. 
So for above array we should return [0, 2, 3]

Naive Approach: For each building check all buildings to the right and make sure that the current building has the max height. 

Linear Aproach: Start with assumption that every building has an ocean view. For any building we are considering we look left 
to see if the current building could block ocean view of a previous building and if so we remove
that building.

heights = [4,2,3,1]
res = []

for height in heights:
    1. height = 4
    res = [0]
    2. height = 2 -> Won't block 4's view
    res =  [0, 1]
    3. height = 3 -> would block 2's view so remove that index
    res = [0]
    Now we will also add 3's index since we assume that it can see the ocean
    res = [0, 2]
    4. height = 1 -> Won't block views
    res = [0, 2, 3]

Complexity: O(N) - Since within the for loop we will end up pushing and poping values from answer only once and those operations are O(1)

The space complexity will be O(N) because the worst case would be that the last building blocks all the ocean views in which case we would
have traversed all the way to the right and then end up popping all other elements from the answer thus using that as a temporary space.
"""
from typing import List

def findBuildingsLinear(heights: List[int]) -> List[int]:
    res = []
    for i in range(len(heights)):
        while res and heights[res[-1]] <= heights[i]:
            res.pop()
        res.append(i)
    return res

"""
Approach 2: We can convert this problem to something like find the next element to the right that is greater than or equal to the current 
element.

Take a maxHeight, start from the right. Now first the right most element becomes the maxHeight. When we process an element in the array from
right to left, if the next element we are processing is less than maxHeight, then that is not valid. Otherwise we update maxHeight and add
the index to result. 

heights = [4,2,3,1]
res = []
maxHeight = -1

for i in range(3,0):
    1. height = 1
        1 > -1 ?
            maxHeight = 1
            res = [3]
    2. height = 3
        3 > 1 ?
            maxHeight = 3
            res = [3, 2]
    3. height = 2
        2 > 3 ? - No
    4. height = 4
        4 > 3 ?
            maxheight = 4
            res = [3, 2, 0]

return reverse of res = [0, 2, 3]
"""
def findBuildingOptimal(heights: list[int]) -> List[int]:
    res = []
    maxHeight = -1
    for i in reversed(range(len(heights))):
        if heights[i] > maxHeight:
            maxHeight = heights[i]
            res.append(i)
    res.reverse()
    return res