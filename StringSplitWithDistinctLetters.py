"""
You are given a string s, a split is called good if you can split s into 2 non-empty strings p and q 
where its concatenation is equal to s and the number of distinct letters in p and q are the same.

Return the number of good splits you can make in s.

Input: s = "aacaba"
Output: 2
Explanation: There are 5 ways to split "aacaba" and 2 of them are good. 
("a", "acaba") Left string and right string contains 1 and 3 different letters respectively.
("aa", "caba") Left string and right string contains 1 and 3 different letters respectively.
("aac", "aba") Left string and right string contains 2 and 2 different letters respectively (good split).
("aaca", "ba") Left string and right string contains 2 and 2 different letters respectively (good split).
("aacab", "a") Left string and right string contains 3 and 1 different letters respectively.


# Idea: Keep 2 sets of unique characters in left and right partitions
# Run a pointer from left to right and update 2 sets along the way.
# Then increase answer if at some point the length of 2 sets are the same.

# There is one catch: It's easy to keep adding new chars to left set, but
# how to know when it's time to remove a char from the right set ? There might be
# cases where current character still appears further to the right side of right partition.

# Therefore, we can only remove character from right partition if it's the last occurrence
# (there is no same character further to the right). An easy way to know is to construct
# a hashmap by going from right to left and record the first apearance of each unique character.
"""

def numSplits(s: str) -> int:
    leftSet = set()
    rightSet = set(s)
    ans = 0
    i = 0
    firstAppear = {}

    for i in range(len(s)-1,-1,-1):
        if s[i] not in firstAppear:
            firstAppear[s[i]] = i

    while i<len(s):
        leftSet.add(s[i])
        if i >= firstAppear[s[i]]:
            rightSet.remove(s[i])
        if len(leftSet) == len(rightSet):
            ans += 1
        i += 1

    return ans