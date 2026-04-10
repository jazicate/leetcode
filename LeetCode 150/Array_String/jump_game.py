# 55. Jump Game - medium
class Solution:
    def canJump(self, nums: List[int]) -> bool: # O(n) time, O(1) space
        '''
            given nums array
            you are positioned at 0, and each element in the array represents your max jump length at that position

            return true if you can reach the last index
            return false otherwise

            so pretty much checking each jump, but instead we can do a greedy approach where we can just track the max jump

            initialize a variable to store the furthest index that can be reached: max_jump
            iterate through nums
              - check if the index is greater than max_jump
                - if it is return False 
              - otherwise, update max_jump

        '''

        max_jump = 0

        for i in range(len(nums)):
            if i > max_jump:
                return False

            max_jump = max(max_jump, i + nums[i])

        return True

