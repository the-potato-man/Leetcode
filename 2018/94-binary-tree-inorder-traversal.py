# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def helper(root, sol):
            if root:
                if root.left:
                    helper(root.left, sol)
                sol.append(root.val)
                if root.right:
                    helper(root.right, sol)
        sol = []
        helper(root, sol)
        return sol

    def inorderTraversalIterative(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        sol = []
        stack = []
        curr = root
        
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            sol.append(curr.val)
            curr = curr.right
        
        return sol