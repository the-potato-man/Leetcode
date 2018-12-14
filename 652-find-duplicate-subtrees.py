# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        def helper(root, count, res):
            if not root:
                return '#'
            
            val = str(root.val)
            leftVal = helper(root.left, count, res)
            rightVal = helper(root.right, count, res)
            
            serial = val + ',' + leftVal + ',' + rightVal
            if serial in count:
                count[serial] += 1
            else:
                count[serial] = 1
                
            if count[serial] == 2:
                res.append(root)
                
            return serial
        
        count = {}
        res = []
        helper(root, count, res)
        return res
