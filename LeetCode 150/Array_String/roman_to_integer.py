# 13. Roman to Integer - easy
class Solution:
    def romanToInt(self, s: str) -> int: # O(n) time, O(1) space
        '''
            s is a valid roman numeral from 1 to 3999

            you need subtraction

            Make a mapping
            Loop through s
              - Check if the current value is less than the next value
                - if it is, subtract
                - else add to res
        '''
        mapping = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        res = 0
        for i in range(len(s)):
            if i < len(s)-1 and mapping[s[i]] < mapping[s[i+1]]:
                res -= mapping[s[i]]
            else:
                res += mapping[s[i]]

        return res
        