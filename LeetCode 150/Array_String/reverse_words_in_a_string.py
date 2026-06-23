# 151. Reverse Words in a String - medium
class Solution:
    def reverseWords(self, s: str) -> str:
        '''
            Given string s, reverse the order of the words
            The words in s is guaranteed to be separated by at least one space.
            Return the reverse order of the words separated by one space with no leading or trailing spaces.
            
            s may contain leading or trailing spaces or multiple spaces between two words

            Constraints:
              - 1 <= s.length <= 10^4 -> max O(n) time solution
              - s contains upper and lower-case letters, digits, and spaces
              - There is at least one word in s
              - Solution should be in-place O(1) space -> in Python it's impossible since strings are immutable

            Edge cases:
              - trailing and leading spaces
              - 1 char words
              - multiple spaces between words

            In Python, since we cannot truly achieve in-place O(1) space, we first need to split s. This will give us a list of all the words in s. We then could reverse that list and join them together with a single space in between each word.
        '''
        s_split = s.split()
        s_reversed = s_split[::-1]

        return " ".join(s_reversed)

        # O(n) time, O(n) space
