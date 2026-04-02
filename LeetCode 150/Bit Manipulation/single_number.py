# 136. Single Number - easy
class Solution:
    def singleNumber(self, nums: List[int]) -> int: # O(n) time, O(1) space
        '''
            nums will never be empty
            every number appears twice except for one -> find the number that only appears once

            - pretty much use XOR -> pairs will cancel itself out
        '''
        res = 0
        
        for num in nums:
            res = res ^ num

        return res
