
'''
You are given two arrays (without duplicates) nums1 and nums2 where nums1’s elements are subset of nums2. 
Find all the next greater numbers for nums1's elements in the corresponding places of nums2.

The Next Greater Number of a number x in nums1 is the first greater number to its right in nums2. If it does not exist, output -1 for this number.
'''

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
