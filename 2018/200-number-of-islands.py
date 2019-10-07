'''
[
    [11110]
    [11010]
    [11000]
    [00000]
[
'''
class Solution(object):
    def numIslands(self, grid): # solved with BFS
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        self.numIslands = 0
        
        if not grid: return 0
        numRows = len(grid)
        numCols = len(grid[0])        

        def isValid(grid, row, col):
            return row >= 0 and col >= 0 and row < numRows and col < numCols and grid[row][col] == '1'
        
        def bfs(grid, row, col):
            self.numIslands += 1
            stack = [(row, col)]
            while stack:
                (row, col) = stack.pop()
                row = int(row)
                col = int(col)
                grid[row][col] = '0'
                
                directions = [(1,0), (-1,0), (0,1), (0,-1)]
                for r, c in directions:
                    tempR, tempC = row + r, col + c
                    if isValid(grid, tempR, tempC):
                        stack.append((tempR, tempC))

        for r in range(numRows):
            for c in range(numCols):
                if isValid(grid, r, c):
                    bfs(grid, r, c)
            
        return self.numIslands
    
    def numIslandsDFS(self, grid): # solved with DFS
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        
        def isValid(grid, row, col):
            return row >= 0 and col >= 0 and row < numRows and col < numCols and grid[row][col] != '0'
        
        def dfs(grid, row, col):   
            if not isValid(grid, row, col):
                return
            
            grid[row][col] = '0'            
            directions = [(1,0), (-1,0), (0,1), (0,-1)]
            for r, c in directions:
                dfs(grid, row + r, col + c)
                
        if not grid: return 0
        numRows = len(grid)
        numCols = len(grid[0])    
        
        numIslands = 0                           
        for r in range(numRows):
            for c in range(numCols):
                if isValid(grid, r, c):
                    numIslands += 1
                    dfs(grid, r, c)
                        
        return numIslands

    class DSU:
        def __init__(self, grid):
            self.count = 0
            m = len(grid)
            n = len(grid[0])
            self.parent = [-1] * (m * n + 1)
            self.rank = [0] * (m * n + 1)
            for i in range(m):
                for j in range(n):
                    if grid[i][j] == '1':
                        self.parent[i * n + j] = i * n + j
                        self.count += 1

        def find(self, x):
            # Path Compression
            if self.parent[x] != x:
                self.parent[x] = self.find(self.parent[x])
            return self.parent[x]

        def union(self, x, y):
            # Union by rank
            xr = self.find(x)
            yr = self.find(y)

            if xr != yr:
                if self.rank[xr] < self.rank[yr]:
                    self.parent[yr] = xr
                elif self.rank[xr] > self.rank[yr]:
                    self.parent[xr] = yr
                else:
                    self.parent[yr] = xr
                    self.rank[yr] += 1
                self.count -= 1
            return True

    class Solution:
        def numIslandsUsingDisjointSet(self, grid):
            """
            :type grid: List[List[str]]
            :rtype: int
            """
            if not grid: return 0
            m = len(grid)
            n = len(grid[0])
            
            def isValid(grid, row, col):
                if row < 0 or col < 0 or row >= m or col >= n or grid[row][col] == '0':
                    return False
                return True

            dsu = DSU(grid)
            for r in range(m):
                for c in range(n):
                    if grid[r][c] == '1':
                        grid[r][c] = '0'
                        for rd, cd in [(1,0), (-1,0), (0,1), (0,-1)]:
                            r2, c2 = r + rd, c + cd
                            if isValid(grid, r2, c2):
                                dsu.union(r * n + c, r2 * n + c2)
            return dsu.count
