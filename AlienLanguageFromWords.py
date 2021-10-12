"""
Given a list of words in an alien language return a string
of unique letters in that string.

You are given a list of strings words from the alien language's dictionary, 
where the strings in words are sorted lexicographically by the rules of this new language.

If a string doesn't meet this rule then return empty string.

Input: words = ["wrt","wrf","er","ett","rftt"]
Output: "wertf"

Approach:
We will need to break this down into 3 parts:
1. Extract dependency rules from the input. For example "A must be before C", 
"X must be before D", or "E must be before B".
2. Put the dependency rules into a graph with letters as nodes and dependencies 
as edges (an adjacency list probably).
3. Topologically sorting the graph nodes.

Why Topological sort ?
Because topological sort is an algorithm that takes a di-grap and returns a list of 
nodes in which each node comes before all the nodes that point to it, and that's is exactly 
what we want to achieve.

How do we build this graph ?

1. iterate over the words, comparing two adjacent pairs at a time, the first word: words[i], 
and the second word, words[i+1]
2. In an inner loop, we iterate over the letters of the two words of the pair at hand
3. keep moving the index of the inner loop as long as the letters/chars in both words are the same.
4. Find the index at which the two words diverge/mismatch
    - Since words are sorted lexicographically
    - the letter from words[i] --(must come before)-- letter from words[i+1]
    - Hence words[i] will have an out-going edge to words[i+1] (As soon as you figure out the direction 
    of this relationship -> build digraph)
    - From this point forward, it's a matter of carrying on with the typical topographical sort algo.
    - Build digraph and modify the in_degree for the second letter (in-degree node) simaltaneoulsy
- Now you have both:
1- di-graph
2- in_degree
- run your topo sort algo!

Time Complexity:
Let N be the total number of strings in the input list.
Let C be the total length of all the words in the input list, added together.
Let U be the total number of unique letters in the alien alphabet

The time complexity will be O(C) since in the worst case, the first and second parts require checking 
every letter of every word

For the third part, DFS has a cost of O(V+E), 
where V is the number of vertices and E is the number of edges.

Space Complexity:
O(V+E) for adjecency list and O(n) for stack in DFS

Example:
Input: words = ["wrt","wrf","er","ett","rftt"]

Building Graph
graph = {}, in_degree = {}
for i in len(words)-1:
    1. i = 0
       j = 0
       until word[0][j] == word[1][j] (considering "wrt","wrf"): j++
            j = 2
       i = 0, j = 2
       word[0][2] = t, word[1][2] = f
       graph = {t: [f]}
       'f' is not in in_degree:
            in_degree = {f: 1}
    2. i = 1
       j = 0
       until word[1][j] == word[2][j] and j is less than length of both words (considering "wrf", "er"): j++
            j = 0 (since first char mismatch)
        i = 1, j = 0
        word[1][0] = w, word[2][0] = e
        graph = {t: [f], w: [e]}
        'e' is not in in_degree:
            in_degree = {f: 1, e: 1}
    3. i = 2
       j = 0
       until word[2][j] == word[3][j] (considering "er","ett"): j++
            j = 1
        i = 2, j = 1
        word[2][1] = r, word[3][1] = t
        graph = {t: [f], w: [e], r: [t]}
        in_degree = {f: 1, e: 1, t: 1}
    4. i = 3
       j = 0
       until word[3][j] == word[4][j] (considering "ett","rftt"): j++
            j = 0
       i = 3, j = 0
       word[3][0] = e, word[4][0] = r
       graph = {t: [f], w: [e], r: [t], e: {r}}
       in_degree = {f: 1, e: 1, t: 1, r: 1}


graph = {t: [f], w: [e], r: [t], e: {r}}
in_degree = {f: 1, e: 1, t: 1, r: 1}

Find all non-zero nodes and add them to stack
letters = {}
for all letters in all words:
    add to set
letters = {w, r, t, e, f}
for node in letters add all nodes that are not in the in_degree dict (this means that those nodes did not have edges coming into them)
we add those into stack

stack = [w], res = []
while stack:
    node = w
    res = [w]

    for neighbors in graph[w]:
        w has only 1 neighbor = e
        in_degree[e] > 1 ? --> No
        in_degree[e] == 1 ? --> yes
            stack = [e] --> append to stack
    
    node = pop stack = e
    res = [w,e]

    for neighbors in graph[e]:
        neighbor of e = r
        in_degree[r] == 1 -> Yes
            stack = [r]
    
    node = pop stack = r
    res = [w, e, r]

    for neighbors in graph[r]:
        neighbor of r = t
        in_degree[t] == 1 ? --> Yes
            stack = [t]
    
    node = pop = t
    res = [w, e, r, t]

    for neighbor in graph[t]:
        neighbor of t = f
        in_degree[f] == 1 ? --> Yes
            stack = [f]
    
    node = pop = f
    res = [w, e, r, t, f]

Stack is empty and length of res == length of letters set meaning that our language has all letters.
return wertf
"""
from typing import List
from collections import defaultdict


def alienOrder(words: List[str]) -> str:
    
    if not words:
        return ""
    
    # build graph
    graph = defaultdict(list)
    in_degree = {}

    for i in range(len(words)-1):
        j = 0 # stores index where words diverge
        while j < len(words[i]) and j < len(words[i+1]) and words[i][j] == words[i+1][j]:
            j += 1
        # we have reached end of word 2 but not end of word 1
        if j == len(words[i+1]) and len(words[i]) > len(words[i+1]) and j <len(words[i]):
            return ""
        # mismatch found so insert into the graph
        if j != len(words[i]) and j != len(words[i+1]):
            graph[words[i][j]].append(words[i+1][j])
            # add in-degree
            if words[i+1][j] in in_degree:
                in_degree[words[i+1][j]] += 1
            else:
                in_degree[words[i+1][j]] = 1

    #Topological sort using DFS
    # Find all the zero-degree nodes/characters and put them into stack
    letters = set() # this set can be used later to validate that our langnage has all the letters.
    for w in words:
        for l in w:
            letters.add(l)
    if len(letters) == 1:
        return letters.pop() # just one letter in this language    
    stack = []
    for node in letters:
        if node not in in_degree:
            stack.append(node)

    #Topological sort using iterative DFS
    res = []
    while stack:
        node = stack.pop()
        res.append(node)

        for neighbor in graph[node]:
            # severe links to neighbours and check if a neigh might turn into a zero-degree as a result
            if in_degree[neighbor] > 1:
                in_degree[neighbor] -= 1
            elif in_degree[neighbor] == 1: # only one left and we're gonna decrement/ severe that link
                stack.append(neighbor)
        
    if len(res) == len(letters): # topological sort is possible
        return "".join(res)
    else: # graph is cyclic and topological sort is not possible
        return ""
