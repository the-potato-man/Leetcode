# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        # Creating pointers so the original lists aren't modified
        p1 = l1
        p2 = l2

        dummy = p3 = ListNode(0)

        while p1 and p2:
            if p1.val < p2.val:
                p3.next = ListNode(p1.val)
                p1 = p1.next
            else:
                p3.next = ListNode(p2.val)
                p2 = p2.next
            p3 = p3.next

        if p1:
            p3.next = p1
        else:
            p3.next = p2

        return dummy.next
