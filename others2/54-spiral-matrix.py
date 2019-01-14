'''
Test cases
[[3]]
[[1,2,3]]
[
  [1]
  [2]
  [3]
]
[
  [1, 2],
  [5, 6]
]
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
'''
class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix: return matrix
        n = len(matrix)
        m = len(matrix[0])
        
        sol = []
        top = 0
        bottom = n - 1
        left = 0
        right = m - 1
        
        while left <= right and top <= bottom:
            if left <= right and top <= bottom:
                for i in range(left, right + 1):
                    sol.append(matrix[top][i])
                top += 1
            if left <= right and top <= bottom:
                for i in range(top, bottom + 1):
                    sol.append(matrix[i][right])
                right -= 1
            if left <= right and top <= bottom:
                for i in range(right, left - 1, -1):
                    sol.append(matrix[bottom][i])
                bottom -= 1
            if left <= right and top <= bottom:
                for i in range(bottom, top - 1, -1):
                    sol.append(matrix[i][left])
                left += 1
                
        return sol
