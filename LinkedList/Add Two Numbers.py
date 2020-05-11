"""
2. Add Two Numbers
https://leetcode.com/problems/add-two-numbers/
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        dummy_head = ListNode(0)
        l3 = dummy_head
        carry = 0
        
        while l1 or l2 or carry:
            temp1 = l1.val if l1 else 0
            temp2 = l2.val if l2 else 0
            
            tempSum = temp1 + temp2 + carry
           
            l3.next = ListNode(tempSum % 10)
            carry = tempSum // 10
            l3 = l3.next
            
            if l1: l1 = l1.next 
            if l2: l2 = l2.next
        return dummy_head.next