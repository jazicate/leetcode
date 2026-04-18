# 1. Two Sum - easy
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]: # O(n) time, O(n) space
        seen = {} # num : index

        for i, num in enumerate(nums):
            complement = target - num

            if complement in seen: # Check if we seen complement that pairs with num
                return [seen[complement], i] # We can return the seen num's index and the current index
            
            seen[num] = i

        return []
