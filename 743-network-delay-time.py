import heapq

class Solution:
    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        # Dijkstra's is like breadth first search with heaps
        
        # Construct the graph, with lists of neighbors
        graph = {}
        for u, v, weight in times:
            if u not in graph: # Ensure all nodes included
                graph[u] = []
            if v not in graph:
                graph[v] = []
            graph[u].append((v, weight))
        
        dist = {} # keep track of all times from k
        heap = [(0, K)] # starting at node K
        while heap:
            d, node = heapq.heappop(heap) # heap tuples are switched
            if node not in dist:
                dist[node] = d
                for v, weight in graph[node]:
                    if v not in dist:
                        heapq.heappush(heap, (weight + d, v))
        
        # Check if all N nodes visited in dist
        if len(dist) == N:
            return max(dist.values())
        else:
            return -1
