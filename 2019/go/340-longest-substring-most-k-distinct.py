
'''
Given a string, find the length of the longest substring T that contains at most k distinct characters.

Example 1:

Input: s = "eceba", k = 2
Output: 3
Explanation: T is "ece" which its length is 3.
'''
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        
        if k == 0: return  0
        n = len(s)
        if n == 0: return 0
        if n == 1: return 1 if k > 0 else 0
        
        window = {}
        l, r = 0, 0
        maxWindowSize = 0
        
        while r < len(s):
            if s[r] in window:
                window[s[r]] += 1
            else:
                window[s[r]] = 1
            
            while l < r and k < len(window):
                if window[s[l]] == 1:
                    del window[s[l]]
                else:
                	window[s[l]] -= 1
                l += 1
        
            windowSize = r - l + 1
            maxWindowSize = max(maxWindowSize, windowSize) 
            
            r += 1
        
        return maxWindowSize
