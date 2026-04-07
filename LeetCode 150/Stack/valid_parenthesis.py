# 20. Valid Parenthesis - easy
class Solution:
    def isValid(self, s: str) -> bool: # O(n) time, O(n) space
        '''
            given a string s with just ( ) { } [ ], determine if the input string is valid

            Valid iff:
            - Open brackets must be closed by the same type of brackets
            - Open brackets must be closed in the CORRECT order
            - Every close bracket has a corresponding open bracket of the same type
        '''

        char_map = {
            "(": ")",
            "{": "}",
            "[": "]"
        }
        stack = []

        if len(s) % 2 != 0:
            return False

        for char in s:
            if char in char_map: # ( { [
                stack.append(char_map[char]) # Push ) } ]
            else:
                if not stack or stack.pop() != char:
                    return False
        
        return len(stack) == 0
