# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # Given a non-empty binary search tree and a target value, find the value in the BST that is closest to the target.
    def closestValue(self, root: TreeNode, target: float) -> int:
        if not root: return None
        cand = root.val
        while root:
            if root.val == target: return root.val
            if abs(root.val - target) < abs(cand - target):
                cand = root.val
            if root.val > target:
                root = root.left
            else:
                root = root.right
        return cand
