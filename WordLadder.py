"""
A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of w
ords beginWord -> s1 -> s2 -> ... -> sk such that:

Every adjacent pair of words differs by a single letter.
Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
sk == endWord
Given two words, beginWord and endWord, and a dictionary wordList, 
return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 
if no such sequence exists.

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", 
which is 5 words long.

Idea:
Since this is a traversal problem, we will use BFS.

1. We will first build a dictionary to hold words that can be formed from any word by
changing 1 letter.
    - To form this dictionary we will replace a character with a wildcard like * to say that that letter
        was changed.
2. Once we have this dictionary we basically have a data scturcure that knows if I change 1 character what
are my possible options. 
3. Now we will use BFS.
    - In BFS when we pop a word we will replace each character with the wildcard and check if there is
        a valid intermediate word in the dictionary and if we find it, we will visit that word. 
    - Continue this way until we find the endWord. 
    - We will also keep track of the depth that we are parsing in the BFS
    - Finally when we reach the end word, the level at that point is our answer

Time Complexity: O(M^2 * N) where M is length of each word and N is number of words.
This is because substring operation for forming intermediate word takes O(M) and then generating
the combo dict will be O(M * N)
"""
from collections import defaultdict
from collections import deque
def wordLadderLength(beginWord, endWord, wordList):
    # Form dictionary to hold words that can be formed from any word by changing one letter.
    # BFS
    if not endWord or not beginWord or not wordList or endWord not in wordList:
        return 0
    # We will form a dictionary of a generic word with * for letter that we remove and value
    # will be a list of words that can be formed with that generic word.
    word_combos = defaultdict(list)
    for word in wordList:
        for i in range(len(beginWord)): # This is safe to do since all words would have to be of same length
            word_combos[word[:i] + '*' + word[i+1:]].append(word)
    queue = deque([(beginWord, 1)])
    # visited to avoid repetition of words
    visited = {beginWord: True}
    while queue:
        current_word, level = queue.popleft()
        for i in range(len(beginWord)):
            intermediate_word = current_word[:i] + '*' + current_word[i+1:]
            for word in word_combos[intermediate_word]:
                if word == endWord:
                    return level + 1
                if word not in visited:
                    visited[word] = True
                    queue.append((word, level+1))
            # This doesn't seem necessary but doing this might save some iterations.
            word_combos[intermediate_word] = []
    return 0