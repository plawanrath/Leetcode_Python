"""
You are given an integer num. You can swap two digits at most 
once to get the maximum valued number.

Return the maximum valued number you can get.

Input: num = 2736
Output: 7236
Explanation: Swap the number 2 and the number 7.

Idea: use a Greedy approachL
1. Find the first digit greater than the previous digit
        If we already reached the end of the number then that is the largest
2. Try and find the rightmost largest digit after this inflection point.
3. Then we need to find the first digit from the left that is smaller than this
   largest digit we already found. That is where we need to swap.
4. Swap      

Example: num = 2736
res = [2, 7, 3, 6], i = 1, n = 4

while i < n:
    1. res[i] > res[i-1] = 7 > 2 ? ---> Yes
            break with i = 1

i == n ? ---> No
bigSwapIndex, j = 1

while j < n:
    1. j = 1, n = 4, bigSwapIndex = 1
    res[1] > res[1] = 7 > 7 ---> No
    2. j = 2
    res[2] > res[1] = 3 > 7 ? ---> No
    3. j = 3
    res[3] > res[1] = 6 > 7 --> No

smallSwapIndex = 0
while smallSwapIndex < i:
    1. smallSwapIndex = 0, i = 1
    res[0] < res[1] = 2 < 7 ? ----> Yes
        break

So we can swap indices 0 and 1 to get [7, 2, 3, 6] which gets 7236 which
is the largest number possible with only 1 swap. 

Complexity: O(n)
"""

def maxSwap(num: int) -> int:
    if num < 10:
        return num

    i = 1
    res = [c for c in str(num)]
    n = len(res)

    
    # We want to find the inflection point which is the first digit that
    # is greater than the previous digit.
    while i < n:
        if res[i] > res[i - 1]:
            break
        i += 1
    
    # If we have alraedy reached the end of res that means that the number is
    # strictly decreasing. Meaning that the number is already the largest and
    # we don't need to swap any digits.
    if i == n:
        return num
    
    bigSwapIndex, j = i, i

    # Now we need to find the rightmost largest number (if any) after the inflection point
    # to see if we can get any other swap candidates.
    while j < n:
        if res[j] >= res[bigSwapIndex]:
            bigSwapIndex = j
        j += 1
    
    smallSwapIndex = 0
    # Now we need to find the first number that is smaller than res[bigSwapIndex]
    # that resides in the left side of the inflection point.
    while smallSwapIndex < i:
        if res[smallSwapIndex] < res[bigSwapIndex]:
            break
        smallSwapIndex += 1

    # Now we just swap
    res[smallSwapIndex], res[bigSwapIndex] = res[bigSwapIndex], res[smallSwapIndex]

    return int(("").join(res))