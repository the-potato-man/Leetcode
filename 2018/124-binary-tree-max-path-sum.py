# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, node):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.localMax = float("-inf")
        self.helper(node)
        return self.localMax
        
    def helper(self, node):
        if not node: return 0

        onlyLeft = self.helper(node.left)
        onlyRight = self.helper(node.right)

        singleMax = node.val
        singleMax = max(singleMax, node.val + onlyLeft)
        singleMax = max(singleMax, node.val + onlyRight)
        
        withTop = node.val + onlyLeft + onlyRight
        bothMax = max(singleMax, withTop)
        self.localMax = max(self.localMax, bothMax)
        
        return singleMax
