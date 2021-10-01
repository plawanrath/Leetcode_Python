from typing import List


"""
s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
wordBreak(s, wordDict)

return:
['cats and dog', 'cat sand dog']
"""

from collections import defaultdict


def wordBreak(s: str, wordDict: List[str]) -> List[str]:
    # recursion with memorization
    res = defaultdict(list)
    res[0] = [['']]
    def dfs(i):
        if i < 0:
            return
        for w in wordDict:
            if s[i - len(w):i] == w:
                if i - len(w) not in res:
                    dfs(i - len(w))
                for prefix in res[i - len(w)]:
                    res[i].append(prefix + [w])
    
    dfs(len(s))
    return [" ".join(words[1:]) for words in res[len(s)]]