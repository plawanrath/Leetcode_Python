"""
Given a string s, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Approach: Use 2 points one from each end and compare to see if characters are same until we reach the middle
"""

def isPalindrome(s: str) -> bool:
    i, j = 0, len(s) - 1

    while i < j:
        while i < j and not s[i].isalnum():
            i += 1
        while i < j and not s[j].isalnum():
            j -= 1
        
        if s[i].lower() != s[j].lower():
            return False
        
        i += 1
        j -= 1
    
    return True