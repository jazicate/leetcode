# 290. Word Pattern - easy
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool: # O(n) time, O(n) space
        '''
            given string pattern and string s, find if s follows the same pattern

            Rules:
              - No two letters can map to the same word
              - No two words can map to the same letter

            basically every unique word maps to one letter

            Use a hashmap

            Get each word in s
            Initialize a hashmap to map word to letter
            Initialize a hashmap to see if a letter has already been seen
            Iterate through each word in s and each index of pattern
              - If the word is not in the word to letter hashmap, add it
              - Else, check if it maps to the same letter
              - Do the same with letter to word

        '''
        word_mapping = {}  # word to letter
        letter_mapping = {} # letter to word

        words = s.split()

        if len(pattern) != len(words): return False

        for i, word in enumerate(words):
            if word not in word_mapping:
                word_mapping[word] = pattern[i]
            else:
                # If it is in the dictionary -> Check if it maps to the same letter
                if word_mapping[word] != pattern[i]:
                    return False

            if pattern[i] not in letter_mapping:
                letter_mapping[pattern[i]] = word
            else:
                if letter_mapping[pattern[i]] != word:
                    return False
        
        return True
