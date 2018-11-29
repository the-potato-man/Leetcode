# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def helper(root, sol):
            if root:
                sol.append(root.val)
                if root.left:
                    helper(root.left, sol)
                if root.right:
                    helper(root.right, sol)                
        
        sol = []
        helper(root, sol)
        return sol

    def preorderTraversalIterative(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        sol = []
        stack = [root]
        
        while stack:
            curr = stack.pop()
            if curr:
                sol.append(curr.val)
                if curr.right:
                    stack.append(curr.right)
                if curr.left:
                    stack.append(curr.left)
        
        return sol
