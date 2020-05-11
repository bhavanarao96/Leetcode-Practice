"""
141. Linked List Cycle
https://leetcode.com/problems/linked-list-cycle/

Given a linked list, determine if it has a cycle in it.

To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.

Check the link for the Examples

Follow up:

Can you solve it using O(1) (i.e. constant) memory?
should use fast a slow pointers for this. Check leetcode
"""

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

        table = []
        i = 0
        while head != None:
            if head in table:
                return True
            else:
                table.append(head)
            i+=1
            head=head.next
        return False