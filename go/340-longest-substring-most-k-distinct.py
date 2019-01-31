
'''
Given a string, find the length of the longest substring T that contains at most k distinct characters.

Example 1:

Input: s = "eceba", k = 2
Output: 3
Explanation: T is "ece" which its length is 3.
'''
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if k == 0: return 0
        n = len(s)
        if n == 0: return 0
        if n == 1: return 1 if k > 0 else 0
        
        count = {}
        left = 0
        right = 0
        maxWindowSize = 0
        
        count[s[0]] = 1
        for i in range(1,n):
            if s[i] in count:
                count[s[i]] += 1
            else:
                count[s[i]] = 1
            right += 1
            while len(count) > k and left < right:
                if count[s[left]] == 1:
                    del count[s[left]]
                else:
                	count[s[left]] -= 1
                left += 1
            windowSize = right - left + 1
            maxWindowSize = max(maxWindowSize, windowSize) 
        
        return maxWindowSize
