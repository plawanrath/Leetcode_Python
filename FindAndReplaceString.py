"""
For example, if s = "abcd", indices[i] = 0, sources[i] = "ab", 
and targets[i] = "eee", then the result of this replacement will be "eeecd".

For example, a testcase with s = "abc", indices = [0, 1], and sources = ["ab","bc"] 
will not be generated because the "ab" and "bc" replacements overlap.

Input: s = "abcd", indices = [0, 2], sources = ["a", "cd"], targets = ["eee", "ffff"]
Output: "eeebffff"
Explanation:
"a" occurs at index 0 in s, so we replace it with "eee".
"cd" occurs at index 2 in s, so we replace it with "ffff".

Input: s = "abcd", indices = [0, 2], sources = ["ab","ec"], targets = ["eee","ffff"]
Output: "eeecd"
Explanation:
"ab" occurs at index 0 in s, so we replace it with "eee".
"ec" does not occur at index 2 in s, so we do nothing.

Return the resulting string after performing all replacement operations on s.

Idea:
The basic idea is to bucket sort since each index can have at most one element starting at that index. 
Then we can just build our output string

Let
m = size of our input string
n = size of the index
s = size of the output string

bucket sort index by when they occur O(n)
find if replacement occur O(mn)
Build a new string with our replacement O(s)
Time: O(mn + s)
Space: O(n + s)
"""
from typing import List


def findReplaceString(s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
    m, n = len(s), len(indices)
    buckets = [None] * m
    for i in range(n):
        index, source, target = indices[i], sources[i], targets[i]
        if s.find(source, index, index + len(source)) == index:
            buckets[index] = (source, target)

    skip = 0
    out = []
    for i, c in enumerate(s):
        if skip > 0:
            skip -= 1
        elif buckets[i]:
            src, target = buckets[i]
            skip = len(src) - 1
            out.append(target)
        else:
            out.append(c)
    
    return "".join(out)

