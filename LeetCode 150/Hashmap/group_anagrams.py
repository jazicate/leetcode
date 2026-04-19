# 49. Group Anagrams - medium
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]: # O(n * klogk) time, O(n * k) space
        '''
            Given strings array strs, group the anagrams together
              - You can return the answer in any order
        '''
        string_count = {}
        for string in strs:
            curr = ''.join(sorted(string))
            if curr not in string_count:
                string_count[curr] = [string]
            else:
                string_count[curr].append(string)
    
        return list(string_count.values())
