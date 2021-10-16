"""
There are several cards arranged in a row, and each card has an associated number of points. 
The points are given in the integer array cardPoints.

In one step, you can take one card from the beginning or from the end of the row. 
You have to take exactly k cards.

Your score is the sum of the points of the cards you have taken.

Given the integer array cardPoints and the integer k, return the maximum score you can obtain.

Input: cardPoints = [1,2,3,4,5,6,1], k = 3
Output: 12
Explanation: After the first step, your score will always be 1. However, 
choosing the rightmost card first will maximize your total score. The optimal strategy 
is to take the three cards on the right, giving a final score of 1 + 6 + 5 = 12.

Algorithm - DP

1. Initialize two arrays of size k + 1, namely frontSetOfCards and rearSetOfCards to store 
the score (prefix sums) obtained by selecting the first i cards and the last i cards in the array.

2. We calculate the prefix sum (sum of 0 <= i <= k cards) for the first k cards 
frontSetOfCards[i + 1] = frontSetOfCards[i] + cardPoints[i] and the last k cards 
rearSetOfCards[i + 1] = cardPoints[n - i - 1] + rearSetOfCards[i].

3. Initialize maxScore to 0.

4. Iterate from i = 0 -> k. At each iteration, we determine the possible score 
by selecting i cards from the beginning of the array and k - i cards from the 
end (currentScore). If this score is greater than the maxScore then we update it.
"""
from typing import List


def maxScore(cardPoints: List[int], k: int) -> int:
    n = len(cardPoints)
    frontCards = [0] * (k+1)
    rearCards = [0] * (k+1)

    for i in range(k):
        frontCards[i+1] = cardPoints[i] + frontCards[i]
        rearCards[i+1] = cardPoints[n - i - 1] + rearCards[i]
    
    maxScore = 0
    for i in range(k+1):
        currScore = frontCards[i] + rearCards[k - i]
        maxScore = max(maxScore, currScore)
    
    return maxScore



"""
Approach 2: Sliding Window
"""
def maxScore2(cardPoints: List[int], k: int) -> int:
    
    if k == 0:
        return 0
    
    if k >= len(cardPoints):
        return sum(cardPoints)
    
    # Only considered those points which are in range, i.e. k cards
    # from begining and k cards from end
    cardPoints = cardPoints[:k] + cardPoints[-k:] # array changed here
    
    # Varibales to handle slinding window
    add_k = 0 # include ith element 
    sub_k = 0 # exclude (k+i)th element
    left_k = sum(cardPoints[:k]) # sum of Left most k element
    right_k = sum(cardPoints[-k:]) # sum of right most k element
    maxsum = max(left_k, right_k) # possible max value
    
    # sliding window, from rigth most window, i.e. consider rotation
    for i in range(k):
        add_k += cardPoints[i]
        sub_k += cardPoints[k+i]
        maxsum = max(right_k - sub_k + add_k, maxsum)
        
    return maxsum