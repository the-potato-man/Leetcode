'''
s = "aa"
p = "a"
Output: false
---
s = "aa"
p = "a*"
Output: true
---
s = "ab"
p = ".*"
Output: true
---
Input:
s = "aab"
p = "c*a*b"
Output: true
---
Input:
s = "mississippi"
p = "mis*is*p*."
Output: false
'''
class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if not s and not p:
            return True
        elif s and not p:
            return False
        elif not s and p:
            if len(p) >= 2 and p[1] == '*':
                return self.isMatch(s, p[2:])
            else:
                return False
        else: # s and p    
            if len(p) >= 2 and p[1] == '*':
                if p[0] != '.' and s[0] != p[0]:
                    return self.isMatch(s, p[2:])
                else:
                    return self.isMatch(s[1:], p) or self.isMatch(s, p[2:])
            elif p[0] != '.' and s[0] != p[0]:
                return False 
            else:
                return self.isMatch(s[1:], p[1:])
        

        