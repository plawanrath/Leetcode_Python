"""
Given a rows x cols screen and a sentence represented as a list of strings, 
return the number of times the given sentence can be fitted on the screen.

The order of words in the sentence must remain unchanged, and a word cannot be split 
into two lines. A single space must separate two consecutive words in a line.

Input: sentence = ["hello","world"], rows = 2, cols = 8
Output: 1
Explanation:
hello---
world---
The character '-' signifies an empty space on the screen.
"""
from typing import List


def wordsTyping(sentence: List[str], rows: int, cols: int) -> int:
    ans = 0
    dp = {}
    # dp[i] = [j, finish]:  
    #    When a row start from the word with index i, we will repeat the whole sentence in 'finish' times, 
    #    and next row will start from the word with index j

    r, startidx = 0, 0

    total_len = sum([len(s) for s in sentence]) + len(sentence) # used to speed up filling dp table

    while r < rows:
        c = 0
        if startidx not in dp:
            finish = 0 # repeat time
            nowIdx = startidx # remain startidx for the key of dp table

            # input as many as possible sentence if there is enough space in this row
            if cols /total_len > 1:
                finish += cols//total_len
                c += total_len*finish

            # input word by word into this row
            while cols - c - len(sentence[nowIdx]) >= 0:
                c += len(sentence[nowIdx])+1
                nowIdx += 1
                if nowIdx == len(sentence):
                    nowIdx = 0
                    finish += 1
            # update DP
            dp[startidx] = [nowIdx, finish]
        startidx, finish = dp[startidx]
        ans += finish
        r += 1
    
    return ans