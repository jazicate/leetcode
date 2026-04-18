# 202. Happy Number - easy
class Solution:
    def isHappy(self, n: int) -> bool: # O(logn) time, O(logn) space
        '''
            Return whether n is happy or not

            You can determine if n is happy with:
              - starting with any positive int, replace the number by the sum of the squares of its digits
              - repeat this until the number equals to 1, OR it loops endlessly in a cycle which doesn't include 1
                -> there could be a cycle so handle cycles
            
            numbers for which this process ends with 1 are happy

            Initalize a hashmap to track seen numbers
            Loop until n doesn't equal 1
              - If the number is already in seen -> there's a cycle
              - Else, add to seen

              - Transform n
                - get digits and add to res
              - Update n
        '''
        seen = {}

        while n != 1:
            if n in seen:
                return False
            
            seen[n] = True

            res = 0
            while n:
                digit = n % 10
                res += digit ** 2

                n //= 10

            n = res

        return True
