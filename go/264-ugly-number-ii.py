# https://medium.com/@rachit.slt/leetcode-ugly-number-a7af445ab14c

import heapq
class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        primes = [5,3,2]
        nums = [2,3,5]
        heapq.heapify(nums)
        
        p = 1
        for i in range(n-1):
            p = heapq.heappop(nums)
            for prime in primes:
                heapq.heappush(nums, p * prime)
                # Skipping over calculate repeats, based on order of primes
                if p % prime == 0: break
        return p
    
    def nthUglyNumberIterative(self, n):
        """
        :type n: int
        :rtype: int
        """
        ugly = [0] * n
        ugly[0] = 1
        
        i2 = i3 = i5 = 0
        
        nextMult2 = 2
        nextMult3 = 3
        nextMult5 = 5
        
        for i in range(1, n):
            ugly[i] = min(nextMult2, nextMult3, nextMult5)
            if ugly[i] == nextMult2:
                i2 += 1
                nextMult2 = ugly[i2] * 2
            if ugly[i] == nextMult3:
                i3 += 1
                nextMult3 = ugly[i3] * 3
            if ugly[i] == nextMult5:
                i5 += 1
                nextMult5 = ugly[i5] * 5
        
        return ugly
