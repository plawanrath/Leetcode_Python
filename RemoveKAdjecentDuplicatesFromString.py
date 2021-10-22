"""
You are given a string s and an integer k, a k duplicate removal consists of 
choosing k adjacent and equal letters from s and removing them, causing the left 
and the right side of the deleted substring to concatenate together.

We repeatedly make k duplicate removals on s until we no longer can.

Return the final string after all such duplicate removals have been made.

Idea:
the idea was quite easy: calculate the number of serial letters and store in tuple with letter in stack. 
once the number reaches k, pop() them all. Eventually the remain of stack would be the string we want.

Time Complexity: O(n)
"""
def removeDuplicates(s: str, k: int) -> str:
    stack = [(s[0], 1)]
    for i in range(1, len(s)):
        cnt = stack[-1][1] + 1 if stack and stack[-1][0] == s[i] else 1
        stack.append((s[i], cnt))
        while stack and stack[-1][1] == k:
            for _ in range(k):
                stack.pop()
    "".join(letter for letter, _ in stack)
