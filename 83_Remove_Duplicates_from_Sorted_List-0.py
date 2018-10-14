# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return head
        now = head
        next = head.next
        while True:
            if now is None or next is None:
                break
            elif now.val != next.val:
                now.next = next
                now = next
            else:
                now.next = None
            next = next.next
        return head
