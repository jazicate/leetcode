# 26. Remove Duplicates from Sorted Array - Easy
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int: # O(n) time, O(1) space
        '''
            In-place, relative order should be the same

            Check edge case: if nums is empty
            Keep track of latest index of unique elements -> k starting with 1
            Loop through nums
              - If element in nums does not equal to nums at k-1
                - place that element at nums[k]
                - increment k
              - If element in nums does equal to nums at k-1
                - continue
            
            Return k
        '''
        if len(nums) == 0: return 0

        k = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[k-1]:
                nums[k] = nums[i]
                k += 1
        
        return k
