# 274. H-Index - medium
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        '''
            Given an int array citations where each element represents the number of citations a researcher received
            for their ith paper
            Return the researcher's h-index

            H-index:
              - the max value of h such that the given researcher has published AT LEAST h papers that have been cited
              AT LEAST h times

            So pretty much an h-index is the largest number h such that at least h papers have >= h citations

            Inefficient Solution:
              - Sort the array in decreasing order
              - Loop through the array
                - Each iterations means how many papers (need i + 1 to represent this because of 0-index)
                  - Check if citations[i] >= i + 1
              - This solution is O(nlogn) time, O(logn) amortized space
            More efficient Solution: Use counting
              - Create a frequency array to count of size n + 1 where
                - count[i] = number of papers with exactly i citations
                - count[n] = number of papers with >= n citations
              - Traverse h from n down to 0, accumulating how many papers have at least h citations
              - The first h where accumulated count >= h is the h-index
              - This solution is O(n) time, O(n) space
        '''
        # citations.sort(reverse=True)

        # h_index = 0
        # for i, citation in enumerate(citations):
        #     if citation >= i + 1:
        #         h_index += 1
        #     else:
        #         break
        
        # return h_index

        n = len(citations)
        count = [0] * (n + 1)

        for citation in citations:
            if citation >= n:
                count[n] += 1
            else:
                count[citation] += 1
        
        total = 0
        for h in range(n, -1, -1):
            total += count[h]

            if total >= h:
                return h
        
        return 0

'''
citations = [3,0,6,1,5]
count = [0,0,0,0,0,0]
index    0 1 2 3 4 5

citation = 3
count = [0,0,0,1,0,0]
citation = 0
count = [1,0,0,1,0,0]
citation = 6
count = [1,0,0,1,0,1]
citation = 1
count = [1,1,0,1,0,1]
citation = 5
count = [1,1,0,1,0,2]

h = 5
total = 2
2 >= 5 -> continue

h = 4
total = 2
2 >= 4 -> continue

h = 3
total = 3
3 >= 3 -> break and return h
'''
