# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def findClosestLeaf(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        def dfs(graph, node, parent):
            if node:
                if node not in graph:
                    graph[node] = []
                if parent not in graph:
                    graph[parent] = []

                graph[node].append(parent)
                graph[parent].append(node)
                dfs(graph, node.left, node)
                dfs(graph, node.right, node)
        
        graph = {}
        dfs(graph, root, None)
        
        visited = set()
        queue = []
        
        for node, val in graph.items():
            if node and node.val == k:
                visited.add(node)
                queue.append(node)
        
        while queue:
            node = queue.pop(0)
            if node:
                if len(graph[node]) <= 1:
                    return node.val
                for neigh in graph[node]:
                    if neigh not in visited:
                        queue.append(neigh)
                        visited.add(neigh)
