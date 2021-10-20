"""
Given two integers dividend and divisor, divide two integers without using multiplication, 
division, and mod operator.

Return the quotient after dividing dividend by divisor.

The integer division should truncate toward zero, which means losing its fractional part. 
For example, truncate(8.345) = 8 and truncate(-2.7335) = -2.

Idea:
1. We know that at max 31 shifts can be done in ab integer value
2. We can keep doing a left shift and keep subtracting left shifted divisor from the dividend
until we complete the division.

Time Complexity: O(log n)
"""

def divide(dividend: int, divisor: int) -> int:
    # -2147483648 through 2147483647
    MIN_VAL = -2147483648
    MAX_VAL = 2147483647
    
    # If divisor is 1 or -1
    if abs(divisor) == 1:
        if dividend == MIN_VAL and divisor == -1:
            return MAX_VAL
        else:
            return dividend if divisor > 0 else -dividend
        
    # Get if the answer will be negative or positive
    sign = -1 if (dividend < 0 and divisor > 0) or (divisor < 0 and dividend > 0) else 1
    res = 0 # result
    shift = 31 # At max 31 left shift can be done on a integer value 
    dividend = abs(dividend) # always take absolute value
    divisor = abs(divisor) # always take absolute value
    
    # While dividend is greater than divisor
    while dividend >= divisor:
        
        # Check how many shifts require of divisor
        # to reach dividend in whole
        while dividend < (divisor << shift):
            shift -= 1
        
        # subtract the left shifted divisor from dividend
        # and do the same process for the remaining value
        dividend = dividend - (divisor<<shift)
        
        # Answer will be how many total left shifted value of 1
        res = res + (1<<shift)

    # return result within range and with proper sign
    res = min(MAX_VAL, max(MIN_VAL, res))
    
    # return
    return  res if sign > 0 else -res