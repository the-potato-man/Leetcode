import heapq

class Solution:
    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        graph = {}
        for u, v, weight in times:
            if u not in graph:
                graph[u] = []
            if v not in graph:
                graph[v] = []
            graph[u].append((v, weight))
        
        dist = {}
        heap = [(0,K)] # starting at node K
        while heap:
            d, node = heapq.heappop(heap)
            if node in dist:
                continue
            dist[node] = d
            for v, weight in graph[node]:
                if v not in dist:
                    heapq.heappush(heap, (d + weight, v))
        
        if len(dist) == N: # ensure there are N total nodes covered
            return max(dist.values())
        else:
            return -1
