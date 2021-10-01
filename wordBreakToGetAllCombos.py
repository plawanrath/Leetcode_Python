from typing import List


"""
s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
wordBreak(s, wordDict)

return:
['cats and dog', 'cat sand dog']

res = {0: [['']]} 
dfs(len(catsanddog)) = dfs(10) --> 1
    for w in wordDict:
        if s[10 - len(cat):i] = s[7:10] = dog == cat ? No
        if s[10 - len(cats):i] = s[6:10] = ddog == cat ? No
        ... "and" ? No
        ... "sand" ? No
        if s[10 - len(dog):i] = s[7:10] = dog == dog ? Yes
            if 10 - len(dog) = 7 not in res ? Yes (its not)
                dfs(10 - len(dog)) = dfs(10-3) = dfs(7) --> 2
                    for w in wordDict:
                        if s[7 - len(cat):7] = s[4:7] = and == cat ? No
                        ... sand == cats ? No
                        ... and == and ? Yes
                        if 4 not in res:
                            dfs(4) --> 3
                                for w in wordDict:
                                    if s[4 - 3:4] = s[1:4] = ats == cat ? No
                                    if s[4-4:4] = s[0:4] = cats == cats ? Yes
                                        if 0 not in res ? No it is..
                                        for prefix in res[0]:
                                            prefix = ['']
                                            res[4] = [['', 'cats']]
                                    res = {0: [['']], 4: [['', 'cats']]}
                                    if s[1:4] = ats == and ? No
                                    if s[0:4] = cats == sand ? No
                                    if s[1:4] = ats = dog ? No
                            dfs(4) -- > return
                            for prefix in res[7 - len(and)]:
                                1. prefix = ['', 'cats']
                                   res[7] = [['', 'cats', 'and']]
                            res = {0: [['']], 4: [['', 'cats']], 7: [['', 'cats', 'and']]}
                        ... s[sand] == sand ? Yes
                        if 7 - len(sand) = 3 not in res ?:
                            dfs(3) --> 4
                              for w in wordDict:
                                  if s[3 - len(cat):3] = s[0:3] = cat == cat ? Yes
                                    if 3 - len(cat) = 0 not in res ? Yes it is..
                                        for prefix in res[0]:
                                            prefix = ['']
                                            res[3] = [['', 'cat']]
                                  res = {0: [['']], 3: [['', 'cat']], 4: [['', 'cats']], 7: [['', 'cats', 'and']]}
                                  if s[3 - len(cats):3] = s[-1:3] = '' == cats ? No
                                  ... s[0:3] == and ? No
                                  ... s[-1:3] == sand ? No
                                  ... s[0:3] == dog ? No
                            dfs(3) --> return
                            for prefix in res[7 - len(sand)] = res[3]:
                                1. prefix = ['', 'cat']
                                   res[7] = [['', 'cats', 'and'], ['', 'cat', 'sand']]
                            res = {0: [['']], 3: [['', 'cat']], 4: [['', 'cats']], 7: [['', 'cats', 'and'], ['', 'cat', 'sand']]}
                        ... s[7 - len(dog):7] = s[4:7] = and == dog ? No
                        dfs(7) --> return
                    for prefix in res[10 - len(dog)] = res[7]:
                        1. prefix = ['', 'cats', 'and']
                            res[10] = [['', 'cats', 'and', 'dog']]
                        2. prefix = ['', 'cat', 'sand']
                            res[10] = [['', 'cats', 'and', 'dog'], ['', 'cat', 'sand', 'dog']]
                res = {0: [['']], 3: [['', 'cat']], 4: [['', 'cats']], 7: [['', 'cats', 'and'], ['', 'cat', 'sand']], 10: [['', 'cats', 'and', 'dog'], ['', 'cat', 'sand', 'dog']]}
    return

for words in res[10]:
    1. ['', 'cats', 'and', 'dog']
        " ".join(word[1:]) = 'cats and dog'
    2. ['', 'cat', 'sand', 'dog']
        " ".join(word[1:]) = 'cat sand dog'

"""

from collections import defaultdict


def wordBreak(s: str, wordDict: List[str]) -> List[str]:
    # recursion with memorization O(N^2)
    res = defaultdict(list)
    res[0] = [['']] # Where key remembers the index from which the split happened i.e. memorization and value is a list of list of word combinations 
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