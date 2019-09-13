'''
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

Example:

Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"
'''

class Solution:
    def minWindow(self, s: str, t: str) -> str:        
        def incrementDict(c, dic):
            if c in dic:
                dic[c] += 1
            else:
                dic[c] = 1
        
        if not t or not s:
            return ""
        
        dicT = {}
        for c in t:
            incrementDict(c, dicT)
        
        # Number of unique characters in t, which need to be present in the desired window
        requiredNum = len(dicT) 
        # How many unique characters in t are present in the current window
        windowMatch = 0
        
        window = {}
        res = float("inf"), None, None
        
        l, r = 0, 0
        
        while r < len(s):
            c = s[r]
            incrementDict(c, window)
            
            # If the frequency of the character added equals the desirted count in t, increment windowMatch
            if c in dicT and window[c] == dicT[c]:
                windowMatch += 1
            
            while l <= r and windowMatch == requiredNum:
                c = s[l]
                # Save the smallest window until now
                if r - l + 1 < res[0]:
                    res = (r - l + 1, l, r)
                    
                window[c] -= 1
                    
                if c in dicT and window[c] < dicT[c]:
                    windowMatch -= 1
                    
                l += 1                
                
            r += 1
        
        return "" if res[0] == float("inf") else s[res[1]: res[2] + 1]
