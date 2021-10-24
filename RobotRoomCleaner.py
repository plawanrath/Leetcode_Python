"""
Room Cleaning using robot

Approach: We can take a Visited list which can store cells we clean and run DFS to
do the actual cleaning
"""
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        self.robot = robot
        self.robot.clean()
        self.visited = [(0,0)]
        self.dfs(0, 0)
    
    def dfs(self, x, y):
        if (x-1, y) not in self.visited and self.up():
            self.robot.clean()
            self.visited.append((x-1, y))
            self.dfs(x-1, y)
            self.down()
        if (x, y-1) not in self.visited and self.left():
            self.robot.clean()
            self.visited.append((x, y-1))
            self.dfs(x, y-1)
            self.right()
        if (x+1, y) not in self.visited and self.down():
            self.robot.clean()
            self.visited.append((x+1, y))
            self.dfs(x+1, y)
            self.up()
        if (x, y+1) not in self.visited and self.right():
            self.robot.clean()
            self.visited.append((x, y+1))
            self.dfs(x, y+1)
            self.left()
        
    
    def up(self):
        return self.robot.move()
        
    def left(self):
        self.robot.turnLeft()
        result = self.robot.move()
        self.robot.turnRight()
        return result
        
    def right(self):
        self.robot.turnRight()
        result = self.robot.move()
        self.robot.turnLeft()
        return result
        
    def down(self):
        self.robot.turnLeft()
        self.robot.turnLeft()
        result = self.robot.move()
        self.robot.turnRight()
        self.robot.turnRight()
        return result
