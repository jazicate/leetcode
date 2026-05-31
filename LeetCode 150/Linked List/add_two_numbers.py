# 2. Add Two Numbers - medium
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]: # O(max(n, m)) time, O(max(n, m)) space
        '''
            Given NON-EMPTY LLs l1 and l2
              - digits are stored in REVERSE ORDER
              - each node contains a single digit
            Add the numbers from the two nodes and return the sum as a linked list

            It is guaranteed that the list represents a number that does not have leading zeros
            It is also guaranteed that both linked lists are not empty.

            Approach:
            Intialize carry
            Intialize a head pointer to track first node of the result LL
            Initiaize a curr pointer to point to the current tail of result LL
              - used to append
            Traverse both LLs at the same time until both lists are exhausted and no carry
              - extract digits from both LLs
                - use 0 if LL is exhausted
              - calculate total, carry
              - calculate digit and make a new node with that digit
              - Insertion
                - Case 1: Check if LL is empty
                  - just make head and curr be the new node
                - Case 2: Check if LL is not empty
                  - set curr.next to be the new node
                  - move curr to next
              - Move l1 and l2 pointers if possible
              - Return head 
        '''
        carry = 0
        head = None # Need this to return the correct pointer
        curr = None
        while l1 or l2 or carry:
            first_digit = l1.val if l1 else 0
            second_digit = l2.val if l2 else 0

            total = first_digit + second_digit + carry
            carry = total // 10

            digit = total % 10
            new_node = ListNode(digit)

            if curr is None: # Case 1: LL is empty
                head = new_node
                curr = new_node
            else: # Case 2: LL is not empty
                curr.next = new_node
                curr = curr.next

            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
        
        return head
