class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
    	if len(nums) == 0: return [[]]
    
    	sol = []
    	first = [nums[0]]
    	perms = self.permute(nums[1:])
    
    	for p in perms:
    		for i in range(len(p)+1):
    			sol.append(p[:i] + first + p[i:])
    	return sol
