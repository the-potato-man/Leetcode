# https://kunigami.blog/2012/09/25/skip-lists-in-python/

import random

class Node:
    def __init__(self, elem=None, height=0):
        self.elem = elem
        self.next = [None] * height

class SkipList:
    def __init__(self):
        self.head = Node()

    def updateList(self, elem):
        update = [None] * len(self.head.next)
        node = self.head
        for i in range(len(self.head.next) - 1, -1, -1):
            while node.next[i] and node.next[i].elem < elem:
                node = node.next[i]
            update[i] = node
        return update
    
    def find(self, elem, update=None):
        if not update:
            update = self.updateList(elem)

        if len(update) > 0:
            node = update[0].next[0]
            if node and node.elem == elem:
                return node 

        return None
    
    def randomHeight(self):
        return random.randint(1, 10)

    def insert(self, elem):
        node = Node(elem, self.randomHeight())
        while len(self.head.next) < len(node.next):
            self.head.next.append(None)

        update = self.updateList(elem)
        if not self.find(elem, update):
            for i in range(len(node.next)):
                node.next[i] = update[i].next[i]
                update[i].next[i] = node
    
    def remove(self, elem):
        update = self.updateList(elem)
        node = self.find(elem, update)
        if node:
            for i in range(len(node.next)):
                update.next[i] = node.next[i]
     