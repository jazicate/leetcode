# 205. Isomorphic Strings - easy
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool: # O(n) time, O(n) space
        '''
            - Map chars -> cannot map to the same character, but a character may map to itself
            - len(s) == len(t)
            - s and t can be any ascii character

            - Basically two different chars in s cannot map to the same character in t

            Initialize a hashmap to map characters from s to t
            Initialize a hashmap to also check if t chars are mapped
            Loop through s and t
              - If the character hasn't been mapped yet
                - Check if t char has already been mapped
                - Map character
                - Also make sure the t char is already seen
              - If not:
                - Check if the character is the same as the one that's already mapped
            Return True after the Loop
        '''

        res = dict()
        t_map = set()

        for i, s_char in enumerate(s):
            if s_char not in res:
                # Check if t char is already mapped
                if t[i] in t_map:
                    return False

                res[s_char] = t[i]
                t_map.add(t[i])
            else:
                if t[i] != res[s_char]:
                    return False

        return True

''' Test Case
s = "badc"
t = "baba"

Step 1: res = {"b":"b"}
Step 2: res = {"b":"b", "a":"a"}
Step 3: res = {"b":"b", "a":"a", "d":"b"} -> return False (cannot map b(t) and d(s))
'''