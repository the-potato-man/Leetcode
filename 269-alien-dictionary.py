class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        self.hasCycle = False

        def topologicalSort(graph): 
            visited = {} 
            stack = [] 
            cycleStack = {}
            for c in graph.keys(): 
                if c not in visited: 
                    helper(graph, c, visited, stack, cycleStack)
            return stack
                    
        def helper(graph, c, visited, stack, cycleStack): 
            visited[c] = True
            cycleStack[c] = True
            for neigh in graph[c]: 
                if neigh not in visited: 
                    helper(graph, neigh, visited, stack, cycleStack)
                elif cycleStack[neigh] == True:
                    self.hasCycle = True
            cycleStack[c] = False    
            stack.insert(0,c) 
        
        graph = {}
        for word in words:
            for c in word:
                if c not in graph:
                    graph[c] = set()
        
        for i in range(1, len(words)):
            w1 = words[i-1]
            w2 = words[i]
            n = min(len(w1), len(w2))
            for j in range(n):
                c1 = w1[j]
                c2 = w2[j]
                if c1 != c2:
                    if c2 not in graph[c1]:
                        graph[c1].add(c2)
                    break
        
        solList = topologicalSort(graph)
        return ''.join(solList) if self.hasCycle == False else ''
    
    # https://zhuhan0.blogspot.com/2017/06/leetcode-269-alien-dictionary.html
    def alienOrder2(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        def buildGraph(words, graph, inDegree):
            for word in words:
                for c in word:
                    if c not in graph:
                        graph[c] = set()
                        inDegree[c] = 0
                        
            for i in range(1, len(words)):
                w1 = words[i-1]
                w2 = words[i]
                length = min(len(w1), len(w2))
                
                for j in range(length):
                    c1 = w1[j]
                    c2 = w2[j]
                    if c1 != c2:
                        if c2 not in graph[c1]:
                            graph[c1].add(c2)
                            inDegree[c2] += 1
                        break
        
        def topologialSort(graph, inDegree):
            queue = []
            for c in graph.keys():
                if inDegree[c] == 0:
                    queue.append(c)
            sb = []
            while queue:
                c = queue.pop(0)
                sb.append(c)
                for neigh in graph[c]:
                    inDegree[neigh] -= 1
                    if inDegree[neigh] == 0:
                        queue.append(neigh)
            return ''.join(sb)
        
        graph = {}
        inDegree = {}
        buildGraph(words, graph, inDegree)
        order = topologialSort(graph, inDegree)
        return order if len(order) == len(graph) else ''
