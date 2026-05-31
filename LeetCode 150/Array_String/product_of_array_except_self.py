# 238. Product of Array Except Self - medium
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]: # O(n) time, O(1) space (according to follow-up)
        '''
            Given an int array nums
            Return an array such that each element is EQUAL TO the product of 
            ALL ELEMENTS OF nums except nums[i]

            We need to calculate the product of the elements on the left side of the current element
                   and calculate the product of the elements on the right side of the current element
                   and finally, calculate the product between the left product and right product

            We could do this my making a prefix sum array to store the left side products for each element as well as making a suffix sum array to store the right side products for each element.
            Afterwards, we would need to multiply the elements of these arrays with each other to get the answer array.
        '''

        answer = []

        prefix = 1
        for i in range(len(nums)):
            answer.append(prefix)
            prefix *= nums[i]

        suffix = 1
        for i in range(len(nums) - 1, -1, -1):
            answer[i] *= suffix
            suffix *= nums[i]

        return answer

        '''
            prefix = 1
            prefix_sum = [1, 0, 0, 0]
            prefix *= 1 -> 1

            prefix = 1
            prefix_sum = [1, 1, 0, 0]
            prefix *= 2 -> 1

            prefix = 2
            prefix_sum = [1, 1, 2, 0]
            prefix *= 3 -> 6

            prefix = 6
            prefix_sum = [1, 1, 2, 6]
            prefix *= 4 -> 24

            prefix_sum = [1, 1, 2, 6]
            --------------------------
            suffix = 1
            suffix_sum = [0, 0, 0, 1]
            suffix *= 4 -> 4

            suffix = 4
            suffix_sum = [0, 0, 4, 1]
            suffix *= 3 -> 12

            suffix = 12
            suffix_sum = [0, 12, 4, 1]
            suffix *= 2 -> 24

            suffix = 24
            suffix_sum = [24, 12, 4, 1]
            suffix *= 1 -> 24

            suffix_sum = [24, 12, 4, 1]
            --------------------------
            ans = [24, 12, 8, 6]
        '''
