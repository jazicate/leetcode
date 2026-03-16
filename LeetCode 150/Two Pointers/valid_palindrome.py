class Solution:
    def isPalindrome(self, s: str) -> bool: # O(n) time, O(1) space
        '''
            Two Pointers Approach:
            - convert s to lowercase

            - Initiate pointers: left index and right index

            - Iterate left and right elements
              - If either is not alnum:
                - Just move on to the next element
                    - Increment/Decrement index
                    - Continue
              - Else:
                - Check if they are the same char
        '''
        s = s.lower()

        left = 0
        right = len(s) - 1

        while left < right:
            if not s[left].isalnum():
                left += 1
                continue
            if not s[right].isalnum():
                right -= 1
                continue
        
            if s[left] != s[right]:
                return False

            left += 1
            right -= 1
        
        return True
    
    
'''
Another solution: O(n) time, O(n) space
s_2 = "".join([char for char in s if char.isalnum()])
    s_2 = s_2.lower()
    return s_2 == s_2[::-1]
'''
