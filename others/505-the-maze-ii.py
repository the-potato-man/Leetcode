import heapq

class Solution:
    def shortestDistance(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: int
        """
        def isValid(r, c, maze):
            n = len(maze)
            m = len(maze[0])
            return 0 <= r < n and 0 <= c < m and maze[r][c] == 0
        
        endR, endC = destination[0], destination[1]
        
        visited = set()
        pq = [(0, start[0], start[1])]
        
        while pq:
            tempSteps, tempR, tempC = heapq.heappop(pq)
            if tempR == endR and tempC == endC:
                return tempSteps
            visited.add((tempR,tempC))
            
            for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                r, c, steps = tempR, tempC, tempSteps 
                while isValid(r + dr, c + dc, maze):
                    r += dr
                    c += dc
                    steps += 1
                if (r,c) not in visited:
                    heapq.heappush(pq, (steps, r, c))
        return -1
