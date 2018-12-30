import collections

class Solution:
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        def dfs(start, end, curr, graph, visited):
            if start not in graph or start in visited: return -1
            if start == end: return curr
            
            visited.add(start)
            for key, val in graph[start].items():
                result = dfs(key, end, curr * val, graph, visited)
                if result != -1:
                    return result
            return -1
        
        graph = collections.defaultdict(dict) # maps to factors of key
        for i in range(len(equations)):
            n = equations[i][0]
            d = equations[i][1]
            val = float(values[i])
            graph[n][d] = val
            graph[d][n] = 1.0 / val
        
        results = [0] * len(queries)
        for i in range(len(results)):
            results[i] = dfs(queries[i][0], queries[i][1], 1, graph, set())
        
        return results
