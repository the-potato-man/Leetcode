# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# heapq with ListNodes only works in Python 2

import heapq        

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        heap = []
        for head in lists:
            if head:
                heapq.heappush(heap, (head.val, head))
            
        dummy = p = ListNode(0)
        while heap:
            priority, node = heapq.heappop(heap)
            p.next = ListNode(node.val)
            p = p.next
            node = node.next
            if node:
                heapq.heappush(heap, (node.val, node))
            
        return dummy.next
