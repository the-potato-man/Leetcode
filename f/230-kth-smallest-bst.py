# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        
        self.res = None
        self.count = k
        
        def inOrder(root):
            if root.left:
                inOrder(root.left)
            self.count -= 1
            if self.count == 0:
                self.res = root.val
            if root.right:
                inOrder(root.right)
        
        inOrder(root)
        return self.res
