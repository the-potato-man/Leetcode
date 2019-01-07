# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

'''
https://leetcode.com/problems/house-robber-iii/discuss/185950/Python-DFS%2BDP-solution-O(N)-time-O(N)-stack-space

If we know maximum profit from left and right tree, the maximum profit is simply the sum of their values plus root's value.

But for a root node, we have two choices:

If we want to pick it, the root of the left and right subtrees cannot be picked.
If we do not pick the current node, we do not care whether any of the child is picked, so the anwer is the sum of (max from left) and (max from right).
For each subtree, we return two max profits, one with root picked, one without root picked, so the parent can decide accordingly.
'''

class Solution:
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(root):
            if not root: return 0, 0
            pickl, nopickl = dfs(root.left)
            pickr, nopickr = dfs(root.right)
            pick = nopickl + nopickr + root.val
            nopick = max(pickl, nopickl) + max(pickr, nopickr)
            return pick, nopick
        pick, nopick = dfs(root)
        return max(pick, nopick)
