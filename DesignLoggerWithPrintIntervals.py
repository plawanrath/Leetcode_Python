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
We can use a dictionary of <message, timestamp> to keep track of messages. 

When doing shouldPrintMessage there are 2 possible cases:
1. The message is new, and we need to add the message to the dict and print
2. The message has passed its 10 second threshold and so its eligible to print in which case we can update the timestamp and print

In any other case, the message cannot be printed. 
"""

from collections import OrderedDict


class Logger:
    def __init__(self) -> None:
        self.logger = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        """

        if message not in self.logger:
            self.logger[message] = timestamp
            return True
        
        if timestamp - self.logger[message] >= 10:
            self.logger[message] = timestamp
            return True
        else:
            return False