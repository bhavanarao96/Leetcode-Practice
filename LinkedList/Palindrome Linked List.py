"""
234. Palindrome Linked List
https://leetcode.com/problems/palindrome-linked-list/

Given a singly linked list, determine if it is a palindrome.

Example 1:

Input: 1->2
Output: false
Example 2:

Input: 1->2->2->1
Output: true
Follow up:
Could you do it in O(n) time and O(1) space?
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None: return True
        fast = head
        slow = head
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        prev = None
        cur = slow
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        slow = prev
        cur = head
        while cur and slow:
            if cur.val != slow.val:
                return False
            cur = cur.next
            slow = slow.next
        
        return True