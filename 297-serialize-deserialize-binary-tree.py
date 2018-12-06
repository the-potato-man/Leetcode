# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    # Preorder Traversal
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def helper(root, string):
            if not root:
                string += 'None,'
            else:
                string += str(root.val) + ','
                string = helper(root.left, string)
                string = helper(root.right, string)
            return string                
        
        return helper(root, '')

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def helper(l):
            val = l.pop(0)
            if val == 'None':
                return None
            root = TreeNode(val)
            root.left = helper(l)
            root.right = helper(l)            
            return root
        
        l = data.split(',')
        return helper(l)
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
