"""
Design a logger system that receives a stream of messages along with their timestamps. Each unique message should only be printed at most every 10 seconds 
(i.e. a message printed at timestamp t will prevent other identical messages from being printed until timestamp t + 10).

All messages will come in chronological order. Several messages may arrive at the same timestamp.

Implement the Logger class:

Logger() Initializes the logger object.
bool shouldPrintMessage(int timestamp, string message) Returns true if the message should be printed in the given timestamp, otherwise returns false.

Approach 1:
We could use a combination of a queue and a set. We can use queue as sort of a sliding window to keep all printable messages.
The message queue will store message and timestamp and timestamp can be used to see if the message should be printed. 

Approach 2: (Optimal)
We can use an OrderedDict in python. OrderedDict will store the values sorted by key which means that we can safely store messages by arrival.
Since messages only live for 10 seconds we could also evict messages that were printed more than 10 seconds ago. This would save space. 

Eviction:
Starting from the left-most element of the dictionary, we remove that element, if its time was before timestamp-10, 
then we can just throw it out and remove the next message from the dictionary. But if it was not, it means that we are done cleaning the obsolete 
messages and we return the removed message to its original place as the left-most message in the OrderedDict.
"""

from collections import OrderedDict


class Logger:
    def __init__(self) -> None:
        self.logger = OrderedDict()

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        """

        # clean obselete messages
        while self.logger:
            m, t = self.logger.popitem(last=False) # This means pop happens in FIFO order
            if t > timestamp - 10:
                self.logger[m] = t
                self.logger.move_to_end(m, last=False) # move the element to the beginning
                break

        if message in self.logger:
            if self.logger[message] <= timestamp - 10:
                self.logger[message] = timestamp
                self.logger.move_to_end(message)
                return True
            else:
                return False
        
        self.logger[message] = timestamp
        return True
