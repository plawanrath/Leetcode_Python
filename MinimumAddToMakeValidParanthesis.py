"""
One move can be inserting a paranthesis at any position.
Return the minimum move to make a string have valid paranthesis. 

s = "())"
output = 1

s = "((("
Output = 3

s = "()"
output = 0


Keep track of the valid status of the string basically number of '(' minus the number of ')'
if we do that then a string is valid when this valid status is 0.

If the string has more opening brackets then this balance will be > 0 and if the string has more
closing brackets then this balance will be < 0. So if this balance becomes >0 we must add a ')' closing bracket
and if this balance becomes -1 we must add a '(' opening bracket. 

We will always add a bracket when balance goes below 0. This means that we will ensure that balance never goes
below -1. At balance  = -1 we will add a bracket. 

If we want to avoid additional space, we will use both balance and the result.

Case 1: When there are all closing brackets let's say ))) answer will be 3 and balance will be 0 at the end
Case 2: When there are more opening brackets than closing brackets, let's say (() here balance will be 1 and answer will be 0
Case 3: When there are more closing brackets than opening brackets, let's say ()) here balance will end up being 0 answer will be 1
Case 4: When there are all opening brackets let's say ((( balance will be 3 and answer will be 0 
"""

def minAddToMakeValid(s: str) -> int:
    ans = bal = 0
    for symbol in s:
        bal += 1 if symbol == '(' else -1
        # It is guaranteed bal >= -1
        if bal == -1:
            ans += 1
            bal += 1
    return ans + bal
