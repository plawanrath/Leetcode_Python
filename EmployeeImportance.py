"""
You have a data structure of employee information, which includes the employee's unique ID, 
their importance value, and their direct subordinates' IDs.

You are given an array of employees employees where:

employees[i].id is the ID of the ith employee.
employees[i].importance is the importance value of the ith employee.
employees[i].subordinates is a list of the IDs of the direct subordinates of the ith employee.
Given an integer id that represents the ID of an employee, return the total importance value 
of this employee and all their direct subordinates.

Approach:
We can use DFS. Its basically traversing the subtree from a given node and adding up the weights.
To make the work simpler we can store a map of employee.id --> employee first. That way we can run
DFS with just the Id and extract employee weights from the dict.
"""
from typing import List


class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates


def getImportance(employees: List['Employee'], id: int) -> int:
    employeeDict = {emp.id: emp for emp in employees}

    def dfs(empId):
        employee = employeeDict[empId]
        return employee.importance + sum(dfs(eid) for eid in employee.subordinates)
    
    return dfs(id)