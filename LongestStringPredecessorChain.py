"""
wordA is a predecessor of wordB if and only if we can insert exactly one letter 
anywhere in wordA without changing the order of the other characters to make it equal to wordB.

A word chain is a sequence of words [word1, word2, ..., wordk] with k >= 1 where word1 is a predecessor
of word2 and word2 is a predecessor of word3 and so on.

Return the length of the longest possible word chain with words chosen from the given list of words.

nput: words = ["a","b","ba","bca","bda","bdca"]
Output: 4
Explanation: One of the longest word chains is ["a","ba","bda","bdca"].

Approach:
Dynamic Programming

1. Sort the list of words in ascending order based on their length.
2. We can iterate over the sorted list and calculate the length of the 
longest sequence possible where the word at index i is the end word.  
3. We store this result in a map where key is the word and value is the sequence length. 
4. By doing this we ensure that, for each word that we encounter, we already know the 
result of all of its possible predecessors.

Time Complexity:
Let N be the number of words in the list and L be the maximum possible length of a word.
Time complexity: O(N (log N + L^2))
"""
from typing import List


def longestStrChain(words: List[str]) -> int:
    dp = {}
    words.sort(key=lambda x: len(x))
    longestWordSequenceLength = 1
    
    for word in words:
        currlength = 1
        # Find all possible predecessors for the current word by removing one letter at a time
        for i in range(len(word)):
            new_word = word[:i] + word[i+1:]
            previousLength = dp[new_word] if new_word in dp else 0
            currlength = max(currlength, previousLength + 1)
        dp[word] = currlength
        longestWordSequenceLength = max(longestWordSequenceLength, currlength)
    return longestWordSequenceLength