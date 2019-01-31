# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def height(node):
            if not node: return 0
            return 1 + max(height(node.left), height(node.right))
        
        if not root:
            return True
        
        if abs(height(root.left) - height(root.right)) > 1:
            return False
        
        return self.isBalanced(root.left) and self.isBalanced(root.right)
