'''
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

Example:

Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"
'''

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not t or not s:
            return ""
        
        dictT = {}
        for c in t:
            if c in dictT:
                dictT[c] += 1
            else:
                dictT[c] = 1
        
        # Number of unique characters in t, which need to be present in the desired window
        required = len(dictT)
        
        l = 0
        r = 0
        
        # How many unique characters in t are present in the current window
        formed = 0
        
        window = {}
        ans = float("inf"), None, None
        
        while r < len(s):
            c = s[r]
            if c in window:
                window[c] += 1
            else:
                window[c] = 1
            
            # If the frequency of the current character added equals to the desired count in t,
            # then increment the formed count by 1            
            if c in dictT and window[c] == dictT[c]:
                formed += 1
        
            while l <= r and formed == required:
                c = s[l]
                
                # # Save the smallest window until now
                if r - l + 1 < ans[0]:
                    ans = (r - l + 1, l, r)
                
                window[c] -= 1
                if c in dictT and window[c] < dictT[c]:
                    formed -= 1
                
                l += 1
            
            r += 1
            
        return "" if ans[0] == float("inf") else s[ans[1] : ans[2] + 1]
