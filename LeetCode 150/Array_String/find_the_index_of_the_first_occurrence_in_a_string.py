# 28 Find the Index of the First Occurrence in a String - easy
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        '''
            Given a needle string and haystack string
            Return the index of the FIRST occurrence of needle in haystack
            Else return -1 if not

            Constraints:
              - 1 <= len(haystack), len(needle) <= 10^4
              - haystack and needle are lowercase English letters

            Edge cases:
              - length of needle can be greater than length of haystack
            
            Since haystack and needle cannot be empty, we can first check the edge case of whether the length of needle is greater than the length of haystack, as in that case we can just return -1. We then loop through each character or index of haystack. While looping, we can check if the substring of length needle starting at the current index equals to needle. If equal, we can just return the current index. If the loop finishes and we didn't return i, we just return -1 to indicate that the needle isn't part of the haystack. 
        '''
        # needle_len = len(needle)

        # if needle_len > len(haystack):
        #     return -1

        # for i in range(len(haystack)): # O(n) time
        #     if haystack[i:i+needle_len] == needle: # O(m) time and O(m) space
        #         return i

        # return -1

        # O(n * m) time, O(m) space

        # Optimal Space Solution
        n = len(haystack)
        m = len(needle)

        if m > n:
            return -1

        for i in range(n - m + 1):
            j = 0

            while j < m and haystack[i+ j] == needle[j]:
                j += 1

            if j == m:
                return i

        return -1

        # O(n * m) time, O(1) space
        