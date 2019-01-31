# Definition for a binary tree node.
# class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        def helper(root, path, sol):
            # Cannot use append because changing the same object in the recursive function
            path = path + [str(root.val)] 
            if not root.left and not root.right:
                sol.append(path)
            if root.left:
                helper(root.left, path, sol)
            if root.right:
                helper(root.right, path, sol)
        
        if not root: return []
        sol = []
        helper(root, [], sol)
        
        solPaths = []
        for path in sol:
            solPaths.append('->'.join(path))
        return solPaths
            
        