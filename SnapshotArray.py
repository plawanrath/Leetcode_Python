"""
Implement a SnapshotArray that supports the following interface:

SnapshotArray(int length) initializes an array-like data structure with the given length.  
Initially, each element equals 0.

void set(index, val) sets the element at the given index to be equal to val.

int snap() takes a snapshot of the array and returns the snap_id: the total 
number of times we called snap() minus 1.

int get(index, snap_id) returns the value at the given index, at the time we 
took the snapshot with the given snap_id
"""

class SnapshotArray:

    def __init__(self, length: int):
        self.snap_id = 0
        self.index_snap_list = [None] * length

    def set(self, index: int, val: int) -> None:
        if not self.index_snap_list[index]:
            self.index_snap_list[index] = {}
        self.index_snap_list[index][self.snap_id] = val
        print(self.index_snap_list)

    def snap(self) -> int:
        curr_snap_id = self.snap_id
        self.snap_id += 1
        return curr_snap_id

    def get(self, index: int, snap_id: int) -> int:
        if self.index_snap_list[index]:
            if snap_id in self.index_snap_list[index]:
                return self.index_snap_list[index][snap_id]
        return -1


"""
Leetcode: Approach - Uses extra space and inefficient for large arrays I think
"""

class SnapshotArray2:

    def __init__(self, length: int):
        self.nums = dict()
        self.snap_id = -1
        self.snaps = []

    def set(self, index: int, val: int) -> None:
        self.nums[index] = val

    def snap(self) -> int:
        self.snap_id += 1
        self.snaps.append(self.nums.copy())
        return self.snap_id

    def get(self, index: int, snap_id: int) -> int:
        if index in self.snaps[snap_id]:
            return self.snaps[snap_id][index]
        return 0