"""
Given a string s which represents an expression, evaluate this expression and return its value. 


The Algorithm:

Put all the numbers with their correct sign into the stack.
Put '(' and the operator before that into the stack.
If we see the ')', pop from the stack until we get to '('. Update the num by the evaluated amount inside the parentheses and the operator before '('.

Input: s = "(1+(4+5/2)-3)"
Output: 4

op, num, stack = '+', 0, []
for c in s + '+':
    # since all empty spaces have a continue we can just ignore those.
    1. c = (
       stack = [+, (]
       op = +
    2. c = 1 --> digit
       num = 1
    3. c = +
       op = +
       stack.append(num) = stack = [+, (, 1]
       num = 0, op = +
    4. c = (
       stack = [+, (, 1, +, (]
    5. c = 4 --> digit
       num = 4, op = +
    6. c = +
       stack.append(num) = stack = [+, (, 1, +, (, 4]
       num = 0, op = +
    7. c = 5 --> digit
       num = 5, op = +
    8. c = /
       op = +, num = 5
       stack.append(num) = stack = [+, (, 1, +, (, 4, 5]
       num = 0, op = /
    9. c = 2 --> digit
       num = 2, op = /
    10. c = )
            op = /
            tmp = int (stack.pop() / num)= int(5 / 2) = 2
            stack = [+, (, 1, +, (, 4]
            while top of stack does not have an opening paranthesis (:
                tmp = tmp + stack.pop() 
                tmp = 2 + 4 = 6
            pop opening paranthesis from stack.
            stack = [+, (, 1, +]
            num =  tmp = 6 since stack.pop() == +
            stack = [+, (, 1]
            op = +
    11. c = -
        num = 6, op = +
        stack.append(num) = [+, (, 1, 6]
        num = 0, op = -
    12. c = 3 --> digit
        num = 3, op = -
    13. c = )
        op = -
        tmp = -3
        while top of stack does not have an opening paranthesis (:
            tmp = tmp + stack.pop()
            tmp = -3 + 6 + 1 = 4
            and then pop paranthesis
        stack = [+]
        num = tmp = 4 since stack.pop = +
        op = +
         ---> Goes to the else
         stack.append(num) since op == +
         stack = [4]
         num = 0, op = +
    return sum(stack) = 4


Example 2: 

Input = "3+2*2" ---> In this scenario to ensure that the final digit is validated we need the additional + and you will need to do the additional sum
Output: 7
op, num, stack = '+', 0, []
for c in s + '+':
    1. c = 3
       num = 3
    2. c = +
       stack.append(num), stack = [3]
       num = 0, op = +
    3. c = 2
        num = 2
    4. c = *
       num = 2, op = +
       stack.append(num) since op == +
       stack = [3, 2]
       num = 0, op = *
    5. c = 2
       num = 0, op = *
       num = 2
    6. c = +
       num = 2, op = *, stack = [3, 2]
       since op == *
            stack.append(stack.pop() * num) = stack = [3, 4]
        num = 0, op = +
    return sum(stack)
    return 7

Answer = 7

O(n) time and space complexity
"""


def calculate(s: str) -> int:
        
    op, num, stack='+', 0, []
    for c in s+'+': # This is just to start with the assertion that the expresison overall is positive expression
        if c==' ': continue
        if c.isdigit():
            num= num*10 + int(c)
        
        elif c=='(':
            # Push op and '(' to the stack
            stack.append(op)
            stack.append(c)
            op='+'
        
        elif c==')':
            # Given op, we put the current number to tmp
            if op=='*':
                tmp=stack.pop() * num
            elif op=='/':
                tmp=int(stack.pop() / num)
            else:
                tmp= num if op=='+' else -num
            
            # Add the elements in stack utill '('.
            while stack[-1]!='(':
                tmp+=stack.pop()    # ----> This works because if the sign was - somewhere inside paranthesis we alraedy negated the number and stored it in stack.
            stack.pop()   # pop '('
            
            # update the num having the op before '('.
            if stack[-1]=='*':
                stack.pop()
                num=stack.pop() * tmp 
            elif stack[-1]=='/':
                stack.pop()
                num=int(stack.pop() / tmp )
            else:
                num=tmp if stack.pop()=='+' else -tmp
            op='+'
        
        else:
            # Given op, update the current number.
            if op=='*':
                stack.append(stack.pop() * num)
            elif op=='/':
                stack.append(int(stack.pop() / num) )
            else:
                stack.append( num if op=='+' else -num )
            num, op = 0, c
    
    return sum(stack)