"""
Given a file and assume that you can only read the file using a given method read4, 
implement a method read to read n characters. Your method read may be called multiple times.

Method read4:

The API read4 reads four consecutive characters from file, then writes those characters 
into the buffer array buf4.

The return value is the number of actual characters read.

Note that read4() has its own file pointer, much like FILE *fp in C.

Definition of read4:

    Parameter:  char[] buf4
    Returns:    int

buf4[] is a destination, not a source. The results from read4 will be copied to buf4[].

Idea: We can use a queue as a global buffer for reads. If the queue has capacity based on
buffer suze we can read from queue. Otherwise read file to buffer

Time and Space: O(N)
"""
from typing import List

class Read:
    def __init__(self):
        self.queue = [] # global "buffer"

    def read(self, buf, n):
        idx = 0

        # if queue is large enough, read from queue
        while self.queue and n > 0:
            buf[idx] = self.queue.pop(0)
            idx += 1
            n -= 1
        
        while n > 0:
            # read file to buf4
            buf4 = [""]*4
            l = self.read4(buf4)

            # if no more char in file, return
            if not l:
                return idx

            # if buf can not contain buf4, save to queue
            if l > n:
                self.queue += buf4[n:l]

            # write buf4 into buf directly
            for i in range(min(l, n)):
                buf[idx] = buf4[i]
                idx += 1
                n -= 1
        return idx

    def read4(self, buf4: List[str]) -> int:
        pass
