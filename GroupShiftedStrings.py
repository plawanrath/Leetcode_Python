"""
We can shift a string by shifting each of its letters to its successive letter.
For example, "abc" can be shifted to be "bcd".

We can keep shifting the string to form a sequence.
For example, we can keep shifting "abc" to form the sequence: "abc" -> "bcd" -> ... -> "xyz".

Given an array of strings strings, group all strings[i] that belong to the same shifting sequence. 
You may return the answer in any order.

Input: strings = ["abc","bcd","acef","xyz","az","ba","a","z"]
Output: [["acef"],["a","z"],["abc","bcd","xyz"],["az","ba"]]


Idea:
# Shifted string is part of the same group if the diff of ascii value between chars of the string is same
# Eg, 
# 1. s1 = 'acd', s2 = 'mop'
#    here, 
#       for s1, 
#               ascii_val_of('c') - ascii_val_od('a') is 2
#               ascii_val_of('d') - ascii_val_od('c') is 1
#       for s2, 
#               ascii_val_of('o') - ascii_val_od('m') is 2
#               ascii_val_of('p') - ascii_val_od('o') is 1
#    so both s1 and s2 are part of the same group
# 2. s1 = 'ae', s2 = 'bd'
#    here, 
#       for s1, 
#               ascii_val_of('e') - ascii_val_od('a') is 4
#       for s2, 
#               ascii_val_of('d') - ascii_val_od('b') is 2
#    so s1 and s2 are not part of the same group
#     
# Now we can find key using the same approach;
# Once we find the keys then we are left with putting string in the dictionary of the same group

For strings = ["abc","bcd","acef","xyz","az","ba","a","z"]
groupMap = {(2, 2, 1): ['acef'], 1: ['a', 'z'], (1, 1): ['abc', 'bcd', 'xyz'], (25): ['az', 'ba']}
Simply return all the values in a list.

Time Complexity: O(n*len(string)) Space: O(n)
"""
from typing import List
from collections import defaultdict


def groupShiftStrings(strings: List[str]) -> List[List[str]]:
    def findKey(s):
        if not s:
            return -1
        if len(s) == 1:
            return 1 # this is because we can just group all the strings with 1 character together.
        
        k = [0] * (len(s) - 1) # this k will store ascii_val(curr_elem) - ascii_val(prev_elem) so it should be 1 less than the length of string.
        for i in range(1, len(s)):
            k[i - 1] = (ord(s[i]) - ord(s[i - 1])) % 26
        # for string s = 'acd', k array would look like [2, 1]

        # Now we can convert the list into a tuple so that hash it. 
        return tuple(k)
    
    groupMap = defaultdict(list)
    for s in strings:
        key = findKey(s)
        groupMap[key].append(s)
    
    return list(groupMap.values())
