class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sol = float('-inf')     
        tempMax = float('-inf')  
        
        for i in range(0, len(nums)):
            tempMax = max(tempMax + nums[i], nums[i])
            sol = max(sol, tempMax) 
                
        return sol
