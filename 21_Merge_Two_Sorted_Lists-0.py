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
        if l1 is None:
            if l2 is None:
                return None
            else:
                return l2
        elif l2 is None:
            return l1
        if l1.val < l2.val:
            l3 = l1
            l1now = l1.next
            l2now = l2
        else:
            l3 = l2
            l1now = l1
            l2now = l2.next
        temp=l3
        while l1now and l2now:
            if l1now.val < l2now.val:
                temp.next = l1now
                l1now = l1now.next
            else:
                temp.next = l2now
                l2now = l2now.next
            temp = temp.next
        if l1now:
            temp.next=l1now
        elif l2now:
            temp.next=l2now
        return l3
