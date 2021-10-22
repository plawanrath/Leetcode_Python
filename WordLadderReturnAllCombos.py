"""
Given two words, beginWord and endWord, and a dictionary wordList, 
return all the shortest transformation sequences from beginWord to endWord, 
or an empty list if no such sequence exists. Each sequence should be returned as a 
list of the words [beginWord, s1, s2, ..., sk].

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: [["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]]
Explanation: There are 2 shortest transformation sequences:
"hit" -> "hot" -> "dot" -> "dog" -> "cog"
"hit" -> "hot" -> "lot" -> "log" -> "cog"

Approach:

Use BFS to find shorterst transformation path from begin word to end word. 
A valid transformation is to change any one character and transformed word should be in the a word list.

Since we need to find all shortest paths, we need to build a search tree during BFS and 
backtrack along that tree to restore all shortest paths.
So we can't stop BFS once we found a transformed word is endword but instead finishing 
searching is this BFS layer since there could be more than one shortest path.

And we still need to rule out all node that we have searched previously. Meanwhile if two nodes have 
a same child node, we need to add that child node to both node's children list as we need to backtrack 
all valid paths. So unlike a regular BFS, we can't use a "seen" set but a more like "explored" set. 
Otherwise, e.g. tree: {x->z, y->z}, z won't be added to y's children list if x is visited first and 
z is already seen in x's search.
"""
from string import ascii_lowercase
from collections import defaultdict


def findLadders(beginWord, endWord, wordList):
	tree, words, n = defaultdict(set), set(wordList), len(beginWord)
	if endWord not in wordList: return []
	found, q, nq = False, {beginWord}, set()
	while q and not found:
		words -= set(q)
		for x in q:
			for y in [x[:i]+c+x[i+1:] for i in range(n) for c in ascii_lowercase]:
				if y in words:
					if y == endWord: 
						found = True
					else: 
						nq.add(y)
					tree[x].add(y)
		q, nq = nq, set()
	def backtrack(x): 
		return [[x]] if x == endWord else [[x] + rest for y in tree[x] for rest in backtrack(y)]
	return backtrack(beginWord)