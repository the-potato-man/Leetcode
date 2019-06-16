class Solution:
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def binarySearch(nums, start, end):
            if start == end:
                return start
            mid = (start + end) // 2
            if nums[mid] > nums[mid+1]:
                return binarySearch(nums, start, mid)
            else:
                return binarySearch(nums, mid+1, end)
            
        return binarySearch(nums, 0, len(nums)-1)
