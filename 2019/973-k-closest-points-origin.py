import heapq
import math

class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """       
            
        def getTuple(i, points):
            point = points[i]
            x = point[0]
            y = point[1]
            dist = math.sqrt(x * x + y * y)
            rank = dist * -1
            return rank, dist, x, y

        pq = []
        for i in range(K):
            rank, dist, x, y = getTuple(i, points)
            heapq.heappush(pq, (rank, dist, x, y))

        for i in range(K, len(points)):
            rank, dist, x, y = getTuple(i, points)

            oldRank, oldDist, oldX, oldX = pq[0]
            if dist < oldDist:
                heapq.heappop(pq)
                heapq.heappush(pq, (rank, dist, x, y))

        res = []
        for i in range(len(pq)):
            rank, dist, x, y = heapq.heappop(pq)
            res.append((x, y))
        return res
