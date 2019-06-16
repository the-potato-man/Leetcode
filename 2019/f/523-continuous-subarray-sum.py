'''
Given a list of non-negative numbers and a target integer k, 
write a function to check if the array has a continuous subarray of size at least 2 
that sums up to the multiple of k, that is, sums up to n*k where n is also an integer.
'''
class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        sums = [0 for _ in range(len(nums))]
        sums[0] = nums[0]
        
        for i in range(1, len(nums)):
            sums[i] = sums[i-1] + nums[i]
        
        for start in range(len(nums)):
            for end in range(start+1, len(nums)):
                temp = sums[end] - sums[start] + nums[start]
                if temp == k or (k != 0 and temp % k == 0):
                    return True
        
        return False
