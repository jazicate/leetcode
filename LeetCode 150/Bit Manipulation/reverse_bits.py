# 190. Reverse Bits - easy
class Solution:
    def reverseBits(self, n: int) -> int:
        '''
            O(1) time, O(1) space
        '''

        # x = bin(n)[2:].zfill(32)
        # x_reversed = x[::-1]

        # return int(x_reversed, 2)

        '''
            O(1) time, O(1) space
        '''
        res = 0
        for i in range(32):
            res = (res << 1) | (n & 1)
            n >>= 1

        return res
