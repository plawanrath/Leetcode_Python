"""
You are given an array of unique strings wordlist where wordlist[i] is 6 letters long, and one word in this list is chosen as secret.

You may call Master.guess(word) to guess a word. The guessed word should have type string and must be from the original list with 6 lowercase letters.

This function returns an integer type, representing the number of exact matches (value and position) of your guess to the secret word. Also, if your guess is not in the given wordlist, it will return -1 instead.

For each test case, you have exactly 10 guesses to guess the word. At the end of any number of calls, if you have made 10 or fewer calls to Master.guess and at least one of these guesses was secret, then you pass the test case.


Approach:
We can summarize the optimal process as so:

We know if we guess a word from the word list, one of three things will occur:
1. score = 6 -> We found the secret and can stop :)
2. score = 0 -> We can remove any words with overlapping chars. Since they share common chars, and we know all of the chars in the current word are wrong, then no words with any overlap will be the secret.
3. score = 1,2,3,4,5 = k -> We know that k chars are correct in our current word. Thus, if another word does not share exactly k overlapping characters with our word, it also is not the secret and we can remove it.

The problem here is with the above approach alone, we can't guarantee we remove "bad" words at a fast enough rate to guarantee we can get the correct secret within the first 10 guesses.
That is because some words might not overlap with any other words at all.

So while we could probably guarantee some approach to say 26 attempts (26 english characters), for this problem, we just need to optimize it to get to 10 or less for the given test cases.
Thus, the missing piece we can infer from above is that we minimize our problem space more quickly when we test words that overlap with others. The reason being, if the overlap between two 
words is non-zero (and assuming the words are distinct it is also not 6), then the more overlaps the more chances we get to cut out words that don't fit our invariant.
"""
from typing import List


class Master:
    def guess(self, word: str) -> int:
        pass

# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:

class Solution:
    def findSecretWord(self, wordlist: List[str], master: 'Master') -> None:
        wordsLeft = set(wordlist)

        def getOverlaps(word1, word2):
            return sum([1 if word1[i] == word2[i] else 0 for i in range(6)]) # this is becuase we are looking for 6 letter words.
        
        def mostOverlap():
            seen = {}
            for word in wordsLeft:
                for index, char in enumerate(word):
                    if char not in seen:
                        seen[char] = [0] * 6 # initialize the char list to track the position
                    seen[char][index] += 1
            
            # Let's get the max overlap possible
            bestWord, maxOverlap = "", -1
            for word in wordsLeft:
                score = sum([seen[char][index] for index, char in enumerate(word)])
                if score > maxOverlap:
                    maxOverlap = score
                    bestWord = word
            
            return bestWord
        
        for i in range(10): # max 10 tries
            if len(wordsLeft) == 0:
                return
            word = mostOverlap()
            wordsLeft.remove(word)
            matches = master.guess(word)
            if matches == 6:
                break
            for other_word in wordsLeft.copy(): # making a copy becuase i will be manipulating wordLeft set
                overlap = getOverlaps(word, other_word)
                if matches == 0 and overlap != 0: # This means that the current word we guessed did not have any matches so any other word that has any overlap with that word can be safely ignored.
                    wordsLeft.remove(other_word)
                if matches != 0 and overlap != matches: # This means that if there were some matches and some overlaps but overlaps didn't match the letters and positions of matches then those can also be removed.
                    wordsLeft.remove(other_word)
        return