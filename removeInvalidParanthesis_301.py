"""
Approach: DFS + Backtracking

Time Complexity: O(2^N)
since in the worst case we will have only left parentheses in the expression and for 
every bracket we will have two options i.e. whether to remove it or consider it.

Space: O(N)
"""
from typing import List


def removeInvalidParentheses(s: str) -> List[str]:
       def getUnmatchedBrackets():
            # calculate the number of unmatched left and right brackets
            ul, ur = 0, 0
            for i in s:
                if i == '(':
                    ul += 1
                elif i == ')':
                    if ul > 0:
                        ul -= 1
                    else:
                        ur += 1
            return ul, ur
       res = set()
       def dfs(index, left, right, unmatched_left, unmatched_right, valid):
            # If we reached the end of the string check if the resulting expression
            # is valid and we removed all mismatched left and right paranthesis
            if index == len(s):
                if left == right and unmatched_left == 0 and unmatched_right == 0:
                    res.add(valid)
                return

            if s[index] == '(':
                if unmatched_left > 0:
                    dfs(index+1, left, right, unmatched_left - 1, unmatched_right, valid)
                # when no unmatched left is found in this case add this to the valid string for
                # further DFS
                dfs(index+1, left+1, right, unmatched_left, unmatched_right, valid + '(')
            elif s[index] == ')':
                if unmatched_right > 0:
                    dfs(index+1, left, right, unmatched_left, unmatched_right - 1, valid)
                if right < left:
                    dfs(index+1, left, right+1, unmatched_left, unmatched_right, valid + ')')
            else:
                dfs(index+1, left, right, unmatched_left, unmatched_right, valid + s[index])
       ul, ur = getUnmatchedBrackets()
       dfs(0, 0, 0, ul, ur, "")
       return list(res)

s = "()())()"
print (removeInvalidParentheses)
# Output: ["(())()","()()()"]