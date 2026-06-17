# 61. Rotate List - medium
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        '''
            Given head node of a linked list, rotate the linked list to the RIGHT by k places

            Constraints:
              - linked list can have up to 500 nodes
              - k can be large -> too many computations
            
            Edge cases: 
              - head is empty
              - if LL only 1 has element
              - if k is 0

            Approach:
              - Since we need to rotate the linked list to the right by k places, we first get a count of the whole linked list. 
                - the count is for eliminating uncessary rotations as we can just simplify k by the count
              - We then do k rotations
                - We get the tail and the node before that to connect the tail to the head and make the prev tail the new tail. We also set the new head.
        '''
        # if not head:
        #     return None
        # if not head.next or k == 0:
        #     return head

        # count = 1
        # curr = head
        # while curr.next:
        #     curr = curr.next
        #     count += 1

        # k = k % count

        # while k > 0:
        #     tail = head
        #     prev = None

        #     while tail.next:
        #         prev = tail
        #         tail = tail.next
            
        #     tail.next = head
        #     head = tail
        #     prev.next = None

        #     k -= 1

        # return head
        # O(n^2) time, O(1) space

        '''
            More efficient solution
        '''
        if not head:
            return None
        if not head.next or k == 0:
            return head

        count = 1
        tail = head
        while tail.next:
            tail = tail.next
            count += 1

        k %= count
        if k == 0:
            return head

        tail.next = head

        i = (count - k) - 1 # Rotating right by k means the new head should be the kth node from the end
        new_tail = head
        for _ in range(i):
            new_tail = new_tail.next
        
        new_head = new_tail.next
        new_tail.next = None

        return new_head

    # O(n) time, O(1) space
    