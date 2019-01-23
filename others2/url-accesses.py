'''
Give an array the address and number of URL accesses, and find the sum of the number of url access addresses
[['google.com', '20'], ['mail.google.com', '10']] => { 'google.com' : 30, 'mail.google.com': 10 }
'''

class Node:
    def __init__(self, val=None):
        self.val = val
        self.dic = {}
        self.numAccess = 0

class Trie:
    def __init__(self):
        self.head = Node()

    def insert(self, words, numAccess):
        node = self.head
        for word in words:
            if word not in node.dic:
                node.dic[word] = Node(word)               
            node = node.dic[word]
            node.numAccess += numAccess

    def getNumAccesses(self, wordList):
        node = self.head
        for word in wordList:
            if word not in node.dic:
                return 0               
            node = node.dic[word]
        return node.numAccess

def findUrlAddressAccesses(urlList):
    trie = Trie()
    for urlPair in urlList:
        urlWords = urlPair[0].split('.')
        urlWords.reverse()
        accesses = urlPair[1]
        urlPair.append(urlWords)
        trie.insert(urlWords, accesses)
    res = {}
    for urlTuple in urlList:
        accesses = trie.getNumAccesses(urlTuple[2])
        res[urlTuple[0]] = accesses
    return res

def main():
    urlList = [['google.com', 20], ['mail.google.com', 10]]
    sol = findUrlAddressAccesses(urlList)
    print(sol)

main()
