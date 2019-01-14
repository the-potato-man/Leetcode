# https://leetcode.com/problems/the-skyline-problem/discuss/197959/Java-Heap-with-Explanations

import heapq

class Point:
    def __init__(self, x, height):
        self.x = x
        self.height = height
        # Negative heights are building starts, positive are building ends
        # Easier than have isStart bool, for writing comparator funct

class Solution:
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        if not buildings: return []
        
        points = []
        for building in buildings:
            points.append(Point(building[0], -building[2])) # Negative height
            points.append(Point(building[1], building[2]))

        points.sort(key=lambda point: (point.x, point.height))
        
        res = []
        pq = [(0,0)] # Handles case when there are no buildings
        currHeight = 0
        for point in points:
            if point.height > 0:    # if at end of building
                pq.remove((-point.height, point.height))
                heapq.heapify(pq)
            else:                   # if at start of the building
                heapq.heappush(pq, (point.height, -point.height))
            if pq and currHeight != pq[0][1]: # rank, height = pq[0][1]
                currHeight = pq[0][1]
                res.append([point.x, currHeight])
        return res
