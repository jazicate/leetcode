# 35. Search Insert Position - easy
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int: # O(logn) time, O(1) space
        '''
            Binary search but return low/left pointer
              - we return this because it always points to the smallest index where target could be inserted
        '''
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (high + low) // 2

            if nums[mid] == target:
                return mid

            elif nums[mid] > target:
                high = mid - 1 # Move left
            else:
                low = mid + 1 # Move right
        
        return low
