# 69. Sqrt(x) - easy
class Solution:
    def mySqrt(self, x: int) -> int:
        '''
            Basically return square root of a number x without using an built-in function or operator.
            Answer should be rounded down to the nearest integer and should be non-negative.

            A straight forward approach would be to try every number and check whether it's square is less than or equal to x. The answer should be the largest number whose square is less than or equal to x, but the time would be O(sqrt(x)) time. There is a more optimal solution using binary search.
            
            For this approach we know that the answer lies between 0 and x. So instead of checking EVERY number, we check the middle number of the current range. If mid * mid is less than or equal to x, the mid could be a valid answer, so we store mid as the current answer and search the right half. If mid * mid is greater than x, we search the left half.
        '''
        # res = 0

        # i = 0
        # while i < x:
        #     if i * i <= x:
        #         res = i
        #     else:
        #         break
        #     i += 1
        
        # return res
        left, right = 0, x
        res = 0

        while left <= right:
            mid = (left+right) // 2

            if mid*mid <= x:
                res = mid
                left = mid + 1
            else:
                right = mid - 1

        return res

        # O(logx) time, O(1) space
