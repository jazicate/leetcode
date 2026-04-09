# 53. Maximum Subarray - medium
class Solution:
    def maxSubArray(self, nums: List[int]) -> int: # O(n) time, O(1) space
        '''
            given nums array, find the subarray with the largest sum
            return its sum

            Kadane's Algorithm
        '''
        local_max = nums[0]
        global_max = nums[0]

        for i in range(1, len(nums)):
            local_max = max(nums[i], local_max + nums[i])

            if local_max > global_max:
                global_max = local_max
            
        return global_max
        