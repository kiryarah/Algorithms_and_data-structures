'''
    2. Add Two Numbers
    https://leetcode.com/problems/add-two-numbers/description/
'''



class ListNode(object):

    def __init__(self, val=0, _next=None):
        self.val = val
        self.next = _next


class Solution(object):

    def addTwoNumbers(self, l1, l2):

        delta = 0
        res = value_next = ListNode()

        while l1 or l2 or delta:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            value = val1 + val2 + delta
            delta = value // 10
            value_next.next = ListNode(value % 10)

            value_next = value_next.next
            l1 = l1 if l1 else None
            l2 = l2 if l2 else None

        return res.next
