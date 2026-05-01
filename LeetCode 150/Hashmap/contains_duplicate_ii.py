# 219. Contains Duplicate II - easy
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool: # O(n) time, O(n) space
        '''
            Given int arr nums and int k
            Return true if there are 2 DISTINCT INDICES i and j 
              - such that nums[i] == nums[j]
              - abs(i-j) <= k

            Use a hashmap to store nums and their indices
            Loop through nums
              - If the num hasn't been seen yet, add it
              - Else, check if the distance between the current index and the stored index are less than or equal to k
                - if yes, return True
                - if not, update the num's index to the current index
        '''
        # seen = {} # val : index

        # for i, num in enumerate(nums):
        #     if num not in seen:
        #         seen[num] = i
        #     else:
        #         if abs(seen[num] - i) <= k:
        #             return True
        #         else:
        #             seen[num] = i # Update index

        # return False

        seen = {}

        for i, num in enumerate(nums):
            if num in seen and abs(seen[num] - i) <= k:
                return True

            seen[num] = i
        
        return False
