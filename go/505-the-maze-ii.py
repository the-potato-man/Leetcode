'''
There is a ball in a maze with empty spaces and walls. The ball can go through empty spaces by rolling up, down, left or right, 
but it won't stop rolling until hitting a wall. When the ball stops, it could choose the next direction.

Given the ball's start position, the destination and the maze, find the shortest distance for the ball to stop at the destination. 
The distance is defined by the number of empty spaces traveled by the ball from the start position (excluded) to the destination (included). 
If the ball cannot stop at the destination, return -1.

The maze is represented by a binary 2D array. 1 means the wall and 0 means the empty space. You may assume that the borders of the maze are all walls. 
The start and destination coordinates are represented by row and column indexes.'
'''

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
