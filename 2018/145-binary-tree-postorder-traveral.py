# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def helper(node, sol):
            if node:
                if node.left:
                    helper(node.left, sol)
                if node.right:
                    helper(node.right, sol)
                sol.append(node.val)
        
        sol = []
        helper(root, sol)
        return sol

    def postorderTraversalIterative(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root: return []
        
        sol = []
        stack = [root]
        
        while stack:
            top = stack[-1] if stack else None        
            if not top.left and not top.right:
                curr = stack.pop()
                if curr: sol.append(curr.val)
            else:
                if top.right:
                    stack.append(top.right)
                    top.right = None
                if top.left:
                    stack.append(top.left)
                    top.left = None
        return sol
        