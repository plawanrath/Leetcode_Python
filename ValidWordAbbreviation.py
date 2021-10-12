"""
Given a string word and an abbreviation abbr, return whether the string matches the given abbreviation.

For example, a string such as "substitution" could be abbreviated as (but not limited to):

"s10n" ("s ubstitutio n")
"sub4u4" ("sub stit u tion")
"12" ("substitution")
"su3i1u2on" ("su bst i t u ti on")
"substitution" (no substrings replaced)

The following are not valid abbreviations:

"s55n" ("s ubsti tutio n", the replaced substrings are adjacent)
"s010n" (has leading zeros)
"s0ubstitution" (replaces an empty substring)

Idea:
We can use 2 pointers to traverse word and abbreviation. When we find a 
number shifr the word by that many numbers at the end both pointers should
be at the end of the two strings. 

O(n)

Example:
word: substitution, abbr = "s10n"
p1 = p2 = 0
while p1 < 12 and p2 < 4:
    abbr[0] = s --> Goes to else:
        word[p1] == abbr[p2] = s == s:
            p1, p2 = 1, 1

    abbr[1] is a digit:
        shift = 0
        while p2 < 4 and abbr[p2] is digit:
            p2 = 1, abbr[p2] = 1
            shift = 0 + 1 = 1
            p2 = 2, abbr[p2] = 0
            shift = 1 * 10 + 0 = 10
            p2 = 3
    p1 = p1 + 10 = 11

    abbr[3] is not a digit:
        word[11] == abbr[3] so p1 = 12, p2 = 4

Since both p1 and p2 have been reaversed we can return True.

Time Complexity: O(n), space: O(1)
"""

def validWordAppriviation(word: str, abbr: str) -> bool:
    p1, p2 = 0, 0
    while p1 < len(word) and p2 < len(abbr):
        if abbr[p2].isdigit():
            if abbr[p2] == "0":
                return False # leading 0 in digits is not valid
            shift = 0
            while p2 < len(abbr) and abbr[p2].isdigit():
                shift = shift * 10 + int(abbr[p2])
                p2 += 1
            p1 += shift # shift p1 by the number found in p2
        else:
            if word[p1] != word[p2]:
                return False
            p1 += 1
            p2 += 1
    return p1 == len(word) and p2 == len(abbr)