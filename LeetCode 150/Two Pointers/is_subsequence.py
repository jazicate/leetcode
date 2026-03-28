# 392. Is Subsequence - easy
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool: # O(n) time, O(1) space
        '''
            Return true is s is a subsequence of t
            Return false otherwise

            2 pointers approach: 
            - Keep track of a pointer to indicate the index of s
            - Keep track of a pointer to indicate the index of t

            Initialize pointers
            Loop through t:
            - if s element is equal to t element AND s_pointer < len(s)
              - If yes, increment s pointer
            - Check if s_pointer is equal to the length of s 

            Otherwise return False
        '''

        '''
        if s == "": return True

        s_pointer = 0
        for char in t:
            if s[s_pointer] == char and s_pointer < len(s):
                s_pointer += 1
            
            if s_pointer == len(s):
                return True

        return False
        '''

        s_pointer = 0
        t_pointer = 0

        while s_pointer < len(s) and t_pointer < len(t):
            if s[s_pointer] == t[t_pointer]:
                s_pointer += 1
            
            t_pointer += 1
        
        return s_pointer == len(s)

