# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if not node: return node
        created = {}
        created[node] = UndirectedGraphNode(node.label)
        stack = [node]
        while stack:
            n = stack.pop()
            for neigh in n.neighbors:
                if neigh not in created:
                    temp = UndirectedGraphNode(neigh.label)
                    created[neigh] = temp
                    created[n].neighbors.append(temp)     
                    stack.append(neigh)
                else:
                    temp = created[neigh]
                    created[n].neighbors.append(temp) 
        
        return created[node]
                    