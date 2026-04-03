# 80. Remove Duplicates from Sorted Array II - medium
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int: # O(n) time, O(1) space
        '''
            given nums list that is sorted
            remove duplicates in-place so that each unique element appears AT MOST TWICE
            relative order should be the same

            anything after k doesn't matter

            must implement this solution in-place

            initialize k to 0
            loop through nums:
              - if k < 2 or element at k - 2 does not equal to num (indirectly counting the duplicates)
                - set nums[k] to be that element
                - increment k
            
            return k
        '''
        k = 0

        for num in nums:
            if k < 2 or nums[k-2] != num:
                nums[k] = num
                k += 1
        
        return k
