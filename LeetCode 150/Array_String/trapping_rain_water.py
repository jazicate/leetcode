# 42. Trapping Rain Water - hard
class Solution:
    def trap(self, height: List[int]) -> int:
        '''
            Given non negative int array that represents an elevation map where the width of each bar is 1
            Compute how much water it can trap after raining

            Constraints:
              - n == height.length
              - 1 <= n <= 2 * 10**4
              - height can be 0 to 10**5

            Observations:
              - Edges (first and last bar) can't hold water
              - Water is trapped in heights where there are taller bars on both the left and right
              - Water level is at the lower of the two taller bars

            A straight forward approach would be to find the tallest bars to its left and right. The amount of water for that height would be just the difference between the smaller of the two tallest bars and its height. This approach would take O(n^2) time since we are recomputing the left and right tallest bars for each height. We can actually cache the left and tallest bars to make O(n) time, but it would take O(n) space.

            A more efficient approach would be to use two pointers to keep track of the tallest left and right bars. This would allow us to just do a single pass. Since water level is pretty much determined by the difference between the current height and the lower of the tallest two bars, we don't have to explicitly find the tallest left and right bars for every height. 
            
            At each step, we move the pointer pointing to the shorter current bar. If the left bar is shorter (or equal), we know there is a right boundary at least as tall as the current left bar, so the amount of water trapped at the left pointer depends only on the tallest bar we've seen from the left. Similarly, if the right bar is shorter, we process the right pointer using the tallest bar seen from the right. As we move inward, we update the running maximum on that side and accumulate the trapped water.
        '''
        left = 0
        right = len(height) - 1

        left_tallest = 0
        right_tallest = 0

        res = 0
        while left < right:
            if height[left] <= height[right]:
                left_tallest = max(left_tallest, height[left])
                res += left_tallest - height[left]
                left += 1
                
            elif height[left] > height[right]:
                right_tallest = max(right_tallest, height[right])
                res += right_tallest - height[right]
                right -= 1

        return res

        # O(n) time, O(1) space
