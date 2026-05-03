# 189. Rotate Array - medium
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        '''
            Given int array nums
            Rotate the array to the RIGHT by k steps
            k is non-negative
            nums is never empty

            Reduce operations if needed, for example, if a list only has 1 element, you don't need to rotate
            Get k last elements
            Modify nums in-place by adding those last elements to the front of the modified nums (without k last elements)
        '''
        # O(n) time, O(n) space
        # n = len(nums)
        # k = k % n # To reduce operations if needed

        # res = []
        # for i in range(k):
        #     res.append(nums.pop(-1))

        # nums[:] = res[::-1] + nums

        '''
            More efficient version

            Create a reverse function to reverse the array in-place -> Use two-pointers
            Reverse the whole array
            Reverse the first k elements
            Reverse the remaining elements
        '''
        # O(n) time, O(1) space
        def reverse(arr, left, right):
            while left < right:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
                right -= 1

        n = len(nums)
        k = k % n

        reverse(nums, 0, n - 1)
        reverse(nums, 0, k - 1)
        reverse(nums, k, n - 1)
