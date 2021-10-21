"""
Given two strings s and t of lengths m and n respectively, 
return the minimum window substring of s such that every character in t 
(including duplicates) is included in the window. If there is no such substring, 
return the empty string "".

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

Approach: Sliding Window

Time and Space Complexity: O(S + T)
"""
from collections import defaultdict, Counter


def minWindow(s: str, t: str) -> str:
    sCount, tCount = defaultdict(lambda: 0), Counter(t)
    conditionsMet = 0
    conditionsNeeded = len(tCount.keys())

    minWindowLen = float("inf")
    minWindowSubstr = ''
    l, r = 0, 0

    while r < len(s):
        letter = s[r]
        sCount[letter] += 1

        if letter in tCount and sCount[letter] == tCount[letter]:
            conditionsMet += 1
        
        while conditionsMet == conditionsNeeded:
            currWindowLength = r - l + 1
            if currWindowLength < minWindowLen:
                minWindowLen = currWindowLength
                minWindowSubstr = s[l:r+1]
        
            letter = s[l]
            sCount[letter] -= 1
            if letter in tCount and sCount[letter] < tCount[letter]:
                conditionsMet -= 1
            l += 1
        r += 1
    
    return minWindowSubstr
