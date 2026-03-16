class Solution:
    def isAnagram(self, s: str, t: str) -> bool: # O(s + t) time, O(1) space
        '''
            anagram: same words with the same letters

            Use a hashmap.

            Count chars and put into a hashmap.
            Check t:
              - If char isn't a key in the hashmap or the count of that char is 0:
                - return False
              - Else:
                - decrement the counter of that char
            
            If counter of that char ever goes 0 -> not an anagram
        '''

        if len(s) != len(t): 
            return False

        count = dict()
        
        for char in s:
            count[char] = count.get(char, 0) + 1
        
        for char in t:
            if char not in count or count[char] == 0:
                return False
            
            count[char] -= 1

        return True
