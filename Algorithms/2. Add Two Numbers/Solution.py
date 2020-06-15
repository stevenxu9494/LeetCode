# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse
# order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list. You may
# assume the two numbers do not contain any leading zero, except the number 0 itself. Example: Input: (2 -> 4 -> 3) +
# (5 -> 6 -> 4) Output: 7 -> 0 -> 8 Explanation: 342 + 465 = 807. Definition for singly-linked list.

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # first step create a new linked list using existing func
        head = l3 = ListNode(0)
        carry = 0

        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next

            l3.val = carry % 10
            carry = carry // 10

            if l1 or l2 or carry:
                l3.next = ListNode(0)
                l3 = l3.next

        return head





