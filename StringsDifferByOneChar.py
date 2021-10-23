"""
Given a list of strings dict where all the strings are of the same length.

Return true if there are 2 strings that only differ by 1 character in the same index, otherwise return false.

Input: dict = ["abcd","acbd", "aacd"]
Output: true
Explanation: Strings "abcd" and "aacd" differ only by one character in the index 1.
"""
from typing import List


def differByOne(dict: List[str]) -> bool:
    # only need one pass to solve the problem using hashset:
    seens = set()
    for word in dict:
        for i, c in enumerate(word):
            # change 'abcd' into the form of '.bcd', 'a.cd' ...
            masked_word = word[:i] + '.' + word[i+1:]
            if masked_word in seens:
                return True
            else:
                seens.add(masked_word)
    return False