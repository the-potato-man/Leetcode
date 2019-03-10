# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        
        self.res = None
        self.count = k
        
        def inorder(root):
            if root.left:
                inorder(root.left)
            # root.val
            self.count -= 1
            if self.count == 0:
                self.res = root.val
            if root.right:
                inorder(root.right)
        
        inorder(root)
        return self.res
