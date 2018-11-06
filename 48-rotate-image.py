'''
[
  [1,2],
  [3,4]
]
[
  [1,2,3],  0, -> 3
  [4,5,6],  1, 1
  [7,8,9]
]
[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
]
[
  [ 5, 1, 9,11, 1], 0, -> 4      n = 5
  [ 2, 4, 8,10, 2], 1, 1-> 3
  [13, 3, 6, 7, 3],
  [15,14,12,16, 4],
  [15,14,12,16, 5]
]
[
  [ 5, 1, 9,11, 1, 1], 0, -> 5      n = 5   
  [ 2, 4, 8,10, 2, 2], 1, 1-> 4             
  [13, 3, 6, 7, 3, 3], 2, 2->3
  [15,14,12,16, 4, 4],
  [15,14,12,16, 5, 5],
  [15,14,12,16, 5, 6],
]

'''
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for r in range(int(n/2)): 
            for c in range(r, n-r-1):
                temp = matrix[r][c]
                # left to top
                matrix[r][c] = matrix[n-c-1][r]               
                # bot to left
                matrix[n-c-1][r] = matrix[n-r-1][n-c-1]        
                # right to bot
                matrix[n-r-1][n-c-1]  = matrix[c][n-r-1]                
                # top to right 
                matrix[c][n-r-1]  = temp                        