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
