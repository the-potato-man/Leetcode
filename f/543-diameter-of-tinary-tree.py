# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.ans = 1 # account for base case if null root
        def depth(node):
            if not node: return 0
            left = depth(node.left)
            right = depth(node.right)
            self.ans = max(self.ans, 1 + left + right)
            return 1 + max(left, right)
        
        depth(root)
        return self.ans - 1
