import collections

class Solution:
    def numBusesToDestination(self, routes, S, T):
        """
        :type routes: List[List[int]]
        :type S: int
        :type T: int
        :rtype: int
        """
        if S == T: return 0
        
        # Converting routes to list of sets
        routes2 = [None] * len(routes)
        for i, route in enumerate(routes):
            routes2[i] = set()
            for j in route:
                routes2[i].add(j)
        routes = routes2
        
        # Creating graph, mapping bus index to index
        graph = collections.defaultdict(set)
        for i in range(len(routes)):
            for j in range(i+1, len(routes)):
                r1 = routes[i]
                r2 = routes[j]
                if r1.intersection(r2):
                    graph[i].add(j)
                    graph[j].add(i)
        
        visited = set()
        targets = set()
        for i, route in enumerate(routes):
            if S in route: visited.add(i)
            if T in route: targets.add(i)
        
        queue = []
        for node in visited:
            queue.append((node, 1))
        
        while queue:
            node, steps = queue.pop(0)
            if node in targets: return steps
            visited.add(node)
            for neigh in graph[node]:
                if neigh not in visited:
                    queue.append((neigh, steps + 1))
        return -1
