# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        pre=head
        while pre:
            if pre.val==val:
                pre=pre.next
            else:
                breal
        if pre is None:
            return None
        head=pre
        now=pre.next
        while now:
            if now.val==val:
                pre.next=now.next
            else:
                pre=now
            now=now.next
        return head
