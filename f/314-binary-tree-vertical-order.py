# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        col = {} # maps index to node
        queue = [(root, 0)]
        while queue:
            node, i = queue.pop(0)
            if node:
                if i not in col: col[i] = []
                col[i].append(node.val)
                queue.append((node.left, i - 1))
                queue.append((node.right, i + 1))
                
        return [col[i] for i in sorted(col)]
  