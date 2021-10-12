"""
A storekeeper is a game in which the player pushes boxes around in a warehouse trying to get them to target locations.

The game is represented by an m x n grid of characters grid where each element is a wall, floor, or box.

Your task is to move the box 'B' to the target position 'T' under the following rules:

The character 'S' represents the player. The player can move up, down, left, right in grid if it is a floor (empty cell).
The character '.' represents the floor which means a free cell to walk.
The character '#' represents the wall which means an obstacle (impossible to walk there).
There is only one box 'B' and one target cell 'T' in the grid.
The box can be moved to an adjacent free cell by standing next to the box and then moving in the direction of the box. This is a push.
The player cannot walk through the box.

Return the minimum number of pushes to move the box to the target. If there is no way to reach the target, return -1.

Input: grid = [["#","#","#","#","#","#"],
               ["#","T","#","#","#","#"],
               ["#",".",".","B",".","#"],
               ["#",".","#","#",".","#"],
               ["#",".",".",".","S","#"],
               ["#","#","#","#","#","#"]]
Output: 3
Explanation: We return only the number of times the box is pushed.


Approach:
Lets break the question into simple parts:

- Lets think that we have no person and we have to find the minimum path between box and the target. Easy right? Simple BFS.
- If you know how to solve the first part, what I actually do is modify first part with few constraints.
    1. I just check whether the box can be shifted to the new position(up, down, left, right)
    2. For it to be shifted to the new position the person has to be in a corresponding position right?
    3. So we check if the person can travel from his old position to his corresponding new position(using another BFS).
    4. If the person can travel to his new position than the box can be shifted, otherwise the box cannot be shifted.
- We keep repeating step 2 until we reach the target or it is not possible to move the box anymore.

Time and Space Complexity: Time = Space = O((rows*cols)^2)
"""
from typing import List
from collections import deque


def minPushBox(grid: List[List[str]]) -> int:
    
    # record the co-ordinates of target, box and person
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "T":
                target = (i,j)
            if grid[i][j] == "B":
                box = (i, j)
            if grid[i][j] == "S":
                person = (i,j)
    
    # helper function to check if given co-ordinates are valid to travel
    def valid(x, y):
        return 0<=x<len(grid) and 0<=y<len(grid[0]) and grid[x][y]!='#'
    
    # Helper function to check whether the person can travel from current position to the destination position using BFS.
    def isValidPath(curr, dest, box):
        q = deque([curr])
        visited = set()
        while q:
            pos = q.popleft()
            if pos == dest:
                return True
            new_pos = [(pos[0]+1,pos[1]),(pos[0]-1,pos[1]),(pos[0],pos[1]+1),(pos[0],pos[1]-1)]
            for x, y in new_pos:
                if valid(x,y) and (x,y) not in visited and (x,y)!=box:
                    visited.add((x,y))
                    q.append((x,y))
        return False
    
    # this is the main bfs which gives us the answer
    queue = deque([(0,box,person)])
    visited = {box + person} # positions where box and the person are present are both visited to start
    while queue:
        dist, box, person = queue.popleft()
        if box == target:
            return dist # return the distance if box is at the target
        
        # these are the new possible coordinates/indices box can be placed in (up, down, right, left).
        new_box_pos = [(box[0]+1,box[1]),(box[0]-1,box[1]),(box[0],box[1]+1),(box[0],box[1]-1)]
        # these are the corresponding coordinates the person has to be in to push the box into the new coordinates
        new_person_pos = [(box[0]-1,box[1]),(box[0]+1,box[1]),(box[0],box[1]-1),(box[0],box[1]+1)]

        for new_box, new_person in zip(new_box_pos, new_person_pos):
            # we check if the new box coordinates are valid and our current state is not in visited
            if valid(new_box[0], new_box[1]) and new_box+new_person not in visited:
                # we check corresponding person coordinates are valid and if it is possible for the person to reach the new coordinates
                if valid(new_person[0], new_person[1]) and isValidPath(person,new_person,box):
                    visited.add(new_box + new_person)
                    queue.append((dist+1,new_box,box))
    
    return -1