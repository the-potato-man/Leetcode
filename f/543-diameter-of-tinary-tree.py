# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

'''
Given a binary tree, you need to compute the length of the diameter of the tree. 
The diameter of a binary tree is the length of the longest path between any two nodes in a tree. 
This path may or may not pass through the root.
'''
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
