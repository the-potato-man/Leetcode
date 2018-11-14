# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        def helper(root, level, sol):
            if not root: return
            
            if len(sol) < level + 1:
                sol.append([])
            sol[level].append(root.val)
            
            helper(root.left, level + 1, sol)
            helper(root.right, level + 1, sol)  
            
        sol = []
        helper(root, 0, sol)
        return sol