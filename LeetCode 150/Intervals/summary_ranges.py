# 228. Summary Ranges - easy
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]: # O(n) time, O(n) space
        '''
            Given a sorted unique int array nums
            Return the minimal list of ranges
              - Each element should be covered
            
            A range should be continuous(consecutive integers) or just a single number
        '''

        if len(nums) == 0: 
            return []

        res = []
        i = 0
        while i < len(nums):
            start = nums[i]

            while i + 1 < len(nums) and nums[i] + 1 == nums[i+1]:
                i += 1

            if start != nums[i]:
                res.append(f"{start}->{nums[i]}")
            else:
                res.append(f"{start}")

            i += 1
        
        return res
            