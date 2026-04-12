# 88. Merge Sorted Array - easy
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None: # O(m + n) time, O(1) space
        """
        Do not return anything, modify nums1 in-place instead.
        """

        '''
            Has to be in-place.

            Ignore 0

            nums1 has length m+n, nums2 has length n

            Plan: Pointers Approach
              - Compare the elements from nums1 and nums2
              - Place the larger element into nums1[k]
              - Move the corresponding pointer
              - Continue until nums2 is exhausted
        '''
        
        i = m - 1
        j = n - 1
        k = m+n - 1

        while i >= 0 and j >= 0: # O(m + n)
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            
            k -= 1

        while j >= 0: # O(n)
            nums1[k] = nums2[j]
            j -= 1
            k -= 1

'''Visualization
Step 1: 
nums1: [1, 2, 3, 0, 0, 6]
                       k
nums2: [2, 5, 6]
        j moves left

> j = 1, k = 4

Step 2:
nums1: [1, 2, 3, 0, 5, 6]
                    k
nums2: [2, 5, 6]
     j moves left

> j = 0, k = 3


Step 3:
nums1: [1, 2, 3, 3, 5, 6]
                 k
nums1 pointer moves

> i = 1, k = 2

Step 4:
nums1: [1, 2, 2, 3, 5, 6]
              k
nums2 pointer moves

j = -1 (stop)
'''