class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        
        memo = [0] * (len(nums) + 1)
        memo[1] = nums[0]
        
        for i in range(1, len(nums)):
            memo[i+1] = max(memo[i], memo[i-1] + nums[i]) # nums is 1 pos behind memo
        
        return memo[-1]

    def rob2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prevMax = 0
        currMax = 0
        
        for i in nums:
            temp = currMax
            currMax = max(prevMax + i, currMax)
            prevMax = temp
        
        return currMax
