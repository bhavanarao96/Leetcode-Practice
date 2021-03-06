"""
# 707. Design Linked List
# https://leetcode.com/problems/design-linked-list/

Design your implementation of the linked list. You can choose to use the singly linked list or the doubly linked list. A node in a singly linked list should have two attributes: val and next. val is the value of the current node, and next is a pointer/reference to the next node. If you want to use the doubly linked list, you will need one more attribute prev to indicate the previous node in the linked list. Assume all nodes in the linked list are 0-indexed.

Implement these functions in your linked list class:

get(index) : Get the value of the index-th node in the linked list. If the index is invalid, return -1.
addAtHead(val) : Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
addAtTail(val) : Append a node of value val to the last element of the linked list.
addAtIndex(index, val) : Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
deleteAtIndex(index) : Delete the index-th node in the linked list, if the index is valid.
 
"""
class Node: 
   
    def __init__(self, val): 
        self.val = val  # Assign data 
        self.next = None  # Initialize next as null 
        
        
class MyLinkedList(object):
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.size = 0

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index < 0 or index >= self.size:
            return -1
        
        cur = self.head
        for i in range(index):
            cur = cur.next
        
        return cur.val

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: None
        """
        self.addAtIndex(0, val)

    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: None
        """
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: None
        """
        if index > self.size:
            return
        
        if index < 0:
            index = 0
        
        node = Node(val)
        
        if index == 0:
            node.next = self.head
            self.head = node
            self.size += 1
            return
        
        cur = self.head
        for i in range(1, index):
            cur = cur.next
        node.next = cur.next
        cur.next = node
        self.size += 1

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: None
        """
        if index < 0 or index >= self.size:
            return
        
        if index == 0:
            self.head = self.head.next
            self.size -= 1
            return
        
        cur = self.head
        for i in range(1, index):
            cur = cur.next
        
        cur.next = cur.next.next
        self.size -= 1
        

# Your MyLinkedList object will be instantiated and called as such:
#obj = MyLinkedList()
#obj.addAtHead(1)
#obj.addAtTail(3)
#obj.addAtIndex(1,2)
#param_1 = obj.get(1)
#obj.deleteAtIndex(1)
#param_2 = obj.get(1)
