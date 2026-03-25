# 169. Majority Element - easy
class Solution:
    def majorityElement(self, nums: List[int]) -> int: # O(n) time, O(1) space
        '''
            3 approaches: 
              - sort then return n//2 element
              - counter hashmap and return the element that appears more than n//2 times
              - Boyer-Moore Voting Algorithm -> more efficient

            keep a candidate
            maintian a count
            increase a count if same element
            decrease if different
            reset candiate when count hits 0
        '''
        
        candidate = None
        count = 0

        for num in nums:
            if count == 0:
                candidate = num

            if num == candidate:
                count += 1
            else:
                count -= 1
        
        return candidate
        