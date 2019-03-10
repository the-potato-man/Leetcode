# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def longestConsecutive(self, root: TreeNode) -> int:
        self.maxLength = 0
        def dfs(node, parent, length):
            if not node: return
            length = length + 1 if parent and parent.val + 1 == node.val else 1
            self.maxLength = max(self.maxLength, length)
            dfs(node.left, node, length)
            dfs(node.right, node, length)
        
        dfs(root, None, 0)
        return self.maxLength
