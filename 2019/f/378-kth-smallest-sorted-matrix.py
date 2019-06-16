'''
Given a n x n matrix where each of the rows and columns are sorted in ascending order, find the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.
'''

import heapq
class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        pq = []
        for row in matrix:
            heapq.heappush(pq, (row[0], row, 1))
        
        for _ in range(k-1):
            val, row, idx = heapq.heappop(pq)
            
            if idx < len(row):
                heapq.heappush(pq, (row[idx], row, idx + 1))
            
        return pq[0][0]
