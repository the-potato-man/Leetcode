# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def levelOrder(root, level, levelList):
            if not root: return
            
            if len(levelList) <= level:
                levelList.append([])
            levelList[level].append(root.val)
            
            levelOrder(root.left, level + 1, levelList)
            levelOrder(root.right, level + 1, levelList)
        
        levelList = []
        levelOrder(root, 0, levelList)
        
        sol = []
        for level in levelList:
            sol.append(level[-1])
        return sol
    