#  21. Merge Two Sorted Lists - easy
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]: # O(n+m) time, O(1) space
        '''
            Given heads list1 and list2
            Merge the two lists into one SORTED list
              - the SORTED list should be made by splicing together the nodes of the first two lists
            Return the head of the merged SORTED list

            Since lists are already sorted, we don't need to create a new list, we can just build upon one.
            Pick a head depending on which val is lower.
            Intialize a tail to point to the last node in the merged list -> every time we attach a new node, we move the tail forward
            Loop through lists to merge
            Attach the remaining nodes if either list is exhausted
        '''
        # Edge case: If both lists are empty
        if not list1 and not list2:
            return None

        # Edge case: If either lists are empty
        if not list1: return list2
        if not list2: return list1
        
        # Pick a head depending on which val is lower
        head = None
        if list1.val <= list2.val:
            head = list1
            list1 = list1.next
        else:
            head = list2
            list2 = list2.next
        
        tail = head # tail will be the pointer to the last node in the merged list so far
        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next

            tail = tail.next

        if list1: # list2 is exhausted, just add remaining nodes of list1
            tail.next = list1
        else:
            tail.next = list2
        
        return head
