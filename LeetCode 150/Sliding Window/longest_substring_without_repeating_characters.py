# 3. Longest Substring Without Repeating Characters - medium
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int: # O(n) time, O(n) space
        '''
            Given string s, find LONGEST substring (not subsequence) without duplicate characters

            Substring -> Use sliding window

            A brute force solution is to get all possible substrings and then checking each subtring if there is a duplicate character. This solution would take O(n^3)

            A more optimal solution would be to do a two pointer approach and a set to use a sliding window. This sliding window will maintain a window of unique characters.
            Expand the window with the right pointer, and whenever there's a duplicate, shrink from the left until there's no duplicate. 
        '''
        seen = set()
        longest_length = 0
        
        left = 0
        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            
            seen.add(s[right])
            longest_length = max(longest_length, len(seen))

        return longest_length
            