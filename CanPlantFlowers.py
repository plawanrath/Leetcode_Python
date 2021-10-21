"""
You have a long flowerbed in which some of the plots are planted, and some are not. 
However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, 
and an integer n, return if n new flowers can be planted in the flowerbed without violating 
the no-adjacent-flowers rule.

Input: flowerbed = [1,0,0,0,1], n = 1
Output: true

Input: flowerbed = [1,0,0,0,1], n = 2
Output: false

Time Complexity: O(n)
Strategy: Traverse the array and count the number of occurrences where the flowerbed before and after are empty.

"""
from typing import List


def canPlaceFlowers(flowerbed: List[int], n: int) -> bool:
    count = 0
    i = 0
    while i < len(flowerbed):
        is_flower = flowerbed[i]
        if not is_flower:     # If flowerbed is empty
            cond = is_flower
            if i > 0: # Boundary condition
                cond = cond or flowerbed[i-1] 
            if i < len(flowerbed) -1 : #Boundary condition
                cond = cond or flowerbed[i+1]
            if not cond: # if the beds before and after will be 0, then x or x-1 or x+1 will be 0
                count +=1
                i +=2 # increment by two spots to avoid double counting the next flowerbed
            else:
                i +=1
        else:
            i +=1
            
    return count >= n