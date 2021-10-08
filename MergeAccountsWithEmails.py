"""
Given a list of accounts where each element accounts[i] is a list of strings, 
where the first element accounts[i][0] is a name, and the rest of the elements 
are emails representing emails of the account.

After merging the accounts, return the accounts in the following format: 
the first element of each account is the name, and the rest of the elements are emails in sorted order.

Merge these accounts:
1. 2 Accounts may not be same even if they have same names. 
2. 2 accounts will only be same if they have atleast 1 common email and same name.

accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
Output: [["John","john00@mail.com","john_newyork@mail.com","johnsmith@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]


Approach:
If we draw a line between 2 emails that are part of the same account and make a graph like that then this is a problem
of finding all connected components in a graph. We can use BFS or DFS to do this.

idea: graph traversal (use a set "visited" to record the visited states)
# (1) build a graph with different individual components to build this graph, for a user link every other email with the first email.
# (2) use graph traversal to find connected components

accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
graph = {}
graph_name = {}
for i in range accounts:
    1. ["John","johnsmith@mail.com","john_newyork@mail.com"]
       name = "John"
       first_email = "johnsmith@mail.com"
       for all emails:
           graph = {"johnsmith@mail.com": {"johnsmith@mail.com", "john_newyork@mail.com"}, "john_newyork@mail.com": {"johnsmith@mail.com"}}
           graph_name = {"johnsmith@mail.com": "John", "john_newyork@mail.com": "John"}
    2. ["John","johnsmith@mail.com","john00@mail.com"]
       name = "John"
       first_email = "johnsmith@mail.com"
       for all emails:
           graph = {"johnsmith@mail.com": {"johnsmith@mail.com", "john_newyork@mail.com", "john00@mail.com"}, "john_newyork@mail.com": {"johnsmith@mail.com"}, "john00@mail.com": {"johnsmith@mail.com"}}
           graph_name = {"johnsmith@mail.com": "John", "john_newyork@mail.com": "John", "john00@mail.com": "John"}
    3. ["Mary","mary@mail.com"]
       name = "Mary"
       first_email = "mary@mail.com"
       for all emails:
           graph = {"johnsmith@mail.com": {"johnsmith@mail.com", "john_newyork@mail.com", "john00@mail.com"}, "john_newyork@mail.com": {"johnsmith@mail.com"}, "john00@mail.com": {"johnsmith@mail.com"}, "mary@mail.com": {"mary@mail.com"}}
           graph_name = {"johnsmith@mail.com": "John", "john_newyork@mail.com": "John", "john00@mail.com": "John", "mary@mail.com": "Mary"}
    4. ["John","johnnybravo@mail.com"]
       name = "John"
       first_email = "johnnybravo@mail.com"
       for all emails:
            graph = {"johnsmith@mail.com": {"johnsmith@mail.com", "john_newyork@mail.com", "john00@mail.com"}, "john_newyork@mail.com": {"johnsmith@mail.com"}, "john00@mail.com": {"johnsmith@mail.com"}, "mary@mail.com": {"mary@mail.com"}, "johnnybravo@mail.com": {"johnnybravo@mail.com"}}
            graph_name = {"johnsmith@mail.com": "John", "john_newyork@mail.com": "John", "john00@mail.com": "John", "mary@mail.com": "Mary", "johnnybravo@mail.com": "John"}

visited = {}
ans = []
for email in graph.keys:
    1. email = "johnsmith@mail.com"
       email not in visited -> Yes
            visited = {"johnsmith@mail.com"}
            queue = ["johnsmith@mail.com"]
            connected = []
            while queue:
                node = "johnsmith@mail.com"
                connected = ["johnsmith@mail.com"]
                for neighbors in graph["johnsmith@mail.com"]:
                    queue = ["johnsmith@mail.com", "john_newyork@mail.com", "john00@mail.com"]
                    visited = ["johnsmith@mail.com", "john_newyork@mail.com", "john00@mail.com"]
                ....
                connected = ["johnsmith@mail.com", "john_newyork@mail.com", "john00@mail.com"]
            ans = [graph_name["john00@mail.com"] + sorted(connected)]
            ans = [["John","john00@mail.com","john_newyork@mail.com","johnsmith@mail.com"]]
    2. email = "john_newyork@mail.com"
       email not in Visited --> No - It is in visited
    
    ... continue for all 3 john emails

        email = "mary@mail.com"
        email not in Visited --> Yes
            queue = ["mary@mail.com"]
            while queue:
                node = "mary@mail.com"
                connected = ["mary@mail.com"]
                for neighbor in graph["mary@mail.com"]:
                    No neighbors
                ans = [["John","john00@mail.com","john_newyork@mail.com","johnsmith@mail.com"], ["Mary", "mary@mail.com"]]

        email = "johnnybravo@mail.com"
        email not in Visited --> Yes
        ....
        ...
        ans = [["John","john00@mail.com","john_newyork@mail.com","johnsmith@mail.com"], ["Mary", "mary@mail.com"], ["John", "johnnybravo@mail.com"]]

Time Complexity: O(n log n)
Space: O(n)
"""
from typing import List
from collections import defaultdict


def accountsMerge(accounts: List[List[str]]) -> List[List[str]]:
    # build a graph
    # each email (component) is connected to 
    # (1) the first email in account + (2) person name
    graph = defaultdict(set)
    graph_name = {}
    for i in range(len(accounts)):
        name = accounts[i][0]
        first_email = accounts[i][1]
        for email in accounts[i][1:]:
            graph[email].add(first_email)
            graph[first_email].add(email)
            graph_name[email] = name
    
    # BFS graph traversal, find connected components
    # iterate each node and connect all its neighbours
    visited = set()
    ans = []
    for email in graph.keys():
        if email not in visited:
            visited.add(email)
            queue = [email] 
            connected = [] # a connected component
            while queue:
                node = queue.pop(0)
                connected.append(node)
                # visit all the neighbours
                for neighbour in graph[node]:
                    if neighbour not in visited:
                        visited.add(neighbour)
                        queue.append(neighbour)
            ans.append([graph_name[email]] + sorted(connected))
    return ans