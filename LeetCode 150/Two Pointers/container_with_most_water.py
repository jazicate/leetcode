# 11. Container With Most Water - medium
class Solution:
    def maxArea(self, height: List[int]) -> int: # O(n) time, O(1) space
        '''
            Find two lines that can contain the most water
            - We're essentially trying to find two pairs of vertical lines that have the most water (area)
              - Area of a rectangle = length * width

            Two-pointer approach
              - We explore the widest container first and gradually narrow it while trying improve the height
                - We move the pointer with the smaller height inward because moving the taller one cannot increase height
              - Repeat until pointers meet

            initialize left and right pointers
            initialize a var to track max area
            loop until pointers meet
              - the current water is just width * the lower of the two end point lines
              - update max area
              - move pointers
        '''
        left = 0
        right = len(height)-1

        max_water = float('-inf')

        while left < right:
            width = (right-left)
            water = width * min(height[left], height[right])
            max_water = max(max_water, water)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_water
