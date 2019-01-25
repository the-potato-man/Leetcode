"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Codec:
    # Preorder Traversal
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: Node
        :rtype: str
        """
        def helper(root):
            if not root: return
            serial.append(str(root.val))            
            for child in root.children:
                helper(child)                
            serial.append('#')    

        serial = []
        helper(root)
        return ' '.join(serial)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: Node
        """      
        def helper(root):
            if not tokens: return
            while tokens[0] != '#':
                child = Node(int(tokens.pop(0)), [])
                root.children.append(child)
                helper(child)
            tokens.pop(0) # Remove ending # symbol
        
        if not data: return None
        tokens = data.split(' ')
        root = Node(int(tokens.pop(0)), [])
        helper(root)
        return root


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))