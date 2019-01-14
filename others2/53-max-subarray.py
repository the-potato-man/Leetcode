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

    def maxSubArrayDivideAndConquer(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        def maxCrossingSum(arr, l, m, r): 
            # Left of mid
            curr = 0
            leftSum = float('-inf')
            for i in range(m, l-1, -1): 
                curr += arr[i]
                leftSum = max(leftSum, curr)

            # Right of mid 
            curr = 0
            rightSum = float('-inf')
            for i in range(m+1, r+1): 
                curr += arr[i] 
                rightSum = max(rightSum, curr)
                    
            return leftSum + rightSum; 

        def maxSubArraySum(arr, l, r): 
            if (l == r): return arr[l] 
            m = (l + r) // 2
            return max(maxSubArraySum(arr, l, m), 
                       maxSubArraySum(arr, m+1, r), 
                       maxCrossingSum(arr, l, m, r))

        return maxSubArraySum(nums, 0, len(nums)-1)
