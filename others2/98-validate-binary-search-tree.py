# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        def helper(root, minVal, maxVal):
            if not root: return True
            if root.val <= minVal or root.val >= maxVal:
                return False
            return helper(root.left, minVal, root.val) and helper(root.right, root.val, maxVal)
        
        return helper(root, float('-inf'), float('inf'))
