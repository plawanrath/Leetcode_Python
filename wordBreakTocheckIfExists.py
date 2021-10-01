"""
s = "applepenapple", wordDict = ["apple","pen"]

Take a Queue
Start with entire string in the queue, loop through the wordDict if the item at the end of the queue
starts with a word in wordDict then remove that word to create a new string and put that new string in the 
queue. Keep doing that until either the queue is empty which would be either when we found all substrings or
we considered all options.

We can take a set to track if we previously encountered a substring in which case we can ignore that.

s = "carrotandcarrotcakes", wordDict = ["carrot","cakes", "and"]

q = ["carrotandcarrotcakes"]
seen = ()
while q:
    qVal = carrotandcarrotcakes
    for word in wordDict:
        ... carrotandcarrotcakes startsWith carrot ? - Yes
                newS = andcarrotcakes
                newS not in seen ? -- Yes
                    q = ["andcarrotcakes"]
                    seen = ("andcarrotcakes")
        ... carrotandcarrotcakes startsWith "cakes" ? - No
        ... carrotandcarrotcakesstartsWith "and" ? - No
    
    qVal = "andcarrotcakes"
    for word in wordDict:
        ... andcarrotcakes startsWith carrot ? - No
        ... andcarrotcakes startsWith "cakes" ? - No
        ... andcarrotcakes startsWith "and" ? - Yes
                newS = carrotcakes
                newS not in seen ? -- Yes
                    q = [carrotcakes]
                    seen = (andcarrotcakes, carrotcakes)
    
    qVal = carrotcakes
    for word in wordDict:
        ... carrotcakes startsWith carrot ? - Yes
                newS = cakes
                newS not in seen ? -- Yes
                    q = ["cakes"]
                    seen = (andcarrotcakes, carrotcakes, cakes)
        ... carrotcakes startsWith cakes ? - No
        ... carrotcakes startsWith and ? - No
    
    qVal = cakes
    for word in wordDict:
        ... cakes starts with carrot ? - No
        ... cakes starts with cakes ?  - Yes
                newS = ''
                    newS is empty so return True

Complexity: O(n^3) - 2 nested loops and substring computation at each iteration.
"""
from typing import List
from queue import Empty, Queue


def wordBreak(s: str, wordDict: List[str]) -> bool:
    q = Queue()
    q.put(s)
    seen = set()
    while not q.empty():
        qVal = q.get()
        for word in wordDict:
            if qVal.startswith(word):
                newS = qVal[len(word):]
                if not newS:
                    return True
                if newS not in seen:
                    q.put(newS)
                    seen.add(newS)
    return False


"""
s = "carrotandcarrotcakes", wordDict = ["carrot","cakes", "and"]

Take a DP array or size len(s) + 1
We will use two indices i and j where i refers to length of a substring s' and j is the index partitioning the
current substring s' into smaller substrings s'(0, j) and s'(j+1, i). To start with we will initialize dp[0] = True

We start by considering all possible substrings using index i call it s'.
For each s' again we will further divide it into substrings s1' and s2' using index j 
    now dp[i] = True only if dp[j]  = True (which is when s1' meets the criteria) and s2' also meets the criteria

At the end of this return dp[len(s)]

s = "carrotandcarrotcakes", wordDict = ["carrot","cakes", "and"]
dp = [True, False, False, ....]

for i in range(1, 21):
    i = 1
    for j in range(1):
        j = 0
        if dp[0] = True and s[0:1] = c in wordSet ? - False
    i = 2
    ...
    ...
    i = 6
    for j in range(6):
        j = 0
        if dp[0] = True and s[0:6] = carrot in wordSet ? - True
            dp[6] = True
    ...
    ...
    i = 9
    for j in range(9):
        j = 0
        if dp[0] = True and s[0:9] = carrotand in wordSet ? - False
        ...
        j = 6
        if dp[6] = True and s[6:9] = and in wordSet ? - True
            dp[9] = True
    ...
    ...
    i = 15
    for j in range(15):
        j = 0
        if dp[0] = True and s[0:15] = carrotandcarrot in wordSet ? - False
        ...
        j = 9
        if dp[9] = True and s[9:15] = carrot in wordSet ? - True
            dp[15] = True
    ...
    ...
    i = 20
    for j in range(20):
        j = 0...14
        j = 15
        if dp[15] = True and s[15:20] = cakes in wordSet ? - True
            dp[20] = True
    

    return dp[20] = True
"""
def wordBreakDP(s: str, wordDict: List[str]) -> bool:
    wordSet = set(wordDict)
    dp = [False] * (len(s) + 1)
    dp[0] = True
    for i in range(1, len(s) + 1):
        for j in range(i):
            if dp[j] and s[j:i] in wordSet:
                dp[i] = True
                break
    
    return dp[len(s)]


