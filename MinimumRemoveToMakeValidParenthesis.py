"""
Given a string s of '(' , ')' and lowercase English characters.

Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the 
resulting parentheses string is valid and return any valid string.

Formally, a parentheses string is valid if and only if:

It is the empty string, contains only lowercase characters, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.

Input: s = "lee(t(c)o)de)"
Output: "lee(t(c)o)de"
Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.
"""

def minRemoveToMakeValid(s: str) -> str:
    stack = []
    extraPos = set()
    res = ""
    for i in range(len(s)):
        if s[i] == '(':
            stack.append((s[i], i))
        elif s[i] == ')':
            if not stack:
                extraPos.add(i)
            else:
                stack.pop()
    if stack:
        for val in stack:
            extraPos.add(val[1])
    for i in range(len(s)):
        if i not in extraPos:
            res += s[i]
    return res
                
    