#!/usr/bin/python3
#coding: utf-8

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        p = dummy = ListNode(-1)
        en = 0
        while l1 and l2:
            s = l1.val + l2.val + en
            en = int(s / 10)
            p.next = ListNode(int(s % 10))
            p = p.next
            l1 = l1.next
            l2 = l2.next
        l = l1 or l2
        while l:
            s = l.val + en
            en = int(s / 10)
            p.next = ListNode(s % 10)
            p = p.next
            l = l.next
        if en:
            p.next = ListNode(en)
        return dummy.next