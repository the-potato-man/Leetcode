# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

'''
Given a binary tree, find the length of the longest consecutive sequence path.

The path refers to any sequence of nodes from some starting node to any node in the tree along the parent-child connections. 
The longest consecutive path need to be from parent to child (cannot be the reverse).

Input:

   1
    \
     3
    / \
   2   4
        \
         5

Output: 3

Explanation: Longest consecutive sequence path is 3-4-5, so return 3.

'''
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
