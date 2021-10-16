"""
Given a string s and an array of strings words, return the number of words[i] that is a subsequence of s.

A subsequence of a string is a new string generated from the original string with some characters 
(can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".

Input: s = "abcde", words = ["a","bb","acd","ace"]
Output: 3
Explanation: There are three strings in words that are a subsequence of s: "a", "acd", "ace".


IDEA:
👉 finding the index of each character in "s" then virtually cutting "s" => from index+1 to last.
👉 repeating above point for all the characters in word, if any ch not found in s then it will return -1.

e.g.-
s="abgheaf"
w=["gef", "gefk"]
index = -1

first found index of "g" in s[index+1 : ] => "abgheaf", which is 2 (i.e. index=2).
Now, we find the index of "e" in s[index+1:] => s[2+1:] => s[3:] => "heaf" which results index=4.
Again find the index of "f" in s[index+1: ] => s[4+1:] => s[5:] => "af" which gives index=6.
Another word:
if we are having word as "gefk" then after repeating previous 3 points we will have index=6.
Now find the index of "k" in s[index+1:] => s[6+1:] => s[7:] =>"" which will give index=-1. i.e. not found.
"""
from typing import List


def numMatchingSubseq(s: str, words: List[str]) -> int:
    def is_sub(word):
        index = -1
        for ch in word:
            index = s.find(ch, index + 1)
            if index == -1:
                return False
        return True

    count = 0
    for word in words:
        if is_sub(word):
            count += 1
    
    return count