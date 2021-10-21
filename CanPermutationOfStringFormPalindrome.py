"""
Given a string s, return true if a permutation of the string could form a palindrome.

Input: s = "code"
Output: false

Input: s = "aab"
Output: true

Idea:
Generally palindromes will have even number of occurances of all characters and only 1 charaacter cah
have odd number of occurance.

Logic:
when we find a character in the string ss that isn't present in the set(indicating an 
odd number of occurrences currently for this character), we put its corresponding entry in the set. 
If we find a character that is already present in the set(indicating an even number of 
occurrences currently for this character), we remove its corresponding entry from the set.

At the end, the size of set indicates the number of elements with odd number of occurrences in ss. 
If it is lesser than 2, a palindromic permutation of the string ss is possible, otherwise not.

Time Complexity: O(N)
Space: O(1) because the Set we form is bound by the number of possible character which is a constant.
"""
def canPermutePalindrome(s: str) -> bool:
    charOcc = set()
    for char in s:
        if char in charOcc:
            charOcc.remove(char)
        else:
            charOcc.add(char)
    return len(charOcc) <= 1
