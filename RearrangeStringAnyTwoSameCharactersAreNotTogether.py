"""
Given a string s, rearrange the characters of s so that any two adjacent characters are not the same.

Return any possible rearrangement of s or return "" if not possible.

Input: s = "aab"
Output: "aba"

Approach:
Create a dictionary of letters and their frequencies. 
Build a max Heap with letters in the string and frequencies.
Then keep popping 2 items at a time from the heap, decrement their frequency and push them back.

Edge Cases:
1. Since we are always popping two items at a time, we will definitely run into an out of bounds error 
if we have an odd number of unique items in the given string. To avoid this, we need to make sure our 
heap at least has two items at any given time. 

2. Again if the there is an odd number of unique letters in the string, 
there will be one last item/letter remaining in the heap when our loop terminates. 
Hence we need to examine that last item:
    - If the last item has a freq greater than 1: -> then return "" becasue we 
        can't escape having the same letter repeated contigiously.
    - If the item has freq = 1, we pop it, add it to our result and we're done.

Time Complexity: O(n log n) to push/pop all unique characters (looping through n
characters in the worst case and pushing to heap is O(log n))

"""
from collections import Counter
import heapq

def reorganizeString(s: str) -> str:
    if not s:
        return ""
    freqs = Counter(s)
    heap = []
    for k, v in freqs.items():
        heapq.heappush(heap, (-v, k))
    res = ""
    while len(heap) > 1:
        freq1, letter1 = heapq.heappop(heap)
        freq2, letter2 = heapq.heappop(heap)

        res += letter1 + letter2

        if abs(freq1) > 1:
            heapq.heappush(heap, (freq1+1, letter1)) # when we do freq1 + 1 we are actually decreasing count since freq is stored as a -ve number
        if abs(freq2) > 1:
            heapq.heappush(heap, (freq2+1, letter2))
    
    while heap:
        freq, letter = heapq.heappop(heap)
        if abs(freq) > 1:
            return ""
        res += letter
    
    return res