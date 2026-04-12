# 141. Linked List Cycle - easy
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool: # O(n) time, O(1) space
        '''
            slow and fast pointer approach

            if slow and fast pointer meet, there is a cycle
        '''
        if head is None:
            return False

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if fast == slow:
                return True
        
        return False

'''
Another method is keep track of visited nodes using a set. If the node has been visited, there is a cycle. If the traversal reaches None, there is no cycle. This method uses O(n) space though.
'''