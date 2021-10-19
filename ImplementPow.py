"""
Implement pow(x, n), which calculates x raised to the power n (i.e., x^n).

Input: x = 2.00000, n = 10
Output: 1024.00000

Brute Force: Multiply x N times.

Technique: 2^4 = 16 = (2^2)^2
For example 5^1024 = 5^half the power = (5^2)^1024

And if with our approach, then 5^1024 = (5^2)^512 we reduced the number of multiplications by 
2 times in one operation!
Let's continue with 5^1024 = (5^2)^512 = (25^2)^256 = (125^2)^128 = ... 10 
recursions will be performed and not 1024 times.
If the degree is odd, then we easily move to even in one iteration x^(2n+1) = x * ( x^(2n) )

Time Complexity: O(log n), Space: O(log n) - call stack 
"""

def myPow(x: float, n: int) -> float:
    if n == 1:
        return x
    if n == 0:
        return 1
    if n < 0:
        return myPow(1/x, -n)
    if n%2 == 0:
        return myPow(x*x, n//2)
    return myPow(x, n - 1) * x