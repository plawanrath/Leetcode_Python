"""
Given an integer array nums and an integer k, return the kth largest element in the array.

nums = [3,2,1,5,6,4], k = 2
Output = 5


Algorithm:
Choose a random pivot.
Use a partition algorithm to place the pivot into its perfect position pos in the sorted array, 
move smaller elements to the left of pivot, and larger or equal ones - to the right.

Compare pos and N - k to choose the side of array to proceed recursively.

The quick select algorithm will return the kth smallest element. Which means that if we call the select 
function with len(array) - k as the value of its parameter k, then that
would give the kth largest element.

nums = [3,2,1,5,6,4], k = 2

    select(0, 5, (6 - 2))
    select(0, 5, 4) --> Get the 4th smallest element which will be the 2nd largest element. ------ inside select 1 -----
        1. Select a random pivot. Let's say pivot_index = 1
        2. pivot_index = partition(0, 5, 1)  -------- inside partition 1 ----------
            pivot = nums[1] = 2, left = 0, right = 5
            Move pivot to end
            [3,4,1,5,6,2]
            store_index = 0
            Move all elements smaller than pivot to left
                Since pivot is 2 only 1 is smaller than pivot. So it will move to current store_index position
            [1,4,3,5,6,2], store_index = 1
            Move pivot to its final position
            [1,2,3,5,6,4]
            return 1 -------- End partition 1 --------
        pivot_index = 1 (returned from partition)
        3. kth_smallest = 4 > pivot_index = 1 ? -> yes
            select(pivot_index+1, 5, 4)
            select(2, 5, 4) ---------------- inside select 2 ---------------
                pivot_index = 3 (random)
                pivot_index = partition(2, 5, 3) ---------- inside partition 2 -------------
                    pivot = nums[3] = 5, left = 2, right = 5
                    Move pivot to end
                    [1,2,3,4,6,5]
                    store_index = 2
                    Move all elements smaller than pivot to left
                        elements smaller than pivot are 1,2,3,4
                    [1,2,3,4,6,5], store_index = 4
                    Move pivot to its final position
                    [1,2,3,4,5,6]
                    return 4 ------------End partition 2 -------------
                pivot_index = 4
                if k_smallest == pivot_index ? -> Yes
                    return nums[4] = 5
    return 5

Time Complexity O(N) in average case and O(N^2) in the worst case
Worst case: Worst case occurs when we pick the largest/smallest element as pivot.
    But by using a random pivot the worst case can be avoided in most cases so the average case will fall closer to the best case scenario.
Best case: Best case occurs when we partition the list into two halves and continue with only the half we are interested in.

Space complexity: O(1)
"""
from typing import List
import random


def findKthLargest(nums: List[int], k: int) -> int:
    def partition(left, right, pivot_index):
        pivot = nums[pivot_index]
        # 1. move pivot to end
        nums[pivot_index], nums[right] = nums[right], nums[pivot_index]  

        # 2. move all smaller elements to the left
        store_index = left
        for i in range(left, right):
            if nums[i] < pivot:
                nums[store_index], nums[i] = nums[i], nums[store_index]
                store_index += 1

        # 3. move pivot to its final place
        nums[right], nums[store_index] = nums[store_index], nums[right]  

        return store_index

    def select(left, right, k_smallest):
        """
        Returns the k-th smallest element of list within left..right
        """
        if left == right:       # If the list contains only one element,
            return nums[left]   # return that element

        # select a random pivot_index between 
        pivot_index = random.randint(left, right)     

        # find the pivot position in a sorted list   
        pivot_index = partition(left, right, pivot_index)

        # the pivot is in its final sorted position
        if k_smallest == pivot_index:
             return nums[k_smallest]
        # go left
        elif k_smallest < pivot_index:
            return select(left, pivot_index - 1, k_smallest)
        # go right
        else:
            return select(pivot_index + 1, right, k_smallest)

    # kth largest is (n - k)th smallest 
    return select(0, len(nums) - 1, len(nums) - k)