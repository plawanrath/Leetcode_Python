"""
We have n cities and m bi-directional roads where roads[i] = [ai, bi] connects city ai 
with city bi. Each city has a name consisting of exactly three upper-case English 
letters given in the string array names. Starting at any city x, you can reach any city y where 
y != x (i.e., the cities and the roads are forming an undirected connected graph).

You will be given a string array targetPath. You should find a path in the graph of the same 
length and with the minimum edit distance to targetPath.

You need to return the order of the nodes in the path with the minimum edit distance. 
The path should be of the same length of targetPath and should be valid (i.e., there should 
be a direct road between ans[i] and ans[i + 1]). If there are multiple answers return any one of them.

Input: n = 5, roads = [[0,2],[0,3],[1,2],[1,3],[1,4],[2,4]], names = ["ATL","PEK","LAX","DXB","HND"], 
targetPath = ["ATL","DXB","HND","LAX"]
Output: [0,2,4,2]
Explanation: [0,2,4,2], [0,3,0,2] and [0,3,1,2] are accepted answers.

Approach: 
0-1 BFS
This is a form of BFS that can replace a path finding algorithm like Dijkistra's of 
Bellmen-Ford Algorithm when the weight constraints are not variable but 0 or 1.

Basically this works same as BFS but just that normally in BFS we would use a queue and
add neighbors to the end of a queue and process queue but in this case we use a Deque and 
0 weighted edges will be added to front of the Deque and 1 weighted edges will be added to
the back of the Deque. 

This order of adding to the Deque ensures that when you pop from the front of the queue, it
will always ensure that we pick nodes with distance K before touching nodes with distances
K+1. Hence, the nodes in the Deque are always sorted as per their distance from the source node.
"""
from typing import List
from collections import defaultdict, deque


def mostSimilar(n: int, roads: List[List[int]], names: List[str], targetPath: List[str]) -> List[int]:
    # build a graph of roads
    graph = defaultdict(list)
    for a,b in roads:
        graph[a].append(b)
        graph[b].append(a)
    
    # sort of defining a circular road for each city with itself
    graph[None] = list(range(n))

    # start with inf distances to each city
    m = len(targetPath)
    distances = [[float('inf')]*n for _ in range(m)]

    # queue tracks path and current distance
    queue = deque()
    queue.append([[None],0])
    while queue:
        path, curr_dist = queue.popleft()
        # because of padding, path will look like [None, 1,0,1,..], so length -1
        k = len(path) - 1
        if k == m:
            return path[1:] # ignoring None
        # we can look at the next cities accessible from the end of the queue
        for next_city in graph[path[-1]]:
            # check if current node was visited or not
            if distances[k][next_city] > curr_dist + (names[next_city] != targetPath[k]):
                # update min distance
                distances[k][next_city] = curr_dist + (names[next_city] != targetPath[k])
                # append to left if weight = 0, append to right if weight == 1.
                if names[next_city] == targetPath[k]:
                    queue.appendleft([path+[next_city],curr_dist])
                else:
                    queue.append([path+[next_city],curr_dist+1])
    return []
