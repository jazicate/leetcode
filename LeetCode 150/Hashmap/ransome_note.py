# 383. Ransom Note - easy
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool: # O(m + n) time, O(n) space
        '''
            counter -> use hashmap
            return true if ransomNote can be constructed using the letters from magazine
            Note: each letter in magazine can only be used once in ransomNote

            initialize a counter hashmap to count occurences of chars in magazine
            loop through ransomNote:
              - if char in ransomNote does not exist in the counter -> return False
              - elif char in ransomeNote exists in the counter, but == 0 -> return False
              - else -= 1
        '''

        counter = defaultdict(int) # Automatically returns 0 for missing keys
        for char in magazine:
            counter[char] += 1

        for char in ransomNote:
            # if char not in counter:
            #     return False
            # elif char in counter and counter[char] == 0:
            #     return False
            # else:
            #     counter[char] -= 1
            if counter[char] == 0:
                return False
            
            counter[char] -= 1
        
        return True
        
