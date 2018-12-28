# This solution is inefficient according to leetcode
# Probably due to isValid() which traverses through the entire count array

class Solution:
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        def isValid(count, k):
            numUnique = 0
            for i in range(len(count)):
                if count[i] > 0:
                    numUnique += 1
            return k >= numUnique

        if k == 0: return 0
        n = len(s)
        if n == 0: return 0
        if n == 1: return 1 if k > 0 else 0
        
        count = [0] * 128
        left = 0
        right = 0
        maxWindowSize = 0
        
        count[ord(s[0])-ord('a')] += 1
        for i in range(1,n):
            count[ord(s[i])-ord('a')] += 1
            right += 1
            while not isValid(count, k) and left < right:
                count[ord(s[left])-ord('a')] -= 1
                left += 1
            windowSize = right - left + 1
            maxWindowSize = max(maxWindowSize, windowSize) 
        
        return maxWindowSize
