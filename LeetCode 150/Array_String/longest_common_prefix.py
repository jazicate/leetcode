# 14. Longest Common Prefix - easy
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str: # O(n*m) time, O(1) space
        '''
            Find longest prefix among the elements in the array
            If no common prefix -> return ""

            Check edge case if strs is empty
            Make the first element the prefix
            Loop through the elements in the array starting with the second element
              - Loop until the string doesn't start with prefix
                - Shrink prefix every time the element doesn't start with the prefix
                - Also check if prefix is empty -> if it is, no prefix exists
        '''
        if not str:
            return ""

        prefix = strs[0]

        for s in strs[::-1]:
            while not s.startswith(prefix):
                prefix = prefix[:-1]

                if not prefix:
                    return ""
        
        return prefix
