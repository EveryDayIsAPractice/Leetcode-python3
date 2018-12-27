# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        new = ListNode(0)
        d1 = l1
        d2 = l2
        now = new
        carry = 0
        while d1.next or d2.next:
            val = d1.val + d2.val + carry
            carry = int(val/10)
            now.val = val%10
            if d1.next:
                if d2.next:
                    d2 = d2.next
                else:
                    d2.val=0
                d1 = d1.next
            else:
                d2 = d2.next
                d1.val = 0
            now.next = ListNode(0)
            now = now.next
        val = val = d1.val + d2.val + carry
        carry = int(val/10)
        now.val = val%10
        while carry>0:
            now.next = ListNode(0)
            now = now.next
            now.val = carry%10
            carry = int(carry/10)
        return new
