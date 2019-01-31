'''
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. 
All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. 
Meanwhile, adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.
'''

class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        
        n = len(nums)
        if n <= 2: return max(nums)
        
        memoRobFirst = [0] * n
        memoSkipFirst = [0] * n
        
        memoRobFirst[0] = nums[0]
        memoRobFirst[1] = nums[0]
        memoSkipFirst[1] = nums[1]
        
        for i in range(2, n):
            memoRobFirst[i] = max(memoRobFirst[i-2] + nums[i] if i != n-1 else memoRobFirst[i-2], memoRobFirst[i-1])
            memoSkipFirst[i] = max(memoSkipFirst[i-2] + nums[i], memoSkipFirst[i-1])
        
        return max(memoRobFirst[-1], memoSkipFirst[-1])
