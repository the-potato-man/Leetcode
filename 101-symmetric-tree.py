# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def helper(p, q):
            if not p and not q: return True
            if p and not q: return False
            if q and not p: return False
            
            if p.val != q.val: return False
            return helper(p.left, q.right) and helper(p.right, q.left)
        
        if not root: return True
        return helper(root.left, root.right)