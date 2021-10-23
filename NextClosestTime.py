"""
Given a time represented in the format "HH:MM", form the next closest time by reusing the current digits. 
There is no limit on how many times a digit can be reused.

You may assume the given input string is always valid. For example, "01:34", "12:09" are all valid. 
"1:34", "12:9" are all invalid.

Input: time = "19:34"
Output: "19:39"
Explanation: The next closest time choosing from digits 1, 9, 3, 4, is 19:39, which occurs 5 minutes later.
It is not 19:33, because this occurs 23 hours and 59 minutes later.
"""
def nextClosestTime(time: str) -> str:
    cur = 60 * int(time[:2]) + int(time[3:]) # max value can be 24 * 60 i.e. 1680
    allowed = {int(x) for x in time if x!= ':'}
    while True:
        cur = (cur + 1) % (24 * 60) # we will keep incrementing the time by one until we get the desired value
        flag = 0 # to know if all the digits are allowed of the current value if 1 then we will not consider 
        # that value and break if 0 then we will simple return that value.
        for block in divmod(cur, 60):
            for digit in divmod(block, 10):
                if digit not in allowed:
                    flag = 1
            if flag:
                break
        if not flag:
            return '{:02d}:{:02d}'.format(divmod(cur,60)[0],divmod(cur,60)[1]) 
        """ :02d is important. Consider the case : "01:32" . Your output would be "1:33" instead of "01:33". """
