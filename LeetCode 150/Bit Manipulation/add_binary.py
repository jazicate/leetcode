# 67. Add Binary - easy
class Solution:
    def addBinary(self, a: str, b: str) -> str: # O(n) time, O(n) space
        '''
            Use bitwise operations
        '''

        # Convert to decimal (base 2)
        x = int(a, 2)
        y = int(b, 2)

        while y != 0 :
            ans = x ^ y
            carry = (x & y) << 1

            x = ans
            y = carry

        return bin(x)[2:]

