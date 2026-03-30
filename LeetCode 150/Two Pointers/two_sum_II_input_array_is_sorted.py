# 167. Two Sum II - Input Array is Sorted - med
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]: # O(n) time, O(1) space
        '''
            constraints -> O(n^2), but since numbers is sorted in non-decreasing order, there's an optimal solution to get O(n)
            - two pointers

            Initialize two pointers for the start(left) and end(right)
            Iterate through numbers:
            - if both elements equals target, return their indices+1 (1-indexed)
            - if the total is smaller than the target:
              - move the left pointer forward (to increase total)
            - else
              - move the right pointer backward (to decrease total)
        '''
        left = 0
        right = len(numbers) - 1

        while left < right:
            total = numbers[left] + numbers[right]

            if total == target:
                return [left+1, right+1]

            if total < target:
                left += 1
            else:
                right -= 1

        return []
