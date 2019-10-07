# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        self.string = ''
        
        def helper(root):
            if not root:
                self.string += 'None,'
            else:
                self.string += str(root.val) + ','
                helper(root.left)
                helper(root.right)
            return string                
        
        helper(root)
        return self.string
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        self.nodes = data.split(',')
        
        def helper():
            val = self.nodes.pop(0)
            if val == 'None':
                return None
            else:
                root = TreeNode(val)
                root.left = helper()
                root.right = helper()            
                return root
        
        return helper()

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
