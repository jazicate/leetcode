# 128. Longest Consecutive Sequence - medium
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int: # O(n) time, O(n) space
        '''
            Given int array nums, return the length of the longest consecutive elements sequence

            Use a hashmap or set.

            Convert nums into a set
            Iterate through each num
              - Start a sequence with num-1 to prevent extra work of checking numbers of the same sequence
              - Count the actual sequence starting with num and length
              - Update longest if necessary
        '''
        elements = set(nums)
        longest = 0

        for num in elements:
            if num-1 not in elements:
                length = 1

                while num+length in elements:
                    length += 1

                longest = max(longest, length)

        return longest
