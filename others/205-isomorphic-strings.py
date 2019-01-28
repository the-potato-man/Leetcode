
'''
Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

Example 1:

Input: s = "egg", t = "add"
Output: true
'''

class Solution:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        sDict = {}
        for i in range(len(s)):
            if s[i] not in sDict:
                sDict[s[i]] = t[i]
            else:
                if sDict[s[i]] != t[i]:
                    return False
                
        tDict = {}
        for i in range(len(t)):
            if t[i] not in tDict:
                tDict[t[i]] = s[i]
            else:
                if tDict[t[i]] != s[i]:
                    return False
                
        return True
