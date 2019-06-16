'''
Given two strings s and t, determine if they are both one edit distance apart.

Note: 

There are 3 possiblities to satisify one edit distance apart:

Insert a character into s to get t
Delete a character from s to get t
Replace a character of s to get t
'''

class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        lenS = len(s)
        lenT = len(t)
        
        if lenT > lenS:
            return self.isOneEditDistance(t, s)
        
        if lenS - lenT > 1: return False
        
        for i in range(lenT):
            if s[i] != t[i]:
                if lenS == lenT:
                    return s[i+1:] == t[i+1:]
                else:
                    return s[i+1:] == t[i:]
        
        return lenS - 1 == lenT