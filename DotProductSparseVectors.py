"""
nums1 = [1,0,0,2,3], nums2 = [0,3,0,4,0]
res = 1*0 + 0*3 + 0*0 + 2*4 + 3*0 = 8

Sparce vector is a vector with mostly 0s

Since we know that its a sparse vectors, to make the dot product fast store only non-zero values and their indices in a dictionary. 
So an index that is not present corresp[onds to 0.
"""
from typing import List


class SparseVector:
    def __init__(self, nums: List[int]):
        self.nonzeros = {}
        for index, val in enumerate(nums):
            if val:
                self.nonzeros[index] = val

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        res = 0
        for index, val in self.nonzeros.items():
            if index in vec.nonzeros:
                res += val * vec.nonzeros[index]
        return res


"""
Dot Product of sparse vectors as 2 lists.

Store first list in a dictionary of nonzero elements.

nums1 = [1,0,0,2,3]
nums2 = [0,3,0,4,0]

nonzeros = {0:1, 3:2, 4:3}
res = 0
for index, val in nums2:
    val = 0 - no action
    val = 3
        index = 1, index is not in nonzero - no action
    val = 0  - no action
    val = 4
        index = 3, index is in nonzeros
            res = 0 + 4 * nonzero[3] = 0 + 4*2 = 8
    val = 0 - no action

return 8

********** This approach may not be accepted. 
"""
def dotProduct(sl1: List[int],sl2: List[int]):
    nonzeros = {}
    for index, val in enumerate(sl1):
        if val:
            nonzeros[index] = val
    res = 0
    for index, val in enumerate(sl2):
        if val and index in nonzeros:
            res += val * nonzeros[index]
    return res

nums1 = [1,0,0,2,3]
nums2 = [0,3,0,4,0]
print(dotProduct(nums1, nums2))


"""
Alternate approach: Use list of tuples instead of dictionary.

nums1 = [1,0,0,2,3]
nums2 = [0,3,0,4,0]
nonzeros1 = [(0,1), (3,2), (4,3)]
nonzeros2 = {(1,3), (3,4)}

res, i, j = 0
1. nz1[0][0] < nz2[0][0] = 0 < 1 ? Yes - res = 0, i = 1, j = 0
2. nz1[1][0] < nz2[0][0] ? 3 < 1 ? No
    nz1[1][0] > nz2[0][0] ? 3 > 1 ? Yes - res = 0, i = 1, j = 1
3. nz1[1][0] < nz2[1][0] = 3 < 3 ? No
    nz1[1][0] > nz2[1][0] = 3 > 3 ? No
        else: res = 0 + nz1[1][1] * nz2[1][1] = 0 + 2 * 4 = 8, i = 2, j = 2

j is now = len(nz2) - end loop

return 8
"""
def dotProductWithoutHash(sl1: List[int],sl2: List[int]):
    nonzeros1 = [(index, val) for index, val in enumerate(nums1) if val]
    nonzeros2 = [(index, val) for index, val in enumerate(nums2) if val]
    res, i, j = 0, 0, 0
    while i < len(nonzeros1) and j < len(nonzeros2):
        # this means that the first list is lagging behind second list
        if nonzeros1[i][0] < nonzeros2[j][0]:
            i += 1
        # this means that the second list is lagging behind first list
        elif nonzeros1[i][0] > nonzeros2[j][0]:
            j += 1
        else:
            res += nonzeros1[i][1] * nonzeros2[j][1]
            i += 1
            j += 1
    return res


print (dotProductWithoutHash(nums1, nums2))