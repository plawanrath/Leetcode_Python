"""
Given a string s which represents an expression, evaluate this expression and return its value. 

The given string only has + and - . Only these 2 operations need to be supported with or without brackets.

s = "1 + 1"
Output = 2

s = "(1+(4+5+2)-3)"
Output = 9

Idea: We will definitely need to use a stack to store and evaluate data. But to make things
easier we can limit our operations to just one operator. Meaning that we can represent our subtractions
as simply addition of negative numbers:

A - B - C = A + (-B) + (-C)

One another thing we can do is let's say we have an expression like (7 - (2 + 3)) instead of pushing everything to
the stack and doing a pop and calculation we could simply calculate 2 + 3 on the go and use that which would reduce the
amount of push and pop operations from the stack. 

Algorithm:
1. Iterate over the expression character by character distinguishing between digit and non-digit
2. Since we are reading strings, when reading digits we would need to form the number:
    For example if we are tryint to read "12" we would read 1 first and then we would need to multiply it by 10 and add 2 to get 12.
3. When we come across an operator + or - we can evaluate the expression on the left and then save the sign for next evaluation.
4. If the character is an opening paranthesis (, we can just push the result calculated so far and the sign onto the stack
5. If the character is a closing parenthesis ), we first calculate the expression to the left. The result from this would be the 
    result of the expression within the set of parenthesis that just concluded. This result is then multiplied with the sign, 
    if there is any on top of the stack

s = "(1+(4+5)-3)"
Output: 7

s = "(1+(4+5)-3)"
stack = []
operand = 0, res = 0, sign = 1
for c in s:
    1. c = (
       stack = [0, 1] # append current res and sign
    2. c = 1 --> digit
       operand = 0 * 10 + 1 = 1
    3. c = +
       res = 0 + 1 * 1 = 1
       operand = 0
       sign = 1
    4. c = (
        stack = [0, 1, 1, 1]
        sign = 1, res = 0
    5. c = 4
       operand = 0 * 10 + 4 = 4
    6. c = +
       res = 0 + 1 * 4 = 4
    7. c = 5
       operand = 5, res = 4, sign = 1
    8. c = )
       res = res + sign * operand = 4 + 1 * 5 = 9
       res = res * stack.pop() --> sign = 9 * 1 = 9, stack = [0, 1, 1]
       res = res + stack.pop() --> operand = 9 + 1 = 10, stack = [0, 1]
       operand = 0
    9. c = -
       res = 10 + 1 * 0 = 10
       dign = -1, operand = 0
    10. c = 3
        operand = 3, sign = -1, res = 10
    11. c = )
        stack = [0, 1]
        res = 10 + -1 * 3 = 7
        res = res * stack.pop() = res * 1 = 7
        res = res + stack.pop() = res + 0 = 7

return 7

COmplexity: O(n) time and space.
"""

def calculate(s: str) -> int:

    stack = []
    operand = 0
    res = 0 # For the on-going result
    sign = 1 # 1 means positive, -1 means negative  

    for ch in s:
        if ch.isdigit():

            # Forming operand, since it could be more than one digit
            operand = (operand * 10) + int(ch)

        elif ch == '+':

            # Evaluate the expression to the left,
            # with result, sign, operand
            res += sign * operand

            # Save the recently encountered '+' sign
            sign = 1

            # Reset operand
            operand = 0

        elif ch == '-':

            res += sign * operand
            sign = -1
            operand = 0

        elif ch == '(':

            # Push the result and sign on to the stack, for later
            # We push the result first, then sign
            stack.append(res)
            stack.append(sign)

            # Reset operand and result, as if new evaluation begins for the new sub-expression
            sign = 1
            res = 0

        elif ch == ')':

            # Evaluate the expression to the left
            # with result, sign and operand
            res += sign * operand

            # ')' marks end of expression within a set of parenthesis
            # Its result is multiplied with sign on top of stack
            # as stack.pop() is the sign before the parenthesis
            res *= stack.pop() # stack pop 1, sign

            # Then add to the next operand on the top.
            # as stack.pop() is the result calculated before this parenthesis
            # (operand on stack) + (sign on stack * (result from parenthesis))
            res += stack.pop() # stack pop 2, operand

            # Reset the operand
            operand = 0

    return res + sign * operand