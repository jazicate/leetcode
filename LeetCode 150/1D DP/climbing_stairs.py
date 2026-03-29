# 70. Climbing Stairs - easy
class Solution:
    def climbStairs(self, n: int) -> int: # O(n) time, O(1) space
        '''
            Fibonacci Sequence
            Recurrence Relation: t(n) = t(n-1) + t(n-2) for t(0) = 0 and t(1) = 1

            Tabulation DP
        '''

        if n <= 2:
            return n

        prev = 1
        curr = 2

        for i in range(3, n + 1):
            prev, curr = curr, prev + curr # curr is the the sum of the previous two

        return curr
