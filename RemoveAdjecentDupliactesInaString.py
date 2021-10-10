"""
Return string after all adjecent duplicates are removed.

Example:
Input: s = "abbaca"
Output: "ca"

For example, in "abbaca" we could remove "bb" since the letters are 
adjacent and equal, and this is the only possible move.  
The result of this move is that the string is "aaca", of which only 
"aa" is possible, so the final string is "ca".

Idea:
This is a stack problem.
Go over the string char by char. First you find a char, push it to the 
stack. Then when you process the next char, if it matches the char
at the top of the stack, pop and if it doesn't match then push the char.
At the end convert stack to string.

s = "abbaca"
stack = []
for ch in s:
    1. ch = a
    stack = [a]
    2. ch = b
    b == stack[-1] = b == a ?  ---> No
    stack = [a, b]
    3. ch = b
    b == stack[-1] = b == b ? ---> Yes
        stack.pop
    stack = [a]
    4. ch = a
    a == stack[-1] = a == a ? ---> Yes
        stack.pop
    stack = []
    5. ch = c
    stack is empty
    stack = [c]
    6. ch = a
    a == stack[-1] = a == c ? ---> No
    stack = [c, a]

Return "ca"

Time and Space Complexity: O(n)
"""

def removeAdjecentDuplicates(s: str) -> str:
    stack = []
    for c in s:
        if stack and c == stack[-1]:
            stack.pop()
        else:
            stack.append(c)
    return "".join(stack)