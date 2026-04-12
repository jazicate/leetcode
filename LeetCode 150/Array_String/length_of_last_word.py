# 58. Length of Last Word - easy
class Solution:
    def lengthOfLastWord(self, s: str) -> int: # O(n) time, O(1) space
        # O(n) time, O(n) space
        # last_word = s.split()[-1]

        # return len(last_word)

        '''
            Return the length of the LAST word

            Initialize length variable
            Iterate backwards
              - Check if the char is an empty space
                - Check if length is greater than 0 -> if it is, you've already found a char but you landed at a space, so just stop the loop
              - If it is not an empty space, you are at a valid char so increment length

            This approach should be more space efficient
        '''

        length = 0
        
        for char in reversed(s):
            if char == ' ':
                if length > 0: # Check if you've already started counting
                    break
            else:
                length += 1
        
        return length
