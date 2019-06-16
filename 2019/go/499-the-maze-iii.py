'''
There is a ball in a maze with empty spaces and walls. 
The ball can go through empty spaces by rolling up (u), down (d), left (l) or right (r), 
but it won't stop rolling until hitting a wall. When the ball stops, it could choose the next direction. 
There is also a hole in this maze. The ball will drop into the hole if it rolls on to the hole.

Given the ball position, the hole position and the maze, find out how the ball could drop into the hole 
by moving the shortest distance. The distance is defined by the number of empty spaces traveled by the ball 
from the start position (excluded) to the hole (included). Output the moving directions by using 'u', 'd', 'l' and 'r'. 
Since there could be several different shortest ways, you should output the lexicographically smallest way. 
If the ball cannot reach the hole, output "impossible".

The maze is represented by a binary 2D array. 1 means the wall and 0 means the empty space. 
You may assume that the borders of the maze are all walls. The ball and the hole coordinates are represented by row and column indexes.
'''

import heapq

class Solution:
    def findShortestWay(self, maze, ball, hole):
        """
        :type maze: List[List[int]]
        :type ball: List[int]
        :type hole: List[int]
        :rtype: str
        """
        self.sol = []
        self.minSteps = float('inf')
        def processSolLexOrder(path, steps):
            if not self.sol:
                self.sol.append(path)
                self.minSteps = min(self.minSteps, steps)
            else:
                if steps == self.minSteps:
                    self.sol.append(path)
        
        def isValid(r, c, maze):
            n = len(maze)
            m = len(maze[0])
            return r >= 0 and r < n and c >= 0 and c < m and maze[r][c] == 0
        
        directions = [(1,0,'d'), (-1,0,'u'), (0,1,'r'), (0,-1,'l')]
        visited = set()
        pq = [(0, '', ball)]
         
        while pq:
            tempSteps, tempPath, ball = heapq.heappop(pq)
            if ball[0] == hole[0] and ball[1] == hole[1]:
                processSolLexOrder(tempPath, tempSteps)
            visited.add((ball[0], ball[1]))
            
            for dr, dc, di in directions:
                r, c, path, steps = ball[0], ball[1], tempPath, tempSteps
                path += di
                while isValid(r + dr, c + dc, maze):
                    r += dr
                    c += dc
                    steps += 1
                    if r == hole[0] and c == hole[1]:
                        processSolLexOrder(path, steps)
                if (r, c) not in visited:
                    heapq.heappush(pq, (steps, path, (r,c)))
        
        if self.sol:
            self.sol.sort()
            print(self.sol)
            return self.sol[0]

        return 'impossible'
