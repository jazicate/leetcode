# 162. Find Peak Element - medium
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        '''
            Given 0-index int array nums, find a peak element and return it's index
              - There may exist multiple peaks, but all you need to do is return one of them

            First and last elements are considered to be greater than than a neighbor outside the array, so only check nums[first_index+1] for the first element and nums[last_index-1] for the last element

            Problem suggests O(logn) time
              - Could do a binary search

            nums = [1, 2, 1, 3, 5, 6, 4]
            output can be 1 or 5 (indices)

                        6    
                       / \    
                      5   4
                     /
                2   3
              /  \ / 
            1     1  

            Observations:
              - nums[mid] is going to be greater than its neighbors
              - a peak may exist at the current index, the left side, or right side
                - so conceptionally, we don't need to compare both neighbors
                  - for example, if we were going upwards on the slope -> nums[mid] < nums[mid+1]:
                    - a peak MUST exist on the right side
                      - either we reach a potential peak that is greater than both neighbors, or we hit the last element (which is also a peak since the element before is less) 
                  - if we were going downwards on the slope -> nums[mid+1] < nums[mid], ideally the same thing will happen
        '''
        left = 0
        right = len(nums)-1

        while left < right:
            mid = (left+right) // 2
            
            # Check if mid is a peak
            if 0 < mid < len(nums)-1:
                if nums[mid-1] < nums[mid] > nums[mid+1]:
                    return mid

            if nums[mid] < nums[mid+1]:
                left = mid+1 # Search right side
            elif nums[mid+1] < nums[mid]:
                right = mid-1 # Search left side
            
        return left

        # O(logn) time, O(1) space
