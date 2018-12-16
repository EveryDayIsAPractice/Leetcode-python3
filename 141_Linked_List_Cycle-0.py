# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        pre=head
        while True:
            if pre:
                if pre.next==pre:
                    return True
                else:
                    now=pre.next
                    pre.next=pre
                    pre=now
            else:
                return False
