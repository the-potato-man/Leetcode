'''
There are two cases for the tree structure to be invalid.
1) A node having two parents;
   including corner case: e.g. [[4,2],[1,5],[5,2],[5,3],[2,4]]
2) A circle exists
---------------------------------------------------------------
1) Check whether there is a node having two parents. 
    If so, store them as candidates A and B, and set the second edge invalid. 
2) Perform normal union find. 
    If the tree is now valid 
           simply return candidate B
    else if candidates not existing 
           we find a circle, return current edge; 
    else 
           remove candidate A instead of B.
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
    def findRedundantDirectedConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        c1 = [-1, -1]
        c2 = [-1, -1]
        parent = [-1] * (len(edges) + 1)

        # Find candidates for cycle, and ignore during checking for parents
        for a, b in edges:
            if parent[b] != -1:
                c1 = [parent[b], b]
                c2 = [a, b]
                break
            parent[b] = a
        
        dsu = DSU()
        for a, b in edges:
            if c1 == [a, b] or c2 == [a, b]:
                continue
            if not dsu.union(a, b):
                return [a, b]
        
        # Check remaining cycle candidates in order
        if not dsu.union(c1[0], c1[1]): return c1
        return c2
