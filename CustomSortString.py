"""
You are given two strings order and s. All the words of order are unique and 
were sorted in some custom order previously.

Permute the characters of s so that they match the order that order was sorted. 
More specifically, if a character x occurs before a character y in order, then x 
should occur before y in the permuted string.

Return any permutation of s that satisfies this property.

Input: order = "cba", s = "abcd"
Output: "cbad"
Explanation: 
"a", "b", "c" appear in order, so the order of "a", "b", "c" should be "c", "b", and "a". 
Since "d" does not appear in order, it can be at any position in the 
returned string. "dcba", "cdba", "cbda" are also valid outputs.

Idea:

The trick is to count the elements of s. After we have some count[char] = 
(the number of occurrences of char in s), we can write these elements in the order we want. 
The order is `Order` + (characters not in `Order` in any order).

Time Complexity: O(Order.length + s.length)
Space: O(s.length)
"""
from collections import Counter

def customSortString(order: str, s: str) -> str:
    counts = Counter(s)
    res = []

    for c in order:
        if c in counts:
            res.append(c * counts[c])
            counts[c] = 0
    
    for c in counts:
        res.append(c * counts[c])
    
    return "".join(res)

