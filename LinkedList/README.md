
- A Linked List is a linear collection of data elements, called nodes, each pointing to the next node by means of a pointer. It is a data structure consisting of a group of nodes which together represent a sequence.
- Singly-linked list: linked list in which each node points to the next node and the last node points to null
- Doubly-linked list: linked list in which each node has two pointers, p and n, such that p points to the previous node and n points to the next node; the last node's n pointer points to null
- Circular-linked list: linked list in which each node points to the next node and the last node points back to the first node

**Time Complexity:
  Access: O(n)
  Search: O(n)
  Insert: O(1)
  Remove: O(1)**

- In a Linked List the first node is called the head and the last node is called the tail. 
- Pros
  - Linked Lists have constant-time insertions and deletions in any position, in comparison, arrays require O(n) time to do the same thing.
  - Linked lists can continue to expand without having to specify their size ahead of time (remember our lectures on Array sizing form the Array Sequence section of the course!)
- Cons
  - To access an element in a linked list, you need to take O(k) time to go from the head of the list to the kth element. In contrast, arrays have constant time operations to access elements in an array.
 
 
**Single LinkedList Implementation:**

class Node(object):    
    def __init__(self,value):     
        self.value = value    
        self.nextnode = None
        
**Double LinkedList Implementation:**

class DoublyLinkedListNode(object):    
    def __init__(self,value): 
        self.value = value    
        self.next_node = None    
        self.prev_node = None
 
