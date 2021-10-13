"""
Given an integer array nums and an integer k, return the k most frequent elements. 
You may return the answer in any order.

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Approach 1: 
Generate a frequency of each element and use a priority queue to store 
elements by descending order of frequency then you can return k elements from the PriorityQueue. 

Time Complexity: O(n log n), space complexity: O(n)
"""
from collections import Counter
from queue import PriorityQueue
def topKFrequent(nums, k):
    freqMap = Counter(nums)
    q = PriorityQueue()
    for num, freq in freqMap.items():
        q.put((-freq, num))
    if len(freqMap) == k:
        return list(freqMap.keys())
    return [q.get()[1] for _ in range(k)]


"""
Approach 2:
1 use counter to count frequency of each element O(n)
2. use partition/quick-select to find k-most biggest frequency O(n)
    Use a partition scheme of choosing a pivot and putting it in its appropriate index
    In the sorted array, move less frequent elements to the left of pivot, 
    and more frequent or of the same frequency - to the right.
3. find the minimum frequency in the k-most biggest frequency list O(n)
4. Use that threshold to find keys in the dictionary. O(n)

Time complexity can be O(n^2) in the worst case when we always keep choosing worse pivots.
Otherwise it will be O(n) 

Example: 
nums = [1,1,1,2,2,3], k = 2

freqMap = {1: 3, 2: 2, 3: 1}
count = [3,2,1]
output = []

k = 2
while not k:
    1. i = partition([3,2,1], 2)
            pivot = 1
            i = 0
            for index, val in count:
                1. index = 0, val = 3:
                    3 >= 1 ? --> Yes
                        swap index and i (since both are 0 nothing to swap)
                        [3, 2, 1]
                        i = 1
                2. index = 1, val = 2:
                    2 >= 1 ? --> Yes
                        swap index and i (both are again same)
                        [3, 2, 1]
                        i = 2
                3. index = 2, val = 3:
                    1 >= 1 ? --> Yes
                        swap index and i (both are same)
                        [3, 2, 1]
                        i = 3
                return 3
        
        i = 3
        Will go to the else case:
            count = count[:2] # take only 2 counts
        count = [3, 2]
    2. i = partition([3, 2], 2)
            pivot = count[-1] = 2
            i = 0
            for index, val in count:
                1. index, val = 0, 3
                    3 >= 2 --> Yes
                        swap (same values for index and i so no-op)
                        [3, 2]
                        i = 1
                2. index, val = 1, 2
                    2 >= 2 ? --> Yes
                        swap (same values for index and i so no-op)
                        [3, 2]
                        i = 2
            return 2

            i = 2
            i == k --> Yes
                kBiggestFreqList = count[:2] = [3, 2]

threshold = min([3, 2]) = 2 --> This means that we need all elements that have 2 oor more occurances and that is our answer

freqMap = {1: 3, 2: 2, 3: 1}
In freqMap 1 and 2 have counts of 3 and 2 respectively so the output will be [1, 2]
"""

def topKFrequent_QuickSelect(nums, k):
    freqMap = Counter(nums)
    n = len(list(freqMap.keys()))
    if n == k:
        return list(freqMap.keys())
    count = list(freqMap.values())
    output = []
    kBiggestFreqList = []
    while k != 0:
        i = partition(count, k)
        if i == k:
            kBiggestFreqList = count[:i]
            k = 0
        elif i < k:
            kBiggestFreqList += count[:i]
            count = count[i:]
            k = k - i
        else:
            count = count[:i-1]
    threshold = min(kBiggestFreqList)
    for key in freqMap:
        if freqMap[key] >= threshold:
            output.append(key)
    return output

def partition(count, k):
    pivot = count[-1]
    i = 0
    for index, val in enumerate(count):
        if val >= pivot:
            count[index], count[i] = count[i], count[index]
            i+=1
    return i