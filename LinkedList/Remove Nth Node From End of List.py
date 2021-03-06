""" 
19. Remove Nth Node From End of List
https://leetcode.com/problems/remove-nth-node-from-end-of-list/
Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:

Given n will always be valid.

Follow up:

Could you do this in one pass?
---for one pass solution check leetcode
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        cur = head
        l = 0  #size of the linkedlist
        
        while cur:
            l+=1
            cur = cur.next
        
        i = l - n #nth node from the end is ith node from beginning 
        j=0
        cur = dummy
        
        while j!=i:
            j = j+1
            cur = cur.next
           
        cur.next = cur.next.next
        
        return dummy.next