'''
In this problem, a tree is an undirected graph that is connected and has no cycles.

The given input is a graph that started as a tree with N nodes (with distinct values 1, 2, ..., N), 
with one additional edge added. The added edge has two different vertices chosen from 1 to N, 
and was not an edge that already existed.

The resulting graph is given as a 2D-array of edges. 
Each element of edges is a pair [u, v] with u < v, 
that represents an undirected edge connecting nodes u and v.

Return an edge that can be removed so that the resulting graph is a tree of N nodes. 
If there are multiple answers, return the answer that occurs last in the given 2D-array. 
The answer edge [u, v] should be in the same format, with u < v.
'''

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
