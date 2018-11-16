class Node():
    def __init__(self, val=None):
        self.val = val
        self.dic = {}
        self.isEnd = False

class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dummy = Node()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        node = self.dummy
        for char in word:
            if char not in node.dic:
                node.dic[char] = Node(char)               
            node = node.dic[char]
        node.isEnd = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node = self.dummy
        for char in word:
            if char not in node.dic:
                return False               
            node = node.dic[char]
        return node.isEnd == True

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        node = self.dummy
        for char in prefix:
            if char not in node.dic:
                return False               
            node = node.dic[char]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
