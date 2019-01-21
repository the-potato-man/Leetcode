class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        stack = []
        dic = {}
        
        for i in range(len(nums)):
            while stack and nums[i] > stack[-1]:
                dic[stack.pop()] = nums[i]
            stack.append(nums[i])
        
        while stack:
            dic[stack.pop()] = -1
        
        res = [0] * len(findNums)
        for i in range(len(findNums)):
            res[i] = dic[findNums[i]]
        return res
