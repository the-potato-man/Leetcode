class Solution:
    def hasPath(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: bool
        """
        def isValid(r, c, maze):
            n = len(maze)
            m = len(maze[0])
            return r >= 0 and r < n and c >= 0 and c < m and maze[r][c] == 0
        
        endR = destination[0]
        endC =  destination[1]
        
        visited = set()
        queue = []
        queue.append((start[0], start[1]))
        
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        
        while queue:
            tempR, tempC = queue.pop(0)
            visited.add((tempR,tempC))
            if tempR == endR and tempC == endC:
                return True
            
            for dr, dc in directions:
                r, c = tempR, tempC
                while isValid(r + dr, c + dc, maze):
                    r += dr
                    c += dc
                if (r, c) not in visited:
                    queue.append((r,c))
        return False
