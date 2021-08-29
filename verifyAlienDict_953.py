from typing import List


def isAlienSorted(words: List[str], order: str) -> bool:
    orderMap = {c: i for i, c in enumerate(order)}
    for i in range(len(words) - 1):
        for j in range(len(words[i])):
            if j >= len(words[i+1]):
                return False
            if words[i][j] != words[i+1][j]:
                if orderMap[words[i][j]] > orderMap[words[i+1][j]]:
                    return False
                break
    return True       


words = ["hello","leetcode"]
order = "hlabcdefgijkmnopqrstuvwxyz"

print(isAlienSorted(words=words, order=order))