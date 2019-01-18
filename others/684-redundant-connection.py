class DSU:
    def __init__(self):
        self.parent = {}
        self.rank = {}
        for i in range(1001):
            self.parent[i] = i
            self.rank[i] = 0

    def find(self, x):
        # Path Compression
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        # Union by rank
        xr = self.find(x)
        yr = self.find(y)

        if xr == yr:
            return False
        elif self.rank[xr] < self.rank[yr]:
            self.parent[yr] = xr
        elif self.rank[xr] > self.rank[yr]:
            self.parent[xr] = yr
        else:
            self.parent[yr] = xr
            self.rank[yr] += 1
        return True


class Solution:
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        dsu = DSU()
        for edge in edges:
            if not dsu.union(*edge):
                return edge
