"""
You are given a string s and an array of strings words. 
You should add a closed pair of bold tag <b> and </b> to wrap the substrings in s 
that exist in words. If two such substrings overlap, you should wrap them 
together with only one pair of closed bold-tag. If two substrings wrapped by bold tags are 
consecutive, you should combine them.

Return s after adding the bold tags.

Input: s = "abcxyz123", words = ["abc","123"]
Output: "<b>abc</b>xyz<b>123</b>"

Input: s = "aaabbcc", words = ["aaa","aab","bc"]
Output: "<b>aaabbc</b>c"

Idea:
Trie Tree is used to speed up string match (faster than find or startwith in large query request).
Using Merge Intervals to reduce Time and Space Complexity, both from O(n) to O(m), m represets 
    interval numbers after merged.

Time and Space Complexity: O(N)
"""
from typing import List
from collections import defaultdict


class TrieNode:
    def __init__(self) -> None:
        self.children = defaultdict(TrieNode)
        self.isWord = False


class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()
    
    def addWord(self, w: str) -> None:
        p = self.root
        for c in w:
            p = p.children[c]
        p.isWord = True
    
    def wordEnd(self, word: str, startIndex: int) -> int:
        # returns the end of a word from string starting from a start index
        p = self.root
        maxEnd = -1
        for i in range(startIndex, len(word)):
            if word[i] not in p.children:
                break
            p = p.children[word[i]]
            if p.isWord:
                maxEnd = i + 1
        return maxEnd



def addBoldTag(s: str, words: List[str]) -> str:
    #build Trie
    trie = Trie()
    for word in words:
        trie.addWord(word)
    
    # interval merge
    def add_interval(interval):
        nonlocal intervals
        if intervals and intervals[-1][1] >= interval[0]:
            if intervals[-1][1] < interval[1]:
                intervals[-1][1] = interval[1]
        else:
            intervals.append(interval)
    
    n, intervals, res = len(s), [], ""

    # make max match and add to interval
    for i in range(n):
        cur = trie
        max_end = cur.wordEnd(s, i)
        if max_end >= 0:
            add_interval([i, max_end])

    # concat result
    res, prev_end = "", 0
    for start, end in intervals:
        res += s[prev_end:start] + '<b>' + s[start:end] + "</b>"
        prev_end = end
    return res + s[prev_end:]