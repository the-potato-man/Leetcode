class Solution:
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        self.hasCycle = False
        
        def topologicalSort(graph):
            visited = set()
            stack = []
            cycleSet = set()
            for key in graph.keys():
                if key not in visited:
                    helper(key, graph, visited, cycleSet, stack)
            return stack
        
        def helper(n, graph, visited, cycleSet, stack):
            visited.add(n)
            cycleSet.add(n)
            for neigh in graph[n]:
                if neigh not in visited:
                    helper(neigh, graph, visited, cycleSet, stack)
                elif neigh in cycleSet:
                    self.hasCycle = True
            cycleSet.remove(n)
            stack.insert(0, n)
            
        graph = {}
        for i in range(numCourses):
            if i not in graph:
                graph[i] = set()
        for course, prereq in prerequisites:
            graph[prereq].add(course)
        
        res = topologicalSort(graph)
        return res if not self.hasCycle else []
