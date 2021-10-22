"""
There are n bulbs that are initially off. You first turn on all the bulbs, then you turn off every second bulb.

On the third round, you toggle every third bulb (turning on if it's off or turning off if it's on). 
For the ith round, you toggle every i bulb. For the nth round, you only toggle the last bulb.

Return the number of bulbs that are on after n rounds.

Input: n = 3
Output: 1
Explanation: At first, the three bulbs are [off, off, off].
After the first round, the three bulbs are [on, on, on].
After the second round, the three bulbs are [on, off, on].
After the third round, the three bulbs are [on, off, off]. 
So you should return 1 because there is only one bulb is on.


Idea:
How many "on" at the end of nth toggle?

--> "on" or "off" at each position in an array of length n?

--> toggle even number times will result in "on", toggle odd number times will result in "off"

--> for position k, the number of toggles is the number of distinct divisors that k has

--> divisors always come in pair, which means even number of divisors, for example, 12 has (1,12),(2,6),(3,4).

--> however, Square Number has odd number of divisors, e.g. 25 has 1,25,5

--> thus, the number of "on", is the number of perfect square number <= n

So this is simply the sqrt of n
"""

def bulbSwitch(n: int) -> int:
    return int(n**0.5)