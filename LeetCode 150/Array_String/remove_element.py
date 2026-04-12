# 27. Remove Element - easy
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int: # O(n) time, O(1) space
        '''
            Given nums array and integer val:
              - remove all occurrences of val in nums
              - return the number of elements in nums which are not equal to val

            The number of elements in nums, which are not equal to val be k
              - change the array nums such that the first k elements of nums contain the elements
            which are not equal to val
              - return k
        '''

        '''
            Loop through nums
              - Check if element is equal to val
                - If not:
                  - Place in front of nearest element not equal to val
                  - increment counter
                - If yes:
                  - change element to 0
        '''

        counter = 0

        for i, number in enumerate(nums):
            if number != val:
                nums[counter] = number
                counter += 1
            else: # Doesn't matter
                number = 0

        return counter
