# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        pre=head
        now=head.next
        head.next=None
        if now:
            new=now.next
        else:
            return head
        while new:
            now.next=pre
            pre=now
            now=new
            new=new.next
        now.next=pre
        return now
