'''
Design a logger system that receive stream of messages along with its timestamps, each message should be printed if and only if it is not printed in the last 10 seconds.

Given a message and a timestamp (in seconds granularity), return true if the message should be printed in the given timestamp, otherwise returns false.
'''

class Logger:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dic = {}
        
    def shouldPrintMessage(self, timestamp, message):
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        :type timestamp: int
        :type message: str
        :rtype: bool
        """
        if message in self.dic:
            if self.dic[message] + 10 > timestamp:
                return False
            else:
                # Can refactor, but leaving as is for studying purposes
                self.dic[message] = timestamp
                return True     
        else:
            self.dic[message] = timestamp
            return True
        


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)