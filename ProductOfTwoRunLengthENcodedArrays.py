"""
You are given two run-length encoded arrays encoded1 and encoded2 
representing full arrays nums1 and nums2 respectively. Both nums1 and nums2 
have the same length. Each encoded1[i] = [vali, freqi] describes the ith segment of nums1, 
and each encoded2[j] = [valj, freqj] describes the jth segment of nums2.

Return the product of encoded1 and encoded2.

Time: O(N)
"""
from typing import List


def findRLEArray(encoded1: List[List[int]], encoded2: List[List[int]]) -> List[List[int]]:
    index1 = 0
    index2 = 0
    
    result = []
    
    while index1 < len(encoded1) and index2 < len(encoded2):
        val1, freq1 = encoded1[index1]
        val2, freq2 = encoded2[index2]
        
        product = val1 * val2
        product_freq = min(freq1, freq2)
        
        if not result or result[-1][0] != product:
            result.append([product, product_freq])
        else:
            result[-1][1] += product_freq
        
        encoded1[index1][1] -= product_freq
        encoded2[index2][1] -= product_freq
        
        index1 += 1 if product_freq == freq1 else 0
        index2 += 1 if product_freq == freq2 else 0
    
    return result