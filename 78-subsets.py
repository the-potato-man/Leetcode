class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        def helper(nums):  
            if len(nums) == 0: return [[]]
        
            result = []
            first = [nums[0]]
            sub = helper(nums[1:])
        
            for s in sub:
                result.append(s)
                result.append(s + first)
            return result
        
        sol = helper(nums)
        for s in sol:
            s.sort()
        
        return sol
