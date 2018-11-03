# 146. LRU Cache

class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.store = {} # node.key mapped to node
        self.length = 0
        
        self.head = None
        self.tail = None
        
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.store:
            node = self.store[key]
            self.removeNode(node)
            self.insertNodeToHead(node)
            return node.val
        else:
            return -1
        
    def removeNode(self, node):
        if node == self.head and node.next == None:
            self.head = None
            self.tail = None
        else:
            if node == self.head:
                self.head = self.head.next
                self.head.prev = None
            elif node == self.tail:
                self.tail = self.tail.prev
                self.tail.next = None
            else:
                prevTemp = node.prev
                nextTemp = node.next
                if prevTemp: prevTemp.next = nextTemp
                if nextTemp: nextTemp.prev = prevTemp   

        del self.store[node.key]
        del node
        self.length -= 1
        
    def insertNodeToHead(self, node):
        if not self.head:
            self.head = self.tail = node
        else:
            oldHead = self.head
            self.head = node
            self.head.next = oldHead
            oldHead.prev = self.head
            
        self.store[node.key] = node
        self.length += 1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.store:
            node = self.store[key]
            self.removeNode(node)

        node = Node(key, value) 
        self.insertNodeToHead(node)  
        
        if self.length > self.capacity:
            self.removeNode(self.tail)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
