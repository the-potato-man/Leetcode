'''
A 2d grid map of m rows and n columns is initially filled with water. 
We may perform an addLand operation which turns the water at position (row, col) into a land.
Given a list of positions to operate, count the number of islands after each addLand operation. 
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
You may assume all four edges of the grid are all surrounded by water.

Example:

Input: m = 3, n = 3, positions = [[0,0], [0,1], [1,2], [2,1]]
Output: [1,1,2,3]
'''

class Solution(object):
    def numIslands2(self, m, n, positions):
        """
        :type m: int
        :type n: int
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        def isValid(r, c):
            return r >= 0 and c >= 0 and r < m and c < n
        
        sol = []
        pos2island = {} # position to island id
        numIslands = 0
        islandId = 0
        
        for r, c in positions:
            neigh = set()
            for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                nextR = r + dr
                nextC = c + dc
                pos = nextR * n + nextC
                if isValid(nextR, nextC) and pos in pos2island:
                    neigh.add(pos2island[pos])
            
            key = r * n + c
            if not neigh:
                numIslands += 1
                islandId += 1                
                pos2island[key] = islandId
            elif len(neigh) == 1:
                pos2island[key] = next(iter(neigh))
            else:
                rootId = next(iter(neigh))
                for pos, landId in pos2island.items():
                    if landId in neigh:
                        pos2island[pos] = rootId
                pos2island[key] = rootId
                numIslands -= (len(neigh) - 1)
            sol.append(numIslands)
            
        return sol
