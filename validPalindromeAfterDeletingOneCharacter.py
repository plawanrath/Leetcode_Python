"""
Given a string s, return true if the s can be palindrome after deleting at most one character from it.


"""

def validPalindrome(s: str) -> bool:
    l, r = 0, len(s) - 1
    while l < r:
        if s[l] == s[r]:
            l += 1
            r -= 1
        else:
            return s[l:r] == s[l:r][::-1] or s[l+1:r+1] == s[l+1:r+1][::-1]
    return True

s1 = "abca"
s2 = "abc"

print(validPalindrome(s1))
print(validPalindrome(s2))