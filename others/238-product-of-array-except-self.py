'''
Algorithm:
1) Construct a temporary array left[] such that left[i] contains product of all elements on left of arr[i] excluding arr[i].
2) Construct another temporary array right[] such that right[i] contains product of all elements on on right of arr[i] excluding arr[i].
3) To get prod[], multiply left[] and right[].
'''
class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums: return None
        
        n = len(nums)
        res, left, right = [0] * n, [0] * n, [0] * n
        left[0], right[-1] = 1, 1
        
        for i in range(1, n):
            left[i] = left[i-1] * nums[i-1]
        
        for i in range(n-2, -1, -1):
            right[i] = right[i+1] * nums[i+1]
        
        for i in range(n):
            res[i] = left[i] * right[i]
        
        return res
