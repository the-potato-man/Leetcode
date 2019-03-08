class Node():
    def __init__(self, val=None):
        self.val = val
        self.dic = {}
        self.isEnd = False

class WordDictionary:

    def __init__(self):
        self.head = Node()

    def addWord(self, word: str) -> None:
        node = self.head
        for char in word:
            if char not in node.dic:
                node.dic[char] = Node(char)               
            node = node.dic[char]
        node.isEnd = True
        
    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        node = self.head
        self.res = False
        self.dfs(node, word)
        return self.res
    
    def dfs(self, node, word):
        if not word:
            if node.isEnd:
                self.res = True
            return
        
        if word[0] == '.':
            for neigh, nNode in node.dic.items():
                self.dfs(nNode, word[1:])
        else:
            if word[0] in node.dic:
                # node will never be passed as None to dfs
                node = node.dic[word[0]]
                self.dfs(node, word[1:])

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
