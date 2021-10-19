"""
Given a string num that contains only digits and an integer target, 
return all possibilities to insert the binary operators '+', '-', and/or '*' 
between the digits of num so that the resultant expression evaluates to the target value.

Input: num = "123", target = 6
Output: ["1*2*3","1+2+3"]
Explanation: Both "1*2*3" and "1+2+3" evaluate to 6.

Approach:

Recursive solution. On each iteration for the current 'num' (which is the remaining string) we do:

1. choose all possible "first operands" by looping through all possible substrings for the current 'num' string
    - disqualify operands beginning with '0' as it's an invalid number
2. choose all possible operations ('+', '-', '*')
3. With respect to chosen operand and operation, calculate the remaining string and remaining target
4. In case of * operation though we also need to factor in its priority since * should happen before any
    + or -. We will use anoteher argument in the recursion which will pass in multiplier. We can use that same
    argument to denote the sign for when we are evaluating addition or subtraction.
5. For all each of those choices, run the next recursive iteration for the remainder 
of the string and calculated remaning target

Time Complexity: O(N * 3^N) --> O(3^N) because there are 3 choices for every recursion and we are looping
through entire N for that.
Space: O(N) for the call stack during recursion

Example:
num = "123", target = 6

addOperators(123, 6, 1)
    result = []
    for i in range(3):
        1. i = 0
        operand = 1
        no 0s to skip
        multiplied_val = 1 * 1 = 1
        i == 2 ? ----> No so go to else
        for res in addOperators(23, 6 - 1, 1) = addOperator(23, 5, 1) ----------- Inside addOperator(23, 5, 1)----
            result = []
            for i in range(2):
                1. i = 0
                operand = 2
                operand is not 0
                multiplied_val = 1 * 2 = 2
                i == 1 --> No go to else
                for res in addOperator(3. 5 - 2, 1) = addOperator(3, 3, 1) --------Inside addOperator(3, 3, 1)----
                    result = []
                    for i in range(1):
                        i = 0
                        operand = 3
                        multiplier_val = 1 * 3 = 3
                        i == 0 ? ---> Yes
                            multiplier_val = 3 == target = 3 ---> Yes
                                result = [3]
                    Return [3]
                    -------End addOperator(3, 3, 1)----
                for res in [3]:
                    result = ["2+3"]
                for res in addOperators(3, 5 - 2, -1) = addOperator(3, 3, -1) --------Inside addOperator(3, 3, -1)----
                    result = []
                    for i in range(1):
                        i = 0
                        operand = 3
                        multiplier_val = -1 * 3 = -3
                        i == 0 ? ---> Yes
                           multiplier_val = -3 == target = 3 ---> No
                            ... 
                            the recursion will end with empty []
                           -------End addOperator(3, 3, -1)---- 
                for res in addOperators(3, 5, multiplier = 2)--------Inside addOperator(3, 5, 2)----
                    result = []
                    for i in range(1):
                        i = 0
                        operand = 3
                        multiplier_val = 2 * 3 = 6
                        i == 0 --> Yes
                        multiplier_val = 6 == target = 5 ---> No
                        ....
                        the recursion will end with empty []
                        -------End addOperator(3, 5, 2)----
            ----------- Inside addOperator(23, 5, 1) res = ["2+3"]----
            for res in ["2+3"]: ---> this is inside outermost addOperators(123, 6, 1)
                result.append(1+2+3)
                res = ["1+2+3"]
            for res in addOperators(23, 6 - 1, -1)
            ...
            for res in addOperators(23, 6, 1)
            ...
"""
from typing import List


def addOperators(num: str, target: int, multiplier: int = 1) -> List[str]:

    result = []
    for i in range(len(num)):
        operand = num[:i+1]

        # skip invalid number beginnging with '0'
        if operand[0] == '0' and len(operand) > 1:
            continue

        # perform multiplication to respect higher precedence
        multiplied_val = multiplier * int(operand)
        if i == len(num) - 1:
            if multiplied_val == target:
                result.append(operand)
        else:
            for res in addOperators(num[i+1:], target - multiplied_val, 1):
                result.append(f"{operand}+{res}") 
            
            for res in addOperators(num[i+1:], target - multiplied_val, -1):
                result.append(f"{operand}-{res}")
            
            for res in addOperators(num[i+1:], target, multiplied_val):
                result.append(f"{operand}*{res}")
        
    return result

