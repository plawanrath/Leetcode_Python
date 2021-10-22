"""
Given an array of distinct integers candidates and a target integer target, 
return a list of all unique combinations of candidates where the chosen numbers sum to target. 
You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. 
Two combinations are unique if the frequency of at least one of the chosen numbers is different.

Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.

Approach: Backtracking
we could incrementally build the combination, and once we find the current combination is not valid, 
we backtrack and try another option.

Time Complexity: O(N^2) N for inner loop and N for backtracking
Space: O(N) for the call stack
"""
from typing import List


def combinationSum(candidates: List[int], target: int) -> List[List[int]]:
    results = []
    def backtrack(remain, comb, start):
        if remain == 0:
            # make a deep copy of the current combination
            results.append(list(comb))
            return
        elif remain < 0:
            # exceed the scope, stop exploration.
            return

        for i in range(start, len(candidates)):
            # add the number into the combination
            comb.append(candidates[i])
            # give the current number another chance, rather than moving on
            backtrack(remain - candidates[i], comb, i)
            # backtrack, remove the number from the combination
            comb.pop()

    backtrack(target, [], 0)

    return results