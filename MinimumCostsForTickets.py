"""
You have planned some train traveling one year in advance. The days of the year 
in which you will travel are given as an integer array days. Each day is an integer from 1 to 365.

Train tickets are sold in three different ways:

a 1-day pass is sold for costs[0] dollars,
a 7-day pass is sold for costs[1] dollars, and
a 30-day pass is sold for costs[2] dollars.
The passes allow that many days of consecutive travel.

For example, if we get a 7-day pass on day 2, then we can travel for 7 days: 2, 3, 4, 5, 6, 7, and 8.
Return the minimum number of dollars you need to travel every day in the given list of days.

Input: days = [1,4,6,7,8,20], costs = [2,7,15]
Output: 11
Explanation: For example, here is one way to buy passes that lets you travel your travel plan:
On day 1, you bought a 1-day pass for costs[0] = $2, which covered day 1.
On day 3, you bought a 7-day pass for costs[1] = $7, which covered days 3, 4, ..., 9.
On day 20, you bought a 1-day pass for costs[0] = $2, which covered day 20.
In total, you spent $11 and covered all the days of your travel.


Idea: 
For each day, if I don't have to travel today then I can basically wait to buy the pass.
When I buy the pass I have 3 choices and I need to choose whichever option gives me the minimum 
cost. We can represent this as a DP.

Algorithm:
1. I will uiterate over days and maintain 2 pointers: 1 for 7 day window and 2nd for 30 day window
2. Call it seven and thirty

Then for each day:
    - Move the seven pointer forward until days[i] > days[seven] + 6
    - Move the thirty pointer forward until days[i] > days[thirty] + 30

3. Finally,
dp[i+1] = min(dp[i] + costs[0], dp[seven] + costs[1], dp[thirty] + costs[2])

Example:
days = [1,4,6,7,8,20], costs = [2,7,15]

dp = [0, 0, 0, 0, 0, 0, 0]
seven = 0, thirty = 0
for i in range(6):
    1. i = 0
    while days[0] > days[seven] + 6:
        days[0] > days[0] + 6 ? -- No
    while days[0] > days[thirty] + 29:
        days[0] > days[0] + 29 ? -- No
    dp[1] = min(2, 7, 15) = 2 i.e. dp = [0,2,0,0,0,0,0]
    2. i = 1
    while days[1] > days[seven] + 6:
        days[1] > days[0] + 6 -- No
    while days[1] > days[thirty] + 6: -- No
    dp[2] = min(2 + 2, 2 + 7, 2 + 15) = 4 i.e. = [0,2,4,0,0,0,0]
    3. i = 2
    while dp[2] > dp[seven] + 6:
        dp[2] > dp[0] + 6 -- No
    while days[2] > days[thirty] + 6: -- No
    dp[3] = min(4 + 2, 4 + 7, 4 + 15) = 6 i.e. = [0,2,4,6,0,0,0]
    4. i = 3
    while days[3] > days[seven] + 6:
        days[3] > days[0] + 6 = 7 > 1 + 6 -- No
    while days[3] > days[thirty] + 6: -- No
    dp[4] = min(6 + 2, 6 + 7, 6 + 15) = 8 i.e. dp = [0,2,4,6,8,0,0]
    5. i = 4
    while days[4] > days[seven] + 6:
        days[4] > days[0] + 6 = 8 > 1 + 6 --- Yes
            seven = 1
    while days[4] > days[thirty] + 6: -- No
    dp[5] = min(8 + 2, dp[seven] + 7, dp[thirty] + 15) = min(8 + 2, dp[1] + 7, dp[0] + 15)
    dp[5] = min(10, 2 + 7, 15) = 9 i.e. dp = [0,2,4,6,8,9,0]
    6. i = 5
    while days[5] > days[seven] + 6:
        days[5] > days[1] + 6 = 20 > 4 + 6 = 10 --- yes
            seven = 2
            days[5] > days[2] + 6 = 20 > 6 + 6 = 12 -- yes
            seven = 3
            days[5] > days[3] + 6 = 20 > 7 + 6 = 13 -- yes
            seven = 4
            days[5] > days[4] + 6 = 20 > 8 + 6 = 14 -- Yes
            seven = 5
            days[5] > days[5] + 6 = 20 > 20 + 6 --- No
    seven = 5
    while days[5] > days[thirty] + 6: -- No
    daps[6] = min(9 + 2, dp[5] + 7, dp[0] + 15) = min(11, 9 + 7, 15) = 11
    dp = [0,2,4,6,8,9,11]

    Return dp[-1] = 11

Time and Space: O(N)
"""
from typing import List


def mincostTickets(days: List[int], costs: List[int]) -> int:
    seven = 0
    thirty = 0
    dp = [0] * (len(days) + 1)

    for i in range(len(days)):
        while days[i] > days[seven] + 6:
            seven += 1
        while days[i] > days[thirty] + 29:
            thirty += 1
        dp[i+1] = min(dp[i] + costs[0], dp[seven] + costs[1], dp[thirty] + costs[2])
    
    return dp[-1]
