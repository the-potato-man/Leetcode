import heapq
import math

def ClosestXdestinations(numDestinations, allLocations, numDeliveries):
    def getTuple(i, allLocations):
        point = allLocations[i]
        x = point[0]
        y = point[1]
        dist = math.sqrt(x * x + y * y)
        rank = dist * -1
        return rank, dist, x, y

    pq = []
    for i in range(numDeliveries):
        rank, dist, x, y = getTuple(i, allLocations)
        heapq.heappush(pq, (rank, dist, x, y))

    for i in range(numDeliveries, numDestinations):
        rank, dist, x, y = getTuple(i, allLocations)

        oldRank, oldDist, oldX, oldX = pq[0]
        if dist < oldDist:
            heapq.heappop(pq)
            heapq.heappush(pq, (rank, dist, x, y))

    res = []
    for i in range(len(pq)):
        rank, dist, x, y = heapq.heappop(pq)
        res.append((x, y, dist))
    return res

def test():
    allLocations = [[3,6], [2,4], [5,3], [2,7], [1,8], [7,9]]
    numDestinations = 6
    numDeliveries = 3
    print(ClosestXdestinations(numDestinations, allLocations, numDeliveries))

test()