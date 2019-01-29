'''
Equations are given in the format A / B = k, where A and B are variables represented as strings, and k is a real number (floating point number). Given some queries, return the answers. If the answer does not exist, return -1.0.

Example:
Given a / b = 2.0, b / c = 3.0. 
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? . 
return [6.0, 0.5, -1.0, 1.0, -1.0 ].

The input is: vector<pair<string, string>> equations, vector<double>& values, vector<pair<string, string>> queries , where equations.size() == values.size(), and the values are positive. This represents the equations. Return vector<double>.

According to the example above:

equations = [ ["a", "b"], ["b", "c"] ],
values = [2.0, 3.0],
queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ]. 
The input is always valid. You may assume that evaluating the queries will result in no division by zero and there is no contradiction.
'''

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


    '''
    class Node:
        def __init__(self, label, val):
            self.label = label
            self.val = val
    '''
    # Possible Union Find Solution
    def calcEquationUnionFind(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        self.graph = {} # mapping string to nodes
        
        def find(s):
            if s not in self.graph: return None
            node = self.graph[s]
            if node.label == s: # checks if the node is a root of group
                return node
            else:
                parent = find(node.label)
                temp = Node(parent.label, parent.val * node.val)
                self.graph[s] = temp
                return temp

        def union(x, y, val):
            if x not in self.graph and y not in self.graph:
                self.graph[x] = Node(y, val)
                self.graph[y] = Node(y, 1) # y is a root, so its parent is itself
            elif x in self.graph and y in self.graph:
                nodeX = find(x)
                nodeY = find(y)
                if nodeX == nodeY: return
                self.graph[nodeX.label] = Node(nodeY.label, val * nodeY.val / nodeX.val)
            elif x not in self.graph:
                nodeY = find(y)
                self.graph[x] = Node(nodeY.label, nodeY.val * val)
            else:
                nodeX = find(x)
                self.graph[y] = Node(nodeX.label, nodeX.val / val)

        for i in range(len(equations)):
            a = equations[i][0]
            b = equations[i][1]
            ans = values[i]
            union(a, b, ans)

        res = [1] * len(queries) # Why does this only work with array of 1's?
        for i in range(len(queries)):
            a, b = queries[i][0], queries[i][1]
            nodeA, nodeB = find(a), find(b)
            if not nodeA or not nodeB:
                res[i] = -1.0
            elif a == b:
                res[i] == 1.0
            elif nodeA.label != nodeB.label:
                res[i] = -1.0
            else:
                res[i] = nodeA.val / nodeB.val
        return res
