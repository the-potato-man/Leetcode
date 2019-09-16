# https://fizzbuzzed.com/top-interview-questions-1/

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        n = len(nums)
        for i in range(n):
            # Never let i refer to the same value twice to avoid duplicates
            if i != 0 and nums[i] == nums[i - 1]: continue
            j = i + 1
            k = n - 1
            while j < k:
                if nums[i] + nums[j] + nums[k] == 0:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    # Never let j refer to the same value twice (in an output) to avoid duplicates
                    while j < k and nums[j] == nums[j-1]: j += 1
                elif nums[i] + nums[j] + nums[k] < 0:
                    j += 1
                else:
                    k -= 1
        return res
