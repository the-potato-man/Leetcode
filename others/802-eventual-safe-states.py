class Solution(object):
#     def eventualSafeNodes(self, graph):
#         """
#         :type graph: List[List[int]]
#         :rtype: List[int]
#         """
#         n = len(graph)
        
#         self.hasCycle = False

#         def helper(i, graph, visited, cycleStack):
#             if self.hasCycle == True: return # end search early
#             if i in sol: return # end search early
#             visited[i] = True
#             cycleStack[i] = True
#             for neigh in graph[i]:
#                 if neigh in sol: continue # end search early
#                 if neigh not in visited:
#                     helper(neigh, graph, visited, cycleStack)
#                 elif cycleStack[neigh]:
#                     self.hasCycle = True
#             cycleStack[i] = False
        
#         sol = []
#         for i in range(n):
#             visited = {}
#             cycleStack = {}
#             helper(i, graph, visited, cycleStack)
#             if self.hasCycle == False:
#                 sol.append(i)
#             self.hasCycle = False
        
#         return sol

    def eventualSafeNodes(self, graph):        
            def dfs(graph, i, visited):                                         
                for j in graph[i]:
                    if j in visited: return False
                    if j in ans: continue # end early
                    visited.add(j)                
                    if not dfs(graph, j, visited): return False
                    visited.remove(j)                                                                            
                ans.add(i)     
                return True                        
            ans = set()
            for i in range(len(graph)):            
                visited = set([i])
                dfs(graph, i, visited)        
            return sorted(list(ans))

