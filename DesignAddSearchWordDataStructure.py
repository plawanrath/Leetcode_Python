"""
Design a data structure that supports adding new words and finding if a string matches any previously added string.

Implement the WordDictionary class:

WordDictionary() Initializes the object.
void addWord(word) Adds word to the data structure, it can be matched later.
bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' 
where dots can be matched with any letter.

Approach:
We can build a Trie that will contain all the words. 
Normally in a trie when doing a search, I would match each character and then keep going down the trie until the end and at the end
if I can determine that its a valid word I would return True. In this case however since '.' can be any character, whenever I 
encounter a '.' I will need to recursively match if any character ignoring that '.' could be added to the string to get a valid search
result. I can do that using a recursive call to the search function itself starting from the position after the '.'.


Time Complexity: Since in english only 26 characters are possible the recursive call is only possible 26^N times. So the worst case
complexity would be O(N 26^N) and Space complexity: O(N)
"""
from collections import defaultdict


class TriNode:
    def __init__(self) -> None:
        self.children = defaultdict(TriNode) # I create a defaultdict becuase that auto handles initialization if a dict value doesn't already exist
        self.isWord = False


class WordDictionary:

    def __init__(self):
        self.root = TriNode()        

    def addWord(self, word: str) -> None:
        pointer = self.root
        for c in word:
            pointer = pointer.children[c]
        pointer.isWord = True

    def _search(self, word, node, i):
        if not node:
            return False
        if i == len(word):
            return node.isWord
        if word[i] == ".":
            return any([self._search(word, n, i+1) for n in node.children.values()])
        else:
            return self._search(word, node.children.get(word[i]), i+1)
            
    def search(self, word: str) -> bool:
        return self._search(word, self.root, 0)