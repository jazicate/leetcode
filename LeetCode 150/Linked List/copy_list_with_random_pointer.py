# 138. Copy List with Random Pointer - medium
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        '''
            Given: A linked list with Node attributes val, next, and random.
            Goal: Make a deep copy of the list.

            This is not a standard deep copy. We need to worry about the random pointer. This random pointer could be anywhere in the list so we can't really just copy it just straight forward like that.

            First approach is to use a hashmap to create a copy of every node. We use the old nodes as the keys and the new nodes as the values. After we set the key values, we map each new node's next and random pointers by looking at the corresponding new nodes of the old node's neighbors. This method is O(n) time and O(n) space.

            A more space efficient approach is to create new nodes in the original list. For old node, we create its copy and insert after the old node. Through this relationship, we can easily just copy their next and random pointers. Afterwards, we can also detach the new nodes from the original list.
        '''
        if not head:
            return None

        curr = head
        while curr:
            new = Node(curr.val)

            new.next = curr.next
            curr.next = new

            curr = new.next

        '''
            A   ->   A'   ->   B   ->   B'
           curr     new      
        '''

        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next # new.random = copy of curr.random

            curr = curr.next.next

        dummy = Node(0)
        tail = dummy

        curr = head
        while curr:
            new = curr.next

            # Add new node to new list
            tail.next = new
            tail = new

            # Restore original list
            curr.next = new.next
            curr = curr.next

        return dummy.next
            