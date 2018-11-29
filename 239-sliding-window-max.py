class Solution:
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        if not nums: return []
        
        sol = []
        queue = []
        
        for i in range(k):
            while queue and nums[queue[-1]] <= nums[i]:
                queue.pop()
            queue.append(i)
        
        n = len(nums)
        for i in range(k, n):
            sol.append(nums[queue[0]])
            while queue and queue[0] <= i-k:
                queue.pop(0)
            while queue and nums[queue[-1]] <= nums[i]:
                queue.pop()
            queue.append(i)
        
        sol.append(nums[queue[0]])
        
        return sol
