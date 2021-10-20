"""
You are given an integer array ribbons, where ribbons[i] represents the length of the ith ribbon, 
and an integer k. You may cut any of the ribbons into any number of segments of positive integer 
lengths, or perform no cuts at all.

For example, if you have a ribbon of length 4, you can:
Keep the ribbon of length 4,
Cut it into one ribbon of length 3 and one ribbon of length 1,
Cut it into two ribbons of length 2,
Cut it into one ribbon of length 2 and two ribbons of length 1, or
Cut it into four ribbons of length 1.
Your goal is to obtain k ribbons of all the same positive integer length. You are 
allowed to throw away any excess ribbon as a result of cutting.

Return the maximum possible positive integer length that you can obtain k ribbons of, 
or 0 if you cannot obtain k ribbons of the same length.

Input: ribbons = [9,7,5], k = 3
Output: 5
Explanation:
- Cut the first ribbon to two ribbons, one of length 5 and one of length 4.
- Cut the second ribbon to two ribbons, one of length 5 and one of length 2.
- Keep the third ribbon as it is.
Now you have 3 ribbons of length 5.

Time Complexity: O(n log n), O(n) for getNumberOfRibbonsWithLength and O(log n) for Binary Search
"""
from typing import List


def getNumberOfRibbonsWithLength(ribbons, length):
    numRibbons = 0
    for ribbon in ribbons:
        numRibbons += ribbon // length
    return numRibbons

def maxLength(ribbons: List[int], k: int) -> int:
    theMaxLen = 0
    lowerBound = 1
    upperBound = max(ribbons)
    
    while lowerBound <= upperBound:
        midPoint = (lowerBound + upperBound) // 2
        numRibbons = getNumberOfRibbonsWithLength(ribbons, midPoint)
        
        if numRibbons >= k:
            theMaxLen = max(theMaxLen, midPoint)
            lowerBound = midPoint + 1
        else:
            upperBound = midPoint - 1
    
    return theMaxLen
