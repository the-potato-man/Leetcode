class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        n = len(M)

        # return list of indicies
        def findNeighbors(i, M, visited):
            res = []
            for j in range(n):
                if M[i][j] == 1 and i != j and j not in visited:
                    res.append(j)
            return res

        numCircles = 0
        visited = set()
        queue = []

        for i in range(n):
            if i not in visited:
                numCircles += 1
                visited.add(i)
                queue += findNeighbors(i, M, visited) # Appends all items in returned list to queue
                while queue:
                    neigh = queue.pop(0)
                    if neigh not in visited:
                        visited.add(neigh)
                        queue += findNeighbors(neigh, M, visited)

        return numCircles
