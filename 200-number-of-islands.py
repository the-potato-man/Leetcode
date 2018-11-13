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
        if not grid: return 0
        numRows = len(grid)
        numCols = len(grid[0])
        
        numIslands = 0
        
        def isValid(grid, row, col):
            if row < 0 or col < 0 or row >= numRows or col >= numCols or grid[row][col] == '0':
                return False
            return True
        
        def bfs(grid, row, col):   
            islandFound = False
            stack = []
            if isValid(grid, row, col):
                stack.append((row, col))
                islandFound = True
            while stack:
                (row, col) = stack.pop()
                row = int(row)
                col = int(col)
                grid[row][col] = '0'
                r1, c1 = row + 1, col
                r2, c2 = row - 1, col
                r3, c3 = row, col + 1
                r4, c4 = row, col - 1
                if isValid(grid, r1, c1): stack.append((r1, c1))
                if isValid(grid, r2, c2): stack.append((r2, c2))
                if isValid(grid, r3, c3): stack.append((r3, c3))
                if isValid(grid, r4, c4): stack.append((r4, c4))
                    
            return islandFound
                           
        for r in range(numRows):
            for c in range(numCols):
                if isValid(grid, r, c):
                    if bfs(grid, r, c):
                        numIslands += 1
            
        return numIslands
    
    def numIslandsDFS(self, grid): # solved with DFS
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid: return 0
        numRows = len(grid)
        numCols = len(grid[0])
        
        numIslands = 0
        
        def isValid(grid, row, col):
            if row < 0 or col < 0 or row >= numRows or col >= numCols or grid[row][col] == '0':
                return False
            return True
        
        def dfs(grid, row, col):   
            if isValid(grid, row, col):
                grid[row][col] = '0'
            else:
                return
            
            r1, c1 = row + 1, col
            r2, c2 = row - 1, col
            r3, c3 = row, col + 1
            r4, c4 = row, col - 1
            dfs(grid, r1, c1)
            dfs(grid, r2, c2)
            dfs(grid, r3, c3)
            dfs(grid, r4, c4)
                           
        for r in range(numRows):
            for c in range(numCols):
                if isValid(grid, r, c):
                    numIslands += 1
                    dfs(grid, r, c)
                        
        return numIslands