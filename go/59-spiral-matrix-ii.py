# Given a positive integer n, generate a square matrix filled with elements from 1 to n^2 in spiral order
class Solution:
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        def isValid(r, c):
            return 0 <= r < n and 0 <= c < n
        
        if n <= 0: return []
        
        res = [[None] * n for _ in range(n)]
        
        dR = [0, 1, 0, -1] # right, down, left, up
        dC = [1, 0, -1, 0]
        r, c, di = 0, 0, 0
        
        for i in range(1, n*n+1):
            res[r][c] = i
            nR = r + dR[di]
            nC = c + dC[di]
            if isValid(nR, nC) and not res[nR][nC]:
                r, c = nR, nC
            else:
                di = (di + 1) % 4
                r += dR[di]
                c += dC[di]
        
        return res
